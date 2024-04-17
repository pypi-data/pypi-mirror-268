"""Tools related to Jinja2 template engine."""

from __future__ import annotations

import jinja2


def get_cssfinder_jinja2_environment() -> jinja2.Environment:
    """Get Jinja2 environment with default settings."""
    return jinja2.Environment(
        loader=jinja2.PackageLoader("cssfinder"),
        autoescape=jinja2.select_autoescape(),
    )
