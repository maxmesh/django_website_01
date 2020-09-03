import os

from django.db import models
class siteTitleManager(models.Manager):
	def control_number(self):
		if len(self.all())==0:
			self.create()
		elif len(self.all())>1:
			for obj in self.all():
				if obj.id!=1:
					if obj.title_icon.path.find('\\default.png')==-1 and obj.title_icon.path.find(
							'/default.png')==-1:
						if os.path.isfile(obj.title_icon.path):
							os.remove(obj.title_icon.path)
					obj.delete()
		return self.filter(id=1).get()
	def change_title(self,title):
		site_title_obj=self.filter(id=1).get()
		site_title_obj.title=title
		site_title_obj.save()
		return site_title_obj
	def change_icon(self,icon):
		site_title_obj=self.filter(id=1).get()
		if site_title_obj.title_icon.path.find('\\default.png')==-1 and site_title_obj.title_icon.path.find(
				'/default.png')==-1:
			if os.path.isfile(site_title_obj.title_icon.path):
				os.remove(site_title_obj.title_icon.path)
		site_title_obj.title_icon=icon
		site_title_obj.save()
		return site_title_obj
class site_title(models.Model):
	title=models.CharField(max_length=100)
	title_icon=models.ImageField(upload_to='title_ico/',default='title_ico/default/default.png',blank=True)
	objects=siteTitleManager()
class slideshowManager(models.Manager):
	def create_slide(self):
		slide=self.create(slide_title='title',slide_body_text="slide body text")
		return slide
	def change_slide_img(self,id,img):
		slide=self.filter(id=id).get()
		if slide.slide_img.path.find('\\default.png')==-1 and slide.slide_img.path.find('/default.png')==-1:
			if os.path.isfile(slide.slide_img.path):
				os.remove(slide.slide_img.path)
		slide.slide_img=img
		slide.save()
		return slide
	def change_slide_title(self,id,title):
		slide=self.filter(id=id).get()
		slide.slide_title=title
		slide.save()
		return slide
	def change_slide_body_text(self,id,text):
		slide=self.filter(id=id).get()
		slide.slide_body_text=text
		slide.save()
		return slide
	def remve_slide(self,id):
		slide=self.filter(id=id).get()
		if slide.slide_img.path.find('\\default.png')==-1 and slide.slide_img.path.find('/default.png')==-1:
			if os.path.isfile(slide.slide_img.path):
				os.remove(slide.slide_img.path)
		slide.delete()
		return slide
	def move_up(self,id):
		slide=self.filter(id=id).get()
		slide_img_copy=slide.slide_img
		slide_title_copy=slide.slide_title
		slide_body_text_copy=slide.slide_body_text
		id_=int(id)-1
		while not self.filter(id=str(id_)).exists():
			id_-=1
		slide_=self.filter(id=str(id_)).get()
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
		slide=self.filter(id=id).get()
		slide_img_copy=slide.slide_img
		slide_title_copy=slide.slide_title
		slide_body_text_copy=slide.slide_body_text
		id_=int(id)+1
		while not self.filter(id=str(id_)).exists():
			id_+=1
		slide_=self.filter(id=str(id_)).get()
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
	slide_img=models.ImageField(upload_to='slides_img/',default='slides_img/default/default.png',blank=True)
	slide_title=models.CharField(max_length=100)
	slide_body_text=models.TextField()
	objects=slideshowManager()
class videoManager(models.Manager):
	def create_video(self):
		slide=self.create(video_title='title',video_description="video description")
		return slide
	def change_cover_img(self,id,img):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.cover_img=img
		_video.save()
		return _video
	def change_video_title(self,id,title):
		_video=self.filter(id=id).get()
		_video.video_title=title
		_video.save()
		return _video
	def change_video_description(self,id,text):
		_video=self.filter(id=id).get()
		_video.video_description=text
		_video.save()
		return _video
	def change_video_url(self,id,url):
		_video=self.filter(id=id).get()
		_video.video_url=url
		_video.save()
		return _video
	def flip(self,id):
		_video=self.filter(id=id).get()
		_video.video_R_dir=not _video.video_R_dir
		_video.save()
		return _video
	def remve_video(self,id):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.delete()
		return _video
	def move_up(self,id):
		_video=self.filter(id=id).get()
		cover_img_copy=_video.cover_img
		video_title_copy=_video.video_title
		video_description_copy=_video.video_description1
		video_url_copy=_video.video_url
		video_R_dir_copy=_video.video_R_dir
		id_=int(id)-1
		while not self.filter(id=str(id_)).exists():
			id_-=1
		_video_=self.filter(id=str(id_)).get()
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
		_video=self.filter(id=id).get()
		cover_img_copy=_video.cover_img
		video_title_copy=_video.video_title
		video_description_copy=_video.video_description
		video_url_copy=_video.video_url
		video_R_dir_copy=_video.video_R_dir
		id_=int(id)+1
		while not self.filter(id=str(id_)).exists():
			id_+=1
		_video_=self.filter(id=str(id_)).get()
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
	cover_img=models.ImageField(upload_to='video/cover_img/',default='video/cover_img/default/default.png',blank=True)
	video_title=models.CharField(max_length=191)
	video_description=models.TextField()
	video_url=models.URLField(default='https://www.youtube.com/embed/17MBllYf6OY',blank=True)
	video_R_dir=models.BooleanField(default=True)
	objects=videoManager()
class servicesManager(models.Manager):
	def create_services(self):
		slide=self.create(title='title',description="description")
		return slide
	def change_services_img(self,id,img):
		_services=self.filter(id=id).get()
		if _services.img.path.find('\\default.png')==-1 and _services.img.path.find('/default.png')==-1:
			if os.path.isfile(_services.img.path):
				os.remove(_services.img.path)
		_services.img=img
		_services.save()
		return _services
	def change_services_title(self,id,title):
		_services=self.filter(id=id).get()
		_services.title=title
		_services.save()
		return _services
	def change_services_description(self,id,text):
		_services=self.filter(id=id).get()
		_services.description=text
		_services.save()
		return _services
	def remve_services(self,id):
		_services=self.filter(id=id).get()
		if _services.img.path.find('\\default.png')==-1 and _services.img.path.find('/default.png')==-1:
			if os.path.isfile(_services.img.path):
				os.remove(_services.img.path)
		_services.delete()
		return _services
	def move_up(self,id):
		_services=self.filter(id=id).get()
		img_copy=_services.img
		title_copy=_services.title
		description_copy=_services.description1
		id_=int(id)-1
		while not self.filter(id=str(id_)).exists():
			id_-=1
		_video_=self.filter(id=str(id_)).get()
		_services.img=_video_.img
		_services.title=_video_.title
		_services.description=_video_.description
		_services.save()
		_video_.img=img_copy
		_video_.title=title_copy
		_video_.description=description_copy
		_video_.save()
		return _services
	def move_down(self,id):
		_services=self.filter(id=id).get()
		img_copy=_services.img
		title_copy=_services.title
		description_copy=_services.description1
		id_=int(id)-1
		while not self.filter(id=str(id_)).exists():
			id_-=1
		_video_=self.filter(id=str(id_)).get()
		_services.img=_video_.img
		_services.title=_video_.title
		_services.description=_video_.description
		_services.save()
		_video_.img=img_copy
		_video_.title=title_copy
		_video_.description=description_copy
		_video_.save()
		return _services
class services(models.Model):
	img=models.ImageField(upload_to='services/img/',default='services/img/default/default.png',blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	objects=servicesManager()
class workSamplesManager(models.Manager):
	def create_video(self):
		slide=self.create(video_title='title',video_description="video description")
		return slide
	def change_cover_img(self,id,img):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.cover_img=img
		_video.save()
		return _video
	def change_video_title(self,id,title):
		_video=self.filter(id=id).get()
		_video.video_title=title
		_video.save()
		return _video
	def change_video_description(self,id,text):
		_video=self.filter(id=id).get()
		_video.video_description=text
		_video.save()
		return _video
	def remve_video(self,id):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.delete()
		return _video
class work_samples(models.Model):
	img=models.ImageField(upload_to='work_samples/img/',default='work_samples/img/default/default.png',blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	url=models.URLField(blank=True)
	objects=servicesManager()
class ourTeamManager(models.Manager):
	def create_video(self):
		slide=self.create(video_title='title',video_description="video description")
		return slide
	def change_cover_img(self,id,img):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.cover_img=img
		_video.save()
		return _video
	def change_video_title(self,id,title):
		_video=self.filter(id=id).get()
		_video.video_title=title
		_video.save()
		return _video
	def change_video_description(self,id,text):
		_video=self.filter(id=id).get()
		_video.video_description=text
		_video.save()
		return _video
	def remve_video(self,id):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.delete()
		return _video
class our_team(models.Model):
	img=models.ImageField(upload_to='services/img/',default='services/img/default/default.png',blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	facebook=models.URLField(blank=True)
	twitter=models.URLField(blank=True)
	instagram=models.URLField(blank=True)
	telegram=models.URLField(blank=True)
	objects=ourTeamManager()
class ourCustomersManager(models.Manager):
	def create_video(self):
		slide=self.create(video_title='title',video_description="video description")
		return slide
	def change_cover_img(self,id,img):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.cover_img=img
		_video.save()
		return _video
	def change_video_title(self,id,title):
		_video=self.filter(id=id).get()
		_video.video_title=title
		_video.save()
		return _video
	def change_video_description(self,id,text):
		_video=self.filter(id=id).get()
		_video.video_description=text
		_video.save()
		return _video
	def remve_video(self,id):
		_video=self.filter(id=id).get()
		if _video.cover_img.path.find('\\default.png')==-1 and _video.cover_img.path.find('/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.delete()
		return _video
class our_customers(models.Model):
	img=models.ImageField(upload_to='services/img/',default='services/img/default/default.png',blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	objects=servicesManager()
