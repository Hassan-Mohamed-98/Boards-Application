from django.contrib import admin
from .models import Board, Topic
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
# Register your models here.

@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    pass
# Change Panel in header
admin.site.site_header = 'Boards Admin Panel'
admin.site.site_title = 'Boards Admin'

class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]

# class TopicAdmin(admin.ModelAdmin):
#     # pass
#     fields = ['subject', 'board', 'created_by', 'views']
#     list_display = ('subject', 'board', 'created_by', 'combine_subject_board')
#     list_display_links = ('board', 'created_by')
#     list_editable = ('subject',)
#     list_filter = ('created_by', 'board')
#     search_fields = ('board','created_by')

    def combine_subject_board(self, object):
        return "{} - {}".format(object.subject , object.board)

admin.site.register(Board, BoardAdmin)
# admin.site.register(Topic, TopicAdmin)
#-----------------------


