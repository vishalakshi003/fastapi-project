from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from src.resolvers.query import Query
from src.resolvers.mutations import Mutation
from src.config.database import get_context
app=FastAPI()
schema = strawberry.Schema(query=Query,mutation=Mutation)
user_service=GraphQLRouter(schema,context_getter=get_context)
app.include_router(user_service,prefix='/graphql')
