from django.urls import path
from django.conf.urls import url


from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('admin/', views.PerformanceView.as_view(), name='admin'),
    path('affiche', views.affiche, name='affiche'),
    path('search/', views.Search.as_view(), name='search'),
    path('contact', views.contact, name='contact'),
    path('people', views.people, name='people'),
    path("filter/", views.FilterPerformsView.as_view(), name='filter'),
    path("<slug:slug>/", views.PerformanceDetailView.as_view(), name="perform_detail"),
    path("news/<str:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("people/<str:slug>/", views.ActorView.as_view(), name="person_detail"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
