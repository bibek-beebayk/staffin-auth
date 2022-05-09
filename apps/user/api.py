from djoser.views import TokenCreateView as DjoserTokenCreateView
from django import utils
from rest_framework import generics, status
from .serializers import TokenSerializer
from rest_framework.response import Response


class TokenCreateView(utils.ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """

    serializer_class = TokenSerializer
    # permission_classes = settings.PERMISSIONS.token_create


    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)       
        # print('\n\nToken: ', token, '\n\n')

        token_serializer = TokenSerializer(token, context={'request': self.request})
        # print(token_serializer_class(token).data)
        # context = {'request': self.request}
        return Response(
            data=token_serializer.data, status=status.HTTP_200_OK
        )
