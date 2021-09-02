#!/usr/bin/env python3

"""
This module implements a script to open a WebSocket and send / receive data over that connection.
"""

import sys
import time
import _thread
import websocket


class WebSocketClient:

    def __init__(self, token):
        # Initialize properties
        self.ws = None
        self.token = token

        # Enable trace
        websocket.enableTrace(True)

    def on_message(self, ws, message):
        print("### on_message ###")
        print(message)

    def on_error(self, ws, error):
        print("### on_error ###")
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("### on_close ###")

    def on_open(self, ws):
        print("### on_open ###")

        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            # ws.close()
            # print("thread terminating...")

        if self.ws:
            _thread.start_new_thread(run, ())

    def connect(self):
        # Open the connection
        self.ws = websocket.WebSocketApp(f"ws://localhost:8000/ws/connect?token={self.token}",
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()


# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get input arguments
        token_argv = sys.argv[1]

        # Create the WebSocket client
        client = WebSocketClient(token_argv)

        # Open the connection
        client.connect()
    else:
        # Output error
        print("Missing required parameter ACCESS_TOKEN.\nUsage: python main.py ACCESS_TOKEN")
