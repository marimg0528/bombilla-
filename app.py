import streamlit as st
import requests

# Definir la URL del emulador Wokwi para encender la bombilla
URL_BOMBILLA = "https://wokwi.com/projects/377066087789108225"

# Función para enviar la señal y encender la bombilla
def encender_bombilla():
    try:
        response = requests.get(URL_BOMBILLA)
        if response.status_code == 200:
            st.success("¡La bombilla se ha encendido!")
        else:
            st.error("Hubo un problema al intentar encender la bombilla.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error de conexión: {e}")

# Configurar la aplicación de Streamlit
st.title("Control de Bombilla Emulada")
st.write("Escribe algo en el siguiente cuadro y presiona el botón para encender la bombilla.")

input_texto = st.text_input("Escribe aquí:")
boton_encender = st.button("Encender Bombilla")

# Manejar la acción del botón
if boton_encender:
    encender_bombilla()
