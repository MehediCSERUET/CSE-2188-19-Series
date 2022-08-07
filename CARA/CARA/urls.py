from django.urls import include, re_path as url
from .views import YoMamaBotView
urlpatterns = [
                  url(r'^fada317c0163d884ab1ba2ed3ba6c78d3d62e1b0b58ef97708/?$', YoMamaBotView.as_view()) 
]