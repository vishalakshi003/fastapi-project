from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import strawberry
from strawberry.fastapi import GraphQLRouter
from src.resolvers.query import Query
from src.resolvers.mutations import Mutation
from src.config.database import get_context
from src.middleware.error_handling import ForceGraphQLHTTPStatusMiddleware


app=FastAPI()
app.add_middleware(ForceGraphQLHTTPStatusMiddleware)

schema = strawberry.Schema(query=Query,mutation=Mutation)

user_service=GraphQLRouter(schema,context_getter=get_context)
app.include_router(user_service,prefix='/graphql')
