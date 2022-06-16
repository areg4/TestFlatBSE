from unicodedata import name
from rest_framework import serializers


class AuthorsSerializers(serializers.Serializer):
    """
        Serilaizer for Authors to format and clean sensible data
        
    """
    
    user_id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    api_url = serializers.SerializerMethodField()
    user_url = serializers.SerializerMethodField()
    repos_url = serializers.CharField()
    user_type = serializers.SerializerMethodField()
    site_admin = serializers.CharField()
    permissions = serializers.JSONField()
    role_name = serializers.CharField()
    
    
    def get_user_id(self, obj):
        return obj.get('id', '')
    
    
    def get_username(self, obj):
        return obj.get("login", '')
    
    
    def get_api_url(self, obj):
        return obj.get('url', '')
    
    
    def get_user_url(self, obj):
        return obj.get('html_url', '')
    
    
    def get_user_type(self, obj):
        return obj.get('type', '')
    