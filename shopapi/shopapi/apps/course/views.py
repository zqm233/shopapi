from django.shortcuts import render
from .serializers import CourseCategorySerializer,CourseSerializer,CourseRetrieveModelSerializer, CourseChapterSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import CourseCategory, Course, CourseChapter
from django_filters.rest_framework import DjangoFilterBackend


class CourseCategoryListAPIView(ListAPIView):
    queryset = CourseCategory.objects.filter(is_show=True, is_del=False).order_by("order", "-id")
    serializer_class = CourseCategorySerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.filter(is_show=True, is_del=False).order_by("order", "-id")
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['course_category']
    ordering_fields = ['id', 'students', 'price']


class CourseChapterAPIView(ListAPIView):
    queryset = CourseChapter.objects.filter(is_show=True, is_del=False).order_by("order", "-id")
    serializer_class = CourseChapterSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('course',)


class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.filter(is_show=True, is_del=False).order_by("order", "-id")
    serializer_class = CourseRetrieveModelSerializer

