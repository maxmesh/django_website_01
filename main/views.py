from django.shortcuts import render

from control_panel.models import (
	site_title,
	slideshow,
	video,
	services,
	work_samples,
	)
def about_us(request):
	return render(request,'main/about-us.html',{'site_title':site_title.objects.all(),'page_name':'about_us'})
def blog_detail(request):
	return render(request,'main/blog-detail.html',{'site_title':site_title.objects.all(),'page_name':'blog_detail'})
def blog_grid(request):
	return render(request,'main/blog-grid.html',{'site_title':site_title.objects.all(),'page_name':'blog_grid'})
def blog_left_siderbar(request):
	return render(request,'main/blog-left-sidebar.html',
				  {'site_title':site_title.objects.all(),'page_name':'blog_left_siderbar'})
def blog_right_siderbar(request):
	return render(request,'main/blog-right-sidebar.html',
				  {'site_title':site_title.objects.all(),'page_name':'blog_right_siderbar'})
def contact_us(request):
	return render(request,'main/contact-us.html',{'site_title':site_title.objects.all(),'page_name':'contact_us'})
def homepage2(request):
	return render(request,'main/homepage-2.html',{'site_title':site_title.objects.all(),'page_name':'homepage2'})
def index(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={'title':slide_title_part.split('{')[0],'span':slide_title_part.split('{')[1]}
					title_parts.append(title_part)
				else:
					title_part={'title':slide_title_part,'span':''}
					title_parts.append(title_part)
			slideshow_arr={'object':slide,'title_parts':title_parts}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={'title':slide.slide_title,'span':''}
			title_parts.append(title_part)
			slideshow_arr={'object':slide,'title_parts':title_parts}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	return render(request,'main/index.html',
				  {
					  'site_title':site_title.objects.all(),
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'page_name':''
					  })
def our_services(request):
	return render(request,'main/our-services.html',{'site_title':site_title.objects.all(),'page_name':'our_services'})
def our_team(request):
	return render(request,'main/our-team.html',{'site_title':site_title.objects.all(),'page_name':'our_team'})
def portfolio_details(request):
	return render(request,'main/portfolio-details.html',
				  {'site_title':site_title.objects.all(),'page_name':'portfolio_details'})
def portfolio_grid(request):
	return render(request,'main/portfolio-grid.html',
				  {'site_title':site_title.objects.all(),'page_name':'portfolio_grid'})
def portfolio_grid_gallery(request):
	return render(request,'main/portfolio-grid-gallery.html',
				  {'site_title':site_title.objects.all(),'page_name':'portfolio_grid_gallery'})
def pricing(request):
	return render(request,'main/pricing.html',{'site_title':site_title.objects.all(),'page_name':'pricing'})
