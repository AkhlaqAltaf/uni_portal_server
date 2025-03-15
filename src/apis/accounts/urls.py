from django.urls import path

from src.apis.accounts import views
app_name = 'accounts'
urlpatterns =[

    path('', views.Accounts.as_view(), name='index'),
]