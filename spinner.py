import threading
import time

class Spinner:
    def __init__(self, message: str = "Loading"):
        self.message = message
        self._stop_running = False
        self._thread = threading.Thread(target=self._spinner_task)

    def _spinner_task(self) -> None:
        symbols = "|/-\\"
        idx = 0
        while not self._stop_running:
            print(f"\r{self.message}... {symbols[idx % len(symbols)]}", end="")
            idx += 1
            time.sleep(0.1)
        print("\r" + " " * (len(self.message) + 10) + "\r", end="")  # Clear line

    def start(self) -> None:
        self._thread.start()

    def stop(self) -> None:
        self._stop_running = True
        self._thread.join()
