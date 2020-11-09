#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IS211 Assignment 11

from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import SubmitForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '885c34b9e491e7f7633ae91e671b964d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Submit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Task('{self.task}', {self.email}, {self.priority})"


# View list of todo items
@app.route('/')
def home():
    entries = Submit.query.all()
    return render_template('home.html', entries=entries)

# The submit page needs: A textbox input for the task named 'task'.
# A textbox input for the task's email named 'email'.
# A dropdown box for the user to choose low, medium, or high named 'priority'.
# A submit button with the label 'Add To Do Item'.
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # return render_template('submit.html', title='Submit')
    form = SubmitForm()
    if form.validate_on_submit():
        # START DROP DOWN EFFORT HERE

        task = Submit(task=form.task.data, email=form.email.data, priority=form.priority.data)
        db.session.add(task)
        db.session.commit()
        flash(f'Task for {form.email.data} added.', 'success')
        return redirect(url_for('home'))


    return render_template('submit.html', form=form)


@app.route('/clear', methods=['GET', 'POST'])
def clear():
    num_rows_deleted = db.session.query(Submit).delete()
    db.session.commit()
    return render_template('clear.html', title='Clear List')


if __name__ == '__main__':
    app.run(debug=True)
