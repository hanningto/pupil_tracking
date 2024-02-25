import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arc.settings')
import django
django.setup()

from arc_app.models import RfidTags


new_record ='34:21:19'
#new_record.save()

tags = RfidTags.objects.all()

for i in tags:
    if new_record == i:
        print("this tag is the database")
    
    else:
        print("this is a new tag")