# -*- coding: utf-8 -*-
#==============================================================================
#  coding by ShimchY shimchy@gmail.com and ... 2017
#==============================================================================
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors 