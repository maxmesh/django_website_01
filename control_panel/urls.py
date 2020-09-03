from django.urls import path

from . import views
urlpatterns=[
	path('',views.index,name='control_panel/index'),
	path('auth/users/<int:id>/change/',views.change_user_data,
		 name='control_panel/auth/users/change_user_data'),
	path('auth/users/create_new_user/',views.create_new_user,
		 name='control_panel/auth/users/create_new_user'),
	path('auth/users/',views.users,name='control_panel/auth/users'),
	path('auth/groups/',views.groups,name='control_panel/auth/groups'),
	path('site/site-title/',views.site_title_,name='control_panel/site/site-title'),
	path('site/slideshow/',views.slideshow_,name='control_panel/site/slideshow'),
	path('site/video/',views.video_,name='control_panel/site/video'),
	path('site/our-services/',views.our_services_,name='control_panel/site/our-services'),
	path('site/work-samples/',views.work_samples_,name='control_panel/site/work-samples'),
	path('site/our-team/',views.our_team_,name='control_panel/site/our-team'),
	path('site/our-customers/',views.our_customers_,name='control_panel/site/our-customers'),
	path('site/footer/',views.footer_,name='control_panel/site/footer'),
	path('site/pictures/',views.pictures_,name='control_panel/site/pictures'),
	path('site/themes/',views.themes_,name='control_panel/site/themes'),
	path('logout/',views.logout,name='control_panel/logout'),
]
