from django.contrib import admin
from .models import Profile, Stand, StandDescription, Question

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','username','user','knowledge','is_guest','is_host')
admin.site.register(Profile, ProfileAdmin)

class StandAdmin(admin.ModelAdmin):
    list_display = ('id','name','owner')
admin.site.register(Stand, StandAdmin)

class StandDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id','stand','knowledge')
admin.site.register(StandDescription, StandDescriptionAdmin)

class QuestionAdminx(admin.ModelAdmin):
    list_display = ('id','title',)
admin.site.register(Question, QuestionAdminx)
