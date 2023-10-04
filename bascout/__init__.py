from flask import Flask, render_template

from .DnsScan import DnsScan
from .Scan import ScanStatus, TargetScan
from .test_data import scans_list


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_prefixed_env(prefix="BASCOUT")

    @app.route('/')
    def index():
        return scans()

    @app.route('/scans')
    def scans():
        scans = scans_list[:20]
        return render_template('scans/overview.html', scans = scans_list)
    
    @app.route('/scan/<int:scan_id>')
    def scan(scan_id: int):
        scan = scans_list[scan_id]
        return render_template('scans/detail.html', targetscan = scan)
    
    return app