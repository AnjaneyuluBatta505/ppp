from django.contrib import admin
from .models import *
from .forms import *

admin.site.site_header = 'practice-placement-papers Administration'


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    exclude = []

    class Media:
        js = ('js/ckeditor/ckeditor.js',
              'js/ckeditor/configuration-ckeditor.js')


class ChoiceInline(admin.StackedInline):
    form = ChoiceForm
    model = Choice
    extra = 4

    def get_extra(self, request, obj=None, **kwargs):
        if obj.id:
            return 0
        return self.extra

    class Media:
        js = ('js/ckeditor/ckeditor.js',
              'js/ckeditor/configuration-ckeditor.js')


class AnswerInline(admin.StackedInline):
    form = AnsForm
    model = Answer
    extra = 1

    class Media:
        js = ('js/ckeditor/ckeditor.js',
              'js/ckeditor/configuration-ckeditor.js')


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    # exclude = []
    inlines = [ChoiceInline, AnswerInline]
    list_filter = ('sub_topic',)
    search_fields = [('data')]

    class Media:
        js = ('js/ckeditor/ckeditor.js',
              'js/ckeditor/configuration-ckeditor.js')


class SubTopicInline(admin.StackedInline):
    model = SubTopic
    extra = 1


class SubTopicAdmin(admin.ModelAdmin):
    model = SubTopic
    extra = 1
    search_fields = [('name')]

    class Media:
        js = ('js/ckeditor/ckeditor.js',
              'js/ckeditor/configuration-ckeditor.js')


class TopicAdmin(admin.ModelAdmin):

    exclude = []
    inlines = [SubTopicInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SubTopic, SubTopicAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Year)
