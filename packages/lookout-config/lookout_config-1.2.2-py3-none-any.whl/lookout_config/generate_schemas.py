import os
from pathlib import Path
import json
from dc_schema import get_schema
from lookout_config import LookoutConfig


def generate_schemas():
    """Generates the schemas for the config files"""
    SCHEMAS_PATH = Path(os.path.dirname(__file__)) / "schemas"
    with open(SCHEMAS_PATH / "lookout.schema.json", "w") as f:
        json.dump(get_schema(LookoutConfig), f, indent=2)


if __name__ == "__main__":
    generate_schemas()
