from duka.favorites.models import Drink, Favorite
from rest_framework import serializers


favorite_update = serializers.HyperlinkedIdentityField(
        view_name='api:favorite_update',
        lookup_field='slug'
    )
favorite_delete = serializers.HyperlinkedIdentityField(
        view_name='api:favorite_delete',
        lookup_field='slug'
    )
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
    delete_url = favorite_delete
    edit_url = favorite_update
    class Meta:
        model = Favorite
        fields = ('id', 'data_collector', 'name', 'collector', 'age_bracket',
                  'location', 'drink', 'slug', 'created', 'updated', 'edit_url',
                  'delete_url')



class FavoriteListSerializer(serializers.HyperlinkedModelSerializer):
    data_collector = serializers.ReadOnlyField(source='collector.user.name')
    favorite_drink = serializers.ReadOnlyField(source='drink.name')
    class Meta:
        model = Favorite
        fields = ('name', 'favorite_drink', 'data_collector',  'url',)
        extra_kwargs = {
            'url': {'view_name': 'api:favorite_detail', 'lookup_field': 'slug'},
        }

