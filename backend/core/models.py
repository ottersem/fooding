# 기존 MySQL 테이블 구조를 SQLAlchemy ORM으로 정의한 모듈

from sqlalchemy import (
  Column,
  Integer,
  String,
  Boolean,
  Date,
  DateTime,
  ForeignKey,
)
from sqlalchemy.orm import relationship
from core.database import Base


class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(10), unique=True, nullable=False)
  email = Column(String(30), unique=True, nullable=False)
  password = Column(String(30), nullable=False)
  is_active = Column(Boolean, nullable=False, default=True)

  profile = relationship("UserProfile", back_populates="user", uselist=False)
  interests = relationship("UserInterest", back_populates="user")
  time_slots = relationship("UserTimeSlot", back_populates="user")
  group_members = relationship("GroupMember", back_populates="user")
  groups_created = relationship("Group", back_populates="creator")
  reviews_written = relationship(
    "Review",
    back_populates="reviewer",
    foreign_keys="Review.reviewer_id",
  )
  reviews_received = relationship(
    "Review",
    back_populates="reviewed",
    foreign_keys="Review.review_ed_id",
  )


class Interest(Base):
  __tablename__ = "interests"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(20), nullable=False)
  code = Column(String(20), unique=True, nullable=False)

  user_interests = relationship("UserInterest", back_populates="interest")
  groups = relationship("Group", back_populates="interest")


class TimeSlot(Base):
  __tablename__ = "time_slots"

  id = Column(Integer, primary_key=True, index=True)
  label = Column(String(50), nullable=False)
  code = Column(String(50), unique=True, nullable=False)

  user_time_slots = relationship("UserTimeSlot", back_populates="time_slot")
  groups = relationship("Group", back_populates="time_slot")


class UserProfile(Base):
  __tablename__ = "user_profiles"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  major = Column(String(30))
  grade = Column(String(10))
  intro_text = Column(String(100)) 
  #프로필 사진은 이름으로 처리... -> 프론트에서 프로필 조회시  profile_image_url == null 이면 그때 렌더링
  profile_image_url = Column(String(255))  # 프로필 이미지 URL 문자열로 저장함

  user = relationship("User", back_populates="profile")


class UserInterest(Base):
  __tablename__ = "user_interests"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  interest_id = Column(Integer, ForeignKey("interests.id"), nullable=False)

  user = relationship("User", back_populates="interests")
  interest = relationship("Interest", back_populates="user_interests")


class UserTimeSlot(Base):
  __tablename__ = "user_time_slots"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  time_slot_id = Column(Integer, ForeignKey("time_slots.id"), nullable=False)

  user = relationship("User", back_populates="time_slots")
  time_slot = relationship("TimeSlot", back_populates="user_time_slots")


class Group(Base):
  __tablename__ = "groups"

  id = Column(Integer, primary_key=True, index=True)
  creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  interest_id = Column(Integer, ForeignKey("interests.id"), nullable=False)
  title = Column(String(30), nullable=False)
  description = Column(String(200), nullable=False)
  meeting_date = Column(Date, nullable=False)
  time_slot_id = Column(Integer, ForeignKey("time_slots.id"), nullable=False)
  place = Column(String(50), nullable=False)
  max_participants = Column(Integer, nullable=False)
  status = Column(String(10), nullable=False)  # RECRUITING / ONGOING / FINISHED
  open_chat_link = Column(String(255))  # 카카오톡 오픈채팅 링크 등

  creator = relationship("User", back_populates="groups_created")
  interest = relationship("Interest", back_populates="groups")
  time_slot = relationship("TimeSlot", back_populates="groups")
  members = relationship("GroupMember", back_populates="group")
  reviews = relationship("Review", back_populates="group")
  category = Column(String(30), nullable = False, default = '기타') #1/18 추가

class GroupMember(Base):
  __tablename__ = "group_members"

  id = Column(Integer, primary_key=True, index=True)
  group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  role = Column(String(20), nullable=False)   # HOST / MEMBER
  status = Column(String(20), nullable=False) # APPLIED / ACCEPTED / REJECTED / CANCELED

  group = relationship("Group", back_populates="members")
  user = relationship("User", back_populates="group_members")


class Review(Base):
  __tablename__ = "reviews"

  id = Column(Integer, primary_key=True, index=True)
  group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
  reviewer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  review_ed_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  score = Column(Integer, nullable=False)
  comment = Column(String(100), nullable=False)

  group = relationship("Group", back_populates="reviews")
  reviewer = relationship("User", foreign_keys=[reviewer_id], back_populates="reviews_written")
  reviewed = relationship("User", foreign_keys=[review_ed_id], back_populates="reviews_received")
