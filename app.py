from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        income = request.form.get('income')
        print(f"Income Submitted: {income}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)