from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'instructor', 'start_date', 'credits_display')
    list_filter = ('instructor', 'start_date')
    search_fields = ('course_code', 'title', 'instructor')
    date_hierarchy = 'start_date'
    fieldsets = (
        (None, {
            'fields': ('course_code', 'title', 'description', 'credits', 'instructor', 'start_date')
        }),
        ('Additional Information', {
            'classes': ('collapse',),
            'fields': ('prerequisites',),
        }),
    )
    readonly_fields = ('credits',)

    def credits_display(self, obj):
        return f"{obj.credits} credits"
    credits_display.short_description = 'Credits'

admin.site.register(Course, CourseAdmin)
