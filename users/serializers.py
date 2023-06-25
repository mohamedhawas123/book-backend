from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Author

class TokenSerlizer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()





class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name' ,'username', 'password', 'tokens']
        extra_kwargs ={'password' :{'write_only': True}}


    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user



class CustomeUserSerializer(UserSerilizers):
    tokens = TokenSerlizer(read_only=True)
    author_id = serializers.SerializerMethodField()

    class Meta(UserSerilizers.Meta):

        fields = ['id', 'first_name', 'last_name', 'username', 'tokens', 'author_id']

    
    def get_author_id(self, obj):
        try:
            author = Author.objects.get(user=obj)
            return author.id 
        except Author.DoesNotExist:
            return None

