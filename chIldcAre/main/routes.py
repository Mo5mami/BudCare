from flask import render_template, url_for, redirect, flash, request,Blueprint,jsonify,send_file
from chIldcAre import  db,bcrypt
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
import pandas as pd
from chIldcAre.ml.utils import *

parents={"name" : "Ahmed" , "surname" : "Bay" }
child1={"name" : "Mohamed" , "surname" : "Bay" }
child2={"name" : "Ibrahim" , "surname" : "Bay" }
child3={"name" : "Nour" , "surname" : "Bay" }
children=[child1,child2,child3]


main = Blueprint('main', __name__)

#@main.route("/", methods=['GET', 'POST'])
@main.route("/parent", methods=['GET', 'POST'])
def parent():
	return render_template('template1.html',user=current_user,parent=parents,children=children)

@main.route("/parent/<n>/<name>", methods=['GET', 'POST'])
def child(n,name):
	data=tweets_table("tweets.csv")
	print(data.columns)
	return render_template('template2.html',user=current_user,parent=parents,children=children,number=int(n),data=data,name=name)

