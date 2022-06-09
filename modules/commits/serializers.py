from rest_framework import serializers


class CommitsSerializers(serializers.Serializer):
    """
        Serializer for Commits to format and clean sensible data
    """
    
    
    sha = serializers.CharField()
    commit = serializers.JSONField()
    url = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    
    
    def get_url(self, obj):
        return obj.get('html_url', '')
    
    
    def get_author(self, obj):
        try:
            return obj.get('author', None).get('login', None)
        except:
            return ''