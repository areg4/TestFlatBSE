from pyexpat import model
from rest_framework import serializers
from .models import PullRequest


class PullRequestsSerializers(serializers.Serializer):
    """
        Serializer for Pull Requests to format and clean sensible data
    """
    
    
    url = serializers.CharField()
    id = serializers.CharField()
    html_url = serializers.CharField()
    number = serializers.IntegerField()
    status = serializers.SerializerMethodField()
    locked = serializers.BooleanField()
    title = serializers.CharField()
    body = serializers.CharField()
    user = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    closed_at = serializers.DateTimeField()
    merged_at = serializers.DateTimeField()
    merge_commit_sha = serializers.CharField()
    head = serializers.SerializerMethodField()
    base = serializers.SerializerMethodField()
    
    
    def get_status(self, obj):
        return obj.get('state', '')
    
    
    def get_user(self, obj):
        try:
            return obj.get('user', None).get('login', None)
        except:
            return ''
        
        
    def get_head(self, obj):
        try:
            return obj.get('head', None).get('label', None)
        except:
            return ''
        
    
    def get_base(self, obj):
        try:
            return obj.get('base', None).get('label', None)
        except:
            return ''
        
        
class PostPullRequestSerializers(serializers.ModelSerializer):
    """
        Serializer for POST Pull Requests
    """
    
    class Meta:
        model = PullRequest
        exclude = ['created_at', 'updated_at']
        read_only_fields = ['number', 'created_at', 'updated_at']


class SavePullRequestSerializers(serializers.ModelSerializer):
    """
        Serializer for Save Pull Requests
    """
    
    description = serializers.SerializerMethodField()
    
    
    def get_description(self, obj):
        return obj.get('body', '')
    
    
    class Meta:
        model = PullRequest
        exclude = ['id', 'created_at', 'updated_at']