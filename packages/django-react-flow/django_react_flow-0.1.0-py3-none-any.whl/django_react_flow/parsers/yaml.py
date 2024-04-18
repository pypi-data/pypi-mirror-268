from pathlib import Path

import yaml
from yaml import Loader

from django_react_flow.parsers.base import Parser


class YAMLParser(Parser):

    def parse(self, path: Path) -> dict | list:
        file_content = path.read_text()
        return yaml.load(file_content, Loader=Loader)
