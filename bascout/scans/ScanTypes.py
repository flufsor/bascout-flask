from enum import Enum

from .DnsScan import DnsScan
from .Geoip import GeoIp


class ScanTypes(Enum):
    DnsScan = DnsScan
    GeoIp = GeoIp
