# from django.contrib import admin
# from .models import Task

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'due_date', 'timestamp')
#     list_filter = ('status', 'due_date')
#     search_fields = ('title', 'tags')
#     fieldsets = (
#         (None, {'fields': ('title', 'description')}),
#         ('Dates', {'fields': ('timestamp', 'due_date')}),
#         ('Other Info', {'fields': ('tags', 'status')}),
#     )
#     readonly_fields = ('timestamp',)
# Register your models here.
from django.contrib import admin # type: ignore
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'tags')
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Dates', {'fields': ('timestamp', 'due_date')}),
        ('Other Info', {'fields': ('tags', 'status')}),
    )
    readonly_fields = ('timestamp',)
    ordering = ('-due_date',)  # added ordering
    list_per_page = 10  # added pagination
    list_editable = ('status',)  # added list editable