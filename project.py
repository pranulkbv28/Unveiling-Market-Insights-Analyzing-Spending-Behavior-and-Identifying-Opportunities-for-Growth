rom flask import Flask

app =Flask(name)
@app.route("/")
def index():
    return render_template('project.html')