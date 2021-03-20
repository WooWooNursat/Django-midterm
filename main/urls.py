from django.urls import path, include
from rest_framework import routers

from main.views import BookViewSet, JournalViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('journals', JournalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]