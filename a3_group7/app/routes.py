from flask import render_template 
from yourapp.models import Event 

@app.route('/events/<int:event_id>')
def event_detail(event_id):
  event = Event.query.get_or_404(event_id)
  return render_template('event_details.html',event=event)
