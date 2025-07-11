import strawberry
from src.resolvers.query import Query
from src.resolvers.mutation import Mutation

schema = strawberry.Schema(query=Query,mutation=Mutation)