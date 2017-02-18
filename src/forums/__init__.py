#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-01-25 20:10:50 (CST)
# Last Update:星期六 2017-2-18 21:42:16 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Flask
from flask_maple.lazy import LazyExtension
from admin.urls import admin
from .urls import register_routes
from .logs import register_logging
from .filters import register_jinja2
import os


def create_app(config=None):
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))

    app = Flask(__name__, template_folder=templates, static_folder=static)
    app.config.from_object(config)
    register(app)
    return app


def register(app):
    register_extension(app)
    register_routes(app)
    register_logging(app)
    register_jinja2(app)


def register_extension(app):
    extension = LazyExtension(
        module='forums.extension.',
        extension=['db', 'avatar', 'cache', 'csrf', 'bootstrap', 'captcha',
                   'error', 'redis_data', 'principal', 'babel',
                   'login_manager', 'maple_app', 'mail', 'middleware'])
    extension.init_app(app)
    admin.init_app(app)
