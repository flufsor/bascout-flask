from .Scan import Scan, ScanResult


class DnsScan(Scan):
    """Testscan class."""
    name = "Test DNS Scan"
    description = "This is a test dns scan."

    def scan(self) -> ScanResult:
        """Scan target."""
        return ScanResult(
            name=self.name,
            headers=["Type", "Name", "Value"],
            values=[
                ["A", "ap.be", "127.0.0.1"],
                ["A", "mail.ap.be", "ap.be"],
                ["MX", "ap.be", "mail.ap.be"],
            ],
        )