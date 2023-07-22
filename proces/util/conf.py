from typing import List, Dict
from pkg_resources import resource_stream

from ruamel.yaml import YAML

yaml = YAML()


def get_yaml(stream_args: List) -> Dict:
    with resource_stream(*stream_args) as stream:
        return yaml.load(stream)


def get_conf() -> Dict:
    stream_args = ["proces", "conf/default.yaml"]
    return get_yaml(stream_args)
