import os
from flask import current_app
from werkzeug.utils import secure_filename

@main.route('/event/create', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        image = form.image.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        new_event = Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            category=form.category.data,
            image=filename,
            user_id=current_user.id
        )
        db.session.add(new_event)
        db.session.commit()
        flash("Event created successfully!", "success")
        return redirect(url_for('main.home'))  # or a page showing all events

    return render_template('create-event.html', form=form)
