from rest_framework.permissions import BasePermission

from trainers.models import UserTrainingProgram


class IsTrainer(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return hasattr(request.user, 'trainer')


class IsTrainerOfTrainingProgram(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            user_program_id = view.kwargs.get('user_program_id')
            user_program = UserTrainingProgram.objects.get(pk=user_program_id)
            return user_program.trainer == request.user
        else:
            user_progress = view.get_object()
            user_program = user_progress.user_program
            return user_program.trainer == request.user
