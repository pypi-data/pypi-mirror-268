from django.views.generic import TemplateView

from django_react_flow.parsers.yaml import YAMLParser
from django_react_flow.settings import django_react_flow_settings


class ReactFlowView(TemplateView):
    template_name = "react_flow.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        yaml_parser = YAMLParser()
        parsed_data = yaml_parser.parse(
            path=django_react_flow_settings.file,
        )
        context["nodes"] = parsed_data.get("nodes", [])
        context["edges"] = parsed_data.get("edges", [])

        return context
