from django.urls import path
from api.views.example_view import ExampleView
app_name = 'api'

urlpatterns = [
    path('example', ExampleView.as_view(), name='example')
]

