import os
from typing import List, Annotated
from httpx import request
from fastapi import FastAPI, Request, File, UploadFile, Depends, Request, Query, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import requests
from fastapi import HTTPException
from sqlalchemy import Integer
from sqlalchemy.orm import Session
from kcelectra import load_swear_words, mask_swear_words, predict, replace_sensitive_words
import crud, models, schemas, database
import httpx
import torch
from starlette.responses import JSONResponse
from transformers import AutoTokenizer, AutoModelForTokenClassification
import pymysql
from pydantic import BaseModel
import sys
import requests
# from sqlalchemy.future import select, func
from clova import ClovaSpeechClient
from sqlalchemy.ext.asyncio import AsyncSession
from models import 회원
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
############ 모델 ############

from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/index.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login.html", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/forgot-password.html", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("forgot-password.html", {"request": request})

@app.get("/charts.html", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("charts.html", {"request": request})

@app.get("/aiCall.html", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("aiCall.html", {"request": request})

############# stt ############

@app.get("/process/")
async def process_audio(db: Session = Depends(get_db)):
    res = ClovaSpeechClient().req_upload(file='static/audio/sample5.mp3', completion='sync')
    res_json = res.json()
    segments = res_json.get('segments', [])
    texts = [segment.get('text', '') for segment in segments]

    member = crud.get_random(db)
    회원코드 = member.회원코드
    아이디 =  member.아이디,
    회원명 = member.회원명,
    휴대폰번호 = member.휴대폰번호,
    특별관리단계 = member.특별관리단계

    sensitive_words = crud.load_sensitive_words()
    found_words, count = crud.find_sensitive_words(texts, sensitive_words)
    욕설내용 = ', '.join(found_words)

    회원상담내용 = ' '.join(texts)
    crud.create_상담내용(db=db, 회원코드=회원코드, 회원상담내용=회원상담내용, 욕설내용=욕설내용, 횟수=count)

    if texts:
        predictions = predict(texts)
        replaced_texts = replace_sensitive_words(texts, predictions)

    return {"message": replaced_texts,
            "회원코드": 회원코드,
            "아이디":아이디,
            '회원명':회원명,
            '휴대폰번호': 휴대폰번호,
            '특별관리단계':특별관리단계,
            "욕설내용": 욕설내용,
            "횟수": count}


@app.get("/dashboard_entry.html", response_class=HTMLResponse)
def read_회원(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    회원들 = crud.get_회원(db, skip=skip, limit=limit)
    return templates.TemplateResponse("dashboard_entry.html", {"request": request, "회원들": 회원들})

@app.get("/tables.html")
def read_members(request: Request, db: Session = Depends(get_db)):
    members = crud.get_특별회원관리(db)
    return templates.TemplateResponse("tables.html", {"request": request, "members": members})



