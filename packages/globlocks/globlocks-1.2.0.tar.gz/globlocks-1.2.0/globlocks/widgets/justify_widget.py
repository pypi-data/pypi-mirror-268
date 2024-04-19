from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from ..choices import (
    text_alignment_choices,
)

import json


class JustifyWidget(widgets.RadioSelect):
    template_name = "globlocks/widgets/justify-widget.html"
    option_template_name = "globlocks/widgets/justify-widget-option.html"
    option_inherits_attrs = False
    default_choices = text_alignment_choices

    def __init__(self, attrs=None, choices=None, targets: list[str] = None):
        choices = choices or self.default_choices
        self.targets = targets or []
        super().__init__(attrs=attrs, choices=choices)


    def create_option(self, name, value, label, selected, index, subindex, attrs):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        value = option["value"]
        if value:
            if not value.startswith("text-"):
                value = f"text-{value}"
            option["icon_name"] = value
        return option


    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        attrs["data-controller"] = "justify-widget"
        attrs["data-justify-widget-targets-value"] = json.dumps(self.targets)
        return attrs
    
    class Media:
        js = [
            "globlocks/widgets/justify/justify-controller.js",
            "globlocks/widgets/justify/justify-widget.js",
        ]
        css = {
            "all": [
                "globlocks/widgets/justify/justify-widget.css",
            ]
        }
