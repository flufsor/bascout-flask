from .Scan import ScanResult, ScanType


class DnsScan(ScanType):
    """Testscan class."""

    name = "Fake DNS Scan"
    description = "This is a fake dns scan."
    headers = ["Type", "Name", "Value"]

    def scan(self, target: str) -> ScanResult:
        """Scan target."""
        return ScanResult(
            headers=self.headers,
            values=[
                ["A", "ap.be", "127.0.0.1"],
                ["A", "mail.ap.be", "ap.be"],
                ["MX", "ap.be", "mail.ap.be"],
            ],
        )
