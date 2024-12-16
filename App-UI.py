import streamlit as st
import langchain_helper
st.set_page_config(page_title="GenAi-Menu-Generator")
st.title("Restaurant Menu GenAI")
cuisine = st.sidebar.selectbox('Pick a cuisine',('Indian','Pakistani','Arabian','Italian','Mexican'))

if cuisine:
    response = langchain_helper.generature_items(cuisine)
    st.header(response['restaurant_name'])
    menu_item = response['menu_item'].split(" ,")
    st.write("## Menu Items## ")

