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
                    s.sendto(b'Error: too many clients (5)', addr_info)        
                    continue
                file_chat.write('New client: (\'%s\', %s)\n' % addr_info)
                clients.add(addr_info)
                  
            file_chat.write('Client %s: %s\n' % (addr_info, data.decode('utf-8')))
            if data.decode('utf-8') == 'exit':
                clients.remove(addr_info)
                file_chat.write('Disconnected: (\'%s\', %s)\n' % addr_info)
                
            for client_addr in clients:
                s.sendto(data, client_addr)
                
        except KeyboardInterrupt:
            break
    
    s.close()
    file_chat.close()

if __name__== '__main__':
    main()  