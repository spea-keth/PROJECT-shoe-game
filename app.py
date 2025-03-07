from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #ORM
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)
#object     #function

#sync db to app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Shoesdb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'password'
    #dictionary #key        #value

#reference db
db = SQLAlchemy(app)

#create db models (table)
class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(50), nullable=False) #java int
    price = db.Column(db.Integer)
    size = db.Column(db.Integer)

#create form for data input
class ShoeForm(FlaskForm):
    #object             #label                  #list with 1 item
    name = StringField("Shoe Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    image = FileField("Add Picture", validators=[DataRequired()])
    price = IntegerField("Enter Price", validators=[DataRequired()])
    size = IntegerField("Enter Size", validators=[DataRequired()])
    btn_submit = SubmitField("Save")

#decorator - determines what func below it does
@app.route('/home')
# #read
@app.route('/') #url for endpoint (landing page)
def index(): #called on route '/'
    query = Shoe.query.all()
    app_title = "Shoe-Game | Home "
    return render_template('index.html', shoes=query, title=app_title)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/detail/<int:shoe_id>') #read
def detail(shoe_id):
    try:
        shoe = Shoe.query.filter_by(id=shoe_id).first()
        return render_template('detail.html', shoe=shoe)
    except:
        msg = "No shoe found"
        return redirect(url_for('index'))
                        #called index()



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/post',methods=['GET','POST']) #create
def post():
    form = ShoeForm()
    if form.validate_on_submit():
        form_name = form.name.data
        form_description = form.description.data
        form_image = form.image.data
        form_price = form.price.data
        form_size = form.size.data

        shoe = Shoe(name=form_name, description=form_description, image=form_image, price=form_price, size=form_size)
        db.session.add(shoe) #save data to db
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('post.html', form=form)

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
