from duka.favorites.models import Favorite
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView)
from .serializers import (FavoriteCreateUpdateSerializer, FavoriteDetailSerializer,
                          FavoriteListSerializer)
from rest_framework import viewsets



class FavoriteCreateAPIView(CreateAPIView):
    serializer_class = FavoriteCreateUpdateSerializer
    queryset = Favorite.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(collector=self.request.user.collector)

class FavoriteDeleteAPIView(DestroyAPIView):
    serializer_class = FavoriteDetailSerializer
    queryset = Favorite.objects.all()
    lookup_field = 'slug'


class FavoriteDetailAPIView(RetrieveAPIView):
    serializer_class = FavoriteDetailSerializer
    queryset = Favorite.objects.all()
    # lookup_url_kwarg = 'name'
    lookup_field = 'slug'


class FavoriteUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = FavoriteCreateUpdateSerializer
    queryset = Favorite.objects.all()
    lookup_field = 'slug'


class FavoriteListAPIView(ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateUpdateSerializer
    permission_classes = []