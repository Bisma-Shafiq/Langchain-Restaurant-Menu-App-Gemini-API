import streamlit as st

st.set_page_config(page_title="GenAi-Menu-Generator")
st.title("Restaurant Menu GenAI")
cuisine = st.sidebar.selectbox('Pick a cuisine',('Indian','Pakistani','Arabian','Italian','Mexican'))

def generature_items(cuisine):
    return{
        'restaurant_name':"Bally Bally",
        'menu_item' :'samosa,patti'
    }

if cuisine:
    response = generature_items(cuisine)
    st.header(response['restaurant_name'])
    menu_item = response['menu_item'].split(" ,")
    st.write("Menu Items")

