from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from flask_wtf.file import FileField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from flask_security import current_user


class FCreatePost(FlaskForm):
    title_field = StringField(label='عنوان مطلب', validators=[validators.DataRequired()])
    picture_field = FileField(label='عکس مطلب - عکس باید دارای ابعاد 16:10 باشد', validators=[validators.Optional()])
    categories = SelectField(label='دسته بندی ها', choices=[('tutorial', 'آموزش ها'),
                                                            ('news', 'بخش خبری')],
                             validators=[validators.DataRequired()])
    short_body_text = StringField(label='متن کوتاه نمایشی', validators=[validators.DataRequired()])
    full_body_text = TextAreaField(label='متن کامل مطلب', validators=[validators.DataRequired()])
    submit_field = SubmitField(label='ثبت مطلب')


class FEditProfile(FlaskForm):
    username = StringField(label='نام کاربری', validators=[validators.DataRequired()])
    e_mail = EmailField(label='ایمیل', validators=[validators.DataRequired()])
