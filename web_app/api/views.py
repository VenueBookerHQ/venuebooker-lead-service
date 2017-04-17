from . import authentication
from web_app.serializers import *

class AuthView(APIView):
    authentication_classes = (authentication.QuietBasicAuthentication,)
    serializer_class = serializers.UserSerializer
 
    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
