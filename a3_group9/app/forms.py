from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_FILE = {'png', 'jpg', 'jpeg', 'gif'}

class EventForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    date = StringField('Event Date', validators=[InputRequired()])
    category = StringField('Category', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(), FileAllowed(ALLOWED_FILE, 'Only image files allowed!')
    ])
    submit = SubmitField('Create Event')
