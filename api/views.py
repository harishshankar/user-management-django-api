from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django import http
from django.contrib.auth import authenticate

from .models import UserManagement
from .serializers import UserManagementSerializers



class UserManagementList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        users = UserManagement.objects.all()
        serializer = UserManagementSerializers(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        userdata = request.data
        # del userdata['id']
        serializer = UserManagementSerializers(data=userdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserManagementDetail(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return UserManagement.objects.get(pk=pk)
        except UserManagement.DoesNotExist:
            raise http.Http404
        
    def get(self, request, pkey):
        user = self.get_object(pkey)
        serializer = UserManagementSerializers(user)
        return Response(serializer.data)
    
    def put(self, request, pkey):
        user = self.get_object(pkey)
        userdata = request.data
        # del userdata['id']
        # del userdata['created']
        # del userdata['modified']
        serializer = UserManagementSerializers(user, data=userdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pkey):
        user = self.get_object(pkey)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class LoginView(APIView):
#     def Post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user:
#             return Response({'token' : user.auth_token.key})
#         return Response({'error' : "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
