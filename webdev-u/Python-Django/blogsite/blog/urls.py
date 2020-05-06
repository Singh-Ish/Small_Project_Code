from django.conf.urls import url
from blog import views
from django.urls import path

urlpatterns =[
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/(?p<pl>\d+)', views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/(?p<pl>\d+)/edit/', views.PostUpdateView.as_view(),name='post_edit'),
    path('post/(?p<pl>\d+)/remove/', views.PostDetailView.as_view(),name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/(?p<pl>\d+)/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/(?p<pl>\d+)/approve/',views.comment_approve,name='comment_approve'),
    path('comment/(?p<pl>\d+)/remove/',views.comment_remove,name='comment_remove'),
    path('post/(?p<pl>\d+)/publish/',views.post_publish,name='post_publish')


]
