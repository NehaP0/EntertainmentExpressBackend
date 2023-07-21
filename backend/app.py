from flask import Flask, jsonify  # Import the jsonify function

app = Flask(__name__)
app.config.from_pyfile('app/config.py')  # Load configuration from config.py


# Import and register the routes from the "routes" folder
from app.routes import user_routes, movie_routes, event_routes, booking_routes, show_routes
app.register_blueprint(user_routes.bp)
app.register_blueprint(movie_routes.bp)
app.register_blueprint(event_routes.bp)
app.register_blueprint(booking_routes.bp)
app.register_blueprint(show_routes.bp)

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested URL was not found on the server.'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)



# In the app.py file, we import the db object from db.py and initialize the MongoDB connection using db.init_app(app).