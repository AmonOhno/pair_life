from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import models
from routers import auth, calendar, finances, locations, relationship

# データベースのテーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pair Life API")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では適切に制限すること
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの登録
app.include_router(auth.router, tags=["認証"], prefix="/auth")
app.include_router(calendar.router, tags=["カレンダー"], prefix="/calendar")
app.include_router(finances.router, tags=["家計簿"], prefix="/finances")
app.include_router(locations.router, tags=["場所"], prefix="/locations")
app.include_router(relationship.router, tags=["関係"], prefix="/relationship")

@app.get("/")
def read_root():
    return {"message": "Pair Life APIへようこそ！"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
