from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
	if request.user.is_authenticated:
		user=User.objects.get(email=request.user.email)
		print(user.email)
		return redirect('/')
	email_errors=list()
	username_errors=list()
	password_errors=list()
	prev_username_email=''
	prev_password=''
	login_log={
		'email_errors':email_errors,
		'username_errors':username_errors,
		'password_errors':password_errors,
		'prev_username_email':prev_username_email,
		'prev_password':prev_password
	}
	if request.method=='POST':
		username_email=request.POST.get('username-email')
		password=request.POST.get('password')
		if '@' in username_email and '.' in username_email:
			email=username_email
			if not User.objects.filter(email=email).exists():
				email_errors.append('ایمیل وارد شده وجود ندارد')
				prev_password=password
				prev_username_email=username_email
			else:
				user=User.objects.get(email=email)
				if user.check_password(password):
					auth.login(request,user)
					return redirect('/')
				else:
					password_errors.append('رمز وارد شده صحیح نمی باشد')
					prev_username_email=username_email
		else:
			username=username_email
			if not User.objects.filter(username=username).exists():
				username_errors.append('کاربری با این نام کاربری وجود ندارد')
				prev_password=password
				prev_username_email=username_email
			else:
				user=User.objects.get(username=username)
				if user.check_password(password):
					auth.login(request,user)
					return redirect('/')
				else:
					password_errors.append('رمز وارد شده صحیح نمی باشد')
					prev_username_email=username_email
		login_log={
			'email_errors':email_errors,
			'username_errors':username_errors,
			'password_errors':password_errors,
			'prev_username_email':prev_username_email,
			'prev_password':prev_password
		}
	return render(request,'users/login.html',{'login_log':login_log})
def signup(request):
	if request.user.is_authenticated:
		user=User.objects.get(email=request.user.email)
		print(user.email)
		return redirect('/')
	first_name_errors=list()
	last_name_errors=list()
	email_errors=list()
	username_errors=list()
	password_errors=list()
	re_password_errors=list()
	prev_first_name=''
	prev_last_name=''
	prev_email=''
	prev_username=''
	prev_password=''
	prev_re_password=''
	signup_log={
		'first_name_errors':first_name_errors,
		'last_name_errors':last_name_errors,
		'email_errors':email_errors,
		'username_errors':username_errors,
		'password_errors':password_errors,
		're_password_errors':re_password_errors,
		'prev_first_name':prev_first_name,
		'prev_last_name':prev_last_name,
		'prev_email':prev_email,
		'prev_username':prev_username,
		'prev_password':prev_password,
		'prev_re_password':prev_re_password
	}
	if (request.method=='POST'):
		first_name=request.POST.get('first-name')
		last_name=request.POST.get('last-name')
		email=request.POST.get('email')
		username=request.POST.get('username')
		password=request.POST.get('password')
		re_password=request.POST.get('re-password')
		if first_name=='' or first_name is None:
			first_name_errors.append('لطفا نام خود را وارد کنید')
		else:
			if len(first_name)<3:
				first_name_errors.append('نام شما باید حداقل سه حرف داشته باشد')
			else:
				prev_first_name=first_name
		if last_name=='' or last_name is None:
			last_name_errors.append('لطفا نام خانوادگی خود را وارد کنید')
		else:
			if len(last_name)<3:
				last_name_errors.append('نام خانوادگی شما باید حداقل سه حرف داشته باشد')
			else:
				prev_last_name=last_name
		if email=='' or email is None:
			email_errors.append('لطفا ایمیل خود را وارد کنید')
		else:
			prev_email=email
			if not '@' in email or not '.' in email:
				email_errors.append('ایمیل شما معتیر نمی باشد')
			else:
				if User.objects.filter(email=email).exists():
					email_errors.append('آیا شما قبلا با ابن ایمیل حساب باز کرده اید ؟ ')
		if username=='' or username is None:
			username_errors.append('لطفا نام کاربری خود را وارد کنید')
		else:
			if User.objects.filter(username=username).exists():
				username_errors.append('این نام کاربری قبلا استفاده شده است')
			else:
				prev_username=username
		if password=='' or password is None:
			password_errors.append('لطفا رمز خود را وارد کنید')
		else:
			if len(password)<8:
				password_errors.append('رمز شما باید حداقل 8 حرف باشد')
			if len(password_errors)<=0:
				if re_password!=password:
					re_password_errors.append('رمز خود را باید دقیقا اینجا تکرار کنید')
					prev_password=password
				else:
					prev_password=password
					prev_re_password=re_password
		if len(first_name_errors)==0 and len(last_name_errors)==0 and len(email_errors)==0 and len(
				username_errors)==0 and len(password_errors)==0 and len(re_password_errors)==0:
			user=User.objects.create_user(
				username=username,
				password=password,
				email=email,
				first_name=first_name,
				last_name=last_name
			)
			user.save()
			return redirect('/login/')
		signup_log={
			'first_name_errors':first_name_errors,
			'last_name_errors':last_name_errors,
			'email_errors':email_errors,
			'username_errors':username_errors,
			'password_errors':password_errors,
			're_password_errors':re_password_errors,
			'prev_first_name':prev_first_name,
			'prev_last_name':prev_last_name,
			'prev_email':prev_email,
			'prev_username':prev_username,
			'prev_password':prev_password,
			'prev_re_password':prev_re_password
		}
	return render(request,'users/signup.html',{'signup_log':signup_log})
def logout(request):
	if not request.user.is_authenticated:
		return redirect('/login/')
	logged_out_user=request.user
	auth.logout(request)
	return render(request,'users/logout.html',{'logged_out_user':logged_out_user})
