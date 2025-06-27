# config.py

import yaml, os
from dotenv import load_dotenv

class DotDict(dict):
    """Recursive dict that supports dot-access (and nested DotDicts)."""
    def __getattr__(self, k):
        v = self.get(k)
        if isinstance(v, dict):
            v = DotDict(v)
        return v
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

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

    # Merge in environment variables (lowercased keys)
    for k, v in os.environ.items():
        # lowercase keys to keep consistency
        config[k.lower()] = v

    _config = DotDict(config)
    return _config
