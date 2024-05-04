from blog.models import Blog,BlogProduct
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1
        
class BlogProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogProduct
        fields = ["product",]
        depth = 2
