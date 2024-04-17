import os
from pathlib import Path
from typing import Optional, Any

from ipfabric import IPFClient
from pydantic import BaseModel

IPF, CONFIGS = None, []


class ConfigFile(BaseModel):
    file: Path
    parsed: Optional[Any] = None


def check_ipfabric(ipf):
    """Check IP Fabric Settings if Configs Exists."""
    settings = []
    try:
        settings = [
            d["taskId"]
            for d in ipf.get(f"snapshots/{ipf.snapshot_id}/settings").json()[
                "discoveryTasks"
            ]
        ]
    except:
        print("Could not get Snapshot please check the token policies/roles.")

    if "tasks/deviceConfig/configSaved" in settings:
        raise NotImplementedError(
            "Saved Config Consistency Discovery Task Not Enabled."
        )


def pytest_addoption(parser):
    parser.addoption(
        "--config-dir",
        help="Path to directory with configurations.",
        action="store",
        type=Path,
    )
    parser.addoption(
        "--snapshot",
        help="Optional: IP Fabric Snapshot ID; defaults to `$last`.",
        action="store",
        default=None,
        type=str,
    )


def pytest_configure(config):
    global IPF, CONFIGS

    if config.getoption("--config-dir"):
        cfg_dir = config.getoption("--config-dir").resolve()
        CONFIGS = [ConfigFile(file=cfg_dir / f) for f in os.listdir(cfg_dir)]
    else:
        IPF = IPFClient(snapshot_id=config.getoption("--snapshot"))
        check_ipfabric(IPF)
