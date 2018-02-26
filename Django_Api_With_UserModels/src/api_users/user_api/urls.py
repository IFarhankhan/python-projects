from django.conf.urls import url
from django.conf.urls import include 

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('Test-viewset',  views.TestViewSets, base_name='test-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
urlpatterns = [
  url('test-view/', views.TestApiView.as_view()),
  url('', include(router.urls))

]
