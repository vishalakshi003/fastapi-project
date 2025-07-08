from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from src.resolvers.query import Query
from src.resolvers.mutation import Mutation
from src.config.database import get_context
app=FastAPI()
schema = strawberry.Schema(query=Query,mutation=Mutation)
user_service=GraphQLRouter(schema,context_getter=get_context)
app.include_router(user_service,prefix='/graphql')