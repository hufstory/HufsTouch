from .models import Post
from rest_framework import serializers, viewsets

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        """ allow rest api to filter by submissions """
        queryset = Post.objects.all()
        major = self.request.query_params.get('major', None)
        if major is not None:
            queryset = queryset.filter(major=major)
        
        return queryset
        