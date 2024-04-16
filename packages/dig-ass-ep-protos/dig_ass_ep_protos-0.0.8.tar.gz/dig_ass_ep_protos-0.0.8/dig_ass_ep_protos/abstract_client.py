from grpc import insecure_channel
from abc import ABC, abstractmethod

class AbstractClient(ABC):
    def __init__(self, address: str) -> None:
        self._channel = insecure_channel(address)

    # https://stackoverflow.com/a/65131927
    def close(self):
        self._channel.close()
    
    def __enter__(self):
        return self

    def __exit__(self):
        self.close()    
