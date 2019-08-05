from flask import Flask, render_template

app = Flask(__name__)
#object     #function

#decorator - determines what func below it does
@app.route('/home')
@app.route('/index') #read
@app.route('/') #url for endpoint (landing page)
def index(): #called on route '/'
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/detail') #read
def detail():
    return 'Detail page'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/post') #create
def post():
    return render_template('post.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/update')
def update():
    return render_template('post.html')


#errors

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
            #allow changes to code displayed by server
                        #default to server pages
