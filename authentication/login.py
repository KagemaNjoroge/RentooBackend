from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import LoginSerializer
from rest_framework.decorators import api_view
from drf_yasg import openapi


@swagger_auto_schema(
    method="POST",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["username", "password"],
        properties={
            "username": openapi.Schema(type=openapi.TYPE_STRING),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD
            ),
        },
    ),
    operation_description="Login a user",
    responses={200: "OK", 401: "Unauthorized"},
)
@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = authenticate(
            username=serializer.data.get("username"),
            password=serializer.data.get("password"),
        )

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            profile_pic = None
            if user.profile_picture:
                profile_pic = user.profile_pic.url

            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "website": user.website,
                    "bio": user.bio,
                    "location": user.location,
                    "birth_date": user.birth_date,
                    "phone_number": user.phone_number,
                    "profile_picture": profile_pic,
                    "kra_pin": user.kra_pin,
                }
            )
        else:
            return Response({"error": "Invalid credentials"}, status=401)
    else:

        return Response(data={"error": "Invalid credentials"}, status=401)
