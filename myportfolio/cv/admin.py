from django.contrib import admin
from .models import UserCV, WorkHistory, Education
# Register your models here.


@admin.register(UserCV)
class UserCVAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'skills')
    search_fields = ('user__username', 'bio', 'skills')
    list_filter = ('user',)

@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_cv_str', 'start_date', 'end_date', 'position', 'description')
    search_fields = ('user_cv__user__username', 'position', 'description')
    list_filter = ('start_date', 'end_date', 'position')

    def user_cv_str(self, obj):
        return str(obj.user_cv)
    user_cv_str.short_description = 'User CV'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user_cv_str', 'start_date', 'end_date', 'title')
    search_fields = ('user_cv__user__username', 'title')
    list_filter = ('start_date', 'end_date', 'title')

    def user_cv_str(self, obj):
        return str(obj.user_cv)
    user_cv_str.short_description = 'User CV'