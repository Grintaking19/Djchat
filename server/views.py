# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .serializers import ServerSerializer

# Create your views here.


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        categories = request.query_params.get("categories")
        by_user = request.query_params.get("by_user") == "true"
        quantity = request.query_params.get("qty")
        by_server_id = request.query_params.get("by_server_id")

        # check if user is authenticated
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail="User is not authenticated")

        # filter servers by categories
        if categories:
            self.queryset = self.queryset.filter(categories__name=categories)

        # filter servers based on user id
        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(members__id=user_id)

        # filter servers based on server id\
        if by_server_id:
            try:
                self.queryset = self.queryset.filter(id=by_server_id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server of id {by_server_id} does not exist")
            except ValueError:
                raise ValidationError(detail=f"Error of Status code {ValueError}")

        # filter servers based on quantity (limit) you want to get
        if quantity:
            self.queryset = self.queryset[: int(quantity)]

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
