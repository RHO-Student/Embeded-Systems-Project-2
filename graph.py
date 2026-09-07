# https://docs.streamlit.io/get-started/installation
# https://pandas.pydata.org/docs/getting_started/install.html
import streamlit
import pandas

streamlit.title("Embedded Systems Sensor project")
streamlit.markdown("---")
data = pandas.read_csv(r"C:\Users\roars\Pictures\cODE SHEET\Embeded-Systems-Project-2\Readings.csv")# add file
streamlit.subheader("Gas sensor readings")
streamlit.dataframe(data,width="content", height="auto")
col1, col2, col3 = streamlit.columns(3)
with col1:
    streamlit.metric(label="Total Logged Data Points", value=len(data))
with col2:
    if 'Con' in data.columns:
        streamlit.metric(label="Max Concentration (Con)", value=f"{data['Con'].max()}")
with col3:
    if 'diff' in data.columns:
        streamlit.metric(label="Avg Sensor Deviation (diff)", value=f"{data['diff'].mean():.2f}")
streamlit.markdown("---")