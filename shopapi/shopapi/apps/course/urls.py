from django.urls import path, re_path
from .views import CourseCategoryListAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseChapterAPIView

urlpatterns = [
    path('category/', CourseCategoryListAPIView.as_view()),
    path('', CourseListAPIView.as_view()),
    re_path('^(?P<pk>\d+)/$',CourseRetrieveAPIView.as_view()),
    path('chapter/',CourseChapterAPIView.as_view())


]
