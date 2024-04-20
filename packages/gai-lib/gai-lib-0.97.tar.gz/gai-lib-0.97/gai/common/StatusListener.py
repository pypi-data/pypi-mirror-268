import websockets
import json
from gai.common.logging import getLogger
logger = getLogger(__name__)
logger.setLevel("INFO")

class StatusListener:

    def __init__(self, uri):
        self.uri = uri
        self.cancellation_token = None

    async def listen(self, callback=None):
        async with websockets.connect(self.uri) as websocket:
            logger.info(f"Connected to {self.uri}")
            try:
                while self.cancellation_token is None:
                    message = await websocket.recv()
                    if callback:
                        callback(message)
                    logger.info(f"Received status update: {message}")

                    if message == "<stop>":
                        self.cancellation_token = message

            except websockets.exceptions.ConnectionClosed as e:
                logger.error(f"Connection closed: {e}")

    def stop(self):
        self.cancellation_token = "<stop>"
        logger.info("Stopping listener")
        return self.cancellation_token
    
