import logging
import sys

from flask import Flask, jsonify, redirect, render_template, request, url_for

from db import get_connection

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s %(message)s",
)

app = Flask(__name__)


@app.get("/")
def index():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, author, title, content, status, created_at
                FROM tickets
                ORDER BY created_at DESC, id DESC
                """
            )
            tickets = cursor.fetchall()

    return render_template("index.html", tickets=tickets)


@app.post("/tickets")
def create_ticket():
    author = request.form.get("author", "").strip()
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if not author or not title or not content:
        return "author, title and content are required", 400

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tickets (author, title, content)
                VALUES (%s, %s, %s)
                """,
                (author, title, content),
            )

    app.logger.info("ticket_created author=%s title=%s", author, title)

    return redirect(url_for("index"), code=303)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)