from django.urls import path
from .views import ContentView,load_more_content

urlpatterns = [
    path('', ContentView.as_view(), name='landing_page'),
    path('load-more-content/', load_more_content, name='load_more_content'),

]
