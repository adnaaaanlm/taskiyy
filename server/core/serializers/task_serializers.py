from rest_framework import serializers
from core.models import Task


# Définition du sérialiseur pour le modèle Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Spécifie le modèle sur lequel le sérialiseur est basé
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'due_date', 'completed', 'canceled',
                  'priority', 'user']  # Liste des champs à inclure dans la sérialisation
        read_only_fields = ['id', 'created_at', 'updated_at',
                            'user']  # Champs qui ne peuvent pas être modifiés par l'utilisateur

    # Méthode pour créer une nouvelle instance de Task
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  # Associe l'utilisateur authentifié à la tâche
        return super().create(validated_data)  # Appelle la méthode create par défaut de ModelSerializer

    # Méthode pour mettre à jour une instance existante de Task
    def update(self, instance, validated_data):
        # Met à jour les attributs de l'instance avec les nouvelles données fournies
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.canceled = validated_data.get('canceled', instance.canceled)
        instance.priority = validated_data.get('priority', instance.priority)

        # Enregistre les modifications apportées à l'instance
        instance.save()
        return instance  # Retourne l'instance mise à jour
