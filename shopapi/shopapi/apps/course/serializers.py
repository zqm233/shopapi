from rest_framework import serializers
from .models import CourseCategory,Teacher,Course,CourseLesson,CourseChapter


class CourseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = ['id', 'name']


class CourseTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'signature', 'title', 'image', 'brief']


class LessonModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseLesson
        fields = ['id', 'name', 'lesson']


class CourseChapterSerializer(serializers.ModelSerializer):
    chapter_lesson = LessonModelSerializer(many=True)

    class Meta:
        model = CourseChapter
        fields = ["id", "name",'chapter_lesson']


class CourseSerializer(serializers.ModelSerializer):
    teacher = CourseCategorySerializer()
    coursechapters = CourseChapterSerializer(many=True)

    class Meta:
        model = Course
        fields = ("id", "name", "course_image", "students", "lessons", "pub_lessons", "price", "teacher",
                  'lesson_list', 'coursechapters')


class CourseRetrieveModelSerializer(serializers.ModelSerializer):
    teacher = CourseTeacherSerializer()

    class Meta:
        model = Course
        fields = ["id","name","course_image","students","lessons","pub_lessons","price","teacher",
                  "level_text","brief","attachment_path"]