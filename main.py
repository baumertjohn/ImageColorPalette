# 100 Days of Code Capstone
# Image Color Palette Generator
# A website that finds the most common colors in an uploaded image.

import os
import shutil

import cv2 as cv
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename

from percent_colors import percent_colors

UPLOAD_FOLDER = "./working_image"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


def allowed_file(filename):
    """Takes a filename and checks for image extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    # Clear upload folder and create empty before uploading file
    try:
        shutil.rmtree(UPLOAD_FOLDER)
    except FileNotFoundError:
        pass
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    if request.method == "POST":
        file = request.files["file"]
        if allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("show_image", user_image=filename))
        else:
            error = (
                'Please choose a image file with extension ".jpg", ".jpeg", or ".png".'
            )
    return render_template("index.html", error=error)


@app.route("/showimage/<user_image>")
def show_image(user_image):
    working_image = cv.imread(app.config["UPLOAD_FOLDER"] + "/" + user_image)
    image_colors = percent_colors(working_image)
    return render_template("showimage.html", image=user_image, colors=image_colors)


@app.route("/workingimage/<filename>")
def working_image(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
