from dataclasses import dataclass


@dataclass
class SQPacket:
    size: int = 0
    timestamp: int = 0
