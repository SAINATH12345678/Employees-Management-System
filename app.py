from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = []

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        email = request.form['email']
        phone = request.form['phone']

        employees.append({
            'name': name,
            'position': position,
            'email': email,
            'phone': phone
        })

        return redirect(url_for('index'))

    return render_template('add_employee.html')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_employee(index):
    if 0 <= index < len(employees):
        employees.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
