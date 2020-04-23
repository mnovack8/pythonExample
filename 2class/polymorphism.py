from abc import ABC, abstractmethod


class Stream(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def open(self):
        pass


class NetworkStream(Stream):

    def open(self):
        print("Network Open")


class MemoryStream(Stream):

    def open(self):
        print("Memory Open")


def openAllStreams(streams):
    for stream in streams:
        stream.open()


network = NetworkStream()
memory = MemoryStream()
openAllStreams([network, memory])
