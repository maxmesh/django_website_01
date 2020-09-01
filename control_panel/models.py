import os

from django.db import models
class site_title(models.Model):
	title=models.CharField(max_length=100)
	title_icon=models.ImageField(upload_to='title_ico/')
class slideshowManager(models.Manager):
	def create_slide(self):
		slide=self.create(slide_title='title',slide_body_text="slide body text")
		return slide
	def change_slide_img(self,id,img):
		slide=slideshow.objects.filter(id=id).get()
		if slide.slide_img.path.find('\\default.png')==-1 and slide.slide_img.path.find('/default.png')==-1:
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
	def remve_slide(self,id):
		slide=slideshow.objects.filter(id=id).get()
		if slide.slide_img.path.find('\\default.png')==-1 and slide.slide_img.path.find('/default.png')==-1:
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
	slide_img=models.ImageField(upload_to='slides_img/',default='slides_img/default/default.png',blank=True)
	slide_title=models.CharField(max_length=100)
	slide_body_text=models.TextField()
	objects=slideshowManager()
