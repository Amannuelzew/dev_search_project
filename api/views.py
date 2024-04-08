from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer
from projects.models import Profiles
@api_view(['GET'])
def get_routes(request):
    routes=[
        {'GET':'api/developers'},
        {'GET':'api/developers/id'},

        {'POST':'api/developers/token'},
        {'POST':'api/developers/token/refresh'},
    ]
    return Response(routes)
@api_view(['GET'])
def get_developers(request):
    Profile=Profiles.objects.all()
    s=ProfileSerializer(Profile,many=True)
    return Response(s.data)
@api_view(['GET'])
def get_developer(request,id):
    Profile=Profiles.objects.get(pk=id)
    s=ProfileSerializer(Profile,many=False)
    return Response(s.data)
