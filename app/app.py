from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    app_env = os.getenv("APP_ENV", "development")

    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Cours SysOps</title>
    </head>
    <body>
        <h1>Bienvenue dans le projet Cours SysOps</h1>
        <p>Application Flask opérationnelle.</p>
        <p>Environment: {app_env}</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
