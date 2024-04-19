from pydantic import BaseModel
from typing import Optional, List
import crud, models, database
from sqlalchemy import Column, Integer, String, text

# 특별회원분류 스키마
class 특별회원분류Base(BaseModel):
    특별관리단계: str
    기준횟수: str
    분류코드: int
    class Config:
        from_attributes = True


class 특별회원분류Create(특별회원분류Base):
    pass

# 회원 스키마
class 회원Base(BaseModel):
    아이디: str = None
    회원명: str
    휴대폰번호: int = None
    회원코드: int
    분류코드: Optional[int] = None
    class Config:
        from_attributes = True

class 회원Create(회원Base):
    pass

# 대화 스키마
class 상담내용Base(BaseModel):
    로그코드 : int
    회원상담내용: Optional[str] = None
    욕설내용: Optional[str] = '없음'
    횟수: Optional[int] = 0
    회원코드: int
    class Config:
        from_attributes = True

class 상담내용Create(상담내용Base):
    pass







