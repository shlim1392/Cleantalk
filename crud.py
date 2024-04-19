from sqlalchemy.orm import Session
import models, schemas, database
from sqlalchemy.future import select
from sqlalchemy import Column, Integer, String, text
from sqlalchemy import func
import json

def get_회원(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.회원).offset(skip).limit(limit).all()

def get_member_info_by_code(db: Session, 회원코드: str):
    return db.query(models.Member).filter(models.Member.회원코드 == 회원코드).first()

def get_특별회원관리(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(
        models.회원.회원코드,
        models.회원.아이디,
        models.회원.회원명,
        models.회원.휴대폰번호,
        models.특별회원분류.특별관리단계,
        models.상담내용.회원상담내용,
        models.상담내용.욕설내용
    ).join(
        models.상담내용, models.회원.회원코드 == models.상담내용.회원코드
    ).join(
        models.특별회원분류, models.회원.분류코드 == models.특별회원분류.분류코드
    ).offset(skip).limit(limit).all()

    return result

def get_random(db: Session):
    result = db.query(models.회원.회원코드,models.회원.회원명,models.회원.아이디,models.회원.휴대폰번호, models.특별회원분류.특별관리단계)\
        .join(models.특별회원분류, models.회원.분류코드 == models.특별회원분류.분류코드)\
        .order_by(func.random())\
        .first()
    return result

def create_상담내용(db: Session, 회원코드: str, 회원상담내용: str, 욕설내용: str, 횟수: int):
    db_상담내용 = models.상담내용(회원코드=회원코드, 회원상담내용=회원상담내용, 욕설내용=욕설내용, 횟수=횟수)
    db.add(db_상담내용)
    db.commit()
    db.refresh(db_상담내용)
    return db_상담내용

def load_sensitive_words():
    with open('static/dict/swear_list.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def find_sensitive_words(texts, sensitive_words):
    found_words = {}
    total_count = 0
    for text in texts:
        for word in sensitive_words["욕설"]:  
            if word in text:
                count = text.count(word)
                if word not in found_words:
                    found_words[word] = count
                else:
                    found_words[word] += count
                total_count += count
    return found_words, total_count


