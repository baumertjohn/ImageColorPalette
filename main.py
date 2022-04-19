# 100 Days of Code Capstone
# Image Color Palette Generator
# A website that finds the most common colors in an uploaded image.

import cv2 as cv
from flask import Flask, render_template

from percent_colors import percent_colors

app = Flask(__name__)


@app.route("/")
def home():
    image = "gfg-660x249.png"
    working_image = cv.imread(f"./static/{image}")
    image_colors = percent_colors(working_image)
    print(image_colors)
    # return render_template("index.html", colors=image_colors)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
