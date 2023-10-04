from .DnsScan import DnsScan
from .Geoip import Geoip
from .Scan import ScanStatus, TargetScan

scans_list = []

apscan = TargetScan(0, "ap.be")
apscan.scan_results.extend((DnsScan().scan(), Geoip().scan()))
apscan.status = ScanStatus.COMPLETED
apscan.last_update = apscan.last_update.replace(day=apscan.last_update.day -3, hour=apscan.last_update.hour - 1)
scans_list.append(apscan)

apscan = TargetScan(1, "google.com")
apscan.scan_results.append(DnsScan().scan())
apscan.status = ScanStatus.RUNNING
scans_list.append(apscan)