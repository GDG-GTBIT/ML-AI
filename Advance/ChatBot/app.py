from flask import Flask, render_template , request
from main import GenericAssistant

app = Flask(__name__,template_folder='templates')

@app.route('/', methods= ['GET', 'POST'])
def home():
    res = ''
    message = ''
    if request.method == 'POST':
        message = request.form.get('size')
        assistant = GenericAssistant('intents.json', model_name="test_model")
        assistant.load_model()
        res = assistant.request(message)
    return render_template('index.html', botResponse = res, userMessage = message)

if __name__=='__main__':
    app.run(debug = True)
