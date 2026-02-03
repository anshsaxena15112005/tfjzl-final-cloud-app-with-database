from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# ✅ Task 2: Inline choices under a question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# ✅ Task 2: Inline questions under a course
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# ✅ Task 2: Question admin shows choices on same page
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# ✅ Register everything
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
