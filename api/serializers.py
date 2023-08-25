from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import Todo
from .models import UserProfile, Lead, Comment

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=200)
    message = serializers.CharField(max_length=1000)
    from_email = serializers.EmailField()
    recipient_list = serializers.CharField()  
    attachments = serializers.ListField(child=serializers.FileField(), required=False)

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'timestamp']


class LeadSerializer(serializers.ModelSerializer):
    number = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'description', 'priority', 'status', 'number', 'comments']

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id','title','memo','created','completed']

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id'] # why need to show id?
        read_only_fields = ['title','memo','created','completed']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    staff_status = serializers.CharField(source='userprofile.staff_status')

    class Meta:
        model = User
        fields = ['id', 'password', 'first_name', 'last_name', 'email', 'staff_status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
        )
        UserProfile.objects.create(user=user, staff_status=validated_data.get('staff_status', 'customer'))
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        # Actualizar el perfil de usuario
        user_profile = instance.userprofile
        staff_status = validated_data.get('staff_status', user_profile.staff_status)

        # Validar el valor de staff_status
        allowed_choices = [choice[0] for choice in UserProfile._meta.get_field('staff_status').choices]
        if staff_status not in allowed_choices:
            raise serializers.ValidationError('Invalid staff status.')

        user_profile.staff_status = staff_status
        user_profile.save()

        instance.save()
        return instance
