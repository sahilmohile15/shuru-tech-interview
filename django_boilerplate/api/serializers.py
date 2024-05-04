from rest_framework import serializers
from .models import *

class MatchesSerializer(serializers.Serializer):    
    class Meta:
        model = Matches
        field = ('__all__')
        
class TeamsSerializer(serializers.Serializer):
    class Meta:
        model = Teams
        field = ('__all__')
        
class TeamWithPlayersSerializer(serializers.Serializer):
    team = serializers.StringRelatedField()
    
    class Meta:
        model = Players
        field = ('__all__')
        
class PlayersSerializer(serializers.Serializer):
    class Meta:
        model = Players
        field = ('__all__')