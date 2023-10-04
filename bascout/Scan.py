from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ScanStatus(Enum):
    """Scan status enum."""
    QUEUED = 0
    RUNNING = 1
    COMPLETED = 2
    FAILED = 3
    CANCELLED = 4
    ABORTED = 5

    def __str__(self):
        return self.name[0] + self.name[1:].lower()

@dataclass
class ScanResult:
    name: str
    headers: list[str]
    values: list

class Scan(ABC):
    name: str
    description: str

    @abstractmethod
    def scan(self, target: str) -> ScanResult:
        ...

class TargetScan():
    id: int
    target: str
    last_update: datetime
    status: ScanStatus
    scan_results: list[ScanResult]

    def __init__(self, id: int, target: str):
        self.id = id
        self.target = target
        self.last_update = datetime.now()
        self.status = ScanStatus.QUEUED
        self.scan_results = list()

