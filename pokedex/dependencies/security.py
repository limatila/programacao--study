from os import getenv
SECRET_KEY = getenv("SECRET_KEY_POKEDEX") #Defined in environment, requires IDE / terminal restart

from fastapi import Security #Depends for security dependencys
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException

bearer = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(bearer)):
    """
    Validates the provided Bearer Token
    
    requires a valid Bearer token to be sent, on any method that has verify_token as a Dependency
    """
    if not credentials:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials of Bearer token")

    if str(credentials.credentials) != str(SECRET_KEY):
        raise HTTPException(status_code=403, detail="Invalid authentication credentials of Bearer token")
    
    return credentials.credentials  # Return token if valid