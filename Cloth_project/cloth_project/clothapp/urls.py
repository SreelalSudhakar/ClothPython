

from django.urls import path

from clothapp import views
app_name='clothapp'


urlpatterns = [
    path('',views.index,name='index'),
    path('cloth/<int:cloth_id>/',views.details,name='details'),
    path('add/',views.add_cloth,name='add_cloth'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]