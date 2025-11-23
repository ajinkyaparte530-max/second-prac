# app.py

import streamlit as st
import calculator

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")

mode = st.selectbox(
    "Choose Calculation Type",
    [
        "Add", "Subtract", "Multiply", "Divide",
        "Power (a^b)", "Square Root", "Logarithm (ln a)",
        "Sine (sin a)", "Cosine (cos a)", "Tangent (tan a)",
        "Factorial"
    ]
)

# Input fields
num1 = st.number_input("Enter first number", value=0.0)

# second number only needed for some operations
num2 = None
if mode in ["Add", "Subtract", "Multiply", "Divide", "Power (a^b)"]:
    num2 = st.number_input("Enter second number", value=1.0)

if st.button("Calculate"):
    if mode == "Add":
        result = calculator.add(num1, num2)
    elif mode == "Subtract":
        result = calculator.subtract(num1, num2)
    elif mode == "Multiply":
        result = calculator.multiply(num1, num2)
    elif mode == "Divide":
        result = calculator.divide(num1, num2)
    elif mode == "Power (a^b)":
        result = calculator.power(num1, num2)
    elif mode == "Square Root":
        result = calculator.sqrt(num1)
    elif mode == "Logarithm (ln a)":
        result = calculator.log(num1)
    elif mode == "Sine (sin a)":
        result = calculator.sin(num1)
    elif mode == "Cosine (cos a)":
        result = calculator.cos(num1)
    elif mode == "Tangent (tan a)":
        result = calculator.tan(num1)
    elif mode == "Factorial":
        result = calculator.factorial(num1)
    else:
        result = "Invalid operation"

    st.success(f"Result = {result}")
