from flask import Flask, render_template, request, redirect
from models import Business
from collections import deque

app = Flask(__name__)

# Queue (FIFO)
business_queue = deque()

@app.route('/')
def home():
    all_businesses = list(business_queue)
    recent_businesses = list(business_queue)[-3:]  # last 3

    return render_template(
        'home.html',
        businesses=all_businesses,
        recent=recent_businesses[::-1]  # newest first
    )

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']

        new_business = Business(name, category)
        business_queue.append(new_business)

        return redirect('/')

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)