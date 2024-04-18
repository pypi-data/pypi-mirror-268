from pathlib import Path

from django.conf import settings as project_settings
from pydantic import Field
from pydantic_settings import BaseSettings

NAMESPACE = "DJANGO_REACT_FLOW"


class DjangoReactFlowSettings(BaseSettings):
    file: Path = Field(..., description="Yaml file path for building flows")


django_react_flow_namespace_settings: dict = getattr(project_settings, NAMESPACE, {})
django_react_flow_settings = DjangoReactFlowSettings(**django_react_flow_namespace_settings)
