'''We can use a templating language like Jinja to integrate our python code or variables into html so as to avoid creating multiple html files for the same type of content. 

For example, in a blog, every blog post structure is the same and so we need not build a html file for eahc post.

Jinja can be used by adding code inside {{}} brackets. We can also pass kwargs into the render_template function and use those variable names in the jinja template brackets.'''

from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    num = random.randint(1, 100)
    year = datetime.date.today().year
    return render_template("index.html", rand = num, year = year)
    '''Here rand is a kwarg and it is passed to the html file and integrated using jinja'''

if __name__ == "__main__":
    app.run(debug=True)