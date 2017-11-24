from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



from book_management.models import Pet




class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pet
        fields=['first_name','last_name','date_of_birth']


















