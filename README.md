# R2100LIDAR-data-reader-server 

A serial reader build with python and pass data out to a website via websocket.


## Tech Stack

- serial
- websockets


  
## Usage/Examples (with javascript )

### Basic patten

```javascript
    const msg = { cmd: 'hexMsg', msg: this.hexMsg };
    this.ws.send(JSON.stringify(msg));
```

### Get serial port list

```javascript
    const requestPortsMsg = { cmd: 'getPortsList' };
    this.ws.send(JSON.stringify(requestPortsMsg));
```

### Connect to serial 

```javascript
    const msg = { cmd: 'openSerial', portName: this.portName, baudrate: this.baudrate };
    this.ws.send(JSON.stringify(msg));
```

### Send message to serial device

```javascript
    const msg = { cmd: 'sendMsg', msg: this.msg };
    this.ws.send(JSON.stringify(msg));
```



  
