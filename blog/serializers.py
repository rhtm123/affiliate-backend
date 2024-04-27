from blog.models import Blog,BlogProduct
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = '__all__'
        
class BlogProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogProduct
        fields = '__all__'
