from flask import render_template, Flask
from app import create_app
from app.Operations import Filer

# config
app = create_app()

@app.route("/")
def index():
    data = Filer().read()
    return render_template("index.html",done=1, data=data)

if __name__=="__main__":
    app.run(port=8000, debug=True)