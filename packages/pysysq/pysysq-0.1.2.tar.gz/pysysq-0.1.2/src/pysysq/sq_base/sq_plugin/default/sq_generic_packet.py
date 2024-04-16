from ...sq_packet import SQPacket
from dataclasses import dataclass


@dataclass
class SQGenericPacket(SQPacket):
    id: int = 0
    priority: int = 0
    class_name: str = ""
    src: str = ""
    destination: str = ""
