import datetime
from flask_security_project.core.extensions import db


class Post(db.Model):
    _id = db.Column(db.INTEGER(), primary_key=True, autoincrement=True)
    title = db.Column(db.TEXT(80))
    img_name = db.Column(db.TEXT, default="default_pic.jpg")
    author = db.Column(db.TEXT(80), default="No One")
    datetime_modified = db.Column(db.DATETIME, default=datetime.datetime.now())
    category = db.Column(db.TEXT, default="")
    has_update = db.Column(db.BOOLEAN, default=False)
    short_body_text = db.Column(db.TEXT, nullable=False)
    short_body_text_update = db.Column(db.TEXT, default="")
    full_body_text = db.Column(db.TEXT, nullable=False)
    full_body_text_update = db.Column(db.TEXT, default="")
    verified = db.Column(db.BOOLEAN, default=False)

    @property
    def get_id(self) -> int:
        return self._id

    @property
    def date_modified(self):
        return f"{self.datetime_modified.year}/{self.datetime_modified.month}/{self.datetime_modified.day}"

    @property
    def subtitle(self):
        if self.category.startswith(";"):
            self.category = self.category[1:]
            db.session.commit()
        if self.category.endswith(";"):
            self.category = self.category[0:-1]
            db.session.commit()
        return f"{self.author} - {self.date_modified} - Category: {' , '.join(self.category.split(';'))}"

