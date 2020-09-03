from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from .models import site_title,slideshow,video
def index(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/index.html',{'messages':messages})
def users(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	users=User.objects.all()
	return render(request,'control_panel/users.html',{'users':users,'messages':messages})
def change_user_data(request,id):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if not User.objects.filter(id=id).exists():
		return redirect('/control_panel/auth/users/')
	if request.method=='POST':
		if request.POST.get('first-name') is not None:
			if not request.user.is_superuser:
				message={'type':'error','body':'You Don\'t Have Permission To Change Users Data.'}
				messages.append(message)
			else:
				user_to_change=User.objects.get(id=id)
				first_name=request.POST.get('first-name')
				last_name=request.POST.get('last-name')
				email=request.POST.get('email')
				username=request.POST.get('username')
				if email is not None and email!='':
					if '@' not in email or '.' not in email:
						message={'type':'error','body':' Email Is Not Valid.'}
						messages.append(message)
					else:
						if User.objects.filter(email=email).exists() and User.objects.get(
								email=email).email!=user_to_change.email:
							message={'type':'error','body':' Email Is Used.'}
							messages.append(message)
				if username is not None and username!='':
					if User.objects.filter(username=username).exists() and User.objects.get(
							username=username).username!=user_to_change.username:
						message={'type':'error','body':' Username Is Used.'}
						messages.append(message)
				allow_to_update_user=True
				for message in messages:
					if message.get('type')=='error':
						allow_to_update_user=False
				if allow_to_update_user:
					if first_name is not None and first_name!='':
						user_to_change.first_name=first_name
					if last_name is not None and last_name!='':
						user_to_change.last_name=last_name
					if email is not None and email!='':
						user_to_change.email=email
					if username is not None and username!='':
						user_to_change.username=username
					user_to_change.save()
					if first_name=='' and last_name=='' and email=='' and username=='':
						message={'type':'info','body':' There Were No Changes To Save.'}
					else:
						message={'type':'success','body':' User Was Updated Successfully.'}
					messages.append(message)
		elif request.POST.get('delete') is not None:
			if not request.user.is_superuser:
				message={'type':'error','body':'You Don\'t Have Permission To Change Users Data.'}
				messages.append(message)
			else:
				user_to_delete=User.objects.get(id=id)
				user_to_delete.delete()
		elif request.POST.get('Ignore') is not None:
			print('Ignore')
			return redirect('/control_panel/auth/users/')
		else:
			if not request.user.is_superuser:
				message={'type':'error','body':'You Don\'t Have Permission To Change Users Data.'}
				messages.append(message)
			else:
				user_to_change=User.objects.get(id=id)
				is_active=request.POST.get('is-active') is not None
				is_staff_status=request.POST.get('is-staff-status') is not None
				is_superuser_status=request.POST.get('is-superuser-status') is not None
				if user_to_change.is_active==is_active and user_to_change.is_staff==is_staff_status and user_to_change.is_superuser==is_superuser_status:
					message={'type':'info','body':' There Were No Changes To Save.'}
					messages.append(message)
				else:
					message={'type':'success','body':' User Was Updated Successfully.'}
					messages.append(message)
				user_to_change.is_active=is_active
				user_to_change.is_staff=is_staff_status
				user_to_change.is_superuser=is_superuser_status
				user_to_change.save()
	try:
		user_to_change=User.objects.get(id=id)
		return render(request,'control_panel/change-user-data.html',
		              {'user_to_change':user_to_change,'messages':messages})
	except:
		return redirect('/control_panel/auth/users/')
def create_new_user(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if not request.user.is_superuser:
			message={'type':'error','body':'You Don\'t Have Permission To Add New User.'}
			messages.append(message)
		else:
			first_name=request.POST.get('first-name')
			last_name=request.POST.get('last-name')
			email=request.POST.get('email')
			username=request.POST.get('username')
			password=request.POST.get('password')
			re_password=request.POST.get('re-password')
			is_active=False
			is_staff_status=False
			is_superuser_status=False
			if request.POST.get('is-active') is not None:
				is_active=True
			if request.POST.get('is-staff-status') is not None:
				is_staff_status=True
			if request.POST.get('is-superuser-status') is not None:
				is_superuser_status=True
			if first_name is None or first_name=='':
				message={'type':'error','body':' First Name Field Is Empty.'}
				messages.append(message)
			if last_name is None or last_name=='':
				message={'type':'error','body':' Last Name Field Is Empty.'}
				messages.append(message)
			if email is None or email=='':
				message={'type':'error','body':' Email Field Is Empty.'}
				messages.append(message)
			else:
				if '@' not in email or '.' not in email:
					message={'type':'error','body':' Email Is Not Valid.'}
					messages.append(message)
				else:
					if User.objects.filter(email=email).exists():
						message={'type':'error','body':' Email Is Used.'}
						messages.append(message)
			if username is None or username=='':
				message={'type':'error','body':' Username Field Is Empty.'}
				messages.append(message)
			else:
				if User.objects.filter(username=username).exists():
					message={'type':'error','body':' Username Is Used.'}
					messages.append(message)
			if password is None or password=='':
				message={'type':'error','body':' Password Field Is Empty.'}
				messages.append(message)
			else:
				if len(password)<8:
					message={'type':'warning','body':' Password Is Weak.'}
					messages.append(message)
			if re_password is None or re_password=='':
				message={'type':'error',
				         'body':' Repeat Password Field Is Empty, You Have To Repeat The Password In This Field.'}
				messages.append(message)
			else:
				if re_password!=password:
					message={'type':'error','body':' The Two Password Fields Didn’t Match.'}
					messages.append(message)
			allow_to_create_user=True
			for message in messages:
				if message.get('type')=='error':
					allow_to_create_user=False
			if allow_to_create_user:
				user=User.objects.create_user(
					first_name=first_name,
					last_name=last_name,
					email=email,
					username=username,
					password=password,
					is_active=is_active,
					is_staff=is_staff_status,
					is_superuser=is_superuser_status,
				)
				user.save()
				message={'type':'success','body':' User Was Created Successfully.'}
				messages.append(message)
	return render(request,'control_panel/create-new-user.html',{'messages':messages})
def groups(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/groups.html',{'messages':messages})
def site_title_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	site_title.objects.control_number()
	if request.method=="POST":
		title=request.POST.get('title')
		title_ico=request.FILES.get('title-ico')
		if title!='':
			site_title.objects.change_title(title)
			message={'type':'success','body':' Your Site Title Was Updated'}
			messages.append(message)
		if title_ico:
			site_title.objects.change_icon(title_ico)
			message={'type':'success','body':' Your Site Title Icon Was Updated'}
			messages.append(message)
		if len(messages)<1:
			message={'type':'info','body':' There Were No Changes To Save.'}
			messages.append(message)
	return render(request,'control_panel/site-title.html',{'messages':messages,'site_title':site_title.objects.all()})
def slideshow_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-slide') is not None:
			slideshow.objects.create_slide()
		elif request.POST.get('remove-slide') is not None:
			id=request.POST.get('remove-slide')
			slideshow.objects.remve_slide(id)
		elif request.POST.get('save') is not None:
			slide_img=request.FILES.get('slide-img')
			slide_title=request.POST.get('slide-title')
			slide_body_text=request.POST.get('slide-body-text')
			id=request.POST.get('save')
			if slide_img:
				slideshow.objects.change_slide_img(id,slide_img)
				message={'type':'success','body':' Slide Image Was Updated'}
				messages.append(message)
			if slide_title!='':
				slideshow.objects.change_slide_title(id,slide_title)
				message={'type':'success','body':' Slide Title Was Updated'}
				messages.append(message)
			if slide_body_text!='':
				slideshow.objects.change_slide_body_text(id,slide_body_text)
				message={'type':'success','body':' Slide Body Text Was Updated'}
				messages.append(message)
			if len(messages)<1:
				message={'type':'info','body':' There Were No Changes To Save.'}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			slideshow.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			slideshow.objects.move_down(id)
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
	return render(request,'control_panel/slideshow.html',{'messages':messages,'slideshow':slideshow_array})
def video_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-video') is not None:
			video.objects.create_video()
		elif request.POST.get('remove-video') is not None:
			id=request.POST.get('remove-video')
			video.objects.remve_video(id)
		elif request.POST.get('save') is not None:
			cover_img=request.FILES.get('cover-img')
			video_title=request.POST.get('video-title')
			video_description=request.POST.get('video-description')
			video_url=request.POST.get('video-url')
			id=request.POST.get('save')
			if cover_img:
				video.objects.change_cover_img(id,cover_img)
				message={'type':'success','body':' Video Cover Image Was Updated'}
				messages.append(message)
			if video_title!='':
				video.objects.change_video_title(id,video_title)
				message={'type':'success','body':' Video Title Was Updated'}
				messages.append(message)
			if video_description!='':
				video.objects.change_video_description(id,video_description)
				message={'type':'success','body':' Video Description Was Updated'}
				messages.append(message)
			if video_url!='':
				video.objects.change_video_url(id,video_url)
				message={'type':'success','body':' Video url Was Updated'}
				messages.append(message)
			if len(messages)<1:
				message={'type':'info','body':' There Were No Changes To Save.'}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			video.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			video.objects.move_down(id)
		elif request.POST.get('r-l') is not None:
			id=request.POST.get('r-l')
			video.objects.flip(id)
	return render(request,'control_panel/video.html',{'messages':messages,'videos':video.objects.all()})
def our_services_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/our-services.html',{'messages':messages})
def work_samples_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/work-samples.html',{'messages':messages})
def our_team_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/our-team.html',{'messages':messages})
def our_customers_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/our-customers.html',{'messages':messages})
def footer_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/footer.html',{'messages':messages})
def pictures_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/pictures.html',{'messages':messages})
def themes_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/themes.html',{'messages':messages})
def logout(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	auth.logout(request)
	return render(request,'control_panel/logout.html',{'messages':messages})
