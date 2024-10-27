from random import choices  # Importation inutile ici, peut être retirée
from djoser.serializers import UserCreateSerializer  # Importation du sérialiseur d'utilisateur de Djoser
from rest_framework import serializers  # Importation du module serializers de Django REST Framework
from rest_framework_simplejwt.tokens import RefreshToken  # Importation de la classe pour générer des tokens JWT
from core.models import AppUser  # Importation du modèle utilisateur personnalisé

# Surcharge du sérialiseur d'utilisateur de Djoser
class UserSerializer(UserCreateSerializer):
    # Champ pour confirmer le mot de passe, uniquement en écriture
    re_password = serializers.CharField(required=True, max_length=100, write_only=True)

    class Meta:
        model = AppUser  # Utilisation du modèle AppUser personnalisé
        fields = (
            'email', 'first_name', 'last_name', 'username', 'password', 're_password'
        )

    def validate(self, attrs):
        # Validation pour s'assurer que le mot de passe et sa confirmation correspondent
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        # Méthode pour créer un nouvel utilisateur
        data = {**validated_data}  # Copie des données validées
        data.pop('re_password', None)  # Suppression du champ de confirmation du mot de passe
        user = AppUser.objects.create_user(**data)  # Création de l'utilisateur avec les données fournies
        return user

    def to_representation(self, instance):
        # Surcharge de la méthode pour ajouter les tokens d'authentification
        representation = super().to_representation(instance)  # Appel à la méthode de représentation par défaut

        # Génération des tokens JWT pour l'utilisateur
        refresh = RefreshToken.for_user(instance)
        representation['refresh'] = str(refresh)  # Ajout du token de rafraîchissement
        representation['access'] = str(refresh.access_token)  # Ajout du token d'accès

        return representation
