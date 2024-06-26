from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from agents.models import Agent
from landlords.models import Landlord
from tenants.models import Tenant


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):

        try:
            # Your authentication logic here
            user = authenticate(
                username=request.data["username"], password=request.data["password"]
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                # get a profile pic if it exists
                profile_pic = None
                if user.profile_picture:
                    profile_pic = user.profile_pic.url

                role = "Unknown"

                if Tenant.objects.filter(user=user).exists():
                    role = "Tenant"
                elif Landlord.objects.filter(user=user).exists():
                    role = "Landlord"
                elif Agent.objects.filter(user=user).exists():
                    role = "Agent"

                return Response(
                    {
                        "token": token.key,
                        # user metadata
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
                        "role": role,
                    }
                )
            else:
                return Response({"error": "Invalid credentials"}, status=400)
        except KeyError as e:
            return Response(
                {
                    "error": "Please provide both username and password",
                },
                status=400,
            )
