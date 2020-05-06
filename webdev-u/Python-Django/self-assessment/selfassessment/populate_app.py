import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','selfassessment.settings')
print("done setting the django setting")
import django
django.setup()
print("done doing the django settings")
## faker pop script

import random
from app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakergen=Faker()

print(" done importing and assigning faker")
topics =['Search','Social','Marketplace','News','Games']

for x in topics:
    print(x)

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get teh topuc for the entry
        top = add_topic()
        # create the fake data for that entry
        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        # cretae the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top , url= fake_url,name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("hello from main fuction")
    print("populating script!")
    populate(20)
    print("populating complete")
