from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from custom_user.views import views_accounts, views_dashboard, views_profile
from jobs.views import UpdateJob, MyJobs, Job, ViewJob, JobPayment
from utils.common import anonymous_required
from django.contrib.auth.decorators import login_required
from contents.views import labs, projects, events, equipments, search, chat
from django.conf import settings

from postman.views import WriteView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about-us/$', TemplateView.as_view(template_name='o/about-us.html'), name='about_us'),
    url(r'^contact-us/$', TemplateView.as_view(template_name='o/contact-us.html'), name='contact_us'),
    url(r'^faq/$', TemplateView.as_view(template_name='o/faq.html'), name='faq'),
    url(r'^privacy-and-policy/$', TemplateView.as_view(template_name='o/pnp.html'), name='privacy'),
    url('^terms-and-conditions/$', TemplateView.as_view(template_name='o/tnc.html'), name='tnc'),
    url('^discussion-boards/$', TemplateView.as_view(template_name='o/discussion-board.html'), name='discussion-board'),
    url(r'^accounts/signup/$', anonymous_required(views_accounts.UserSignup.as_view()), name='signup'),
    url(r'^accounts/login/$', anonymous_required(views_accounts.UserLogin.as_view()), name='login'),
    url(r'^accounts/logout/$', views_accounts.UserLogout.as_view(), name='logout'),
    url(r'^accounts/users/$', views_accounts.UsersMessage.as_view(), name='users'),
    url(r'^accounts/getuser/$', views_accounts.GetUserById.as_view(), name='get_user_by_id'),
    url(r'^accounts/verify/(?P<verify_number>(\w+))$', anonymous_required(views_accounts.UserAccountActivate.as_view()), name='activate_account'),
    url(r'^accounts/forgot-password/$', anonymous_required(views_accounts.UserForgotPassword.as_view()), name='forgot_password'),
    url(r'^accounts/password/reset/(?P<verify_number>(\w+))$', anonymous_required(views_accounts.UserResetPassword.as_view()), name='forgot_reset'),
    url(r'^accounts/dashboard/$', login_required(views_dashboard.UserDashboard.as_view()), name='dashboard'),
    url(r'^accounts/edit-profile/$', login_required(views_profile.UserEditProfile.as_view()), name='edit_profile'),
    url(r'^accounts/edit-network/$', login_required(views_profile.UserEditNetwork.as_view()), name='edit_network'),
    url(r'^accounts/change-password/$', login_required(views_profile.UserChangePassword.as_view()), name='change_password'),
    url(r'^lab/create/$', login_required(labs.Lab.as_view()), name='create_lab'),
    url(r'^labs/get_departments/(?P<institute_id>[0-9])/$', login_required(labs.GetDepartments.as_view()), name='get_departments'),
    url(r'^accounts/upload/profile_photo/$', login_required(views_profile.UploadProfilePhoto.as_view()), name='upload_profile_photo'),
    url(r'^my-labs/$', login_required(labs.MyLabs.as_view()), name='my_labs'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^lab/edit/(?P<lab_id>(\d+))$', login_required(labs.UpdateLab.as_view()), name='edit_lab'),
    url(r'^my-projects/$', login_required(projects.MyProjects.as_view()), name='my_projects'),
    url(r'^project/create/$', login_required(projects.Project.as_view()), name='create_project'),
    url(r'^project/edit/(?P<project_id>(\d+))$', login_required(projects.UpdateProject.as_view()), name='edit_project'),
    url(r'^my-events/$', login_required(events.MyEvents.as_view()), name='my_events'),
    url(r'^event/create/$', login_required(events.Event.as_view()), name='create_event'),
    url(r'^event/edit/(?P<event_id>(\d+))$', login_required(events.UpdateEvent.as_view()), name='edit_event'),
    url(r'^event/edit/(?P<event_id>(\d+))$', login_required(equipments.UpdateEquipment.as_view()), name='edit_equipment'),
    url(r'^lab/view/(?P<pk>\d+)$', labs.ViewLab.as_view(), name='view_lab'),
    url(r'^project/view/(?P<pk>(\d+))$', projects.ViewProject.as_view(), name='view_project'),
    url(r'^event/view/(?P<pk>(\d+))$', events.ViewEvent.as_view(), name='view_event'),
    url(r'^my-equipments/$', login_required(equipments.MyEquipments.as_view()), name='my_equipments'),
    url(r'^equipment/edit/(?P<equipment_id>(\d+))$', login_required(equipments.UpdateEquipment.as_view()), name='edit_equipment'),
    url(r'^equipment/create/$', login_required(equipments.Equipment.as_view()), name='create_equipment'),
    url(r'^equipment/view/(?P<pk>(\d+))$', equipments.ViewEquipment.as_view(), name='view_equipment'),
    url(r'^search/labs/$', search.SearchLabs.as_view(), name='search_labs'),
    url(r'^search/projects/$', search.SearchProjects.as_view(), name='search_projects'),
    url(r'^search/events/$', search.SearchEvents.as_view(), name='search_events'),
    url(r'^search/equipments/$', search.SearchEquipments.as_view(), name='search_equipments'),
    url(r'^search/jobs/$', search.SearchJobs.as_view(), name='search_jobs'),
    url(r'^search/jobs/(?P<job_starts_with>(\w+))', search.SearchJobs.as_view(), name='search_jobs'),
    url(r'^my-jobs/', login_required(MyJobs.as_view()), name='my_jobs'),
    url(r'^jobs/job-payment/', login_required(JobPayment.as_view()), name='job_payment'),
    url(r'^jobs/edit/(?P<job_id>(\d+))$', login_required(UpdateJob.as_view()), name='edit_job'), 
    url(r'^jobs/post-job/$', login_required(Job.as_view()), name='post_job'),      
    url(r'^jobs/view/(?P<pk>(\d+))$', ViewJob.as_view(), name='view_job'),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^write/(?:(?P<recipients>[^/#]+)/)?$', WriteView.as_view(autocomplete_channels='ff_users'), name='write'),
    
    url(r'^chat/main/$', chat.ChatMain.as_view(), name='chat_main'),
    url(r'^chat/toolbar/$', chat.ChatToolbar.as_view(), name='chat_toolbar'),
    url(r'^chat/login/$', chat.ChatLogin.as_view(), name='chat_login'),
    url(r'^chat/options/$', chat.ChatOptions.as_view(), name='chat_options'),
    url(r'^chat/save/$', chat.ChatSaveMessages.as_view(), name='chat_save'),    
)
