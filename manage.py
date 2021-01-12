# -*- coding: utf-8 -*-
#  coding by ShimchY shimchy@gmail.com and ... 2017

import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

#@app.errorhandler(404)
# def page_not_found(e):
#    return render_template('404.html'), 404

#@app.errorhandler(500)
# def internal_server_error(e):
#    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()
