from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_text'], 'classes': {'collapse'}}),
        ('Date Information', {'fields': ['pub_date'], 'classes': {'collapse'}}),
    ]
    inlines = [ChoiceInline]
    list_display=('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
