from rest_framework import serializers
from .models import HandbookElement


class HandbookElementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandbookElement
        fields = '__all__'


class HandbookElementListSerializerValidate(serializers.ModelSerializer):
    '''
    Валидация
    '''
    class Meta:
        model = HandbookElement
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('code') > 3:
            raise serializers.ValidationError('Длина кода должна состовлять более 3 символов')
        else:
            return attrs
