from rest_framework import serializers


class PullRequestsSerializers(serializers.Serializer):
    """
        Serializer for Pull Requests to format and clean sensible data
    """
    
    
    url = serializers.CharField()
    id = serializers.CharField()
    html_url = serializers.CharField()
    number = serializers.IntegerField()
    state = serializers.CharField()
    locked = serializers.BooleanField()
    title = serializers.CharField()
    user = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    closed_at = serializers.DateTimeField()
    merged_at = serializers.DateTimeField()
    merge_commit_sha = serializers.CharField()
    head = serializers.SerializerMethodField()
    base = serializers.SerializerMethodField()
    
    
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
        