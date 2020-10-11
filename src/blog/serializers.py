from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Post


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        print
        if not user:
            raise serializers.ValidationError("Incorect email or password")

        return {"user": user}


class UserSerializer(serializers.HyperlinkedModelSerializer):

    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name="post-detail", queryset=Post.objects.all()
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "posts"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Post
        fields = ["url", "id", "title", "body", "created", "owner"]