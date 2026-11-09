"""REST API for the band's picture catalogue."""
from . import app
import os
import json
from flask import jsonify, request, url_for

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
with open(json_url, encoding="utf-8") as source:
    data = json.load(source)


def find_picture(picture_id):
    return next((picture for picture in data if picture["id"] == picture_id), None)


def read_picture():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or not isinstance(payload.get("id"), int):
        return None
    return payload


@app.route("/health")
def health():
    return jsonify(status="OK"), 200


@app.route("/count")
def count():
    return jsonify(length=len(data)), 200


@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data), 200


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = find_picture(id)
    if picture is None:
        return jsonify(message="Picture not found"), 404
    return jsonify(picture), 200


@app.route("/picture", methods=["POST"])
def create_picture():
    picture = read_picture()
    if picture is None:
        return jsonify(message="A JSON object with an integer id is required"), 400
    if find_picture(picture["id"]) is not None:
        return jsonify(Message=f"picture with id {picture['id']} already present"), 302
    data.append(picture.copy())
    return jsonify(picture), 201, {"Location": url_for("get_picture_by_id", id=picture["id"])}


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    picture = find_picture(id)
    if picture is None:
        return jsonify(message="Picture not found"), 404
    replacement = read_picture()
    if replacement is None or replacement["id"] != id:
        return jsonify(message="Body id must match the URL id"), 400
    picture.clear()
    picture.update(replacement)
    return jsonify(picture), 200


@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    picture = find_picture(id)
    if picture is None:
        return jsonify(message="Picture not found"), 404
    data.remove(picture)
    return "", 204
