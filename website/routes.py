from website import application, db
from flask import render_template, redirect, request, flash, url_for
from website.forms import LoginForm, RegistrationForm, ChallengeForm
from flask_login import current_user, login_user, login_required, logout_user
from website.models import User, Levels
from werkzeug.urls import url_parse
from instance import config


@application.route('/')
@application.route('/home')
@login_required
def home():
    user = User.query.filter_by(username=current_user.username).first()
    return render_template('index.html', title="Welcome!", user=user)

@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title="Log In", form=form)

@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, rank='1')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register!", form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@application.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    info = User.query.filter_by(username=current_user.username).first()
    return render_template('account.html', title="Account", user=info, levels=info.levels)

@application.route('/create',  methods=['GET', 'POST'])
@login_required
def create():
    form = ChallengeForm()
    if form.validate_on_submit():
        level = Levels(title=form.title.data, description=form.description.data, output=form.output.data, user_id=current_user.id)
        db.session.add(level)
        db.session.commit()
        flash ('Congratulations, you have created a new level!', 'success')
        return redirect(url_for('account'))
    return render_template('create.html', title='Create Level', form=form)