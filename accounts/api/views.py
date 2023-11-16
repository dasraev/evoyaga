from datetime import datetime

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.http import JsonResponse, Http404
from django.middleware import csrf
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters import rest_framework as filters

from accounts.models import CustomUser
from . import serializers
from .paginations import UserPagination
from .filters import UserFilter

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# @api_view(['GET'])
# @authentication_classes([])
# @permission_classes([AllowAny])
# Create your views here.
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, format=None):
        data = request.data

        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                print(data)
                # response.set_cookie(
                #     settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                #     data["refresh_token"],
                #     httponly=True,
                #     expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                #     max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_MAX_AGE'],
                # )
                csrf.get_token(request)
                response.data = {"access_token": data["access"]}

                return response
            else:
                return Response({"No active": "This account is not active!!"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Invalid username or password!!"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RefreshView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, format=None):
        refresh = request.COOKIES.get(
            settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        response = Response()
        if refresh is None or refresh == '':
            response.status_code = 401
            response.data = {'message': "refresh token is invalid"}
            return response
        try:
            token = RefreshToken(refresh)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=token.access_token,
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.data = {"Success": "refresh successfully"}
            return response
        except Exception:
            response.status_code = 401
            response.data = {'message': "refresh token is invalid"}
            return response


class MeApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializers = serializers.MeSerializer

    def get(self, format=None):
        serializer = serializers.MeSerializer(self.request.user)
        return Response(serializer.data)


def logout_view(request):
    response = JsonResponse({'message': 'Logged out'})
    response.set_cookie('csrftoken', expires=datetime(2000, 1, 1))
    response.set_cookie(
        key='access_token',
        expires=datetime(2000, 1, 1),
        samesite='None',
        secure=True,
        httponly=True
    )
    response.set_cookie('refresh_token', expires=datetime(2000, 1, 1))
    return response


class UserCreateForApparatAPIView(generics.CreateAPIView):
    model = CustomUser
    serializer_class = serializers.UserCreateForApparatSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        markaz_id = request.data['markaz']
        group_code = request.data['groups']
        request_code = None
        if request.user.is_superuser == False:
            request_code = request.user.groups.all()[0].code
        if request_code == 1:
            users = CustomUser.objects.all().filter(markaz=markaz_id)
            for user in users:
                try:
                    user_instance_code = user.groups.all()[0].code
                except:
                    user_instance_code = None
                if user_instance_code:
                    if user_instance_code == 2 and group_code == '2':
                        return Response({"Bu viloyatga direktor allaqachon qo'shilgan!"},
                                        status=status.HTTP_400_BAD_REQUEST)
            if 'photo' in request.data and request.data['photo']:
                immutable = request.data._mutable if hasattr(request.data, '_mutable') else True
                if not immutable:
                    request.data._mutable = True
                photo = request.data.pop('photo', None)
                if not immutable:
                    request.data._mutable = False
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.create(serializer.data, photo[0])
                    return Response({"message": "Foydalanuvchi muvaffaqqiyatli qo'shildi!"}, status=status.HTTP_201_CREATED)
                return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Rasm yuklanishi shart"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "joriy foydalanuvchi apparat emas!"}, status=status.HTTP_401_UNAUTHORIZED)


class UserUpdateForApparatAPIView(APIView):
    queryset = CustomUser.objects.all()

    def put(self, request, pk, format=None):
        instance = CustomUser.objects.get(pk=pk)
        request_code = request.user.groups.all()[0].code
        group_code = request.data['groups']
        markaz_id = request.data['markaz']

        if request_code == 1:
            users = CustomUser.objects.all().filter(markaz=markaz_id)
            for user in users:
                try:
                    user_instance_code = user.groups.all()[0].code
                except:
                    user_instance_code = None
                if user_instance_code:
                    if user_instance_code == 2 and group_code == '2':
                        return Response({"Bu viloyatga direktor allaqachon qo'shilgan!"})
            serializer = serializers.UserUpdateForApparatSerializer(instance, data=request.data)
            if serializer.is_valid():
                instance.set_password(serializer.validated_data.get("password"))
                instance.save()
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Joriy foydalanuvchi Apparat emas!"}, status=status.HTTP_401_UNAUTHORIZED)


class UserCreateForDirektorAPIView(generics.CreateAPIView):
    model = CustomUser
    serializer_class = serializers.UserCreateForDirektorSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser == False:
            request_code = request.user.groups.all()[0].code
        if request_code == 2:
            if 'photo' in request.data and request.data['photo']:
                photo = request.data.pop('photo', None)
                markaz = self.request.user.markaz
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.create(serializer.data, photo[0], markaz)
                    return Response({"message": "Foydalanuvchi muvaffaqqiyatli qo'shildi"}, status=status.HTTP_201_CREATED)
                return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response( {"message": "Rasm yuklanishi shart!"} ,status=status.HTTP_400_BAD_REQUEST)
        return Response( {"message": "Joriy foydalanuvchi direktor emas!"}, status=status.HTTP_401_UNAUTHORIZED)


class MonitoringUserCreateAPIView(generics.CreateAPIView):
    model = CustomUser
    serializer_class = serializers.MonitoringUserCreateSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        request_code = None
        if request.user.is_superuser == False:
            request_code = request.user.groups.all()[0].code
        # if request_code == 1:
            if 'photo' in request.data and request.data['photo']:
                immutable = request.data._mutable if hasattr(request.data, '_mutable') else True
                if not immutable:
                    request.data._mutable = True
                photo = request.data.pop('photo', None)
                if not immutable:
                    request.data._mutable = False
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.create(serializer.data, photo[0])
                    return Response({"message": "Foydalanuvchi muvaffaqqiyatli qo'shildi!"}, status=status.HTTP_201_CREATED)
                return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Rasm yuklanishi shart"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "joriy foydalanuvchi apparat emas!"}, status=status.HTTP_401_UNAUTHORIZED)


class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()

    def list(self, request):
        groups = request.user.groups.all()
        queryset = None
        for group in groups:
            if group.code == 1:
                queryset = Group.objects.all().filter(code__gte=2)
            elif group.code == 2:
                queryset = Group.objects.all().filter(code__gte=3)
        serializer = serializers.GroupListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListAPIView(generics.ListAPIView):
    def get_queryset(self,):
        position = self.request.query_params.get('position')
        markaz = self.request.query_params.get('markaz')
        markaz_tuman = self.request.query_params.get('markaz_tuman')
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_markaz = self.request.user.markaz
        user_code = list(group_codes)[0]

        if user_code == 1:
            print('hello world')
            if markaz_tuman and position:
                return CustomUser.objects.all().filter(groups__code=position).filter(markaz_tuman_id=markaz_tuman).filter(groups__code__gte=2)
            if markaz and position:
                return CustomUser.objects.all().filter(groups__code=position).filter(markaz_id=markaz).filter(groups__code__gte=2)
            return CustomUser.objects.all().filter(groups__code=position).filter(groups__code__gte=2)

        return CustomUser.objects.filter(markaz=user_markaz).filter(groups__code__gte=3)
    pagination_class = UserPagination
    serializer_class = serializers.UserListSerializer


class UserDeleteAPIView(GenericAPIView):
    serializer_class = serializers.UserListSerializer
    queryset = CustomUser.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)