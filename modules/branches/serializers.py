from rest_framework import serializers


class BranchesSerializers(serializers.Serializer):
    """
        Serializer for Branches to format and clean sensible data
    """
    
    
    name = serializers.CharField()
    sha_commit = serializers.SerializerMethodField()
    protected = serializers.BooleanField()
    
    
    def get_sha_commit(self, obj):
        try:
            return obj.get('commit', None).get('sha', None)
        except:
            return ''
