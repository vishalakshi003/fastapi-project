from fastapi import HTTPException,status

class HttpError:
    @staticmethod
    def already_exists(details="Data already exists"):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=details)
    
    def not_found(details="Data not found"):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=details)
    def unauthorized(details="You are not authenticated to perform this action !"):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=details)
    def invalid_mobile_number(details="Invalid mobile number"):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=details)
    def verify_password(details="Invalid password"):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=details)
    def exception_handling(details="Something went wrong"):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=details)