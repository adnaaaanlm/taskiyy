from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Task
from .serializers.task_serializers import TaskSerializer

# Vue pour lister les tâches
class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer  # Spécifie le sérialiseur à utiliser
    permission_classes = [IsAuthenticated]  # Nécessite que l'utilisateur soit authentifié

    def get_queryset(self):
        # Retourne les tâches pour l'utilisateur authentifié
        return Task.objects.filter(user=self.request.user)

# Vue pour créer une nouvelle tâche
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer  # Spécifie le sérialiseur à utiliser
    permission_classes = [IsAuthenticated]  # Nécessite que l'utilisateur soit authentifié

    def perform_create(self, serializer):
        # Surcharge de la méthode pour ajouter l'utilisateur à la tâche créée
        print('serializer :', serializer)  # Pour débogage
        serializer.save(user=self.request.user)  # Enregistre la tâche avec l'utilisateur

# Vue pour éditer une tâche existante
class TaskEditView(generics.UpdateAPIView):
    serializer_class = TaskSerializer  # Spécifie le sérialiseur à utiliser
    permission_classes = [IsAuthenticated]  # Nécessite que l'utilisateur soit authentifié
    lookup_field = 'id'  # Utilise 'id' pour identifier la tâche à mettre à jour

    def get_queryset(self):
        # Retourne les tâches de l'utilisateur authentifié
        return Task.objects.filter(user=self.request.user)

# Vue pour annuler une tâche
class TaskCancelView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]  # Nécessite que l'utilisateur soit authentifié
    lookup_field = 'id'  # Utilise 'id' pour identifier la tâche à annuler

    def get_queryset(self):
        # Retourne les tâches de l'utilisateur authentifié
        return Task.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        # Méthode pour annuler la tâche
        instance = self.get_object()  # Récupère l'instance de la tâche
        instance.canceled = True  # Définit le champ 'canceled' à True
        instance.save()  # Enregistre les modifications
        return Response({'status': 'task canceled'}, status=status.HTTP_200_OK)  # Retourne une réponse de succès

# Vue pour marquer une tâche comme complétée
class TaskCompleteView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]  # Nécessite que l'utilisateur soit authentifié
    lookup_field = 'id'  # Utilise 'id' pour identifier la tâche à compléter

    def get_queryset(self):
        # Retourne les tâches de l'utilisateur authentifié
        return Task.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        # Méthode pour compléter la tâche
        instance = self.get_object()  # Récupère l'instance de la tâche
        instance.completed = True  # Définit le champ 'completed' à True
        instance.save()  # Enregistre les modifications
        return Response({'status': 'task completed'}, status=status.HTTP_200_OK)  # Retourne une réponse de succès

# Vue pour supprimer une tâche
class TaskDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]  # Nécessite que l'utilisateur soit authentifié
    lookup_field = 'id'  # Utilise 'id' pour identifier la tâche à supprimer

    def get_queryset(self):
        # Retourne les tâches de l'utilisateur authentifié
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        # Méthode pour supprimer la tâche
        instance = self.get_object()  # Récupère l'instance de la tâche
        instance.delete()  # Supprime l'instance
        return Response(status=status.HTTP_204_NO_CONTENT)  # Retourne une réponse de succès sans contenu
