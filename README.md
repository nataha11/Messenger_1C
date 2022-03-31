## Messenger_1C
**Messenger_1C** is a simple UDP messenger. Server receives messages from up to 5 clients at the same time, sends this message to other clients and writes chat history to file chat.txt.<br/>

Usage:<br/>
1. Open terminal.<br/>
2. Make sure you have python3 installed:<br/>
```
sudo apt install python3
```
3. Download the project:<br/>
```
mkdir messenger
cd messenger
git init
git clone https://github.com/nataha11/Messenger_1C.git
chmod +x server.py client.py
```
4. Execute:<br/>
```
./server.py
```
Open another terminal(s) by Ctrl+Shift+T and run<br/>
```
./client.py
```
Write 'hello' and start messaging with yourself.<br/>

To clear chat history run:<br/>
```
rm chat.txt
```

Thanks for using Messenger_1C!
