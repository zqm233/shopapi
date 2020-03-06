from django.urls import path
from .views import CartAPIView
from course.views import CourseListAPIView
urlpatterns = [
    path('', CartAPIView.as_view({"post": "add",
                                  'get': 'get',
                                  'delete': 'delete',
                                  'patch': 'patch',
                                  'put': 'put',
                                  })),
]