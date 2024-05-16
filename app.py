import paho.mqtt.client as paho
import time
import streamlit as st
import requests

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("Intento1")

def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

client1.on_message = on_message
client1.on_publish = on_publish

client1.connect(broker, port)

URL_MOTOR_ON = "https://wokwi.com/api/simulations/launch?url=https://wokwi.com/arduino/libraries/DigitalWrite&code=%2F%2F%20Wokwi%20DigitalWrite%20example%0A%23include%20%3CDigitalWrite.h%3E%0A%0AVirtualPin%20LED%20%3D%20%7B12%2C%20OUTPUT%7D%3B%0A%0Avoid%20setup%28%29%20%7B%0A%20%20pinMode%28LED%2C%20OUTPUT%29%3B%0A%7D%0A%0Avoid%20loop%28%29%20%7B%0A%20%20digitalWrite%28LED%2C%20HIGH%29%3B%20%2F%2F%20turn%20the%20LED%20on%0A%20%20delay%281000%29%3B%20%2F%2F%20wait%20for%201%20second%0A%20%20digitalWrite%28LED%2C%20LOW%29%3B%20%2F%2F%20turn%20the%20LED%20off%0A%20%20delay%281000%29%3B%20%2F%2F%20wait%20for%201%20second%0A%7D"

URL_MOTOR_OFF = "https://wokwi.com/api/simulations/launch?url=https://wokwi.com/arduino/libraries/DigitalWrite&code=%2F%2F%20Wokwi%20DigitalWrite%20example%0A%23include%20%3CDigitalWrite.h%3E%0A%0AVirtualPin%20LED%20%3D%20%7B12%2C%20OUTPUT%7D%3B%0A%0Avoid%20setup%28%29%20%7B%0A%20%20pinMode%28LED%2C%20OUTPUT%29%3B%0A%7D%0A%0Avoid%20loop%28%29%20%7B%0A%20%20digitalWrite%28LED%2C%20LOW%29%3B%20%2F%2F%20turn%20the%20LED%20off%0A%7D"

def control_motor(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.success("¡Operación exitosa!")
        else:
            st.error("Hubo un problema al intentar controlar el motor.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error de conexión: {e}")

st.title("Control de Motor")
st.write("Escribe 'hola' para encender el motor y 'adios' para apagarlo.")

input_texto = st.text_input("Escribe aquí:")
boton_control = st.button("Controlar Motor")

if boton_control:
    if input_texto == "hola":
        control_motor(URL_MOTOR_ON)
    elif input_texto == "adios":
        control_motor(URL_MOTOR_OFF)
