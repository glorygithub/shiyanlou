#! /usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template

qa = Blueprint('qa',__name__,url_prefix='')


@qa.route('/<title>')
@qa.route('/',defaults={'title':None})
def index(title):
	return render_template("qa/index.html",title=title,tem_str="world")

