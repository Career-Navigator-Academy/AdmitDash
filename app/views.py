from flask import Blueprint, render_template

views_bp = Blueprint("views", __name__)


@views_bp.route("/", methods=["GET"])
def home():
    val = {"c_name": "John"}
    return render_template("index.html", **val)
