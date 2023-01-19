import sqlite3
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config["DEBUG"] = True

UPLOAD_FOLDER = r'static\files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mydb = sqlite3.connect("dataset.db")

mcr = mydb.cursor()

for x in mcr:
    print(x)
