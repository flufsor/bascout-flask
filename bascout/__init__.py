from flask import Flask, flash, redirect, render_template, request, url_for

from .config import Config
from .scans import ScanTypes, TargetScan
from .test_data import scans_list

SCANTYPES = list(map(lambda x: x.name, ScanTypes))


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    @app.route("/")
    def index():
        return scans()

    @app.route("/scans")
    def scans():
        scans = scans_list[:20]
        return render_template("scans/overview.html", scans=scans_list)

    @app.route("/scans/add", methods=["GET", "POST"])
    def add_scan():
        if request.method == "POST":
            target = request.form["target"]
            scantypes = request.form.getlist("scantypes")

            if not target:
                flash("Target is required")
            elif not scantypes:
                flash("Scantype is required")
            else:
                new_target_scan = TargetScan(len(scans_list), target)

                for scantype in scantypes:
                    if scantype in ScanTypes.__members__:
                        scan_type = ScanTypes[scantype].value()
                        new_target_scan.add_scan(scan_type)
                        scan_type.scan(target)

                scans_list.append(new_target_scan)

                new_target_scan.execute_scans()

                return redirect(url_for("scans"))

        return render_template("scans/add.html", scantypes=SCANTYPES)

    @app.route("/scan/<int:scan_id>")
    def scan(scan_id: int):
        scan = scans_list[scan_id]
        print(scan)
        return render_template("scans/detail.html", targetscan=scan)

    return app
