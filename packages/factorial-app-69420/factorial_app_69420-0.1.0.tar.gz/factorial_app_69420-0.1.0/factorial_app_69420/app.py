from factorial_app_69420.factorial import fact
import streamlit as st
import streamlit.web.cli as stcli

def main():
    st.title("Factorial")
    number = st.number_input("Put number you want to find it factor: ", min_value=  1, max_value=  900)

    if st.button("submit"):
        result = fact(number)
        st.write(f"Factorial of {number} is {result}")


if __name__ == "__main__":
    main()