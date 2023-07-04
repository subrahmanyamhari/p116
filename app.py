# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home1():

    name = "subrahmanyam hari" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home2():

    name = "SK hari" # write your name
    age = "47" # write your age

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/mother")
def home3():

    name = "Sushama hari" # write your name
    age = "44" # write your age

    return render_template('mother.html' , name = name , age = age)
# define the route to friends webpage
@app.route("/friends")
def home4():
    name = "Aarav and Arihant"  # write your name
    age = "13 and 14"  # write your age

    return render_template('friends.html', name=name, age=age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
