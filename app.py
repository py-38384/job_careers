from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Dhaka, Bangladesh',
        'salary': 'Tk. 20,00,000'
    },
    {
        'id': 2,
        'title': 'Data scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 35,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'New York, USA',
        'salary': '$150000'
    },
]

@app.route("/")
def index():
    return render_template('home.html',jobs=jobs)

@app.route("/api/jobs")
def api():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)