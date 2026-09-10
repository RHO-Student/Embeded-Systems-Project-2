# https://docs.streamlit.io/get-started/installation
# https://pandas.pydata.org/docs/getting_started/install.html
# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
# https://docs.streamlit.io/develop/api-reference/data/st.dataframe
# https://docs.streamlit.io/develop/api-reference/widgets/st.toggle

import streamlit
import pandas

streamlit.set_page_config(layout="wide",page_title ="Shed Status")

streamlit.title("Embedded Systems Sensor project")
streamlit.markdown("---")

data = pandas.read_csv(r"C:\Users\roars\Pictures\cODE SHEET\Embeded-Systems-Project-2\Readings.csv") #D:\Readings.csv  or C:\Users\roars\Pictures\cODE SHEET\Embeded-Systems-Project-2\
streamlit.subheader("Gas sensor readings")
Show_Graph = streamlit.toggle("Toggle Datagrid / Graph")
if Show_Graph:
    graph_data = data.set_index('Time')
    metrics = ['Control', 'Raw Sensor']
    existing_metrics = [m for m in metrics if m in graph_data.columns]
    streamlit.subheader("Readings Over Time")
    if existing_metrics:
        streamlit.line_chart(graph_data[existing_metrics], width="stretch")
else:
    streamlit.dataframe(data,width="content", height="auto")
    show_startup = streamlit.toggle("Toggle Startup / Current Data") #this used to be ai code for a button and holy shit never let AI cook again

    if show_startup:
        metric_cols = streamlit.columns(3)
        with metric_cols [0]:
            streamlit.metric(label="Time of Last Sensor reading", value=data['Time'].iloc[-1])
        with metric_cols [1]:
            if 'Contamination Level' in data.columns or ' Contamination Level' in data.columns:
                streamlit.metric(label="Last Status",  value=data['Contamination Level'].iloc[-1])
        with metric_cols [2]:
            if 'Difference Voltage' in data.columns or ' Difference Voltage' in data.columns:
                streamlit.metric(label="Last Voltage Difference", value=data['Difference Voltage'].iloc[-1])
    else:
        start_cols = streamlit.columns(4)
        with start_cols[0]:
            streamlit.metric(label="Total Logged Data Points", value=len(data))
        with start_cols[1]:
            if 'Startup Control' in data.columns or ' Startup Control' in data.columns:
                streamlit.metric(label="Average Control at startup", value=f"{data['Adjusted Sensor'].mean():.2f}")
        with start_cols[2]:
            if 'Startup Sensor' in data.columns or ' Startup Sensor' in data.columns:
                streamlit.metric(label="Average Sensor at startup", value=f"{data['Adjusted Sensor'].mean():.2f}")
        with start_cols[3]:
            if 'Difference' in data.columns or ' Difference' in data.columns:
                streamlit.metric(label="Average Sensor Deviation", value=f"{data['Difference'].mean():.2f}")
streamlit.markdown("---")

