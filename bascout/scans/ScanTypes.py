from enum import Enum

from .DnsScan import DnsScan
from .Geoip import GeoIp
from .SlowScan import SlowScan


class ScanTypes(Enum):
    DnsScan = DnsScan
    GeoIp = GeoIp
    SlowScan = SlowScan
