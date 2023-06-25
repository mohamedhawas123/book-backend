from rest_framework import routers
from .views import AuthorViewSet, BookViewSet, PageViewSet
from django.urls import include, path


router = routers.DefaultRouter()


router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('page/(?P<book_id>\d+)', PageViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]
