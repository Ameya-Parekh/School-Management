from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.add_show,name="addandshow"),
    path('delete/<int:id>/',v.delete_logic,name="delete"),
    path('edit/<int:id>/',v.update_logic,name="edit")

]