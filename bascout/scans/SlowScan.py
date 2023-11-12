import time
from datetime import datetime

from .Scan import ScanResult, ScanType


class SlowScan(ScanType):
    """SlowScan class."""

    name = "Slowscan"
    description = "This is a Slowscan to test background scanning."
    headers = ["time"]

    def scan(self, target: str) -> ScanResult:
        """Scan target."""
        start = datetime.now()

        time.sleep(50)

        end = datetime.now()

        print(end - start)

        return ScanResult(
            headers=self.headers,
            values=[
                [end - start],
            ],
        )
