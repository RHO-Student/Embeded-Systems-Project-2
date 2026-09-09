# Embedded Systems Project 2 
## Gas and Smoke Detector
The Aim of this project is to use cheap MQ-2 Smoke and gas sensors to monitor air contamination for future use in my 3d printing set up. 
I intend to do this by getting two sensors and then taking readings from one in clean air and one in the contaminated shed and using a differential comparison work out how contaminated the air is.
Then over serial connection i have a program asking for readings then recording and time stamping them as a row in a CSV file witch is used for the data for a streamlit.io monitoring web app.
--- 

<img width="734" height="712" alt="Circut diagram" src="https://github.com/user-attachments/assets/3daad3b0-13d3-4565-bc42-dfd8a2900f7d" /> \
*made with circuit.io*

## Limitations
- Due to the power requirements when requesting several readings or having a rapid change in status the micro controler has to have a external power supply and usb or use a modifyed version of the code that hard codes the initial control data other wise we get data drifting
- Due to the power requirements i was unable to implement the temp and humidity sensor while keeping the non power supplyed version of the project stable
- While the sensor differential works with one of my primary sources of contamination i would have liked to get slightly better sensors or have multiple types to cover some of a the failings of the mq-2
