import json
import os

from bascout import TargetScan


def load_scans():
    scans = []
    directory = os.path.join(os.getcwd(), 'results')

    for filename in os.listdir(directory):
        full_filename = os.path.join(directory, filename)
        if filename.endswith(".json"):
            with open(full_filename, 'r') as f:
                scans.append(json.loads(f.read()))
    return scans

print(load_scans())

def scanTarget(target):
    targetScan = TargetScan(0,target)

