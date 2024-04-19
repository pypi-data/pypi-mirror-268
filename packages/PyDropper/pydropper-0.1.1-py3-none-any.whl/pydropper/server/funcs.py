import uvicorn
from threading import Thread, Event
import httpx
import time


class Server(Thread):
    def __init__(self):
        super().__init__()
        self.config = uvicorn.Config(
            app="PyDrop.server.server_main:app",
            host="0.0.0.0",
            port=8001,
            log_level="info",
        )
        self.server = uvicorn.Server(config=self.config)
        self._stop_event = Event()

    def run(self):
        self.server.run()

    def stop(self):
        self.server.should_exit = True
        self.server.force_exit = True
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def check_server():
    while True:
        try:
            response = httpx.get("http://localhost:8001")
            if response.status_code == 200:
                print("Server successfully started")
                return
        except httpx.RequestError:
            pass
        print("waiting for server to start")
        time.sleep(0.5)
