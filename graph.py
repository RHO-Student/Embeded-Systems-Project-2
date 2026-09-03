# https://docs.streamlit.io/get-started/installation
# https://pandas.pydata.org/docs/getting_started/install.html
import streamlit
import pandas

streamlit.title("Embedded Systems Sensor project")
data = pandas.read_csv()# add file
streamlit.dataframe(data)