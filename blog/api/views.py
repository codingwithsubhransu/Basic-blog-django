from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import *
from bloginterface.models import *
from bloginterface.models import *




# Create your views here.

class blogsView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = blogserializer




class BlogDeleteView(generics.DestroyAPIView):
    """Only the author of the post can delete it."""
    queryset = Post.objects.all()
    serializer_class = blogserializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:  # Ensure only the author can delete
            return Response({"error": "You can only delete your own posts"}, status=403)
        return super().delete(request, *args, **kwargs)


class blogView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = blogserializer
    lookup_field = 'pk'

class registerView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = registerserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    'message': 'User registered successfully',
                    'user': serializer.data,
                    'access': access_token,
                    'refresh': str(refresh),
                },status= status.HTTP_201_CREATED
            )
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
class loginview(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username= username, password= password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = registerserializer(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        
        return Response({'error': 'Invalid credential'}, status= status.HTTP_401_UNAUTHORIZED)

    
    
class logoutview(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')

            if not refresh_token:
                return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()

        except Exception:
            return Response({'error': 'Invalid token'}, status= status.HTTP_400_BAD_REQUEST)

