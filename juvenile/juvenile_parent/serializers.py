from rest_framework import serializers

from juvenile import models


class JuvenileParentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileParent
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "pinfl",
            "birth_date",
            "employment",
        )


class JuvenileParentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileParent
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "pinfl",
            "birth_date",
            "employment",
        )


class JuvenileParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileParent
        fields = (
            'id',
            "first_name",
            "last_name",
            "father_name",
            "pinfl",
            "birth_date",
            "employment",
        )


class JuvenileParentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileParent
        fields = (
            'id',
            "first_name",
            "last_name",
            "father_name",
            "pinfl",
            "birth_date",
            "employment",
        )
