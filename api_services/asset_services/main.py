from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api_services.asset_services.src.schemas.schema import  schema
from api_services.asset_services.src.config.database import get_context 

# from src.config.database import get_context
app=FastAPI()
user_service=GraphQLRouter(schema,context_getter=get_context)
app.include_router(user_service,prefix='/graphql')