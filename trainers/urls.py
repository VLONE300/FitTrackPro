from django.urls import path

from trainers.views import TrainersListView

urlpatterns = [
    path('', TrainersListView.as_view(), name='trainers-list')
]
