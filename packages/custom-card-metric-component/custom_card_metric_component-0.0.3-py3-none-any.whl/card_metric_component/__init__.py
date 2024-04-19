import os
import streamlit.components.v1 as components

_RELEASE = True  


if not _RELEASE:
    _card_metric = components.declare_component(
        "card_metric",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _card_metric = components.declare_component("card_metric", path=build_dir)

def card_metric(dataCards=None, imageWidthHeight="40", skillImageWidthHeight="50", key=None, default=None):
    
    component_value = _card_metric(dataCards=dataCards, imageWidthHeight=imageWidthHeight, skillImageWidthHeight=skillImageWidthHeight, key=key, default=default)

    return component_value
