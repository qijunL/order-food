# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, url_for, redirect, flash, jsonify, json

from application import app
from common.models.User import User
from form.user import LoginForm
from flask_login import login_user, logout_user
route_user = Blueprint('user_page', __name__)


@route_user.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST'and form.validate():
        user = User.query.filter_by(login_name=form.login_name.data).first()
        if user:  # and user.check_password(form.login_pwd.data):
            app.logger.info("进到了判断")
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('index_page.index')
            return redirect(next)
        else:
            return None
    return render_template("user/login.html")
    # return json.dumps(request.form)

@route_user.route('/logout', methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('index_page.index'))

@route_user.route( "/edit" )
def edit():
    return render_template( "user/edit.html" )


@route_user.route( "/reset-pwd" )
def resetPwd():
    return render_template( "user/reset_pwd.html" )