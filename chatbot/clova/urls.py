from django.urls import path, include
import clova.views

app_name = 'clova'


urlpatterns = [
    path('chatbot/',clova.views.chatbot,name="chatbot"),
]
