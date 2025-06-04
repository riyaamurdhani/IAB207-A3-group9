class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100))  # Filename of the uploaded image
    status = db.Column(db.String(20), default="Open")  # Open, Sold Out, Cancelled, Inactive
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='events')