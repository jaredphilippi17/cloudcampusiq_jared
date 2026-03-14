from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to CloudCampusIQ!"

@app.route("/courses")
def courses():
    return jsonify({
        "courses": [
            "Cloud Computing Fundamentals",
            "Python for Beginners",
            "Cybersecurity Basics"
        ]
    })

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == '__main__':
    app.run()
