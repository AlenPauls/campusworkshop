"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr1n8u9tun42u5707g-a.oregon-postgres.render.com",
        database="demo_80cg",
        user="demo_80cg_user",
        password="Hj6pjvPBg0jUS5anFsvH5P6jXUpyBUik")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
