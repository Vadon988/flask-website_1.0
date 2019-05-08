import wikipedia
import requests
import json,os
from twython import Twython
from project.db import Database
from datetime import datetime

class Api():

	def config(cls):
		#print(os.getcwd())
		json_file='/home/vadon/Desktop/Code/config.init'
		with open(json_file,'r',encoding='utf-8') as f:
			data=json.loads(f.read())
		return data
		

	def wiki_search(cls,query):
		
		try:
			page=wikipedia.page(query)
			title=page.title
			content=wikipedia.summary(query,sentences=6)
			img=page.images[1]
			url=page.url
			wiki_list=[title,img,content,url]
			return wiki_list
		except Exception as err:
			return err

	def github_api(cls):
		r=requests.get('https://api.github.com/users/:vadon998/repos')
		print(r.text)

	def twitter_api(cls):
		config=cls.config()
		
		API_KEY=config['twitter'][0]['api_key']
		API_SECRET_KEY=config['twitter'][0]['api_secret_key']
		ACCESS_TOKEN=config['twitter'][0]['access_token']
		ACCESS_TOKEN_SECRET=config['twitter'][0]['access_token_secret']

		twitter=Twython(API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
		twitter=twitter.get_home_timeline()
		if twitter!=None:
			Database().delete_from('twitter_timeline',None,None)
		x=0
		while x<len(twitter):
			try:
				created=twitter[x]['created_at']
				text=twitter[x]['text']
				link=twitter[x]['user']['url']
				name=twitter[x]['user']['screen_name']
				img=twitter[x]['user']['profile_image_url']
				Database().insert_into('twitter_timeline',created,text,link,name,img)
				x+=1
			except Exception as err:
				print(err)
	
	def imdb_api(cls,movie):
		config=cls.config()
		config=config['omdb']
		url=f'http://www.omdbapi.com/?apikey={config}&t={movie}'
		try:
			r=requests.get(url)
			if r.status_code==200:
				data=json.loads(r.text)
				title=data['Title']
				year=data['Year']
				runtime=data['Runtime']
				genre=data['Genre']
				director=data['Director']
				actors=data['Actors']
				plot=data['Plot']
				poster=data['Poster']
				rating=data['imdbRating']
				production=data['Production']
				Database().insert_into('imdb_movie',title,year,runtime,genre,director,actors,plot,poster,rating,production)


		except Exception as err:
			print(err)