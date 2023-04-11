const net = require('net');
const socket_path = './socket_file';

class Client {
    constructor(address) {
        this.socket = net.createConnection(address);
        this.socket.setTimeout(3000);
        this.socket.on("connect", () => {
            console.log("connected");
        });
        this.socket.on("data", (data) => {
            console.log("Received data: " + data.toString());
        });
        this.socket.on("end", () => {
            console.log("Disconnected");
        });
        this.socket.on("timeout", () => {
            console.log("Socket timeout");
            this.socket.destroy();
        });
        this.socket.on("error", (e) => {
            console.error(e.message);
        });
    }

    async write(data) {
        try {
            await new Promise((resolve, reject) => {
                this.socket.write(data, (e) => {
                    if (e) {
                        reject(e);
                    } else {
                        resolve();
                    }
                })
            })
        } catch (e) {
            console.error(`Failed to send data: ${data}`);
            throw e;
        }
    }

    async sendAllData(data, interval) {
        for (let i = 0; i < data.length; i++) {
            try {
                await this.write(JSON.stringify(data[i]));
                console.log(`Sent data: ${JSON.stringify(data[i])}`);
                if (i < data.length - 1) {
                    await new Promise((resolve) => setTimeout(resolve, interval));
                }
            } catch (e) {
                console.error(`Failed to send data: ${JSON.stringify(data[i])}`);
            }
        }
        await new Promise((resolve) => this.socket.end(resolve));
    }
}

const client = new Client(socket_path);
client.sendAllData([
    {
        "method": "floor",
        "params": 3.1415,
        "param_types": "double",
        "id": 1
    },
    {
        "method": "nroot",
        "params": [4, 64],
        "param_types": ["int", "int"],
        "id": 2
    },
    {
        "method": "reverse",
        "params": "pythonserver",
        "param_types": "string",
        "id": 3
    },
    {
        "method": "validAnagram",
        "params": ["javascript", "sajtpavcri"],
        "param_types": ["string", "string"],
        "id": 4
    },
    {
        "method": "sort",
        "params": ["banana", "apple", "orange", "grape", "strawberry", "mango"],
        "param_types": "string[]",
        "id": 5
    }
], 0)