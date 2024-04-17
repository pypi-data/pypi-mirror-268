# IMPORTANT
# After changing this file, run `python3 -m gama_config.generate_schemas`
# To re-generate the json schemas

import os
import yaml
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from dacite import from_dict, Config
from typing import Optional, Any, List
from gama_config import LogLevel
from gama_config.helpers import write_config, read_config, find_gama_config, serialise
from greenstream_config.types import CameraOverride

GAMA_VESSEL_FILE_NAME = "gama_vessel.yml"
GAMA_VESSEL_SCHEMA_URL = (
    "https://greenroom-robotics.github.io/gama/schemas/gama_vessel.schema.json"
)


class Mode(str, Enum):
    SIMULATOR = "simulator"
    HARDWARE = "hardware"
    STUBS = "stubs"
    # A silly mode for when you want to actuate but not run autonomy
    # This is useful if you want to run the autonomy on a different computer but still want to actuate
    HARDWARE_ACTUATION_ONLY = "hardware_actuation_only"


class Network(str, Enum):
    SHARED = "shared"
    HOST = "host"


class Variant(str, Enum):
    WHISKEY_BRAVO = "whiskey_bravo"
    EDUCAT = "educat"
    ORACLE_2_2 = "oracle_2_2"
    ORACLE_22 = "oracle_22"
    ARMIDALE = "armidale"


@dataclass
class GamaVesselConfig:
    ros_domain_id: int = 0
    namespace_vessel: str = "vessel_1"
    namespace_groundstation: str = "groundstation"
    variant: Variant = Variant.WHISKEY_BRAVO
    mode: Mode = Mode.SIMULATOR
    network: Network = Network.SHARED
    prod: bool = False
    log_level: LogLevel = LogLevel.INFO
    ubiquity_user: Optional[str] = None
    ubiquity_pass: Optional[str] = None
    ubiquity_ip: Optional[str] = None
    static_peers: Optional[str] = None
    camera_overrides: Optional[List[Optional[CameraOverride]]] = None
    record: bool = False


def parse_vessel_config(config: dict[str, Any]) -> GamaVesselConfig:
    return from_dict(
        GamaVesselConfig,
        config,
        config=Config(cast=[Mode, Network, Variant, LogLevel]),
    )


def get_vessel_config_path():
    return find_gama_config() / GAMA_VESSEL_FILE_NAME


def read_vessel_config(path: Optional[Path] = None) -> GamaVesselConfig:
    return read_config(path or get_vessel_config_path(), parse_vessel_config)


def read_vessel_config_env() -> GamaVesselConfig:
    config_str = os.environ.get("GAMA_VESSEL_CONFIG")
    if config_str is None:
        raise ValueError("GAMA_VESSEL_CONFIG environment variable not set")
    return parse_vessel_config(yaml.safe_load(config_str))


def write_vessel_config(config: GamaVesselConfig):
    return write_config(get_vessel_config_path(), config, GAMA_VESSEL_SCHEMA_URL)


def serialise_vessel_config(config: GamaVesselConfig):
    return serialise(config)
