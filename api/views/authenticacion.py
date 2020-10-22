import json
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db import IntegrityError
from api.serializers import UserSerializer
from api.models import User

class CreateUserMobile(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        new_user = data['new_user']
        try:
            user = User.objects.create(**new_user)
            Token.objects.create(user=user)
            return Response(user)
        except IntegrityError as error:
            return Response({'message': error.__cause__})

class UpdateUserProfile(APIView):

    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None # Should check it TODO

    def put(self, request, user_id):
        data = json.loads(request.body.decode('utf-8'))
        user = self.get_object(user_id)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomAuthtoken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
        })
