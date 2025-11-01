from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Flask app deployed via jenkins on AWS EC2! Hurray I did it!!!"

@app.route('/health')
def health():
  return { "status" : "Healthy"}, 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port = 5000)
