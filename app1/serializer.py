from rest_framework.fields import empty
from .models import *

from rest_framework import serializers



class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    
    poll = PollSerializer()
    
    class Meta:
        model = Author
        fields = ['name','age','poll']
