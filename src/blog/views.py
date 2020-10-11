from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import generics, permissions, authentication
from rest_framework import views
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Post
from .serializers import LoginSerializer, PostSerializer, UserSerializer


@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "users": reverse("user-list", request=request),
            "posts": reverse("post-list", request=request),
            "login": reverse("login", request=request),
        }
    )


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        login(request, user)
        return Response(UserSerializer(user, context={"request": request}).data)


class UserView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)