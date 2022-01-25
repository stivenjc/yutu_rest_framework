from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializers

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializers(users, many=True)
        return Response(user_serializer.data)

    elif request.method == 'POST':
        user_serializer = UserSerializers(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
