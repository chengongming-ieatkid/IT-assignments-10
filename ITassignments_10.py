#exercise 1
import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data['value'])
    else:
        print("cannot use the joke.")

if __name__ == "__main__":
    get_chuck_norris_joke()


#exercise 2
import requests

def get_weather():
    api_key = "Minh0210"  
    city = input("Nhập tên thành phố: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        
        print(f"Thời tiết tại {city}: {weather_desc}")
        print(f"Nhiệt độ: {temp_celsius:.2f}°C")
    else:
        print("Không tìm thấy thông tin thành phố.")

if __name__ == "__main__":
    get_weather()



#exercise 3
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)



#exercise 4
import json
from flask import Flask, jsonify

app = Flask(__name__)
def load_airports():
    try:
        with open('airports.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport(icao):
    airports = load_airports()
    airport = next((a for a in airports if a['icao'].upper() == icao.upper()), None)
    
    if airport:
        return jsonify({
            "icao": airport['icao'],
            "name": airport['name'],
            "city": airport['city'],
            "country": airport['country']
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)