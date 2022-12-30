from rest_framework import serializers
# from .models import Women
from rest_framework.renderers import JSONRenderer

from women.models import Women


    
class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta: 
        model = Women # указываем модель 
        fields = ('__all__')  #  поля для заполнения 
        
        
        
    
    # def create(self, validated_data): # метод добавления данных в бд
    #     return Women.objects.create(**validated_data)
    
    # def update(self, instance, validated_data): # Изменение существуюих записей 
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance
        
        
