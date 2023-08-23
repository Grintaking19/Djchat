from django.db.models import Count
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Server
from .serializers import ServerSerializer

# Create your views here.


class ServerListViewSet(viewsets.ViewSet):
    """
    A viewset for listing servers with various filtering options.

    Attributes:
        queryset (QuerySet): The base queryset for Server objects.

    Methods:
        list(request): List servers based on given query parameters.

    Returns:
        Response: A response containing serialized server data.
    """

    queryset = Server.objects.all()

    def list(self, request):
        """
        List servers based on provided query parameters.

        Args:
            request (HttpRequest): The HTTP request object.

        Query Parameters:
            categories (str): Filter servers by a specific category name.
            by_user (bool): Filter servers based on user membership (true/false).
            qty (int): Limit the number of server results to a specific quantity.
            by_server_id (int): Filter servers by a specific server ID.

        Example:
            To list servers filtered by category "gaming", for a user's servers,
            limited to 10 results, and filtering by server ID 5:
            GET /servers/?categories=gaming&by_user=true&qty=10&by_server_id=5

        Returns:
            Response: A response containing serialized filtered server data.

        Raises:
            AuthenticationFailed: If the user is not authenticated.
            ValidationError: If validation errors occur during filtering.
        """

        categories = request.query_params.get("categories")
        by_user = request.query_params.get("by_user") == "true"
        quantity = request.query_params.get("qty")
        by_server_id = request.query_params.get("by_server_id")

        # Check if user is authenticated
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail="User is not authenticated")

        # Filter servers by categories
        if categories:
            self.queryset = self.queryset.filter(categories__name=categories)

        # Filter servers based on user id
        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(members__id=user_id)

        # Filter servers based on server id
        if by_server_id:
            try:
                self.queryset = self.queryset.filter(id=by_server_id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server of id {by_server_id} does not exist")
            except ValueError:
                raise ValidationError(detail=f"Error with status code {ValueError}")

        # Filter servers based on quantity (limit)
        if quantity:
            self.queryset = self.queryset[: int(quantity)]

        # Annotate with number of members if servers exist
        if self.queryset.exists():
            self.queryset = self.queryset.annotate(num_members=Count("members"))

        # Serialize the queryset and return as response
        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
