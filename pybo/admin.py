from django.contrib import admin
from .models import Question,Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'create_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)