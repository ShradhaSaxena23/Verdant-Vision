from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('detect/', views.detect, name='detect'),
	path('detect/predict/', views.predict, name='predict'),
	path('testing/', views.testing, name='testing'),
	path("contact/",views.contact_page,name="contact"),
	path("sign-in/",views.sign_in,name="sign-in"),
	path("register/",views.register,name="register"),
	path("about/",views.about ,name="about"),
]
