from flask import render_template,url_for, flash,redirect,session,request
from datetime import datetime,timedelta,time
import time,threading
from project import app
from project.loginForm import LoginForm,LogoutForm
from project.wikiForm import WikiForm
from project.eventForm import EventForm,GoogleForm
from project.api import Api
from project.db import Database
from project.scrap import Scrap


@app.route('/',methods=['GET','POST'])
def login():
	loginForm=LoginForm()

	if loginForm.validate_on_submit():
		if loginForm.username.data=='vadon' and loginForm.email.data=='1' and loginForm.password.data=='1':
			session['user']=loginForm.username.data
			return redirect(url_for('index'))
	return render_template('login.html',loginForm=loginForm)

@app.route('/index',methods=['GET','POST'])
def index():

	user=session.get('user')
	logoutForm=LogoutForm(prefix='A')
	wikiForm=WikiForm(prefix='B')
	eventForm=EventForm(prefix='C')
	googleForm=GoogleForm(prefix='D')

	#RUN-UPDATE
	#Scrap().imdb_scrap()
	#Api().twitter_api()
	#Scrap().science_scrap()
	#Scrap().populer_machine()
	#Scrap().youtube_scrap()
	#Scrap().boi_rate()

	#FROM HANDLER
	if logoutForm.validate_on_submit() and logoutForm.logout.data:
		session.pop(logoutForm.username.data,None)
		return redirect(url_for('login'))

	if googleForm.validate_on_submit() and googleForm.submit_g.data:
		Scrap().google_query(googleForm.query_g.data)
		return redirect(url_for('index'))

	
	if wikiForm.validate_on_submit() and wikiForm.submit.data:
		res=Api().wiki_search(wikiForm.query.data)
		if type(res)==list:
			Database().delete_from('wiki_search',None,None)
			Database().insert_into('wiki_search',res[0],user,res[2],res[1],res[3])
			return redirect(url_for('index'))

	if eventForm.validate_on_submit() and eventForm.save_e.data:
		Database().insert_into('events',user,eventForm.event.data,eventForm.hour.data,eventForm.discreption.data,eventForm.type_e.data,eventForm.date.data)
		#flush
		return redirect(url_for('index'))


	#MYSQL SELECT
	rate=Database().select_from('rate')

	events=Database().select_from('events','username',user)

	wikiQuery=Database().select_from('wiki_search','user',user)
	if len(wikiQuery)<1:
		res=Api().wiki_search('internet')
		Database().insert_into('wiki_search',res[0],user,res[2],res[1],res[3])
		wikiQuery=Database().select_from('wiki_search',None,None)

	imdb=Database().select_from('imdb_movie')
	if len(imdb)<1:
		Database().insert_into('imdb_movie',None,None,None,None,None,None,None,None,None,None)
		imdb=Database().select_from('imdb_movie')

	twitter=Database().select_from('twitter_timeline')
	if len(twitter)<1:
		Database().insert_into('twitter_timeline',None,None,None,None,None)
		twitter=Database().select_from('twitter_timeline')

	science_news=Database().select_from('science_news')
	if len(science_news)<1:
		Database().insert_into('science_news',None,None,None,None,None,None)
		science_news=Database().select_from('science_news')

	popluer_machine=Database().select_from('popluer_machine')
	if len(popluer_machine)<1:
		Database().insert_into('popluer_machine',None,None,None,None,None)

	youtube=Database().select_from('yt_channels')


	if 'user' in session:
		user=session.get('user')
		return render_template('index.html'
								,user=user,
								googleForm=googleForm,
								logoutForm=logoutForm,
								rate=rate,
								events=events,
								science_news=science_news,
								popluer_machine=popluer_machine,
								wikiForm=wikiForm,
								wikiQuery=wikiQuery,
								eventForm=eventForm,
								imdb=imdb,
								twitter=twitter,
								youtube=youtube
								)
	
	return redirect(url_for('login'))

