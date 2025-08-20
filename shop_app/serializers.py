from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Tag, Product, ProductOption
from django.db import transaction


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name')
        extra_kwargs = {"name": {"validators": []}}


class productOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ('pk', 'name', 'price')


class productSerializer(WritableNestedModelSerializer):
    tag_set = TagSerializer(many=True, required=False)
    option_set = productOptionSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('pk', 'name', 'option_set', 'tag_set')

    def _resolve_tag(self, t):
        if 'pk' in t and t['pk'] is not None:
            return Tag.objects.get(id=t['pk'])
        return Tag.objects.get_or_create(name=t['name'])[0]

    def create(self, validated_data):
        tags_data = validated_data.pop('tag_set', [])
        product = super().create(validated_data)
        for t in tags_data:
            product.tag_set.add(self._resolve_tag(t))
        return product

    @transaction.atomic
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tag_set', None)
        product = super().update(instance, validated_data)

        if tags_data is not None:
            current = set(product.tag_set.values_list('pk', flat=True))
            new = set(self._resolve_tag(t).pk for t in tags_data)

            # 제거는 안 하고 추가만
            for pk in (new - current):
                product.tag_set.add(pk)

        return product
