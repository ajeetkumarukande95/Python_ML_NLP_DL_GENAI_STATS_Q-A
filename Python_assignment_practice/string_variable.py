#11.	Write a program to find the length of the string "machine learning" with and without using len function.
import streamlit as st
st.write("""Q1.Write a program to find the length of the string "machine learning" with and without using len function""")
def len_string(str1):
    cnt  = 0
    for i in str1:
        cnt  = cnt + 1
    return cnt

input_string = st.text_input("Enter your string here",key = 'input_string_len')
submit_button = st.button("Get Length of input string!!")
if submit_button:
    result = len_string(input_string)
    result

st.write("""Q2.Write a program to check if the word 'orange' is present in the "This is orange juice".""")
def check_substring(input_str,substring):
    return substring in input_str

input_str = st.text_input("Enter your string here:", key = "string_input")
substring = st.text_input("Enter your substring",key = "substring_input")
check_button = st.button("check for substring")
if check_button and input_str and substring:
    if check_substring(input_str,substring):
        st.write("Substring is present inside the given input string")
    else:
        st.write("Substring not present inside the given input string")

  git config --global user.email "ajeetkumarukande95@gmail.com"
  git config --global user.name "ajeetkumarukande"


