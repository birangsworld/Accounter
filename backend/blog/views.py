from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer

from logging import getLogger


logger = getLogger(__name__)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, *args, **kwargs):
        logger.info(f"### Categories List - GET - /categories/ ### - {request}")
        return super().get(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        logger.info(f"### Categories Create - POST - /categories/ ### - {request}")
        return super().post(request, *args, **kwargs)


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        logger.info(f"### Categories Retrieve - GET - /categories/{self.lookup_field}/ ### - {request}")
        return super().get(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        logger.info(f"### Categories Update - PUT - /categories/{self.lookup_field}/ ### - {request}")
        return super().put(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
        logger.info(f"### Categories Partial Update - PATCH - /categories/{self.lookup_field}/ ### - {request}")
        return super().patch(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        logger.info(f"### Categories Delete - DELETE - /categories/{self.lookup_field}/ ### - {request}")
        return super().delete(request, *args, **kwargs)


class ArticleListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get(self, request, *args, **kwargs):
        logger.info(f"### Articles List - GET - /articles/ ### - {request}")
        return super().get(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        logger.info(f"### Articles Create - POST - /articles/ ### - {request}")
        return super().post(request, *args, **kwargs)


class ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        logger.info(f"### Articles Retrieve - GET - /blog/{self.lookup_field}/ ### - {request}")
        return super().get(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        logger.info(f"### Articles Update - PUT - /blog/{self.lookup_field}/ ### - {request}")
        return super().put(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
        logger.info(f"### Articles Partial Update - PATCH - /blog/{self.lookup_field}/ ### - {request}")
        return super().patch(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        logger.info(f"### Articles Delete - DELETE - /blog/{self.lookup_field}/ ### - {request}")
        return super().delete(request, *args, **kwargs)
