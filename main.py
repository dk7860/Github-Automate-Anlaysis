
import streamlit as st
#import pandas as pd
from repo_complexity import find_most_complex_repository

# streamlit framework
st.title('Github Automated Analysis ')
github_url=st.text_input("Please Enter The GitHub User's URL ")


# Example github_url = 'https://github.com/your github id'
most_complex_repository = find_most_complex_repository(github_url)


if github_url:
    if most_complex_repository :
        st.write(f" # The most technically complex repository from user is '{github_url}' is '{most_complex_repository}'.")
    else:
        st.write("Some Error Occured")
