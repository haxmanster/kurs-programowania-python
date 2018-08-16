from flask import Flask, render_template
import platform
import os
import sys

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('index.html')

@app.route('/about')

def about():
  return render_template('about.html')

@app.route('/Login')

def login():
  return render_template('login.html')

@app.route('/register')

def register():
  return render_template('register.html')

@app.route('/location')

def location():
  return render_template('location.html')

status = [platform.uname()]

def platform():
    for info in status:
      return info
  return

app.jinja_env.globals.update(platform=platform)

if __name__ == "__main__":
    app.run()
