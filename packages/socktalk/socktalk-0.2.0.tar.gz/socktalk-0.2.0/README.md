# "socktalk" Socket-based AI chat server and multi-user chat client

## Install "socktalk" from Github
If installing from the github repository, create and enter a virtual environment:  
Clone the socktalk repository to your working folder if you haven't already, then enter into terminal:  
"cd socktalk"  
Hit enter, then run:  
"python setup.py install"

## Install "socktalk" using pip
If installing socktalk using pip, create and enter a virtual environment then enter into your terminal:  
"pip install socktalk"  

You can use the following terminal commands:
1) "socktalk --ai": Runs the chat server with a connected AI client. Uses gpt-3.5-turbo model by default.
    You should create an environment file named ".env" in the working directory from which you execute the terminal
    commands to call the package, in order to adjust the AI modes and chat server settings.

    Below is an example for your .env file. You will need to update the OpenAI chatgpt API key. In order for the API key
    to function you will need to load at least 5$ of credit on your OpenAI account. The AI client has two modes which
    can be toggled on or off using "True" or "False". AI response intervals can be adjusted. AI model can be adjusted.
    Mode2 content can be adjusted. You can adjust a setting to send the full chat history to the chatgpt API, so that
    the chatbot will have memory. See below for more details.
    

   ### AI Client Modes:
i. Respond every N lines: the bot reads the conversation and responds to the conversation once every N lines  
ii. Respond every N seconds: the bot says something completely new and unrelated every N seconds

-------------------------------------------
### ".env" file example

    OPENAI_API_KEY=<OPENAI_API_KEY_HERE>  
    SERVER_IP_ADDRESS=127.0.0.1  
    SERVER_PORT=1234  
    SEND_FULL_CHAT_HISTORY=True  
    AI_MODE1_ACTIVE=True  
    AI_MODE1_INTERVAL=1  
    AI_MODE1_MODEL=gpt-3.5-turbo  
    AI_MODE2_ACTIVE=True  
    AI_MODE2_INTERVAL=60  
    AI_MODE2_MODEL=gpt-3.5-turbo  
    AI_MODE2_CONTENT="Say something interesting from a random Wikipedia page and start your response with 'Did you know', but don't mention the source."

-------------------------------------------

2) "socktalk --server": Runs a chat server without a connected AI client. No .env file necessary.


3) "socktalk --client": Runs the advanced multi-user chat client.  


4) "socktalk --terminal": Runs the simplistic and limited terminal-based multi-user chat client.





## Python Networking Task: Building a Chat Server and Client

Server

The server should be able to handle multiple clients concurrently. It should be able to receive a message from a client and broadcast it to all other connected clients. The server should use non-blocking sockets and select.select() to handle multiple connections.

Client

The client should be able to connect to the server, send messages, and receive messages from other clients. The client should be able to send and receive messages concurrently. You can use threading to handle sending and receiving messages concurrently.

Message Protocol

The server and client should use a simple protocol for messages. Each message should start with a fixed-length header that contains the length of the actual message. This way, the server knows when it has received the full message. The client should follow this protocol when sending messages.

Requirements

The server should be able to handle multiple clients concurrently.
The client should be able to send and receive messages concurrently.
The server should broadcast incoming messages to all connected clients.
The client and server should use a simple protocol for messages.

AI Client

The AI client will connect to the server and respond to the chat. It has two modes:
1. Respond every N lines: the bot reads the conversation and responds to the conversation once every N lines
2. ⁠Respond every N seconds: the bot says something completely new and unrelated every N seconds



