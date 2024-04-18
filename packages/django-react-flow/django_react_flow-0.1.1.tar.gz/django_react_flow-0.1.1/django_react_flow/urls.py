from django.urls import path

from django_react_flow.views.react_flow import ReactFlowView


urlpatterns = [
    path("flow", ReactFlowView.as_view()),
]
