import os
import tomllib
from pathlib import Path


def default_config() -> Path:
    conf_file = Path.home() / ".config" / "inni" / "config.toml"
    if xdg_dir := os.environ.get("XDG_CONFIG_HOME"):
        path = Path(xdg_dir)
        xdg_file = path / "inni" / "config.toml"
        if xdg_file.exists():
            return xdg_file
        elif conf_file.exists():
            return conf_file
        else:
            return xdg_file
    return conf_file


def read_config(path: str):
    with open(path, "rb") as f:
        content = tomllib.load(f)

    defaults = {
        "login": [],
        "logout": [],
        "prompts": {},
    }

    if "inni" not in content:
        content["inni"] = defaults

    for key, value in defaults.items():
        if key not in content["inni"]:
            content[key] = value

    return content
