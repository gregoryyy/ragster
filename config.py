import yaml
import os
from dotenv import load_dotenv

_config = None

def get_config(path="config.yaml"):
    """
    Load and cache configuration from YAML and .env, merged into one dict.
    """
    global _config
    if _config is not None:
        return _config

    # Load .env variables into environment
    load_dotenv()

    # Load config.yaml
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    # Merge all environment variables (override or add)
    for key, value in os.environ.items():
        config[key.lower()] = value  # lowercase keys to keep consistency

    _config = config
    return _config
