from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "this site actually fixed and ready for work🔥🔥💻"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
