from django.contrib import admin
from .models import Attachmenttype, Department, Jobposition, Member

for model in [Attachmenttype, Department, Jobposition, Member]:
    admin.site.register(model)
