from .models import CourseCategory, Course, CourseChapter, CourseLesson, Teacher
import xadmin


class CourseCategoryModelAdmin:
    pass


class CourseModelAdmin:
    pass


class CourseChapterModelAdmin:
    pass


class CourseLessonModelAdmin:
    pass


class TeacherModelAdmin:
    pass


xadmin.site.register(CourseCategory, CourseCategoryModelAdmin)
xadmin.site.register(Course, CourseModelAdmin)
xadmin.site.register(CourseChapter, CourseChapterModelAdmin)
xadmin.site.register(CourseLesson, CourseLessonModelAdmin)
xadmin.site.register(Teacher, TeacherModelAdmin)
