import time
import websockets
import numpy as np
import pandas as pd
import lz4.frame as lz4f
import asyncio
import struct
import json


from SharedData.Logger import Logger
from SharedData.IO.ServerWebSocket import ServerWebSocket
from SharedData.IO.ClientSocket import ClientSocket


class ClientWebSocket():

    @staticmethod
    async def table_subscribe_thread(table, host, port,
            lookbacklines=1000, lookbackdate=None, snapshot=False, bandwidth=1e6):

        while True:
            try:
                # Connect to the server
                async with websockets.connect(f"ws://{host}:{port}") as websocket:

                    # Send the subscription message
                    msg = ClientSocket.table_subscribe_message(
                        table, lookbacklines, lookbackdate, snapshot, bandwidth)
                    msgb = msg.encode('utf-8')
                    await websocket.send(msgb)

                    # Subscription loop
                    await ClientWebSocket.table_subscription_loop(table, websocket)
                    time.sleep(15)

            except Exception as e:
                msg = 'Retrying subscription %s,%s,%s,table,%s!\n%s' % \
                    (table.database, table.period,
                     table.source, table.tablename, str(e))
                Logger.log.warning(msg)
                time.sleep(15)

    @staticmethod
    async def table_subscription_loop(table, websocket):
        shnumpy = table.records
        hasindex = table.hasindex
        bytes_buffer = bytearray()

        while True:
            try:
                # Receive data from the server
                data = await websocket.recv()                
                if data == b'':
                    msg = 'Subscription %s,%s,%s,table,%s closed !' % \
                        (table.database, table.period,
                            table.source, table.tablename)
                    Logger.log.warning(msg)
                    websocket.close()
                else:
                    # Decompress the data                    
                    data = lz4f.decompress(data)
                    bytes_buffer.extend(data)

                    if len(bytes_buffer) >= shnumpy.itemsize:
                        # Determine how many complete records are in the buffer
                        num_records = len(
                            bytes_buffer) // shnumpy.itemsize
                        # Take the first num_records worth of bytes
                        record_data = bytes_buffer[:num_records *
                                                   shnumpy.itemsize]
                        # And remove them from the buffer
                        del bytes_buffer[:num_records *
                                         shnumpy.itemsize]
                        # Convert the bytes to a NumPy array of records
                        rec = np.frombuffer(
                            record_data, dtype=shnumpy.dtype)
                        
                        if hasindex:
                            # Upsert all records at once
                            shnumpy.upsert(rec)
                        else:
                            # Extend all records at once
                            shnumpy.extend(rec)

            except Exception as e:
                msg = 'Subscription %s,%s,%s,table,%s error!\n%s' % \
                    (table.database, table.period,
                     table.source, table.tablename, str(e))
                Logger.log.error(msg)
                websocket.close()
                break
    
    @staticmethod
    async def table_publish_thread(table, host, port,
            lookbacklines=1000, lookbackdate=None, snapshot=False, bandwidth=1e6):

        while True:
            try:
                # Connect to the server
                async with websockets.connect(f"ws://{host}:{port}") as websocket:

                    # Send the subscription message
                    msg = ClientSocket.table_publish_message(
                        table, lookbacklines, lookbackdate, snapshot, bandwidth)
                    msgb = msg.encode('utf-8')
                    await websocket.send(msgb)

                    response = await websocket.recv()
                    if response == b'':
                        msg = 'Subscription %s,%s,%s,table,%s closed  on response!' % \
                            (table.database, table.period,
                                table.source, table.tablename)
                        Logger.log.error(msg)
                        websocket.close()
                        break

                    response = json.loads(response)
                    
                    # Subscription loop
                    client = json.loads(msg)
                    client['conn'] = websocket
                    client['table'] = table
                    client['addr'] = (host, port)
                    client.update(response)
                    await ClientWebSocket.table_publish_loop(client)
                    time.sleep(15)

            except Exception as e:
                msg = 'Retrying subscription %s,%s,%s,table,%s!\n%s' % \
                    (table.database, table.period,
                     table.source, table.tablename, str(e))
                Logger.log.warning(msg)
                time.sleep(15)

    @staticmethod
    async def table_publish_loop(client):
        conn = client['conn']
        addr = client['addr']

        Logger.log.info('Publishing updates of %s/%s/%s/%s -> %s' %
                        (client['database'], client['period'],
                         client['source'], client['tablename'], addr[0]))
                
        table = client['table'].records
        hasindex = table.table.hasindex
        
        if hasindex:
            timestamp = float(client['mtime'])
            datetime_ns = np.datetime64(int(timestamp), 's')
            datetime_ns += np.timedelta64(int((timestamp % 1)*1e9), 'ns')
            client['mtime'] = datetime_ns            
            
            lookbacklines = int(client['lookbacklines'])
            lookbackfromid = None
            if 'lookbackdate' in client:
                lookbackfromdate = pd.Timestamp(client['lookbackdate'])
                lookbackfromid, _ = table.get_date_loc(lookbackfromdate)
                if lookbackfromid == -1:
                    lookbackfromid = table.count

            snapshot = False
            if 'snapshot' in client:
                snapshot = client['snapshot']

            if lookbackfromid is not None:
                lookbackid = lookbackfromid
            else:
                lookbackid = table.count-lookbacklines
            if lookbackid < 0:
                lookbackid = 0
            
            lastsenttimesize = table.size-lookbackid
            lastsentimestartrow = lookbackid
            lastsenttime = np.full((lastsenttimesize,),fill_value=client['mtime'], dtype='datetime64[ns]')

        transfer_rate = 0
        client['maxrows'] = int(
                np.floor(ServerWebSocket.BUFF_SIZE/table.itemsize))
        maxrows = client['maxrows']

        bandwidth = float(client['bandwidth'])

        while True:
            try:
                ids2send = []
                
                lastcount = client['count']

                if hasindex:
                    # mtime update check                    
                    if lookbackfromid is not None:
                        lookbackid = lookbackfromid
                    else:
                        lookbackid = table.count-lookbacklines
                    if lookbackid < 0:
                        lookbackid = 0

                    if table.count>lookbackid:
                        tblcount = table.count.copy()
                        lastsenttimestartid = lookbackid-lastsentimestartrow
                        lastsenttimeendid = tblcount-lastsentimestartrow

                        currmtime = table[lookbackid:tblcount]['mtime'].copy()
                        updtidx = currmtime > lastsenttime[lastsenttimestartid:lastsenttimeendid]
                        if updtidx.any():
                            updtids = np.where(updtidx)
                            if len(updtids) > 0:
                                ids2send.extend(updtids[0]+lookbackid)
                                lastsenttime[lastsenttimestartid:lastsenttimeendid] = currmtime
                                                
                    if snapshot:
                        snapshot = False
                        lastcount = lookbackid

                # count update check
                curcount = table.count.copy()
                if curcount > lastcount:
                    newids = np.arange(lastcount, curcount)
                    ids2send.extend(newids)
                    client['count'] = curcount

                if len(ids2send) > 0:
                    ids2send = np.unique(ids2send)
                    ids2send = np.sort(ids2send)

                    rows2send = len(ids2send)
                    sentrows = 0
                    tini = time.time_ns()
                    while sentrows < rows2send:
                        msgsize = min(maxrows, rows2send)
                        t = time.time_ns()
                        message = table[ids2send[sentrows:sentrows +
                                                 msgsize]].tobytes()
                        compressed = lz4f.compress(message)
                        msgbytes = len(compressed)
                        # msgbytes = msgsize*table.itemsize
                        msgmintime = msgbytes/bandwidth
                        length = struct.pack('!I', len(compressed))
                        # await conn.sendall(length)
                        await conn.send(compressed)
                        sentrows += msgsize
                        msgtime = (time.time_ns()-t)*1e-9
                        ratelimtime = max(msgmintime-msgtime, 0)
                        if ratelimtime > 0:
                            await asyncio.sleep(ratelimtime)

                    totalsize = (sentrows*table.itemsize)/1e6
                    totaltime = (time.time_ns()-tini)*1e-9
                    if totaltime > 0:
                        transfer_rate = totalsize/totaltime
                    else:
                        transfer_rate = 0
                    client['transfer_rate'] = transfer_rate

                # clear watchdog
                client['watchdog'] = time.time_ns()
                await asyncio.sleep(0.001)
            except Exception as e:
                Logger.log.error(
                    'Client %s disconnected with error:%s' % (addr, e))
                time.sleep(5)
                break


if __name__ == '__main__':
    import sys
    from SharedData.Logger import Logger
    from SharedData.SharedData import SharedData
    shdata = SharedData('SharedData.IO.ClientWebSocket', user='master')

    if len(sys.argv) >= 2:
        _argv = sys.argv[1:]
    else:
        msg = 'Please specify IP and port to bind!'
        Logger.log.error(msg)
        raise Exception(msg)

    args = _argv[0].split(',')
    host = args[0]
    port = int(args[1])
    database = args[2]
    period = args[3]
    source = args[4]
    tablename = args[5]
    if len(args) > 6:
        pubsub = int(args[6])
    
    table = shdata.table(database, period, source, tablename)
    if pubsub == 'publish':
        table.publish(host, port)
    elif pubsub == 'subscribe':
        table.subscribe(host, port)

    while True:
        time.sleep(1)        
