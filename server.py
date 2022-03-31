#!/usr/bin/env python3

import socket
import codecs

PORT = 65535

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.bind(('', PORT))
    file_chat = open('chat.txt', 'a')
    clients = set()
    print('Listening on port', PORT)

    while True:
        try:
            data, addr_info = s.recvfrom(4096)
            
            if addr_info not in clients:
                if len(clients) == 5:
                    continue
                file_chat.write('New client: (\'%s\', %s)\n' % addr_info)
                clients.add(addr_info)   
                         
            file_chat.write('Client %s: %s\n' % (addr_info, data.decode('utf-8')))

            for client_addr in clients:
                s.sendto(data, client_addr)
                
        except KeyboardInterrupt:
            break
    
    s.close()
    file_chat.close()

if __name__== '__main__':
    main()  