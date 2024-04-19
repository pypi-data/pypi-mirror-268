from sample.appliance.appliance import SampleAppliance
from sample.appliance.config import LocalConfig, ApplianceConfig
from sample.widgets.globals import set_appliance_for_dash


def run_server():
    set_appliance_for_dash(SampleAppliance(LocalConfig()))
    from app import app
    app.run(debug=True, port=8045)


if __name__ == '__main__':
    run_server()
else:
    set_appliance_for_dash(SampleAppliance(ApplianceConfig()))
    from app import app

    SERVER = app.server
