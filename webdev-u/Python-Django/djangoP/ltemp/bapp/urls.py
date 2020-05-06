from django.conf.urls import url,include
from bapp import views

# template tagging
app_name = 'bapp'

urlpatterns=[
    url('relative/',views.relative,name='relative'),
    url('other/',views.other,name='other'),
]
