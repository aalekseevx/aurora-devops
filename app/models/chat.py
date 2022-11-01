from app.models.db import BaseModel, TimedBaseModel, db


class Chat(TimedBaseModel):
    __tablename__ = "chats"

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    language = db.Column(db.String(12), default="en")
    desired_kp = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    mute = db.Column(db.DateTime(False), server_default=db.func.now())
    subscribe = db.Column(db.DateTime(False), server_default=db.func.now())
    geonames_data = db.Column(db.Text)
    weather_info = db.Column(db.Text)
    user_info = db.Column(db.Text)


class ChatRelatedModel(BaseModel):
    __abstract__ = True

    chat_id = db.Column(
        db.ForeignKey(
            f"{Chat.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
    )
