# 100 Days of Code Capstone
# Image Color Palette Generator
# A website that finds the most common colors in an uploaded image.

import os

import cv2 as cv
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from percent_colors import percent_colors

UPLOAD_FOLDER = "./static"
ALLOWED_EXTENSIONS = {"jpg", "png"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_PATH"] = 1_000_000


@app.route("/", methods=["GET", "POST"])
def home():
    # os.remove(os.path.join(app.config["UPLOAD_FOLDER"]), '*.*')
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("show_image", user_image=filename))
    return render_template("index.html")


@app.route("/showimage/<user_image>")
def show_image(user_image):
    working_image = cv.imread(os.path.join(app.config["UPLOAD_FOLDER"], user_image))
    image_colors = percent_colors(working_image)
    # os.remove(user_image)
    return render_template("showimage.html", image=user_image, colors=image_colors)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
