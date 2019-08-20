# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from flask_login import login_required

route_index = Blueprint( 'index_page',__name__ )


@route_index.route("/")
@login_required
def index():
    return render_template( "index/index.html" )
