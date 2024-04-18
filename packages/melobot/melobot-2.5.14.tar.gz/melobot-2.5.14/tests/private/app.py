from flask import Flask, render_template

path = r"E:\projects\Python\git-proj\melobot\docs\build\html"
app = Flask(__name__, static_folder=path, static_url_path="/", template_folder=path)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
