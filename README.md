# About RPC
A remote proceducre call (RPC) is a way for one computer program to ask another program to perform a certain function or task.

The RPC process begins with the client sending a request message to the server. This request message contains the name of the process the client wished to invoke and the required paramseters. The server receives the request, performs the requested processing, and sends a response message back to the client containing the results of the processing.

The main characteristic of RPC is that the client program can make requests as if it were calling a function in the same program, even though it is actually calling a function on a different machine, and the two programs communicate over the network.

This is a useful feature because it allows programs to separate different tasks that need to be performed across multiple machines and still make requests for those tasks in a simple and straightforward manner. 

# Functions
### The server provides the following functions to the client as RPCs.
</br>

・floor(double x): truncates the decimal number x to the nearest integer and returns the result as an integer.

・nroot(int n, int x) : Calculates the value of r in the equation rn = x.

・reverse(string s) : Takes a string s as input and returns a new string that is the reverse of the input string.

・validAnagram(string str1, string str2) : Takes two strings as input and returns a boolean indicating whether or not the two input strings are anagrams of each other.

・sort(string[] strArr) : Takes an array of strings as input, sorts the array, and returns an array of sorted strings.

# Execution and Results
### Server(Python)
![Alt text](./server.png?raw=true "Title")

### Client (JavaScript)
![Alt text](./client.png?raw=true "Title")