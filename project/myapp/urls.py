"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('no_page', views.no_page, name='no_page'),


    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),


    path('admin_event_details_add', views.admin_event_details_add, name='admin_event_details_add'),
    path('admin_event_details_view', views.admin_event_details_view, name='admin_event_details_view'),
    path('admin_event_details_delete', views.admin_event_details_delete, name='admin_event_details_delete'),
    path('admin_event_details_edit', views.admin_event_details_edit, name='admin_event_details_edit'),

    path('admin_event_pics_add', views.admin_event_pics_add, name='admin_event_pics_add'),
    path('admin_event_pics_view', views.admin_event_pics_view, name='admin_event_pics_view'),
    path('admin_event_pics_delete', views.admin_event_pics_delete, name='admin_event_pics_delete'),


    path('admin_add_college_details', views.admin_add_college_details, name='admin_add_college_details'),
    path('admin_college_details_update', views.admin_college_details_update, name='admin_college_details_update'),
    path('admin_college_details_view', views.admin_college_details_view, name='admin_college_details_view'),
    path('admin_college_profile_pic_add', views.admin_college_profile_pic_add, name='admin_college_profile_pic_add'),
    path('admin_college_profile_pic_update', views.admin_college_profile_pic_update, name='admin_college_profile_pic_update'),

    path('admin_alumni_details_view', views.admin_alumni_details_view, name='admin_alumni_details_view'),
    path('admin_branch_details_add', views.admin_branch_details_add, name='admin_branch_details_add'),
    path('admin_branch_details_view', views.admin_branch_details_view, name='admin_branch_details_view'),
    path('admin_branch_details_edit', views.admin_branch_details_edit, name='admin_branch_details_edit'),
    path('admin_branch_details_delete', views.admin_branch_details_delete, name='admin_branch_details_delete'),


####################ALUMNI#################################################

    path('alumni_login', views.alumni_login, name='alumni_login'),
    path('alumni_logout', views.alumni_logout, name='alumni_logout'),
    path('alumni_changepassword', views.alumni_changepassword, name='alumni_changepassword'),
    path('alumni_home', views.alumni_home, name='alumni_home'),
    path('alumni_details_add', views.alumni_details_add, name='alumni_details_add'),

    path('alumni_details_edit', views.alumni_details_edit, name='alumni_details_edit'),

    path('alumni_alumni_details_search', views.alumni_alumni_details_search, name='alumni_alumni_details_search'),

    path('alumni_job_details_view', views.alumni_job_details_view, name='alumni_job_details_view'),
    path('alumni_job_details_add', views.alumni_job_details_add, name='alumni_job_details_add'),
    path('alumni_job_details_delete', views.alumni_job_details_delete, name='alumni_job_details_delete'),
    path('alumni_job_details_edit', views.alumni_job_details_edit, name='alumni_job_details_edit'),

    path('alumni_event_details_view', views.alumni_event_details_view, name='alumni_event_details_view'),
    path('alumni_event_pics_view', views.alumni_event_pics_view, name='alumni_event_pics_view'),

    path('alumni_posts_add', views.alumni_posts_add, name='alumni_posts_add'),
    path('alumni_posts_delete', views.alumni_posts_delete, name='alumni_posts_delete'),
    path('alumni_posts_view', views.alumni_posts_view, name='alumni_posts_view'),

    path('alumni_posts_all_view', views.alumni_posts_all_view, name='alumni_posts_all_view'),
    path('alumni_profile_view', views.alumni_profile_view, name='alumni_profile_view'),

    path('alumni_profile_pic_update', views.alumni_profile_pic_update, name='alumni_profile_pic_update'),

    path('no_result', views.no_result, name='no_result'),

]
