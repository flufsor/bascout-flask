from .scans import DnsScan, GeoIp, TargetScan

scans_list = []

apscan = TargetScan(0, "ap.be")
dns_scan = DnsScan()
apscan.add_scan(DnsScan())
apscan.add_scan(GeoIp())

googlescan = TargetScan(0, "google.be")
googlescan.add_scan(DnsScan())
googlescan.add_scan(GeoIp())

scans_list.extend([apscan, googlescan])

for target_scan in scans_list:
    target_scan.execute_scans()
