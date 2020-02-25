from django.db import models
from shopapi.utils.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class CourseCategory(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='课程分类名称')

    class Meta:
        db_table = 'shop_course_category'
        verbose_name = '课程分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Course(BaseModel):

    course_type_choices = (
        (0, '付费'),
        (1, 'VIP'),
        (2, '学位课程'),
    )

    course_level = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )

    name = models.CharField(max_length=128, verbose_name='课程名称')
    course_image = models.ImageField(upload_to='course', verbose_name='课程图片', blank=True, null=True)
    course_type = models.SmallIntegerField(choices=course_type_choices, default=0, verbose_name='付费类型')
    brief = RichTextUploadingField(max_length=200, verbose_name='简介', blank=True, null=True)
    level = models.SmallIntegerField(choices=course_level, default=0, verbose_name='课程等级')
    pub_date = models.DateTimeField(auto_now=True,)
    period = models.IntegerField(verbose_name='学习周期', default=7)
    attachment_path = models.FileField(upload_to="course_attachment", max_length=255, verbose_name="课件路径", blank=True,
                                       null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")
    course_category = models.ForeignKey('CourseCategory',on_delete=models.DO_NOTHING, blank=True, null=True)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    lessons = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_lessons = models.IntegerField(verbose_name="课时更新数量", default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="课程原价", default=0)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name="授课老师")

    @property
    def lesson_list(self):
        data_list = self.course_lesson.filter(is_recommend=True)
        if len(data_list) < 1:
            return []

        data = []
        for item in data_list:
            data.append({
                "id": item.id,
                "name": item.name,
                "lesson": item.lesson,
                "section_type": item.section_type,
                "section_link": item.section_link,
                "free_trail": item.free_trail,
            })
        return data

    @property
    def level_text(self):
        return self.course_level[self.level][1]

    class Meta:
        db_table = 'shop_course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Teacher(BaseModel):

    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
        )
    name = models.CharField(max_length=32, verbose_name="讲师名字")
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_name="讲师身份")
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, verbose_name="导师签名", help_text="导师签名", blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, verbose_name="讲师封面")
    brief = models.TextField(max_length=1024, verbose_name="讲师描述")

    class Meta:
        db_table = "shop_teacher"
        verbose_name = "讲师导师"
        verbose_name_plural = "讲师导师"

    def __str__(self):
        return "%s" % self.name


class CourseChapter(BaseModel):
    """课程章节"""
    course = models.ForeignKey(Course, related_name='coursechapters', on_delete=models.CASCADE, verbose_name="课程名称")
    chapter = models.SmallIntegerField(verbose_name="第几章", default=1)
    name = models.CharField(max_length=128, verbose_name="章节标题")
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)

    class Meta:
        db_table = "shop_course_chapter"
        verbose_name = "课程章节"
        verbose_name_plural = "课程章节"

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)


class CourseLesson(BaseModel):
    """
    课程课时
    """
    section_type_choices = (
        (0, '文档'),
        (1, '练习'),
        (2, '视频')
    )
    chapter = models.ForeignKey("CourseChapter", related_name='chapter_lesson', on_delete=models.CASCADE,
                                verbose_name="课程章节")
    course = models.ForeignKey("Course", related_name="course_lesson", on_delete=models.CASCADE, verbose_name="课程名称")
    name = models.CharField(max_length=128,verbose_name = "课时标题")
    lesson = models.IntegerField(default=1, verbose_name="第几课时")
    section_type = models.SmallIntegerField(default=2, choices=section_type_choices, verbose_name="课时种类")
    section_link = models.CharField(max_length=255, blank=True, null=True, verbose_name="课时链接",
                                    help_text="若是video，填vid,若是文档，填link")
    duration = models.CharField(verbose_name="视频时长", blank=True, null=True, max_length=32)  # 仅在前端展示使用
    pub_date = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    free_trail = models.BooleanField(verbose_name="是否可试看", default=False)
    is_recommend = models.BooleanField(verbose_name="是否推荐到课程列表", default=False)

    class Meta:
        db_table = "shop_course_lesson"
        verbose_name = "课程课时"
        verbose_name_plural = "课程课时"

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)
