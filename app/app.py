from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/tickets")
def create_ticket():
    author = request.form.get("author", "").strip()
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if not author or not title or not content:
        return "author, title and content are required", 400

    return redirect(url_for("index"), code=303)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)