from django.contrib import admin
from .models import (
    Classroom, Enrollment, Announcement, Assignment, Submission, Comment,
    Quiz, Question, Choice, QuizSubmission, Answer,
    DiscussionThread, DiscussionMessage, MessageReaction
)

# ---------- QUIZ SYSTEM ADMIN ----------

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'created_by', 'start_time', 'end_time', 'is_published', 'created_at')
    list_filter = ('is_published', 'classroom', 'start_time')
    search_fields = ('title', 'classroom__name', 'created_by__username')
    ordering = ('-created_at',)
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'points', 'created_at')
    search_fields = ('question_text', 'quiz__title')
    list_filter = ('quiz',)
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'is_correct')
    search_fields = ('choice_text', 'question__question_text')
    list_filter = ('is_correct', 'question__quiz')


class QuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'is_submitted', 'total_score', 'submitted_at')
    search_fields = ('quiz__title', 'student__username')
    list_filter = ('is_submitted', 'submitted_at')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('submission', 'question', 'choice', 'is_correct')
    search_fields = ('submission__student__username', 'question__question_text')
    list_filter = ('is_correct', 'question__quiz')


# ---------- DISCUSSION SYSTEM ADMIN ----------

class DiscussionThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'created_by', 'is_pinned', 'last_activity')
    search_fields = ('title', 'classroom__name', 'created_by__username')
    list_filter = ('is_pinned', 'classroom')
    ordering = ('-is_pinned', '-last_activity')


class DiscussionMessageAdmin(admin.ModelAdmin):
    list_display = ('thread', 'created_by', 'content', 'created_at', 'is_edited')
    search_fields = ('thread__title', 'created_by__username', 'content')
    list_filter = ('created_at', 'is_edited')
    ordering = ('created_at',)


class MessageReactionAdmin(admin.ModelAdmin):
    list_display = ('message', 'user', 'reaction', 'created_at')
    search_fields = ('message__content', 'user__username')
    list_filter = ('reaction', 'created_at')


# ---------- EXISTING ADMIN SETUP ----------

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_code', 'created_by', 'created_at')
    search_fields = ('name', 'class_code', 'created_by__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'student', 'enrolled_at')
    search_fields = ('classroom__name', 'student__username')
    list_filter = ('enrolled_at',)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'created_by', 'created_at', 'file')
    search_fields = ('title', 'content', 'classroom__name', 'created_by__username')
    list_filter = ('created_at',)


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'created_by', 'due_date', 'created_at', 'file')
    search_fields = ('title', 'classroom__name', 'created_by__username')
    list_filter = ('due_date', 'created_at')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at', 'file', 'grade')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('submitted_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_by', 'assignment', 'announcement', 'is_private', 'created_at')
    search_fields = ('content', 'created_by__username', 'assignment__title', 'announcement__title')
    list_filter = ('created_at', 'is_private')
    ordering = ('-created_at',)
    list_display_links = ('content',)


# ---------- REGISTER EVERYTHING ----------

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(QuizSubmission, QuizSubmissionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.register(DiscussionThread, DiscussionThreadAdmin)
admin.site.register(DiscussionMessage, DiscussionMessageAdmin)
admin.site.register(MessageReaction, MessageReactionAdmin)
