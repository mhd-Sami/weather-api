from flask import Flask, jsonify, request, render_template
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_KEY = '5ccc694960fa44a14945d4e559ed8b98'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed'],
        }
        return jsonify(weather_info), 200
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



# from flask import Flask, jsonify, request
# import requests
# from flask_cors import CORS
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# # Retrieve the API key from the environment variable
# API_KEY = os.getenv('API_KEY')  
# BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# @app.route('/api/weather', methods=['GET'])
# def get_weather():
#     city = request.args.get('city')
#     if not city:
#         return jsonify({"error": "City is required"}), 400

#     url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         weather_info = {
#             "city": data['name'],
#             "temperature": data['main']['temp'],
#             "description": data['weather'][0]['description'],
#             "humidity": data['main']['humidity'],
#             "wind_speed": data['wind']['speed'],
#         }
#         return jsonify(weather_info), 200
#     else:
#         return jsonify({"error": "City not found"}), 404

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
