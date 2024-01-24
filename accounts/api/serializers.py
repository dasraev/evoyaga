from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from accounts.models import CustomUser, CustomAccountManager
from info.models import Markaz, MarkazTuman


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


class UserGroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class MeSerializer(serializers.ModelSerializer):
    full_name_position = serializers.SerializerMethodField('get_user_full_name')
    position = serializers.SerializerMethodField('get_position')
    region = serializers.SerializerMethodField('get_region')

    def get_user_full_name(self, obj):
        position = {obj.groups.all()[0]}
        full_name = f"{obj.first_name} {obj.last_name} {obj.father_name}"
        for item in position:
            if item.code == 1:
                return f"Ichki ishlar vazirligi e-voya tizimi | {item}"
            else:
                return f"{full_name} | {item}"

    def get_position(self, obj):
        position = {obj.groups.all()[0]}
        for item in position:
            return item.name

    def get_region(self, obj):
        if obj.markaz:
            return obj.markaz.region.id


    class Meta:
        model = CustomUser
        fields = ('username', 'full_name_position', 'position', 'region')


class UserCreateForApparatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'father_name',
                  'markaz', 'groups', 'photo', 'birth_date', "email", 'password', 'login')
    def create(self, validated_data, photo):
        email = validated_data.pop('email')
        login = validated_data.pop('login')
        password = validated_data.pop('password')
        groups = validated_data.pop('groups')
        markaz_id = validated_data.pop('markaz')
        markaz_instance = Markaz.objects.get(pk=markaz_id)

        user = CustomUser.objects.create_user(email=email, password=password, login=login, **validated_data)
        user.photo = photo
        user_role = Group.objects.get(code=groups[0])
        role_id = user_role.id
        user.groups.set([role_id])
        user.markaz = markaz_instance
        user.save()


class UserUpdateForApparatSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id','first_name', 'last_name', 'father_name',
                  'photo', 'birth_date', "email", 'password', 'login')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # def to_internal_value(self, data):
    #     groups_data = data.get('groups', [])
    #     if groups_data:
    #         data['groups'] = [Group.objects.get(code = groups_data[0]).id]
    #     return super().to_internal_value(data)


    def update(self, instance, validated_data):
        # print('1100000',validated_data)
        # groups = validated_data.pop('groups')

        # user_role = Group.objects.get(code=groups[0].code)
        # role_id = user_role.id
        # user.groups.set([role_id])

        # user_role = Group.objects.get(code=groups[0].code)
        # role_id = user_role.id
        # instance.groups.set([role_id])

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        # instance.markaz = validated_data.get('markaz', instance.markaz)
        # instance.markaz_tuman = validated_data.get('markaz_tuman', instance.markaz_tuman)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.email = validated_data.get('email', instance.email)
        instance.login = validated_data.get('login', instance.login)
        instance.photo = validated_data.get('photo', instance.photo)
        # if validated_data.get('markaz_tuman'):
        #     instance.markaz = None
        instance.save()
        return instance


class MonitoringUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'father_name',
                  'markaz_tuman', 'groups', 'photo', 'birth_date', "email", 'password', 'login')

    def create(self, validated_data, photo):
        email = validated_data.pop('email')
        login = validated_data.pop('login')
        password = validated_data.pop('password')
        groups = validated_data.pop('groups')
        markaz_tuman_id = validated_data.pop('markaz_tuman')
        markaz_instance = MarkazTuman.objects.get(pk=markaz_tuman_id)

        user = CustomUser.objects.create_user(email=email, password=password, login=login, **validated_data)
        user.photo = photo
        user_role = Group.objects.get(code=groups[0])
        role_id = user_role.id
        user.groups.set([role_id])
        user.markaz_tuman = markaz_instance
        user.save()


class UserCreateForDirektorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'father_name', 'groups', 'photo', 'birth_date', "email", 'password', 'login')

    def create(self, validated_data, photo, markaz):
        email = validated_data.pop('email')
        login = validated_data.pop('login')
        password = validated_data.pop('password')
        groups = validated_data.pop('groups')

        user = CustomUser.objects.create_user(email=email, password=password, login=login, **validated_data)
        user.photo = photo
        user_role = Group.objects.get(code=groups[0])
        role_id = user_role.id
        user.groups.set([role_id])
        user.markaz = markaz
        user.save()


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('code', 'name', 'id')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'is_active']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserListSerializer(serializers.ModelSerializer):
    markaz = serializers.StringRelatedField()
    markaz_tuman = serializers.StringRelatedField()
    full_name = serializers.SerializerMethodField('get_user_full_name')
    position = serializers.SerializerMethodField('get_position')
    
    def get_user_full_name(self, obj):
        full_name = f"{obj.first_name} {obj.last_name} {obj.father_name}"
        return full_name

    def get_position(self, obj):
        groups = obj.groups.all()
        for item in groups:
            return item.name   

    class Meta:
        model = CustomUser
        fields = ('id','login','first_name','last_name','father_name','full_name', 'markaz','email', 'markaz_tuman', 'birth_date', 'photo', 'position','is_active')
