from django.contrib import admin

# Register your models here.
from chat.models import UserProfile, ClientProfile, ClientChat, OperatorChat
admin.site.register(UserProfile)
admin.site.register(ClientProfile)
admin.site.register(ClientChat)
admin.site.register(OperatorChat)