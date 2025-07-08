from fastapi import HTTPException
from graphql import GraphQLError

def custom_error_formatter(error: GraphQLError, debug: bool) -> dict:
    if hasattr(error.original_error, "status_code"):
        status_code = error.original_error.status_code
    else:
        status_code = 400

    return {
        "message": error.message,
        "status_code": status_code,
    }
