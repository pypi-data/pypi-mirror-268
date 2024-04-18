#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/4/11
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response


class CreateRelModelMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = None
        return response

    def perform_create(self, serializer):
        key = self.get_parent_key()
        kwargs = {
            key: self.kwargs[key]
        }
        serializer.save(create_user_id=self.request.user.id, **kwargs)


class DestroyRelModelMixin(DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_destroy(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, serializer):
        kwargs = {
            f'{self.lookup_field}__in': serializer.validated_data[f'{self.lookup_field}s']
        }
        queryset = self.get_queryset().filter(**kwargs)
        queryset.delete()


class UpdateRelModelMixin(UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
