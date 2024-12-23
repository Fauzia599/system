from django.urls import path
from myapp  import views
#from rest_framework_simplejwt.views import TokenObtainPairview

urlpatterns  = [

#url for Cleaner
path('Cleaner/',views.manage_Cleaner),
path('Cleaner/<int:id>',views.manage_Cleaner),

#url for Task
path('Task/',views.manage_Task),
path('Task/<int:id>',views.manage_Task),


#url for Facility
path('Facility/',views.manage_Facility),
path('Facility/<int:id>',views.manage_Facility),
]