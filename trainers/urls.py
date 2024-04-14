from django.urls import path
from rest_framework.routers import SimpleRouter

from trainers.views import TrainersListView, TrainersProgramView

router = SimpleRouter()
router.register(r'trainers-program', TrainersProgramView)

urlpatterns = [
    path('', TrainersListView.as_view(), name='trainers-list')
]

urlpatterns += router.urls
