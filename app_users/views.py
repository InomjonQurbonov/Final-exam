from datetime import datetime
from random import randint

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from config import settings
from app_users.models import PasswordResets
from config.permissions import IsOwnerOrSuperUser
from app_users.serializers import UserSerializer, ProfileSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProfileUpdateView(ModelViewSet):
    queryset = get_user_model().objects.all()
    http_method_names = ['put', 'patch', 'delete', 'get']
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrSuperUser,)


@api_view(['POST'])
def password_change_view(request):
    try:
        old_password = request.data['old_password']
        new_password = request.data['new_password']
    except KeyError:
        return Response(
            data={'message': 'Old password or new password is missing'},
            status=status.HTTP_400_BAD_REQUEST
        )
    user = request.user
    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return Response(
            data={'message': 'Your password successfully changed!'},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            data={'message': 'Old password entered wrong!'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'POST'])
def password_reset_view(request):
    if request.method == 'POST':
        try:
            reset_code = request.data['code']
            new_password = request.data['new_password']
        except KeyError:
            return Response(
                data={'message': 'code or new password is missing'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            reset_user = PasswordResets.objects.get(reset_code=reset_code)
            if reset_user.status:
                if datetime.now().timestamp() - reset_user.created_at.timestamp() > 600:
                    # return time out error if code sent more than 10 minutes ago
                    return Response(
                        data={'message': 'Code time out'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    data={'message': 'Password already reset with this code'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                data={'message': 'Code invalid!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = get_user_model().objects.get(pk=int(reset_user.user_id))
            PasswordResets.objects.filter(reset_code=reset_code).update(status=False)
            user.set_password(new_password)
            user.save()
            return Response(
                data={'message': 'Your password successfully reset!'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'GET':
        try:
            email = request.data['email']
        except KeyError:
            return Response(
                data={'message': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = get_user_model().objects.filter(email=email).first()
        if user:
            reset_code = f"{randint(100, 999)}-{randint(100, 999)}"
            try:
                reset_request = PasswordResets.objects.create(user=user, reset_code=reset_code)
                reset_request.save()
                send_mail(
                    subject='Password Reset Request',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    message=f'Please, insert this code to reset your password: {reset_code}!\n\n'
                            f'Code will expire in 10 minutes.',
                )
                return Response(
                    data={'message': 'Code for reset your password sent to your email, check your email, please!'},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                # print(e)
                return Response(
                    data={'message': 'An internal server error, try again please!'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                data={'message': 'User with this email not found!'},
                status=status.HTTP_400_BAD_REQUEST
            )

