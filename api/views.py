from django.http import JsonResponse
from projects.models import Profiles
def get_routes(request):
    routes=[
        {'GET':'api/developers'},
        {'GET':'api/developers/id'},

        {'POST':'api/developers/token'},
        {'POST':'api/developers/token/refresh'},
    ]
    return JsonResponse(routes,safe=False)
def get_developers(request):
    Profile=Profiles.objects.all()
    return JsonResponse(Profile,safe=False)
