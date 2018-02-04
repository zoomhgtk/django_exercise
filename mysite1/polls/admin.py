from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.

# admin.site.register(Question)
# previous line 6 was replaced by the following codes in tutorial 7

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    #This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Question description', {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collasps']}),
            ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# This particular change above makes the “Publication date” come before the “Question” field
