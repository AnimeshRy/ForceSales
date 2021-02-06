from django.contrib import admin
from .models import Lead, Agent, User, UserProfile

admin.site.register(Lead)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Agent)
