print('hello')

import asyncio
import websockets

import json

import serial
from serial.tools.list_ports import comports

ser = None

async def echo(websocket, path):
    print('echo')
    async for message in websocket:
        response = parseCommand(message)
        print(response)
        await websocket.send(str(json.dumps(response)))


        # await websocket.send(greeting)
        # print(f"> {greeting}")

def parseCommand(cmd):
    global ser
    content = json.loads(cmd)
    print(content)
    cmd = content['cmd']

    if cmd == 'getPortsList':
        portslist = getPortsList()
        return {"cmd":"portsList", "data":portslist}
    elif cmd == 'openSerial':
        portName = content['portName']
        baudrate = content['baudrate']
        ser = serial.Serial(portName,baudrate = baudrate, timeout=0.1)
        return {"cmd":"connectedPort", "name":ser.name}
    elif cmd == 'sendMsg':
        msg = content['msg']
        encode_string = msg.encode()
        btye_array = bytearray(encode_string)
        print(btye_array)
        ser.write(btye_array)
        data = ser.read(40)
        print('received:', data)
        return {"cmd":"distData", "data": data.hex()}
    elif cmd == 'hexMsg':
        msg = content['msg']
        byte_array = bytes.fromhex(msg)
        print(byte_array)
        ser.write(byte_array)
        data = ser.read(40)
        print('received:', data)
        return {"cmd": "distData", "data": data.hex()}





def getPortsList():
    portslist = []
    for n, (port, desc, hwid) in enumerate(comports(), 1):
        if hwid != 'n/a':
            portslist.append(port)
    return portslist

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 5000))
asyncio.get_event_loop().run_forever()