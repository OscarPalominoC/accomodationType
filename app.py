from flask import Flask, render_template, request
from flask import jsonify

from prediction import predict

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict', methods=['POST'])
def prediction():
    data = [request.form['days_of_stay'],
            int(request.form['genre']),
            request.form['age'],
            int(request.form['kids']),
            request.form['destination']
            ]
    result = predict(data)
    return render_template('index.html', prediction_text='{}'.format(result))    

if __name__ == "__main__":
    application.debug=False
    application.run()