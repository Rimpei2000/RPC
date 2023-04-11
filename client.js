const net = require('net')
const server_address = './socket_file'

const socket = net.connect(server_address);

class Client {
    constructor(address) {
        this.socket = net.createConnection(address)
    }

    async sendAllData(data, interval) {
        
    }
}

const client = new Client(server_address);
client.sendAllData([
    {
        "method": "floor",
        "params": 3.1415,
        "param_types": "double",
        "id": 1
    },
    {
        "method": "nroot",
        "params": [3, 9],
        "param_types": ["int", "int"],
        "id": 2
    },
    {
        "method": "reverse",
        "params": "takatoshi",
        "param_types": "string",
        "id": 3
    },
    {
        "method": "validAnagram",
        "params": ["takatoshi", "tishokata"],
        "param_types": ["string", "string"],
        "id": 4
    },
    {
        "method": "sort",
        "params": ["soccer", "baseball", "tennis", "golf"],
        "param_types": "string[]",
        "id": 5
    }
], 0)