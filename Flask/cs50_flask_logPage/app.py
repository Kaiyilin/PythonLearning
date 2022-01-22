from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session
)

from flask.ext.session import Session