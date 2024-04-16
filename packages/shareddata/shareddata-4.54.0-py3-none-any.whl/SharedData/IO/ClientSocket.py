import time
import sys
import socket
import numpy as np
import pandas as pd
import json
import os
from cryptography.fernet import Fernet
import lz4.frame as lz4f
import struct

from SharedData.Logger import Logger
from SharedData.IO.ServerSocket import ServerSocket


class ClientSocket():
    @staticmethod
    def table_subscribe_thread(table, host, port, 
        lookbacklines=1000, lookbackdate=None, snapshot=False, bandwidth=1e6):
        
        while True:
            try:
                # Connect to the server
                client_socket = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))

                # Send the subscription message
                msg = ClientSocket.table_subscribe_message(
                    table, lookbacklines, lookbackdate, snapshot)
                msgb = msg.encode('utf-8')
                bytes_sent = client_socket.send(msgb)

                # Subscription loop
                ClientSocket.table_subscription_loop(table, client_socket)
                time.sleep(15)

            except Exception as e:
                msg = 'Retrying subscription %s,%s,%s,table,%s!\n%s' % \
                    (table.database, table.period,
                     table.source, table.tablename, str(e))
                Logger.log.warning(msg)
                time.sleep(15)

    @staticmethod
    def table_subscribe_message(table, lookbacklines, lookbackdate, snapshot, bandwidth):
        shnumpy = table.records        
                
        key = os.environ['SHAREDDATA_SECRET_KEY'].encode()        
        cipher_suite = Fernet(key)
        cipher_token = cipher_suite.encrypt(os.environ['SHAREDDATA_SOCKET_TOKEN'].encode())
        msg = {
            'token': cipher_token.decode(),
            'action': 'subscribe',
            'database': table.database,
            'period': table.period,
            'source': table.source,
            'container': 'table',
            'tablename': table.tablename,
            'count': int(shnumpy.count),
            'mtime': float(shnumpy.mtime),
            'lookbacklines': lookbacklines,
            'bandwidth': bandwidth
        }
        if isinstance(lookbackdate, pd.Timestamp):            
            msg['lookbackdate'] = lookbackdate.strftime('%Y-%m-%d')
        if snapshot:
            msg['snapshot'] = True
        msg = json.dumps(msg)
        return msg
    
    @staticmethod
    def table_subscription_loop(table, client_socket):
        shnumpy = table.records
        hasindex = table.hasindex
        bytes_buffer = bytearray()
        
        while True:
            try:
                # Receive data from the server
                data = client_socket.recv(4)                
                if data == b'':
                    msg = 'Subscription %s,%s,%s,table,%s closed !' % \
                        (table.database, table.period,
                            table.source, table.tablename)
                    Logger.log.warning(msg)
                    client_socket.close()
                else:  
                    length = struct.unpack('!I', data)[0]
                    
                    compressed = b''
                    while len(compressed) < length:
                        chunk = client_socket.recv(length - len(compressed))
                        if chunk == b'':
                            msg = 'Subscription %s,%s,%s,table,%s closed !' % \
                                (table.database, table.period,
                                    table.source, table.tablename)
                            Logger.log.warning(msg)
                            client_socket.close()
                            raise Exception(msg)
                        compressed += chunk

                    data = lz4f.decompress(compressed)
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
                client_socket.close()                
                break

    @staticmethod
    def table_publish_thread(table, host, port, 
        lookbacklines=1000, lookbackdate=None, snapshot=False, bandwidth=1e6):
        
        while True:
            try:
                # Connect to the server
                client_socket = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))

                # Send the subscription message
                msg = ClientSocket.table_subscribe_message(
                    table, lookbacklines, lookbackdate, snapshot)
                msgb = msg.encode('utf-8')
                bytes_sent = client_socket.send(msgb)

                response = client_socket.recv(1024)
                if response == b'':
                    msg = 'Subscription %s,%s,%s,table,%s closed on response!' % \
                        (table.database, table.period,
                            table.source, table.tablename)
                    Logger.log.error(msg)
                    client_socket.close()
                    break
                response = json.loads(response)

                # Subscription loop
                client = json.loads(msg)
                client['conn'] = client_socket
                client['table'] = table
                client['addr'] = (host, port)
                client.update(response)
                ClientSocket.table_publish_loop(client)
                time.sleep(15)

            except Exception as e:
                msg = 'Retrying subscription %s,%s,%s,table,%s!\n%s' % \
                    (table.database, table.period,
                     table.source, table.tablename, str(e))
                Logger.log.warning(msg)
                time.sleep(15)
    
    @staticmethod
    def table_publish_message(table, lookbacklines, lookbackdate, snapshot, bandwidth):
        shnumpy = table.records        
                
        key = os.environ['SHAREDDATA_SECRET_KEY'].encode()        
        cipher_suite = Fernet(key)
        cipher_token = cipher_suite.encrypt(os.environ['SHAREDDATA_SOCKET_TOKEN'].encode())
        msg = {
            'token': cipher_token.decode(),
            'action': 'publish',
            'database': table.database,
            'period': table.period,
            'source': table.source,
            'container': 'table',
            'tablename': table.tablename,
            'count': int(shnumpy.count),
            'mtime': float(shnumpy.mtime),
            'lookbacklines': lookbacklines,
            'bandwidth': bandwidth
        }
        if isinstance(lookbackdate, pd.Timestamp):            
            msg['lookbackdate'] = lookbackdate.strftime('%Y-%m-%d')
        if snapshot:
            msg['snapshot'] = True
        msg = json.dumps(msg)
        return msg
    
    @staticmethod
    def table_publish_loop(client):
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
                np.floor(ServerSocket.BUFF_SIZE/table.itemsize))
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
                        message = table[ids2send[sentrows:sentrows + msgsize]].tobytes()
                        compressed = lz4f.compress(message)
                        msgbytes = len(compressed)
                        # msgbytes = msgsize*table.itemsize
                        msgmintime = msgbytes/bandwidth
                        length = struct.pack('!I', len(compressed))
                        conn.sendall(length)
                        conn.sendall(compressed)
                        sentrows += msgsize
                        msgtime = (time.time_ns()-t)*1e-9
                        ratelimtime = max(msgmintime-msgtime,0)
                        if ratelimtime > 0:
                            time.sleep(ratelimtime)

                    totalsize = (sentrows*table.itemsize)/1e6
                    totaltime = (time.time_ns()-tini)*1e-9
                    transfer_rate = totalsize/totaltime                                            
                    client['transfer_rate'] = transfer_rate

                # clear watchdog
                client['watchdog'] = time.time_ns()
                time.sleep(0.001)
            except Exception as e:
                Logger.log.error(
                    'Client %s disconnected with error:%s' % (addr, e))
                time.sleep(5)
                break


if __name__ == '__main__':
    import sys
    from SharedData.Logger import Logger
    from SharedData.SharedData import SharedData
    shdata = SharedData('SharedData.IO.ClientSocket', user='master')

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