from flask import Blueprint
from pluggy import HookimplMarker

from .models import *  # noqa: F403, F401

impl = HookimplMarker("svcishop")


@impl
def svcishop_load_blueprints(app):
    discount = Blueprint("discount", __name__)
    app.register_blueprint(discount, url_prefix="/discount")
