from duka.favorites.models import Drink, Favorite
from rest_framework import serializers


class FavoriteCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'name', 'age_bracket',
                  'location', 'drink',)

    def create(self, validated_data):
        device = Favorite.objects.create(**validated_data)
        return device

class FavoriteDetailSerializer(serializers.ModelSerializer):
    data_collector = serializers.ReadOnlyField(source='collector.user.name')
    class Meta:
        model = Favorite
        fields = ('id', 'data_collector', 'name', 'collector', 'age_bracket',
                  'location', 'drink', 'slug', 'created', 'updated')



class FavoriteListSerializer(serializers.ModelSerializer):
    data_collector = serializers.ReadOnlyField(source='collector.user.name')
    class Meta:
        model = Favorite
        fields = ('id', 'data_collector', 'name', 'slug')


