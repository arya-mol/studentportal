
from django.urls import path
from student import views

urlpatterns=[
    path('signup',views.SignupView.as_view(),name="signup"),
    path('signin',views.ListView.as_view(),name="signin")
]
