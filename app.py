from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace with your PostgreSQL database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost/your_database'
db = SQLAlchemy(app)


class PersonalizationSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    settings = db.Column(db.JSON, default={})


@app.route('/personalization_settings/<int:user_id>', methods=['GET', 'POST', 'DELETE'])
def personalization_settings(user_id):
    if request.method == 'GET':
        settings_record = PersonalizationSettings.query.filter_by(user_id=user_id).first()
        if settings_record:
            return jsonify(settings_record.settings)
        else:
            return jsonify({})

    elif request.method == 'POST':
        data = request.json
        settings_record = PersonalizationSettings.query.filter_by(user_id=user_id).first()
        if not settings_record:
            settings_record = PersonalizationSettings(user_id=user_id, settings=data)
            db.session.add(settings_record)
        else:
            settings_record.settings = data
        db.session.commit()
        return jsonify({'message': 'Personalization settings saved successfully'})

    elif request.method == 'DELETE':
        settings_record = PersonalizationSettings.query.filter_by(user_id=user_id).first()
        if settings_record:
            db.session.delete(settings_record)
            db.session.commit()
            return jsonify({'message': 'Personalization settings deleted successfully'})
        else:
            return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    # Create the database tables
    db.create_all()

    # Run the Flask app
    app.run(debug=True)
