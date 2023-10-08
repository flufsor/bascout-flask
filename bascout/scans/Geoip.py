from .Scan import ScanResult, ScanType


class GeoIp(ScanType):
    """Testscan class."""

    name = "Fake Geoip Scan"
    description = "This is a test geoip scan."
    headers = ["IP", "Location"]

    def scan(self, target: str) -> ScanResult:
        """Scan target."""
        return ScanResult(
            headers=self.headers,
            values=[
                ["127.0.0.1", "Home"],
                ["1.1.1.1", "Somewhere else"],
            ],
        )
