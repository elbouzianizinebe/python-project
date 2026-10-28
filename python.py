from flask import render_template
import json

with open('data.json') as file:
    data = json.load(file)

from flask import Flask
app = Flask (__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template ('home.html' , students=data['students'])
def init_app():
    pass
if __name__ == "__main__":
    init_app()
    app.run(debug=True)