from django.urls import path, include
from django.contrib.auth import views as ApprovalsView
from rest_framework import routers
from .views import approvereject

router = routers.DefaultRouter()
router.register('myapi', ApprovalsView)
urlpatterns = [
	path('form/', ApprovalsView.myform, name='myform'),
    path('api/approvereject/', approvereject, name='approvereject'),
 
] 
