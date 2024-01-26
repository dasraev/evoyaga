from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from info import enums
from juvenile import models
from . import serializers


class JuvenileParentViewset(ModelViewSet):
    def get_queryset(self):
        return models.JuvenileParent.objects.all()

    def get_serializer_class(self):
        serializer_class = serializers.JuvenileParentListSerializer

        if self.action in ['create']:
            serializer_class = serializers.JuvenileParentCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.JuvenileParentDetailSerializer
        elif self.action in ['list']:
            serializer_class = serializers.JuvenileParentListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.JuvenileParentDetailSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        parent_info_juvenile_id = request.GET.get('parent_info_juvenile_id', None)
        serializer = self.get_serializer(data=request.data['parents'], many=True)
        parents = request.data['parents']

        if serializer.is_valid():
            for parent in parents:
                parent_type = parent.pop('parent_type')
                pinfl = parent['pinfl']
                try:
                    parent_obj = models.JuvenileParent.objects.get(pinfl=pinfl)
                except ObjectDoesNotExist:
                    print(33309,parent)
                    parent_obj = models.JuvenileParent.objects.create(**parent)

                parent_info_juvenile = models.ParentInfoJuvenile.objects.get(pk=parent_info_juvenile_id)

                try:
                    models.Relationship.objects.get(parent_info_juvenile=parent_info_juvenile, parent=parent_obj)
                except ObjectDoesNotExist:
                    models.Relationship.objects.create(parent_info_juvenile=parent_info_juvenile, parent=parent_obj,
                                                       parent_type=parent_type)

            return Response({"message": "Bolaning qarovchisi muvaffaqqiyatli qo'shildi!"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, format=None):
        queryset = self.get_queryset()
        parent = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(parent, request.data)
        parent_type = request.data.pop('parent_type')

        juvenile_id = request.GET.get('juvenile_id', None)

        if serializer.is_valid():
            models.Relationship.objects.filter(juvenile=juvenile_id, parent=pk).update(parent_type=parent_type)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, format=None):
        queryset = self.get_queryset()
        parent = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(parent)

        juvenile_id = request.GET.get('juvenile_id', None)
        if juvenile_id:
            relationship = models.Relationship.objects.get(juvenile=juvenile_id, parent=pk)

            new_data = dict(serializer.data)

            for item in enums.PARENT_TYPE_CHOICE:
                if item[0] == int(relationship.parent_type):
                    new_data['parent_type'] = item[1]

            return Response(new_data)
        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        queryset = self.get_queryset()
        parent = get_object_or_404(queryset, pk=pk)
        juvenile_id = request.GET.get('juvenile_id', None)
        models.Relationship.objects.filter(juvenile=juvenile_id, parent=parent).delete()
        try:
            models.Relationship.objects.get(parent=pk)
        except ObjectDoesNotExist:
            models.JuvenileParent.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)