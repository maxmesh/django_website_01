import os
import shutil

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.conf import settings

from .models import site_title,slideshow
def index(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/index.html',{'messages':messages})
def users(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	# region get all users data
	users=User.objects.all()
	# endregion
	return render(request,'control_panel/users.html',{'users':users,'messages':messages})
def change_user_data(request,id):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	# region check if user that we wanna change exists
	if not User.objects.filter(id=id).exists():
		return redirect('/control_panel/auth/users/')
	# endregion
	if request.method=='POST':
		# region save user settings
		if request.POST.get('first-name') is not None:
			# region check if user is superuser
			if not request.user.is_superuser:
				message={'type':'error','body':'You Don\'t Have Permission To Change Users Data.'}
				messages.append(message)
			else:
				# endregion
				# region get user to change
				user_to_change=User.objects.get(id=id)
				# endregion
				# region get user data
				first_name=request.POST.get('first-name')
				last_name=request.POST.get('last-name')
				email=request.POST.get('email')
				username=request.POST.get('username')
				# endregion
				# region check user data
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
				# endregion
				# region new user registration
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
		# endregion
		# region delete
		elif request.POST.get('delete') is not None:
			# region check if user is superuser
			if not request.user.is_superuser:
				message={'type':'error','body':'You Don\'t Have Permission To Change Users Data.'}
				messages.append(message)
			else:
				# endregion
				# region delete the user
				user_to_delete=User.objects.get(id=id)
				user_to_delete.delete()
		# endregion
		# region ignore
		elif request.POST.get('Ignore') is not None:
			print('Ignore')
			return redirect('/control_panel/auth/users/')
		# endregion
		else:
			# region check if user is superuser
			if not request.user.is_superuser:
				message={'type':'error','body':'You Don\'t Have Permission To Change Users Data.'}
				messages.append(message)
			# endregion
			else:
				# region get user to change
				user_to_change=User.objects.get(id=id)
				# endregion
				# region get user data
				is_active=request.POST.get('is-active') is not None
				is_staff_status=request.POST.get('is-staff-status') is not None
				is_superuser_status=request.POST.get('is-superuser-status') is not None
				# endregion
				# region save user data
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
	# endregion
	try:
		user_to_change=User.objects.get(id=id)
		return render(request,'control_panel/change-user-data.html',
		              {'user_to_change':user_to_change,'messages':messages})
	except:
		# endregion
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
			# region check user data
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
			# endregion
			# region new user registration
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
	# endregion
	return render(request,'control_panel/create-new-user.html',{'messages':messages})
def groups(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/groups.html',{'messages':messages})
def site_title_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=="POST":
		id=request.POST.get('save')
		title=request.POST.get('title')
		title_ico=request.FILES.get('title-ico')
		site_title_obj=site_title.objects.filter(id=id).get()
		if title!='':
			site_title_obj.title=title
			message={'type':'success','body':' Your Site Title Was Updated'}
			messages.append(message)
		if title_ico:
			for filename in os.listdir(settings.MEDIA_ROOT):
				file_path=os.path.join(settings.MEDIA_ROOT,filename)
				try:
					if os.path.isfile(file_path) or os.path.islink(file_path):
						os.unlink(file_path)
					elif os.path.isdir(file_path):
						shutil.rmtree(file_path)
				except Exception as e:
					print('Failed to delete %s. Reason: %s'%(file_path,e))
			site_title_obj.title_icon=title_ico
			message={'type':'success','body':' Your Site Title Icon Was Updated'}
			messages.append(message)
		if len(messages)<1:
			message={'type':'info','body':' There Were No Changes To Save.'}
			messages.append(message)
		else:
			site_title_obj.save()
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
def video(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/video.html',{'messages':messages})
def our_services(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/our-services.html',{'messages':messages})
def work_samples(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/work-samples.html',{'messages':messages})
def our_team(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/our-team.html',{'messages':messages})
def our_customers(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/our-customers.html',{'messages':messages})
def footer(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/footer.html',{'messages':messages})
def pictures(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/pictures.html',{'messages':messages})
def themes(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	return render(request,'control_panel/themes.html',{'messages':messages})
def logout(request):
	# region check if user is staff
	if not request.user.is_staff:
		return redirect('/')
	# endregion
	# region create messages list
	messages=list()
	# endregion
	# region logout the current user
	auth.logout(request)
	# endregion
	return render(request,'control_panel/logout.html',{'messages':messages})
