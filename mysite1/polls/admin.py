from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.

# admin.site.register(Question)
# previous line 6 was replaced by the following codes in tutorial 7

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Question description', {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
            ]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# This particular change above makes the “Publication date” come before the “Question” field
