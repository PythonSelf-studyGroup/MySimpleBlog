# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, RegistrationForm
from ..decorators import admin_required,permission_required
from ..email import send_email
from flask_login import current_user 


#@auth.route('/',methods=['GET','POSST'])
#@auth.route('/index',methods=['GET','POST'])
#@login_required
#def index():
#    return render_template('auth/index.html')


#登录验证前的动作



#网站登入
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	user = User.query.filter_by(email=form.email.data).first()
    	if user is not None and user.verify_password(form.password.data):
    		login_user(user, form.remember_me.data)
    		flash('valid username or password. 有效的用户名或密码.')
    		return redirect(url_for('main.index'))
    	flash('Invalid username or password. 无效的用户名或密码。')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account', 
                'auth/email/confirm', user=user, token=token) #需要根据实际修改模板位置和文件名称
        flash('A confirmation email has been send to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return "For administrators!"
