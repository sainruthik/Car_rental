from flask import Flask, render_template, request

app = Flask(__name__)

# Sample car data
cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "year": 2020, "price_per_day": 50, "category": "Sedan"},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2019, "price_per_day": 60, "category": "Sedan"},
    {"id": 3, "brand": "Ford", "model": "Fusion", "year": 2018, "price_per_day": 70, "category": "Sedan"},
    {"id": 4, "brand": "Toyota", "model": "Rav4", "year": 2020, "price_per_day": 80, "category": "SUV"},
    {"id": 5, "brand": "Honda", "model": "CR-V", "year": 2019, "price_per_day": 90, "category": "SUV"},
    {"id": 6, "brand": "Ford", "model": "Explorer", "year": 2018, "price_per_day": 100, "category": "SUV"},
    {"id": 7, "brand": "Chevrolet", "model": "Malibu", "year": 2021, "price_per_day": 75, "category": "Sedan"},
    {"id": 8, "brand": "Volkswagen", "model": "Jetta", "year": 2020, "price_per_day": 65, "category": "Sedan"},
    {"id": 9, "brand": "Nissan", "model": "Altima", "year": 2019, "price_per_day": 55, "category": "Sedan"},
    {"id": 10, "brand": "Jeep", "model": "Grand", "year": 2020, "price_per_day": 110, "category": "SUV"},
    {"id": 11, "brand": "Subaru", "model": "Outback", "year": 2019, "price_per_day": 95, "category": "SUV"},
    {"id": 12, "brand": "Mazda", "model": "CX-5", "year": 2018, "price_per_day": 85, "category": "SUV"},
    {"id": 13, "brand": "Hyundai", "model": "Elantra", "year": 2021, "price_per_day": 60, "category": "Sedan"},
    {"id": 14, "brand": "Kia", "model": "Optima", "year": 2020, "price_per_day": 70, "category": "Sedan"},
    {"id": 15, "brand": "Audi", "model": "Q5", "year": 2020, "price_per_day": 120, "category": "SUV"},
    {"id": 16, "brand": "BMW", "model": "X3", "year": 2019, "price_per_day": 130, "category": "SUV"},
    {"id": 17, "brand": "Mercedes-Benz", "model": "GLC", "year": 2018, "price_per_day": 140, "category": "SUV"},
    {"id": 18, "brand": "Lexus", "model": "RX", "year": 2021, "price_per_day": 150, "category": "SUV"}
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/filter', methods=['POST'])
def filter_cars():
    category = request.form.get('category')
    price_range = request.form.get('price_range')
    # Set default price_range if not provided
    price_range = int(price_range) if price_range else float('inf')
    filtered_cars = [car for car in cars if (not category or car['category'] == category) and car['price_per_day'] <= price_range]
    return render_template('index.html', cars=filtered_cars)


@app.route('/car/<int:car_id>')
def car_details(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        return render_template('car_details.html', car=car)
    else:
        return "Car not found", 404

@app.route('/rent/<int:car_id>', methods=['GET', 'POST'])
def rent_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if request.method == 'POST':
        # Process rental form
        days = int(request.form['days'])
        total_price = days * car['price_per_day']
        return render_template('rent_confirmation.html', car=car, days=days, total_price=total_price)
    else:
        return render_template('rent_car.html', car=car)

if __name__ == '__main__':
    app.run(port=5001)
