from flask import render_template

from flask import Flask
app = Flask (__name__)
lessons =[
{
     'title' : "lesson 1",
     'course': "python",
     'professor': " ahmed",
},
{
     'title' : "lesson 2",
     'course': "c",
     'professor': "omar",
}    
    ]
@app.route("/")
@app.route("/home")

def home():
    return render_template ('home.html', lessons=lessons)
# @app.route("/about")
# def about():
#    return render_template ('about.html')
if __name__ == "__main__":
    app.run(debug=True)