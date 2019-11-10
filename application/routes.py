from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import User, Note, db, ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        include_fk = True


class NoteSchema(ma.ModelSchema):
    class Meta:
        model = Note


user_schema = UserSchema()
users_schema = UserSchema(many=True)
note_schema = NoteSchema()


@app.route('/users', methods=['GET', 'POST'])
def handle_user():
    # TODO: Create All the CRUD operations
    if request.method == 'GET':
        id = request.args.get('id')
        if id is None:
            users = User.query.all()
            result = users_schema.dump(users)
            return {"users": result}
        else:
            user = User.query.filter(User.id == id).first()
            return user_schema.dump(user)
    if request.method == 'POST':
        name = request.args.get('user')
        email = request.args.get('email')
        return create_user(name, email)


def create_user(name, email):
    if name and email:

        existing_user = User.query.filter(
            User.name == name or User.email == email).first()
        if existing_user:
            return make_response(f'{name} ({email}) already created!')
        new_user = User(name=name,
                        email=email,
                        created=dt.now(),
                        phone="+12312312313")  # Create an instance of the User class
        # TODO: Create Note endpoint to remove below line
        examplenote = Note(content="this is a note")
        new_user.notes.append(examplenote)
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_user.name} successfully created!")
