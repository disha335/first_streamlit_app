import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale , spinach & rocket smoothie')
streamlit.text('🐔Hand-bolied Free-range Egg')
streamlit.text('🥑🍞Avocado Toast')
# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),default=['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains :")
# streamlit.dataframe(my_data_rows)
# my_cur.execute("insert into fruit_load_list values('from streamlit')")

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('jackfruit','papaya','guava','kiwi')")
    return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to have?')
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
