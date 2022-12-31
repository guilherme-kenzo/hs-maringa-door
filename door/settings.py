import os

DEBUG = os.getenv("DEBUG", False)
PORT = os.getenv("PORT", 5000)
SECRET_KEY = os.getenv("SECRET_KEY")
HOST = os.getenv("HOST", "127.0.0.1")

if SECRET_KEY == "":
    raise ValueError("SECRET_KEY env variable must be set.")
