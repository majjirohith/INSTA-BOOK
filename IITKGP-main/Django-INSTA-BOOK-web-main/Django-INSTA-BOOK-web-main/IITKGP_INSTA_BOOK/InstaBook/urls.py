from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg_log, name = 'Insta-Book'),
    path('main_page', views.main_page, name = 'Insta-Book'),
    path('main_page_L', views.main_page_L, name = 'Insta-Book'),
    path('main_page_R', views.main_page_R, name = 'Insta-Book'),
    path('register_login', views.reg_log, name = 'Insta-Book'),
    path('main_page_U', views.main_page_U, name = 'Insta-Book'),
    path('del_my_details', views.del_my_details, name = 'Insta-Book'),
    path('post_comments', views.post_comments, name = 'Insta-Book'),
    path('your_profile', views.your_profile, name = 'Insta-Book'),
    path('register', views.register, name = 'register'),
    path('view_comments', views.view_comments, name = 'Insta-Book'),
    path('upload_profile_pic', views.profile_pic, name = 'Insta-Book'),
    path('user_name-user_details', views.user_name_user_details, name = 'Insta-Book'),
    path('post_likes', views.post_likes, name = 'post_likes'),
    path('official_page', views.official_page, name = "official_page"),
]

urlpatterns += [
    path('nitc-fests', views.fests, name = 'fests'),
    path('nitc-clubs', views.clubs, name = 'clubs'),
    path('nitc-sports', views.sports, name = 'sports'),
    path('nitc-acedemic', views.acedemic, name = 'sports'),
    path('odyssey', views.odyssey, name = 'odyssey'),
    path('foot_ball', views.foot_ball, name = 'foot_ball'),
    path('chatting', views.chatting, name='foot_ball'),
    path('all_chatting', views.all_chatting, name='chatting groups'),
    path('post_message', views.post_message, name='message'),
]

#def filter_users(a,b):
    #a -- user_posts
    #b -- users
#    s1={}
#    q=[]
#    for i in a:
#        if i.u_name[-1] == 'U':
#            q.append(i)
#            str0 = ''
#            for j in i.u_name:
#                if j == ':':
#                    break
#                str0 += j
#            s1[str0] = 0
#    p = []
#    for i in b:
#        if i.username == "VidyaSagar":
#            continue
#        if i.username not in s1:
#            p.append(i)
# p-- not profile picture
#    return q,p
