import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale , spinach & rocket smoothie')
streamlit.text('🐔Hand-bolied Free-range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list).
