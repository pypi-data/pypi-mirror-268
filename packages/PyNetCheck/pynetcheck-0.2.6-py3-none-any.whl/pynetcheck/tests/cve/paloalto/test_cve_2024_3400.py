"""
https://security.paloaltonetworks.com/CVE-2024-3400
"""

import re

import pytest
from netutils.os_version import compare_version_loose

from pynetcheck.models.device import IPFDevice
from pynetcheck.tests.paloalto.conftest import PA_FW

pytestmark = [pytest.mark.cve, pytest.mark.paloalto]

TELEMETRY = re.compile(r"\s?telemetry enable;")
GLOBAL_PROTECT = re.compile(
    r"^\s*global-protect\s*\{[^}]*(portals|gateways) enable;[^}]*",
    flags=re.DOTALL | re.M,
)


@pytest.mark.parametrize(
    "device", PA_FW, ids=[d.inventory.hostname for d in PA_FW], scope="class"
)
class TestPaloAltoTelemetryGlobalProtect:
    # If no devices then skip
    __test__ = True if PA_FW else False

    @pytest.fixture(autouse=True, scope="class")
    def load_device_data(self, device: IPFDevice):
        if not device.loaded:
            device.load_data()
        if not device.config.current:
            pytest.skip("No configs for device.")
        yield
        device.clear_data()

    def test_device_telemetry_disabled(self, device: IPFDevice):
        if (
            (
                compare_version_loose(device.inventory.version, ">=", "11.1")
                and compare_version_loose(device.inventory.version, "<", "11.1.2-h3")
            )
            or (
                compare_version_loose(device.inventory.version, ">=", "11.0")
                and compare_version_loose(device.inventory.version, "<", "11.0.4-h1")
            )
            or (
                compare_version_loose(device.inventory.version, ">=", "10.2")
                and compare_version_loose(device.inventory.version, "<", "10.2.7-h8")
            )
            or (
                compare_version_loose(device.inventory.version, ">=", "10.2.8")
                and compare_version_loose(device.inventory.version, "<", "10.2.8-h3")
            )
            or (
                compare_version_loose(device.inventory.version, ">=", "10.2.9")
                and compare_version_loose(device.inventory.version, "<", "10.2.9-h1")
            )
        ):
            telemetry = bool(TELEMETRY.search(device.config.current))
            global_protect = bool(GLOBAL_PROTECT.search(device.config.current))
            assert not (
                telemetry and global_protect
            ), ("Possibly Vulnerable: Device Telemetry enabled with GlobalProtect Gateway and/or Portal. "
                "Please upgrade device or disable telemetry.")
        pytest.skip(
            f"{device.inventory.hostname}:{device.inventory.sn} is not an affected SW Version {device.inventory.version}."
        )
