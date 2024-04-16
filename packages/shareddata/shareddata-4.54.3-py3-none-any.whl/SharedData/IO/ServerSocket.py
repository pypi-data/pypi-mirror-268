
import time
import sys
import socket
import threading
import time
import select
import numpy as np
import pandas as pd
import json
import os
from cryptography.fernet import Fernet
import lz4.frame as lz4f
import struct

from SharedData.Logger import Logger

#TODO: DONT SERVE DATA IF TABLE IS NOT IN MEMORY
class ServerSocket():

    BUFF_SIZE = 65536 # 64KB
    
    # Dict to keep track of all connected client sockets
    clients = {}
    # Create a lock to protect access to the clients Dict
    lock = threading.Lock()
    server = None
    shdata = None
    accept_clients = None

    @staticmethod
    def runserver(shdata, host, port):

        ServerSocket.shdata = shdata

        ServerSocket.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This line allows the address to be reused
        ServerSocket.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Create the server and start accepting clients in a new thread
        ServerSocket.accept_clients = threading.Thread(
            target=ServerSocket.accept_clients_thread, args=(host, port))
        ServerSocket.accept_clients.start()

    @staticmethod
    def accept_clients_thread(host, port):
        ServerSocket.server.bind((host, port))
        ServerSocket.server.listen()

        Logger.log.info(f'Listening on {host}:{port}')

        while True:
            conn, addr = ServerSocket.server.accept()
            threading.Thread(target=ServerSocket.handle_client_thread,
                             args=(conn, addr)).start()

    @staticmethod
    def handle_client_thread(conn, addr):
        Logger.log.info(f"New client connected: {addr}")
        conn.settimeout(60.0)

        # Add the client socket to the list of connected clients
        with ServerSocket.lock:
            ServerSocket.clients[conn] = {
                'watchdog': time.time_ns(),
                'transfer_rate': 0.0,
            }

        client = ServerSocket.clients[conn]
        client['conn'] = conn
        client['addr'] = addr
                
        try:
            ServerSocket.handle_client_socket(client)
        except Exception as e:
            Logger.log.error(f"Client {addr} disconnected with error: {e}")
        finally:
            with ServerSocket.lock:
                ServerSocket.clients.pop(conn)
            Logger.log.info(f"Client {addr} disconnected.")
            conn.close()

    @staticmethod
    def handle_client_socket(client):
        
        client['authenticated'] = False
        conn = client['conn']
        while not client['authenticated']:
            # Check if there is data ready to be read from the client
            ready_to_read, _, _ = select.select([conn], [], [], 0)
            if not ready_to_read:
                time.sleep(0.1)
            else:
                # Receive data from the client
                data = conn.recv(ServerSocket.BUFF_SIZE)
                if data:
                    # clear watchdog
                    client['watchdog'] = time.time_ns()
                    data = data.decode()
                    login_msg = json.loads(data)
                    # authenticate
                    key = os.environ['SHAREDDATA_SECRET_KEY'].encode()
                    token = os.environ['SHAREDDATA_SOCKET_TOKEN']
                    cipher_suite = Fernet(key)
                    received_token = cipher_suite.decrypt(login_msg['token'].encode())
                    if received_token.decode() != token:
                        errmsg = 'Client %s authentication failed!' % (client['addr'][0])
                        Logger.log.error(errmsg)
                        raise Exception(errmsg)
                    else:
                        client['authenticated'] = True
                        Logger.log.info('Client %s authenticated' % (client['addr'][0]))

                        client.update(login_msg)
                        if client['action'] == 'subscribe':
                            if client['container'] == 'table':
                                ServerSocket.send_table_updates(client)
                        elif client['action'] == 'publish':
                            if client['container'] == 'table':
                                ServerSocket.receive_table_updates(client)

    @staticmethod
    def send_table_updates(client):
        conn = client['conn']
        addr = client['addr']
                           
        Logger.log.info('Serving updates of %s/%s/%s/%s -> %s' %
                    (client['database'], client['period'],
                    client['source'], client['tablename'],addr[0]))
        
        client['table'] = ServerSocket.shdata.table(
            client['database'], client['period'],
            client['source'], client['tablename'])
        table = client['table']
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
                    'Client %s disconnected with error:%s' % (addr,e))
                time.sleep(5)
                break
        
    @staticmethod
    def receive_table_updates(client):
        
        shdata = ServerSocket.shdata

        table = shdata.table(client['database'], client['period'],
                             client['source'], client['tablename'])
        shnumpy = table.records
        hasindex = table.hasindex
        bytes_buffer = bytearray()
        
        conn = client['conn']
        rmsg = {
            'mtime': float(shnumpy.mtime),
            'count': int(shnumpy.count),
        }
        conn.sendall(json.dumps(rmsg))

        while True:
            try:
                # Receive data from the server
                data = conn.recv(4)
                if data == b'':
                    msg = 'Subscription %s,%s,%s,table,%s closed !' % \
                        (table.database, table.period,
                            table.source, table.tablename)
                    Logger.log.warning(msg)
                    conn.close()
                else:  
                    length = struct.unpack('!I', data)[0]
                    
                    compressed = b''
                    while len(compressed) < length:
                        chunk = conn.recv(length - len(compressed))
                        if chunk == b'':
                            msg = 'Subscription %s,%s,%s,table,%s closed !' % \
                                (table.database, table.period,
                                    table.source, table.tablename)
                            Logger.log.warning(msg)
                            conn.close()
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
                conn.close()                
                break


if __name__ == '__main__':

    from SharedData.Logger import Logger
    from SharedData.SharedData import SharedData
    shdata = SharedData('SharedData.IO.ServerSocket', user='master')

    if len(sys.argv) >= 2:
        _argv = sys.argv[1:]
    else:
        errmsg = 'Please specify IP and port to bind!'
        Logger.log.error(errmsg)
        raise Exception(errmsg)
    
    args = _argv[0].split(',')
    host = args[0]
    port = int(args[1])
    ServerSocket.runserver(shdata, host, port)

    Logger.log.info('ROUTINE STARTED!')
    while True:
        n = 0
        sendheartbeat = True
        # Create a list of keys before entering the loop
        client_keys = list(ServerSocket.clients.keys())
        for client_key in client_keys:
            n = n+1
            c = ServerSocket.clients.get(client_key)
            if c is not None:
                if 'table' in c:
                    table = c['table'].table
                    tf = c['transfer_rate']
                    Logger.log.debug('#heartbeat#%.2fMB/s,%i:%s,%s' %
                                    (tf,n, client_key.getpeername(), table.relpath))
                else:            
                    Logger.log.debug('#heartbeat# %i:%s' %
                                    (n, client_key.getpeername()))
                sendheartbeat = False
        if sendheartbeat:
            Logger.log.debug('#heartbeat#host:%s,port:%i' % (host, port))
        time.sleep(15)