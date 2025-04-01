from blog.urls import *
from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', blogsView.as_view(), name='blogs_view'),
    path('blog/<int:pk>', blogView.as_view(), name= "blogview"),
    path('register/', registerView.as_view(), name= 'register'),
    path('login/', loginview.as_view(), name= 'login'),
    path('logout/', logoutview.as_view(), name= 'logout'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name= 'delete'),
]