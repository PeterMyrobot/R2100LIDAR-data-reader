# R2100LIDAR-data-reader-server 

# A Python serial reader 

A serial reader User interface build with vue.js.

Accept serial data via websockets and plot on canvas after parse it.




## Tech Stack

- Vue.js
- canvas
- websockets


  
## Run Locally

Need to work with real device and the serial read part build by pyhton [repo](https://github.com/PeterMyrobot/R2100LIDAR-data-reader-server)

Clone the project

```bash
  git clone https://github.com/PeterMyrobot/R2100LIDAR-data-reader-client.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
    yarn install
```

Start the server

```bash
    yarn serve
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



  
