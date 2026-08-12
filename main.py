from flask import Flask,redirect,url_for, render_template


app=Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# a dynamic route that changes based on data provided

@app.route('/user/<user>')
def hello_user(user):
    return f'hello {user}, Welcome to this Flask series'

# Dynamic route using specified var rules
@app.route('/users/<int:userId>')
def user_list(userId):
    return f'Welcome user {userId}'


# url for is very useful for making routes

@app.route('/child')
def child():
    return 'You are a child'

@app.route('/teen')
def teen():
    return 'You are a teen'

@app.route('/adult')
def adult():
    return 'You are an Adult'

@app.route('/age/<int:age>')
def age(age):
    if(age<=12):
        return redirect(url_for('child'))
    elif age>=13 and age<=19:
        return redirect(url_for('teen'))
    else:
        return redirect(url_for('adult'))

# template renderind
@app.route('/home')
def welcome():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True,port=5000)