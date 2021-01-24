from django.contrib import admin
from .models import Lead, Agent, User

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Agent)
