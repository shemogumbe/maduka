import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import (
    Category as CategoryModel,
    Product as ProductModel) 

from graphql import GraphQLError

class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel

class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel

class CreateCategory(graphene.Mutation):
    """ Mutation to create product categories"""
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False)
    category = graphene.Field(Category)

    def mutate(self, info, **kwargs):
        category = CategoryModel(**kwargs)
        category.save()
        return CreateCategory(category=category)

class Query(graphene.ObjectType):
    cateries = graphene.List(Category)
    products = graphene.List(Product)

    def resolve_categories(self, info):
        results = Category.get_query(info)
        return results.all()
    
    def resolve_products(self, info):
        results = Product.get_query(info)
        return results.all()
