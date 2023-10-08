from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


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
    headers: List[str]
    values: List


class ScanType(ABC):
    name: str
    description: str
    headers: List[str]

    @abstractmethod
    def scan(self, target) -> ScanResult:
        ...

    def __str__(self):
        return self.name


class Scan(ABC):
    def __init__(
        self,
        scan_type: ScanType,
        status: ScanStatus = ScanStatus.QUEUED,
        last_update: datetime = datetime.now(),
    ):
        self.scan_type = scan_type
        self.status = status
        self.result = ScanResult(scan_type.headers, values=[])
        self.last_update = last_update

    def scan(self, target: str):
        self.status = ScanStatus.RUNNING
        try:
            self.result = self.scan_type.scan(target)
            self.status = ScanStatus.COMPLETED
        except Exception as e:
            self.status = ScanStatus.FAILED
            print(f"Scan failed: {str(e)}")

    def __str__(self):
        return f"Scan({self.scan_type}, {self.status}, {self.result})"

    def __repr__(self):
        return self.__str__()


class TargetScan:
    def __init__(self, id: int, target: str):
        self.id = id
        self.target = target
        self.scans = []
        self.last_update = datetime.now()
        self.status = ScanStatus.QUEUED

    def add_scan(self, scan_type: ScanType):
        """Add scan to target."""
        self.scans.append(Scan(scan_type))

    def execute_scans(self):
        """Execute all scans."""
        self.status = ScanStatus.RUNNING
        try:
            for scan in self.scans:
                scan.scan(self.target)
            self.status = ScanStatus.COMPLETED
        except Exception as e:
            self.status = ScanStatus.FAILED
            print(f"Scan failed: {str(e)}")

    def __str__(self):
        return f"TargetScan({self.id}, {self.target}, {self.status}, {self.scans})"

    def __repr__(self):
        return self.__str__()
