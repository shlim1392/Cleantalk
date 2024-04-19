# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class 상담내용(Base):
    __tablename__ = '상담내용'
    로그코드 = Column(Integer, primary_key=True)
    회원코드 = Column(Integer, nullable=False)
    회원상담내용 = Column(String(5000))
    욕설내용 = Column(String(10000), server_default=text("'없음'"))
    횟수 = Column(Integer, server_default=text("'0'"))



class 특별회원분류(Base):
    __tablename__ = '특별회원분류'

    분류코드 = Column(Integer, primary_key=True)
    특별관리단계 = Column(String(30))
    기준횟수 = Column(String(45), nullable=False)


class 회원(Base):
    __tablename__ = '회원'

    회원코드 = Column(Integer, primary_key=True)
    아이디 = Column(String(30))
    회원명 = Column(String(45), nullable=False)
    휴대폰번호 = Column(String(45))
    분류코드 = Column(ForeignKey('특별회원분류.분류코드'), index=True)

    특별회원분류 = relationship('특별회원분류')
