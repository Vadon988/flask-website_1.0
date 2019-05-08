from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from project.api import Api
from project.db import Database

class Scrap():

	def google_query(cls,query):
		url='https://www.google.com/en'
		driver=webdriver.Firefox(executable_path='project/geckodriver.exe')
		try:
			driver.get(url)
			input_=driver.find_element_by_class_name('gLFyf')
			input_.send_keys(query)
			btn=driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[3]/center/input[1]')
			btn.click()
		except Exception as err:
			print(err)



	def boi_rate(cls):

		url=['https://www.boi.org.il/en/Markets/ExchangeRates/Pages/Default.aspx']
		driver=webdriver.Firefox(executable_path='project/geckodriver.exe')
		for x in url:
			try:
				driver.get(x)
				soup=BeautifulSoup(driver.page_source,'lxml')
				td=soup.find_all('td')
				list_rate=[]
				for z in td:
					#rate=z.find('td',{'data-wcag-dynamic-font':'true'}).text
					list_rate.append(z.text)
				if len(list_rate)>1:
					Database().delete_from('rate')
					d_rate=list_rate[8]
					d_xrate=list_rate[9]
					p_rate=list_rate[14]
					p_xrate=list_rate[15]
					y_rate=list_rate[20]
					y_xrate=list_rate[21]
					e_rate=list_rate[26]
					e_xrate=list_rate[27]
					Database().insert_into('rate',d_rate,d_xrate,p_rate,p_xrate,y_rate,y_xrate,e_rate,e_xrate)
				
			except Exception as err:
				print(err)
			finally:
				driver.close()

	def imdb_scrap(cls):
		url='https://www.imdb.com/?ref_=nv_home'
		#try:
		r=requests.get(url)
		if r.status_code==200:
			Database().delete_from('imdb_movie',None,None)
			soup=BeautifulSoup(r.text,'lxml')
			link=soup.find_all('div',class_='title')
			x=0
			while x<3:
				film=(link[x].text)
				Api().imdb_api(film)
				x+=1

	def youtube_scrap(cls):
		
		url=[
				'https://www.youtube.com/user/schafer5/videos',
				'https://www.youtube.com/user/TechGuyWeb/videos',
				'https://www.youtube.com/channel/UCnxGkOGNMqQEUMvroOWps6Q/videos'
			]
		Database().delete_from('yt_channels')
		for z in url:
			try:
				driver=webdriver.Firefox(executable_path=r'project/geckodriver.exe')
				driver.get(z)
				soup=BeautifulSoup(driver.page_source,'lxml')
				link=soup.find_all('a',id='video-title')
			
				x=0
				yt_dict={'title':[],'views':[],'href':[]}
				while x<len(link):
					temp=link[x].get('aria-label')
					if temp!=None and temp!='':
						yt_dict['title'].append(temp.split('by')[0])
						yt_dict['views'].append(temp.split('by')[1])
					href=link[x].get('href')
					if href!=None and href!='':
						href=href.split('=')[1]
						yt_dict['href'].append(href)
					x+=1
			
				if yt_dict!=None:
					i=0
					while i<5:
						Database().insert_into('yt_channels',None,yt_dict['title'][i],yt_dict['views'][i],yt_dict['href'][i],)
						i+=1
			except Exception as err:
				print(err)
			finally:
				driver.close()

	def science_scrap(cls):

		url=['https://www.scientificamerican.com/']
		driver=webdriver.Firefox(executable_path=r'project/geckodriver.exe')
		try:
			for z in url:
				driver.get(z)
				soup=BeautifulSoup(driver.page_source,'lxml')
				#grid=soup.find('div',class_='listing-wide__thumb')
				grid=soup.find_all('div',class_='grid__col large-up-1 medium-1-2')
				h3=soup.find_all('div',class_='listing-wide__inner')
				p=soup.find_all('p',class_='t_body listing-wide__inner__desc')
				meta=soup.find_all('div',class_='t_meta')
				science_dict={'source':[],'img':[],'link':[],'title':[],'text':[],'meta':[]}
				
				for x in grid:
					source=x.find('source')['srcset']
					img=x.find('img')['src']
					science_dict['source'].append(source)
					science_dict['img'].append(img)
					
				for x in h3:
					link=x.find('a')['href']
					title=x.find('a').string
					science_dict['link'].append(link)
					science_dict['title'].append(title)
				
				for x in p:
					text=x.string
					science_dict['text'].append(text)
				

				for x in meta:
					meta=x.string
					science_dict['meta'].append(meta)

				if science_dict['source']!=None:
					Database().delete_from('science_news')
					x=0
					while x<5:
						Database().insert_into('science_news',str(science_dict['source'][x]),str(science_dict['img'][x]),str(science_dict['link'][x]),str(science_dict['title'][x]),str(science_dict['text'][x]),str(science_dict['meta'][x]))
						x+=1
				
		except Exception as err:
			print(err)
		finally:
			driver.close()

	def populer_machine(cls):

		url=['https://www.popularmechanics.com/']
		driver=webdriver.Firefox(executable_path='project/geckodriver.exe')
		for z in url:
			try:
				driver.get(z)
				soup=BeautifulSoup(driver.page_source,'lxml')
				link_item=soup.find_all('div',class_='full-item')
				dict_items={'link':[],'img':[],'title':[],'content':[],'author':[]}
				
				for x in link_item:
					link=x.find('a',class_='full-item-image item-image')['href']
					img=x.find('span')['data-lqip']
					img=img.split('?')[0]
					title=x.find('a',class_='full-item-title item-title').string
					content=x.find('div',class_='full-item-dek item-dek').text
					author=x.find('span',class_='byline-name').string
					
					dict_items['link'].append(link)
					dict_items['img'].append(img)
					dict_items['title'].append(title)
					dict_items['content'].append(content)
					dict_items['author'].append(author)

				if dict_items['link']!=None:
					Database().delete_from('popluer_machine')
				z=0
				while z<len(dict_items['link']):
					if z>1 and z<7:
						Database().insert_into('popluer_machine',str(dict_items['link'][z]),str(dict_items['img'][z]),str(dict_items['title'][z]),str(dict_items['content'][z]),str(dict_items['author'][z]))
					z+=1
				
			except Exception as err:
				print(err)
			finally:
				driver.close()

		




