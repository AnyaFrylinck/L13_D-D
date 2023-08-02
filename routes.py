#imports
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D&D.db"
app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False

db = SQLAlchemy(app)

class character(db.Model):
    id =  id = db.Column(db.Integer, primary_key=True)

class p1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    class_level = db.Column(db.String(50))
    race = db.Column(db.String(50))
    alignment = db.Column(db.String(50))
    background = db.Column(db.String(50))
    exp_point = db.Column(db.String(10))

class p1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength_base= db.Column(db.Integer())
    dex_base= db.Column(db.Integer())
    constitution_base= db.Column(db.Integer())
    intelligence_base= db.Column(db.Integer())
    wisdom_base= db.Column(db.Integer())
    charisma_base= db.Column(db.Integer())
    strength_mod= db.Column(db.Integer())
    dex_mod= db.Column(db.Integer())
    constitution_mod= db.Column(db.Integer())
    intelligence_mod= db.Column(db.Integer())
    charisma_mod= db.Column(db.Integer())
    
class p1_colum_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inspiration= db.Column(db.Integer())
    proficiency_bonus= db.Column(db.Integer())
    strength_save_throw= db.Column(db.Integer())
    dex_save_throw= db.Column(db.Integer())
    constitution_save_throw= db.Column(db.Integer())
    intelligence_save_throw= db.Column(db.Integer())
    wisdom_save_throw= db.Column(db.Integer())
    charisma_save_throw= db.Column(db.Integer())
    acrobatics= db.Column(db.Integer())
    animal_handling= db.Column(db.Integer())
    arcana= db.Column(db.Integer())
    athletics= db.Column(db.Integer())
    deception= db.Column(db.Integer())
    history= db.Column(db.Integer())
    insight= db.Column(db.Integer())
    intimidation= db.Column(db.Integer())
    investigation= db.Column(db.Integer())
    medicine= db.Column(db.Integer())
    nature= db.Column(db.Integer())
    preception= db.Column(db.Integer())
    preformance= db.Column(db.Integer())
    persuasion= db.Column(db.Integer())
    religion= db.Column(db.Integer())
    sleight_of_hand= db.Column(db.Integer())
    stealth= db.Column(db.Integer())
    survival= db.Column(db.Integer())
    passive_wisdom= db.Column(db.Integer())

class p1_other_prof_and_languages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proficiencies= db.Column(db.String(200))
    languages= db.Column(db.String(100))

class p1_column_3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    armor_class= db.Column(db.Integer())
    initiative= db.Column(db.Integer())
    speed= db.Column(db.Integer())
    hit_point_max= db.Column(db.Integer())
    current_hit_point= db.Column(db.Integer())
    temp_hit_point= db.Column(db.Integer())
    total_dice_hit= db.Column(db.Integer())
    dice_hit= db.Column(db.Integer())
    successes= db.Column(db.Integer())
    failures= db.Column(db.Integer())

class p1_atk_and_spellcasting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))
    atk_bonus= db. Column(db.Integer())
    damage= db.Column(db.String(50))

class p1_equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))
    cp= db. Column(db.Integer())
    sp= db. Column(db.Integer())
    ep= db. Column(db.Integer())
    gp= db. Column(db.Integer())
    pp= db. Column(db.Integer())

class p1_column_4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personal_traits= db.Column(db.String(400))
    ideals= db.Column(db.String(400))
    bonds= db.Column(db.String(400))
    flaws= db.Column(db.String(400))

class p1_features_and_traits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    features_and_traits= db.Column(db.String(350))


#routes
#home page route 
@app.route('/')
def home():
    return render_template ('home.html' ,)

@app.route ('/create')
def about():
    return render_template ('form.html')


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']= 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite'

    db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, port=8080,
host='0.0.0.0')