from userPTK.models import UserPTK
from userPTK.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminPTK

class UserDealerList(APIView):
    """
    View to get list of Dealers
    """
    permission_classes = [IsAuthenticated, IsAdminPTK]
    
    def get(self, request, format=None):
        dealer_list = UserPTK.objects.filter(role='DEA')
        dealer_list_serializer = UserSerializer(dealer_list, many=True)
        
        return Response(dealer_list_serializer.data)

class UserTokenAccessValid(APIView):
    """
    View to check if user token is valid
    """
    def get(self, request, format=None):
        """
        Return status 200 if token is valid
        """
        return Response()