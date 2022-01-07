from rest_framework import serializers

from apps.models import Patient, Address, Subject, Message


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'user', 'gender', 'last_name', 'first_name', 'phone']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'created_at', 'message', 'user']


class SubjectDetailSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['id', 'title', 'messages']

    def get_messages(self, instance):
        # Le paramètre 'instance' est l'instance de la catégorie consultée.
        # Dans le cas d'une liste, cette méthode est appelée autant de fois qu'il y a
        # d'entités dans la liste

        # On applique le filtre sur notre queryset pour n'avoir que les produits actifs
        queryset = instance.get_messages
        # Le serializer est créé avec le queryset défini et toujours défini en tant que many=True
        serializer = MessageSerializer(queryset, many=True)
        # la propriété '.data' est le rendu de notre serializer que nous retournons ici
        return serializer.data
