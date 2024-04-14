from rest_framework.permissions import BasePermission


class IsTrainer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'trainer')


class IsTrainerOfTrainingProgram(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.trainer.user == request.user
