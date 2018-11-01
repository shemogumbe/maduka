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
    
    class Arguments:

        name = graphene.String(required=True)
        description= graphene.String(required=True)

    category = graphene.Field(Category)

    def mutate(self, info, **kwargs):
        category = CategoryModel(**kwargs)
        category.save()
        return CreateCategory(category=category)

class UpdateCategory(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        description= graphene.String()
        category_id = graphene.String()
    category = graphene.Field(Category)

    def mutate(self, info, category_id, **kwargs):
        category = Category.get_query(info)
        category_obj = category.filter(
            CategoryModel.id == category_id
        ).first()        
        category = CategoryModel(**kwargs)
        category.save()
        return CreateCategory(category=category)

class DeleteCategory(graphene.Mutation):

    class Arguments:
        category_id = graphene.Int(required=True)
    category = graphene.Field(Category)

    def mutate(self, info, category_id):
        category = Category.get_query(info)
        category_obj = category.filter(
            CategoryModel.id == category_id
        ).first()  
        if not category_obj:
            raise GraphQLError("Category Not Found!")
        category_obj.delete()      
        return DeleCategory(category=category)



class CreateProduct(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        description= graphene.String()
        image = graphene.String()
        price = graphene.Int()
        category_id = graphene.Int()
    product = graphene.Field(Product)

    def mutate(self, info, **kwargs):
        product = ProductModel(**kwargs)
        product.save()
        return CreateProduct(product=product)

class UpdateProduct(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        description= graphene.String()
        display_image = graphene.String()
        price = graphene.Int()
    product = graphene.Field(Product)

    def mutate(self, info, product_id, **kwargs):
        product = Product.get_query(info)
        product_obj = product.filter(
            ProductModel.id == product_id
        ).first()        
        product = ProductModel(**kwargs)
        product.save()
        return UpdateProduct(product=product)

class DeleteProduct(graphene.Mutation):

    class Arguments:
        product_id = graphene.Int(required=True)
    product = graphene.Field(Category)

    def mutate(self, info, category_id):
        product = Product.get_query(info)
        product_obj = category.filter(
            ProductModel.id == category_id
        ).first()  
        if not product_obj:
            raise GraphQLError("Category Not Found!")
        product_obj.delete()      
        return DeleCategory(category=category)



class Query(graphene.ObjectType):
    categories = graphene.List(Category)
    products = graphene.List(Product)
    get_product_by_name = graphene.List(Product,
        name=graphene.String())

    def resolve_categories(self, info):
        results = Category.get_query(info)
        return results.all()
    def resolve_products(self, info):
        results = Product.get_query(info)
        return results.all()

    def resolve_get_product_by_name(self, info, name):
        query = Product.get_query(info)
        if name == "":
            raise GraphQLError("Please supply a Product Name")
        product = list(query.filter(ProductModel.name.ilike("%" + name + "%")).all())
        if not product:
            raise GraphQLError("Product not found")
        return product


    
class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_product = CreateProduct.Field()
    update_product = CreateProduct.Field()
    delete_product = DeleteProduct.Field()