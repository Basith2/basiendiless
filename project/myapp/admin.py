from django.contrib import admin

# Register your models here.
from . models import user_login,alumni_details,college_details,college_profile_pic,alumni_job,branch_details
from . models import alumni_posts,event_details

admin.site.register(user_login)
admin.site.register(alumni_details)
admin.site.register(college_details)
admin.site.register(college_profile_pic)
admin.site.register(alumni_job)
admin.site.register(branch_details)
admin.site.register(alumni_posts)
admin.site.register(event_details)