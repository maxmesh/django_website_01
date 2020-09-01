from django.urls import path
from . import views
urlpatterns = [
    path('about-us/', views.about_us, name='main/about-us'),
    path('blog-detail/', views.blog_detail, name='main/blog-detail'),
    path('blog-grid/', views.blog_grid, name='main/blog-grid'),
    path('blog-left-sidebar/', views.blog_left_siderbar,
         name='main/blog-left-sidebar'),
    path('blog-right-sidebar/', views.blog_right_siderbar,
         name='main/blog-right-sidebar'),
    path('contact-us/', views.contact_us, name='main/contact-us'),
    path('homepage2/', views.homepage2, name='main/homepage2'),
    path('', views.index, name='main/index'),
    path('our-services/', views.our_services, name='main/our-services'),
    path('our-team/', views.our_team, name='main/our-team'),
    path('portfolio-details/', views.portfolio_details,
         name='main/portfolio-details'),
    path('portfolio-grid/', views.portfolio_grid,
         name='main/portfolio-grid'),
    path('portfolio-grid-gallery/', views.portfolio_grid_gallery,
         name='main/portfolio-grid-gallery'),
    path('pricing/', views.pricing, name='main/pricing'),
]