from django.urls import path
from blog import views
from blog import api

# TODO: APP NAME 
app_name="blog"

urlpatterns = [
    path("",views.blog_index,name="blog_index"),
    # path('',views.blog_view,name="blog_view"),
    path('create/',views.blog_create,name="blog_create"),
    path('edit/<int:id>/',views.blog_edit,name="blog_edit"),
    path('delete/<int:id>/',views.blog_delete,name="blog_delete"),
    path('new/<str:data>/',views.data_view,name='data_view'),
    path('login/',views.loginPage,name='loginPage'),
    # path("redirect",views.test_redirect,name="test_redirect")

    #path('api/',api.hello_world,name='api_view'),
    path('api/blood_doner/',api.blood_doner,name ="blood_doner"),
    path('api/blood_doner_update/<int:id>/',api.blood_doner_update,name ="blood_doner_update"),
    path('api/blood_doner_delete/<int:id>/',api.blood_doner_delete,name ="blood_doner_delete")
]