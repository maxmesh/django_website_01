import os

from django.db import models
class siteTitleManager(models.Manager):
	def control_number(self):
		if len(site_title.objects.all())==0:
			site_title.objects.create()
		elif len(site_title.objects.all())>1:
			for obj in site_title.objects.all():
				if obj.id!=1:
					if obj.title_icon.path.find(
							'\\default.png')==-1 and obj.title_icon.path.find(
						'/default.png')==-1:
						if os.path.isfile(obj.title_icon.path):
							os.remove(obj.title_icon.path)
					obj.delete()
		return site_title.objects.filter(id=1).get()
	def change_title(self,title):
		site_title_obj=site_title.objects.filter(id=1).get()
		site_title_obj.title=title
		site_title_obj.save()
		return site_title_obj
	def change_icon(self,icon):
		site_title_obj=site_title.objects.filter(id=1).get()
		if site_title_obj.title_icon.path.find(
				'\\default.png')==-1 and site_title_obj.title_icon.path.find(
			'/default.png')==-1:
			if os.path.isfile(site_title_obj.title_icon.path):
				os.remove(site_title_obj.title_icon.path)
		site_title_obj.title_icon=icon
		site_title_obj.save()
		return site_title_obj
class site_title(models.Model):
	title=models.CharField(max_length=100)
	title_icon=models.ImageField(upload_to='title_ico/',
								 default='title_ico/default/default.png',
								 blank=True)
	objects=siteTitleManager()
class slideshowManager(models.Manager):
	def create_slide(self):
		slide=slideshow.objects.create(slide_title='title',
									   slide_body_text="slide body text")
		return slide
	def change_slide_img(self,id,img):
		slide=slideshow.objects.filter(id=id).get()
		if slide.slide_img.path.find(
				'\\default.png')==-1 and slide.slide_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(slide.slide_img.path):
				os.remove(slide.slide_img.path)
		slide.slide_img=img
		slide.save()
		return slide
	def change_slide_title(self,id,title):
		slide=slideshow.objects.filter(id=id).get()
		slide.slide_title=title
		slide.save()
		return slide
	def change_slide_body_text(self,id,text):
		slide=slideshow.objects.filter(id=id).get()
		slide.slide_body_text=text
		slide.save()
		return slide
	def remove_slide(self,id):
		slide=slideshow.objects.filter(id=id).get()
		if slide.slide_img.path.find(
				'\\default.png')==-1 and slide.slide_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(slide.slide_img.path):
				os.remove(slide.slide_img.path)
		slide.delete()
		return slide
	def move_up(self,id):
		slide=slideshow.objects.filter(id=id).get()
		slide_img_copy=slide.slide_img
		slide_title_copy=slide.slide_title
		slide_body_text_copy=slide.slide_body_text
		id_=int(id)-1
		while not slideshow.objects.filter(id=str(id_)).exists():
			id_-=1
		slide_=slideshow.objects.filter(id=str(id_)).get()
		slide.slide_img=slide_.slide_img
		slide.slide_title=slide_.slide_title
		slide.slide_body_text=slide_.slide_body_text
		slide.save()
		slide_.slide_img=slide_img_copy
		slide_.slide_title=slide_title_copy
		slide_.slide_body_text=slide_body_text_copy
		slide_.save()
		return slide
	def move_down(self,id):
		slide=slideshow.objects.filter(id=id).get()
		slide_img_copy=slide.slide_img
		slide_title_copy=slide.slide_title
		slide_body_text_copy=slide.slide_body_text
		id_=int(id)+1
		while not slideshow.objects.filter(id=str(id_)).exists():
			id_+=1
		slide_=slideshow.objects.filter(id=str(id_)).get()
		slide.slide_img=slide_.slide_img
		slide.slide_title=slide_.slide_title
		slide.slide_body_text=slide_.slide_body_text
		slide.save()
		slide_.slide_img=slide_img_copy
		slide_.slide_title=slide_title_copy
		slide_.slide_body_text=slide_body_text_copy
		slide_.save()
		return slide
class slideshow(models.Model):
	slide_img=models.ImageField(upload_to='slides_img/',
								default='slides_img/default/default.png',
								blank=True)
	slide_title=models.CharField(max_length=100)
	slide_body_text=models.TextField()
	objects=slideshowManager()
class videoManager(models.Manager):
	def create_video(self):
		_video=video.objects.create(video_title='title',
									video_description="video description")
		return _video
	def change_cover_img(self,id,img):
		_video=video.objects.filter(id=id).get()
		if _video.cover_img.path.find(
				'\\default.png')==-1 and _video.cover_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.cover_img=img
		_video.save()
		return _video
	def change_video_title(self,id,title):
		_video=video.objects.filter(id=id).get()
		_video.video_title=title
		_video.save()
		return _video
	def change_video_description(self,id,text):
		_video=video.objects.filter(id=id).get()
		_video.video_description=text
		_video.save()
		return _video
	def change_video_url(self,id,url):
		_video=video.objects.filter(id=id).get()
		_video.video_url=url
		_video.save()
		return _video
	def flip(self,id):
		_video=video.objects.filter(id=id).get()
		_video.video_R_dir=not _video.video_R_dir
		_video.save()
		return _video
	def remove_video(self,id):
		_video=video.objects.filter(id=id).get()
		if _video.cover_img.path.find(
				'\\default.png')==-1 and _video.cover_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.delete()
		return _video
	def move_up(self,id):
		_video=video.objects.filter(id=id).get()
		cover_img_copy=_video.cover_img
		video_title_copy=_video.video_title
		video_description_copy=_video.video_description1
		video_url_copy=_video.video_url
		video_R_dir_copy=_video.video_R_dir
		id_=int(id)-1
		while not video.objects.filter(id=str(id_)).exists():
			id_-=1
		_video_=video.objects.filter(id=str(id_)).get()
		_video.cover_img=_video_.cover_img
		_video.video_title=_video_.video_title
		_video.video_description=_video_.video_description
		_video.video_url=_video_.video_url
		_video.video_R_dir=_video_.video_R_dir
		_video.save()
		_video_.cover_img=cover_img_copy
		_video_.video_title=video_title_copy
		_video_.video_description=video_description_copy
		_video_.video_url=video_url_copy
		_video_.video_R_dir=video_R_dir_copy
		_video_.save()
		return _video
	def move_down(self,id):
		_video=video.objects.filter(id=id).get()
		cover_img_copy=_video.cover_img
		video_title_copy=_video.video_title
		video_description_copy=_video.video_description
		video_url_copy=_video.video_url
		video_R_dir_copy=_video.video_R_dir
		id_=int(id)+1
		while not video.objects.filter(id=str(id_)).exists():
			id_+=1
		_video_=video.objects.filter(id=str(id_)).get()
		_video.cover_img=_video_.cover_img
		_video.video_title=_video_.video_title
		_video.video_description=_video_.video_description
		_video.video_url=_video_.video_url
		_video.video_R_dir=_video_.video_R_dir
		_video.save()
		_video_.cover_img=cover_img_copy
		_video_.video_title=video_title_copy
		_video_.video_description=video_description_copy
		_video_.video_url=video_url_copy
		_video_.video_R_dir=video_R_dir_copy
		_video_.save()
		return _video
class video(models.Model):
	cover_img=models.ImageField(upload_to='video/cover_img/',
								default='video/cover_img/default/default.png',
								blank=True)
	video_title=models.CharField(max_length=191)
	video_description=models.TextField()
	video_url=models.URLField(
		default='https://www.youtube.com/embed/17MBllYf6OY',blank=True)
	video_R_dir=models.BooleanField(default=True)
	objects=videoManager()
class servicesManager(models.Manager):
	def create_service(self):
		service=services.objects.create(title='title',description="description")
		return service
	def change_service_img(self,id,img):
		_service=services.objects.filter(id=id).get()
		if _service.img.path.find(
				'\\default.png')==-1 and _service.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_service.img.path):
				os.remove(_service.img.path)
		_service.img=img
		_service.save()
		return _service
	def change_service_title(self,id,title):
		_service=services.objects.filter(id=id).get()
		_service.title=title
		_service.save()
		return _service
	def change_service_description(self,id,text):
		_service=services.objects.filter(id=id).get()
		_service.description=text
		_service.save()
		return _service
	def remove_service(self,id):
		_service=services.objects.filter(id=id).get()
		if _service.img.path.find(
				'\\default.png')==-1 and _service.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_service.img.path):
				os.remove(_service.img.path)
		_service.delete()
		return _service
	def move_up(self,id):
		_service=services.objects.filter(id=id).get()
		img_copy=_service.img
		title_copy=_service.title
		description_copy=_service.description1
		id_=int(id)-1
		while not services.objects.filter(id=str(id_)).exists():
			id_-=1
		_service_=services.objects.filter(id=str(id_)).get()
		_service.img=_service_.img
		_service.title=_service_.title
		_service.description=_service_.description
		_service.save()
		_service_.img=img_copy
		_service_.title=title_copy
		_service_.description=description_copy
		_service_.save()
		return _service
	def move_down(self,id):
		_service=services.objects.filter(id=id).get()
		img_copy=_service.img
		title_copy=_service.title
		description_copy=_service.description1
		id_=int(id)-1
		while not services.objects.filter(id=str(id_)).exists():
			id_-=1
		_service_=services.objects.filter(id=str(id_)).get()
		_service.img=_service_.img
		_service.title=_service_.title
		_service.description=_service_.description
		_service.save()
		_service_.img=img_copy
		_service_.title=title_copy
		_service_.description=description_copy
		_service_.save()
		return _service
class services(models.Model):
	img=models.ImageField(upload_to='services/img/',
						  default='services/img/default/default.png'
						  ,blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	objects=servicesManager()
class workSamplesManager(models.Manager):
	def create_work_sample(self):
		work_sample=work_samples.objects.create(title='title',
												description="description")
		return work_sample
	def change_work_sample_img(self,id,img):
		work_sample=work_samples.objects.filter(id=id).get()
		if work_sample.img.path.find(
				'\\default.png')==-1 and work_sample.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(work_sample.img.path):
				os.remove(work_sample.img.path)
		work_sample.img=img
		work_sample.save()
		return work_sample
	def change_work_sample_title(self,id,title):
		work_sample=work_samples.objects.filter(id=id).get()
		work_sample.title=title
		work_sample.save()
		return work_sample
	def change_work_sample_description(self,id,text):
		work_sample=work_samples.objects.filter(id=id).get()
		work_sample.description=text
		work_sample.save()
		return work_sample
	def change_work_sample_url(self,id,url):
		work_sample=work_samples.objects.filter(id=id).get()
		work_sample.url=url
		work_sample.save()
		return work_sample
	def remove_work_sample(self,id):
		work_sample=work_samples.objects.filter(id=id).get()
		if work_sample.img.path.find(
				'\\default.png')==-1 and work_sample.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(work_sample.img.path):
				os.remove(work_sample.img.path)
		work_sample.delete()
		return work_sample
class work_samples(models.Model):
	img=models.ImageField(upload_to='work_samples/img/',
						  default='work_samples/img/default/default.png',
						  blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	url=models.URLField(blank=True)
	objects=workSamplesManager()
class ourTeamManager(models.Manager):
	def create_team_member(self):
		mem=our_team.objects.create(title='title',
									description="description")
		return mem
	def change_team_member_img(self,id,img):
		mem=our_team.objects.filter(id=id).get()
		if mem.img.path.find(
				'\\default.png')==-1 and mem.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(mem.img.path):
				os.remove(mem.img.path)
		mem.img=img
		mem.save()
		return mem
	def change_team_member_title(self,id,title):
		mem=our_team.objects.filter(id=id).get()
		mem.title=title
		mem.save()
		return mem
	def change_team_member_description(self,id,text):
		mem=our_team.objects.filter(id=id).get()
		mem.description=text
		mem.save()
		return mem
	def change_team_member_facebook(self,id,url):
		mem=our_team.objects.filter(id=id).get()
		mem.facebook=url
		mem.save()
		return mem
	def change_team_member_twitter(self,id,url):
		mem=our_team.objects.filter(id=id).get()
		mem.twitter=url
		mem.save()
		return mem
	def change_team_member_instagram(self,id,url):
		mem=our_team.objects.filter(id=id).get()
		mem.instagram=url
		mem.save()
		return mem
	def change_team_member_telegram(self,id,url):
		mem=our_team.objects.filter(id=id).get()
		mem.telegram=url
		mem.save()
		return mem
	def remove_member(self,id):
		mem=our_team.objects.filter(id=id).get()
		if mem.img.path.find(
				'\\default.png')==-1 and mem.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(mem.img.path):
				os.remove(mem.img.path)
		mem.delete()
		return mem
class our_team(models.Model):
	img=models.ImageField(upload_to='our_team/img/',
						  default='our_team/img/default/default.png',
						  blank=True)
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	facebook=models.URLField(blank=True)
	twitter=models.URLField(blank=True)
	instagram=models.URLField(blank=True)
	telegram=models.URLField(blank=True)
	objects=ourTeamManager()
class ourCustomersManager(models.Manager):
	def create_customer(self):
		customer=our_customers.objects.create(name='name',job='job',
											  description='description')
		return customer
	def change_customer_img(self,id,img):
		customer=our_customers.objects.filter(id=id).get()
		if customer.img.path.find(
				'\\default.png')==-1 and customer.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(customer.img.path):
				os.remove(customer.img.path)
		customer.img=img
		customer.save()
		return customer
	def change_customer_name(self,id,name):
		customer=our_customers.objects.filter(id=id).get()
		customer.name=name
		customer.save()
		return customer
	def change_customer_job(self,id,job):
		customer=our_customers.objects.filter(id=id).get()
		customer.job=job
		customer.save()
		return customer
	def change_customer_description(self,id,text):
		customer=self.filter(id=id).get()
		customer.description=text
		customer.save()
		return customer
	def remove_customer(self,id):
		customer=our_customers.objects.filter(id=id).get()
		if customer.img.path.find(
				'\\default.png')==-1 and customer.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(customer.img.path):
				os.remove(customer.img.path)
		customer.delete()
		return customer
class our_customers(models.Model):
	img=models.ImageField(upload_to='customers/img/',
						  default='customers/img/default/default.png',
						  blank=True)
	name=models.CharField(max_length=100,blank=True)
	job=models.CharField(max_length=100,blank=True)
	description=models.TextField()
	objects=ourCustomersManager()
class themeManager(models.Manager):
	def create_theme(self,color,color_ba):
		theme_num=0
		while os.path.isfile(
				'static/web_01/css/style-theme'+str(theme_num)+'.css'):
			theme_num+=1
		theme=site_theme.objects.create(theme_name='-theme'+str(theme_num),
										color=color,color_ba=color_ba)
		style=open('static/web_01/css/style-base.css','r')
		responsive=open('static/web_01/css/responsive-base.css','r')
		code=style.read().replace('#69b8d1','#'+str(color))
		code=code.replace('#a4bfd2','#'+str(color_ba))
		code_r=responsive.read().replace('#69b8d1','#'+str(color))
		style.close()
		responsive.close()
		style=open('static/web_01/css/style-theme'+str(theme_num)+'.css','w+')
		responsive=open(
			'static/web_01/css/responsive-theme'+str(theme_num)+'.css','w+')
		style.write(code)
		responsive.write(code_r)
		style.close()
		responsive.close()
		return theme
	def active_theme(self,id):
		for obj in site_theme.objects.all():
			obj=site_theme.objects.filter(id=obj.id).get()
			obj.active=False
			obj.save()
		if int(id)!=-1:
			theme=site_theme.objects.filter(id=id).get()
			theme.active=True
			theme.save()
			return theme
		return None
	def remove_theme(self,id):
		theme=site_theme.objects.filter(id=id).get()
		if os.path.isfile(
				'static/web_01/css/style'+str(theme.theme_name)+'.css'):
			os.remove('static/web_01/css/style'+str(theme.theme_name)+'.css')
		theme.delete()
		return theme
class site_theme(models.Model):
	active=models.BooleanField(default=False)
	theme_name=models.CharField(max_length=21)
	color=models.CharField(max_length=6)
	color_ba=models.CharField(max_length=6)
	objects=themeManager()
