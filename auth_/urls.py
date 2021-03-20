from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from auth_ import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.UserViewSet.as_view({'post': 'create'}))
]