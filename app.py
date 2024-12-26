from flask import Flask, request, jsonify, abort
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

load_dotenv()
DATABASE_URL = os.getenv('POSTGRES_URL')

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL set for Flask application")

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/adduser/<username>/<email>", methods=["POST"])
def add_user(usernamee, emaill):
    db = SessionLocal()
    try:
        db_unit = UserDB(username=usernamee, email=emaill)
        db.add(db_unit)
        db.commit()
        db.refresh(db_unit)
        return jsonify({"id": db_unit.id, "username": db_unit.username, "email": db_unit.email}), 201
    finally:
        db.close()


@app.route('/users', methods=['GET'])
def get_users():
    db = SessionLocal()
    try:
        users = db.query(UserDB).all()
        return jsonify([
            {"id": user.id, "username": user.username, "email": user.email}
            for user in users
        ])
    finally:
        db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=3000 ,debug=True)
