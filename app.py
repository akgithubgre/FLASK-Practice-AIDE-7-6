from flask import Flask, render_template

app=Flask(__name__)

#create a route decorator
# otherwise @app.route('/index.html')
@app.route('/')# routed to dashboard
# def index():
#     return "<h1>HEllo World!</h1>"


# safe
# capitalize
# lower
# upper
# title
# trim
# striptags
def index():
    favourite=['a','b','c','d',123456]
    first_name="John"
    stuff="This is <strong>BOLD</strong> Text"
    return render_template("index.html",first_name=first_name,stuff=stuff,favourite=favourite)
#localhost:5000/user/john
@app.route('/user/<name>')
# def user(name):
#     return "<h1>Hello {} </h1>".format(name)
def user(name):
    return render_template("user.html",user_name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)