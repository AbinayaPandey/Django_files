from django.contrib import admin
from student.models import profile, marks, group

admin.site.register(profile)


class MarksAdmin(admin.ModelAdmin):
    list_display = ("id", "stu_sub", "marks")


admin.site.register(marks, MarksAdmin)


@admin.register(group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "group_rank")
