from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")  # Directly serve index.html from the current folder

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)  # Serve all other files like CSS and JS

if __name__ == "__main__":
    app.run(debug=True)