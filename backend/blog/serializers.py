from rest_framework import serializers

from .models import Article, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
    def to_representation(self, instance):
        return super().to_representation(instance)
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)
    
    def validate(self, attrs):
        return super().validate(attrs)


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
    def to_representation(self, instance):
        return super().to_representation(instance)
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)
    
    def validate(self, attrs):
        return super().validate(attrs)


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
        
    def to_representation(self, instance):
        return super().to_representation(instance)
        
    def to_internal_value(self, data):
        return super().to_internal_value(data)
        
    def validate(self, attrs):
        return super().validate(attrs)

