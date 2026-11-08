from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_tax(income):
    """This will calculate a progressive tax across three different brackets."""
    if income <= 12000:
        return income * 0.10
    elif income <= 45000:
        return 1200.0 + (income - 12000) * 0.15
    else:
        return 6150.0 + (income - 45000) * 0.25

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    raw_income = request.form.get('income', '').strip()

    try:
        income = float(raw_income)
    except ValueError:
        error_msg = "Please enter a valid numeric income." 
        return render_template('index.html', error=error_msg), 400

    # Task 4: Rejecting negative income
    if income < 0:
        error_msg = "Income cannot be negative."
        return render_template('index.html', error=error_msg), 400

    tax_amount = calculate_tax(income)

    # Task 3: Formatting values as a currency that has 2 decimal places and the dollar sign
    formatted_income = f"${income:,.2f}"
    formatted_tax = f"${tax_amount:,.2f}"

    return render_template('result.html', income=formatted_income, tax=formatted_tax)

if __name__ == '__main__':
    app.run(debug=True)



