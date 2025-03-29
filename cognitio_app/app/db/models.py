from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

from app.db.base import Base

# Ассоциативные таблицы M:N
student_technology = Table(
    "student_technology",
    Base.metadata,
    Column("student_id", ForeignKey("student.student_id"), primary_key=True),
    Column("tech_id", ForeignKey("technology.tech_id"), primary_key=True),
)

student_hobby = Table(
    "student_hobby",
    Base.metadata,
    Column("student_id", ForeignKey("student.student_id"), primary_key=True),
    Column("hobby_id", ForeignKey("hobby.hobby_id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    age = Column(Integer)
    description = Column(String(500))
    city_id = Column(Integer, ForeignKey("city.city_id"))

    # Связи
    city = relationship("City", back_populates="students")
    technologies = relationship("Technology", secondary=student_technology, back_populates="students")
    hobbies = relationship("Hobby", secondary=student_hobby, back_populates="students")
    sent_likes = relationship("Like", foreign_keys="Like.sender_id", back_populates="sender")
    received_likes = relationship("Like", foreign_keys="Like.receiver_id", back_populates="receiver")
    matches1 = relationship("Match", foreign_keys="Match.student1_id", back_populates="student1")
    matches2 = relationship("Match", foreign_keys="Match.student2_id", back_populates="student2")
    photos = relationship("Photo", back_populates="student")
    settings = relationship("Settings", back_populates="student", uselist=False)


class Technology(Base):
    __tablename__ = "technology"
    tech_id = Column(Integer, primary_key=True)
    tech_name = Column(String(50), unique=True)
    students = relationship("Student", secondary=student_technology, back_populates="technologies")


class Hobby(Base):
    __tablename__ = "hobby"
    hobby_id = Column(Integer, primary_key=True)
    hobby_name = Column(String(50), unique=True)
    students = relationship("Student", secondary=student_hobby, back_populates="hobbies")


class City(Base):
    __tablename__ = "city"
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String(50), unique=True)
    students = relationship("Student", back_populates="city")


class Like(Base):
    __tablename__ = "like"
    like_id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("student.student_id"))
    receiver_id = Column(Integer, ForeignKey("student.student_id"))
    status = Column(Boolean)  # True = лайк, False = дизлайк
    timestamp = Column(DateTime, default=datetime.utcnow)
    sender = relationship("Student", foreign_keys=[sender_id], back_populates="sent_likes")
    receiver = relationship("Student", foreign_keys=[receiver_id], back_populates="received_likes")


class Match(Base):
    __tablename__ = "match"
    match_id = Column(Integer, primary_key=True)
    student1_id = Column(Integer, ForeignKey("student.student_id"))
    student2_id = Column(Integer, ForeignKey("student.student_id"))
    match_date = Column(DateTime, default=datetime.utcnow)
    student1 = relationship("Student", foreign_keys=[student1_id], back_populates="matches1")
    student2 = relationship("Student", foreign_keys=[student2_id], back_populates="matches2")
    chat = relationship("Chat", back_populates="match", uselist=False)


class Chat(Base):
    __tablename__ = "chat"
    chat_id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("match.match_id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    match = relationship("Match", back_populates="chat")
    messages = relationship("Message", back_populates="chat")


class Message(Base):
    __tablename__ = "message"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chat.chat_id"))
    sender_id = Column(Integer, ForeignKey("student.student_id"))
    content = Column(String(500))
    sent_at = Column(DateTime, default=datetime.utcnow)
    chat = relationship("Chat", back_populates="messages")
    sender = relationship("Student")


class Photo(Base):
    __tablename__ = "photo"
    photo_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.student_id"))
    url = Column(String(200), nullable=False)
    is_main = Column(Boolean, default=False)
    student = relationship("Student", back_populates="photos")


class Settings(Base):
    __tablename__ = "settings"
    settings_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.student_id"), unique=True)
    private_profile = Column(Boolean, default=False)
    notify_likes = Column(Boolean, default=True)
    notify_messages = Column(Boolean, default=True)
    student = relationship("Student", back_populates="settings")