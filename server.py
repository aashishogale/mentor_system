from flask import Flask
from urls import mentor_system
app = Flask(__name__)
app.register_blueprint(mentor_system)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)