from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('occupied/', views.occupiedSeats, name="occupied_seat"),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('admin/', views.PerformanceView.as_view(), name='admin'),
    path('affiche/', views.affiche, name='affiche'),
    path('search/', views.Search.as_view(), name='search'),
    path('contact', views.contact, name='contact'),
    path('people', views.people, name='people'),
    path("register/", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("filter/", views.FilterPerformsView.as_view(), name='filter'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("<slug:slug>/", views.PerformanceDetailView.as_view(), name="perform_detail"),
    path("news/<str:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("people/<str:slug>/", views.ActorView.as_view(), name="person_detail"),
    path('<str:slug>/booking/', views.BookingView.as_view(), name='booking'),
]
