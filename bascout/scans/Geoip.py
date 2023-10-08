from .Scan import Scan, ScanResult


class Geoip(Scan):
    """Testscan class."""
    name = "Test Geoip Scan"
    description = "This is a test geoip scan."

    def scan(self) -> ScanResult:
        """Scan target."""
        return ScanResult(
            name=self.name,
            headers=["IP", "Location"],
            values=[
                ["127.0.0.1", "Home"],
                ["1.1.1.1", "Somewhere else"],
            ],
        )