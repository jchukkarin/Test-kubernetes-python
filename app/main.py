from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
import os

app = FastAPI()

# 🔐 secret key (กันพลาด)
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set")

ALGORITHM = "HS256"

# 👤 user mock
fake_user_db = {
    "admin": {
        "username": "admin",
        "password": "1234"
    }
}

# 📦 request schema
class LoginRequest(BaseModel):
    username: str
    password: str

security = HTTPBearer()

# 🔑 create token
def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# 🔍 verify token
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# 🔐 login
@app.post("/login")
def login(data: LoginRequest):
    user = fake_user_db.get(data.username)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_token(data.username)
    return {"access_token": token}

# 🔒 protected
@app.get("/protected")
def protected(user: str = Depends(verify_token)):
    return {"message": f"Hello {user}, you are authenticated 🚀"}

# 🏠 root
@app.get("/")
def root():
    return {"message": "Login API is running"}