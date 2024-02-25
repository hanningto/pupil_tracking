import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arc.settings')

import django
django.setup()

from arc_app.models import RfidTags

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()

try:
	id, text = reader.read()
	print(id)
	print(text)
	pup_dict = RfidTags.objects.all().values_list('tag_no')	
	print(pup_dict)
	y = str(id)
	for i in pup_dict:
		x = str(i[0])
		print(x)
		if x == y:
			print("Tag aready in data base")
			break
		else:
			continue
finally:
	GPIO.cleanup()
