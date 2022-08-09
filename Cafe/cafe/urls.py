from.import views
from django.urls import path


urlpatterns = [
    path('',views.index, name='index' ),
    path('menyu',views.menyu, name='menyu' ),
    path('menyu_detail/<int:pk>/',views.menyu_detail, name='menyu_detail' ),
    path('about',views.about, name='about' ),
    path('menyu_crate',views.menyu_create, name='menyu_crate' ),
    path('menyu_update/<int:pk>/',views.menyu_update, name='menyu_update' ),
    path('menyu_delete/<int:pk>/',views.menyu_delete, name='menyu_delete' ),
    path('sector/',views.sector, name='sector' ),
    path('connect/',views.connect, name='connect' ),


]
 