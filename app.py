from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS=[
  {
    "title":"Data Analyst",
    "Location":"Bengaluru, India",
    "salary":"Rs. 10,00,000"
  },
  {
    "title":"Data Scientist",
    "Location":"Berlin area, Germany",
    "salary":"Rs. 15,20,000"
  },
  {
    "title":"Software Engineer",
    "Location":"Hyderabad, India",
    "salary":"Rs. 17,00,000"
  },
  {
    "title":"Quality Analyst",
    "Location":"Kolkata, India",
    "salary":"Rs. 7,00,000"
  }
]

@app.route("/")
def index():
  return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
