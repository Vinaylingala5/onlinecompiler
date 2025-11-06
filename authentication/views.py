from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users
from .serializers import UserRegisterSerializer, UserLoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'full_name': user.full_name
            }
        }, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)

            token.blacklist()  # blacklist the token so it can’t be reused
            return Response({"message": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
