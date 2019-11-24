from flask import render_template, url_for, redirect, flash, request,Blueprint,jsonify,send_file
from chIldcAre import  db,bcrypt
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
from chIldcAre.ml.utils import *
from chIldcAre.ml.prediction import predict
import pandas as pd

ml = Blueprint('ml', __name__)
@ml.route('/plots/plot1', methods=['GET','POST'])
def correlation_matrix():
    bytes_obj = do_plot()
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@ml.route('/test', methods=['GET','POST'])
def test():
	return '<img src="http://localhost:5000/plots/plot1" />'


@ml.route('/predict', methods=['GET','POST'])
def prediction():
	res=predict(['JOy','sadness'])
	return render_template('testTemplate.html',res=res)


@ml.route('/plots/plot2', methods=['GET','POST'])
def correlation_matrix2():
    bytes_obj = do_plot1()
    return send_file(bytes_obj,
                     attachment_filename='plot2.png',
                     mimetype='image/png')

@ml.route('/plots/plot3', methods=['GET','POST'])
def correlation_matrix3():
    bytes_obj = do_plot2()
    return send_file(bytes_obj,
                     attachment_filename='plot3.png',
                     mimetype='image/png')
