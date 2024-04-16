# IMPORTANT
# After changing this file, run `python3 -m lookout_config.generate_schemas`
# To re-generate the json schemas
import yaml
import os
from dataclasses import dataclass, field
from enum import Enum
from dacite import from_dict, Config
from typing import Optional, Any, List, Annotated
from dc_schema import SchemaAnnotation
from dataclasses import asdict
from pathlib import Path
from greenstream_config.types import CameraOverride


LOOKOUT_CONFIG_FILE_NAME = "lookout.yml"
LOOKOUT_SCHEMA_URL = "https://greenroom-robotics.github.io/lookout/schemas/lookout.schema.json"


def join_lines(*lines: str) -> str:
    return "\n".join(lines)


class Mode(str, Enum):
    SIMULATOR = "simulator"
    HARDWARE = "hardware"
    STUBS = "stubs"
    ROSBAG = "rosbag"


class LogLevel(str, Enum):
    INFO = "info"
    DEBUG = "debug"


class Network(str, Enum):
    SHARED = "shared"
    HOST = "host"


@dataclass
class LookoutConfig:
    ros_domain_id: int = 0
    namespace_vessel: str = "vessel"
    gama_vessel: bool = False
    mode: Mode = Mode.STUBS
    log_level: LogLevel = LogLevel.INFO
    camera_overrides: Optional[List[Optional[CameraOverride]]] = None
    network: Network = Network.HOST
    gpu: bool = False


def find_config() -> Path:
    """Returns the path to the .config/greenroom directory"""
    return Path.home().joinpath(".config/greenroom")


def dacite_to_dict(obj: Any):
    def dict_factory(data: Any):
        def convert_value(obj: Any):
            if isinstance(obj, Enum):
                return obj.value
            return obj

        return {k: convert_value(v) for k, v in data}

    return asdict(obj, dict_factory=dict_factory)


def get_path():
    return find_config() / LOOKOUT_CONFIG_FILE_NAME


def parse(config: dict[str, Any]) -> LookoutConfig:
    return from_dict(
        LookoutConfig,
        config,
        config=Config(cast=[LogLevel, Mode, Network]),
    )


def read() -> LookoutConfig:
    path = get_path()
    with open(path) as stream:
        return parse(yaml.safe_load(stream))


def write(config: LookoutConfig):
    path = get_path()
    # Make the parent dir if it doesn't exist
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w") as stream:
        print(f"Writing: {path}")
        headers = f"# yaml-language-server: $schema={LOOKOUT_SCHEMA_URL}"
        data = "\n".join([headers, yaml.dump(dacite_to_dict(config))])
        stream.write(data)
