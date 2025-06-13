from flask import Flask,g,request,render_template,redirect, url_for, flash, session
import numpy as np
import pandas as pd
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


from sklearn.preprocessing import StandardScaler
from src.pipeline.test_model import CustomData,PredictPipeline

application=Flask(__name__)

app=application

app.secret_key = 'your_secret_key'

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # to access columns by name
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/services/login')
def login():
    return render_template('services/login.html')

@app.route('/services/registration')
def register():
    return render_template('services/registration.html')

@app.route('/get_information', methods=['GET', 'POST'])
def get_information():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        try:
            
            c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return render_template('services/login.html')
        except sqlite3.IntegrityError:
            flash('Email already exists!', 'danger')
        finally:
            conn.close()
    return render_template('services/registration.html')

@app.route('/get_login', methods=['POST'])
def get_login():
    email = request.form['email']
    password = request.form['password']
    conn = sqlite3.connect('database.db')
    cur  = conn.cursor()
    cur.execute("SELECT name, password, is_admin FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    print("EMAIL:", email)
    print("PASSWORD:", password)

    if row and check_password_hash(row[1], password):
        session['user']       = row[0]        # username
        session['user_email'] = email         # email
        session['is_admin']   = bool(row[2])  # True/False
        flash("Login successful!", "success")
        return render_template('home.html')
    else:
        flash("Invalid email or password.", "error")
        return render_template('services/login.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('progress.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    
@app.route('/admin_users')
def admin_users():
    if 'user_email' not in session or session['user_email'] != 'megharashokashok@gmail.com':
        return redirect(url_for('login'))  # restrict non-admins
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, email,password FROM users")
    users = c.fetchall()
    conn.close()
    return render_template('services/admin_user.html', users=users)

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)      


