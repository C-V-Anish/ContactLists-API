from django.urls import path,include
from .views import ContactLC,ContactRUD


urlpatterns = [
    path('',ContactLC.as_view()),
    path('<int:id>/',ContactRUD.as_view()),
]