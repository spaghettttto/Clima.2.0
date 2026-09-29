import streamlit as st

st.title("Clasificador y Conversor de Clima")

unidad = st.selectbox(
    "Selecciona la unidad de medida:",
    ["Grados Celsius (°C)", "Grados Fahrenheit (°F)", "Kelvin (K)"]
)

temp_input = st.number_input(
    "Ingresa la temperatura:", 
    value=25.0, 
    step=0.5,
    format="%.1f"
)

humedad = st.number_input("Ingresa la humedad (%):", min_value=0, max_value=100, value=50)
llueve = st.checkbox("¿Está lloviendo?")

if st.button("Evaluar Clima", type="primary"):
    if "Fahrenheit" in unidad:
        temperatura_celsius = (temp_input - 32) * 5 / 9
    elif "Kelvin" in unidad:
        temperatura_celsius = temp_input - 273.15
    else:
        temperatura_celsius = temp_input
    if temperatura_celsius >= 30:
        if humedad >= 70:
            clasificacion = "Calor húmedo"
        else:
            clasificacion = "Calor seco"
    elif temperatura_celsius >= 15:
        if llueve:
            clasificacion = "Templado lluvioso"
        else:
            clasificacion = "Templado"
    else:
        clasificacion = "Frío"
    st.divider()
    st.subheader("Resultado de la Evaluación")
    st.success(f"Clasificación: **{clasificacion}**")
    st.write(f"**Temperatura ingresada:** {temp_input} {unidad.split()[1]}")
    st.write(f"**Temperatura equivalente:** {temperatura_celsius:.1f} °C")
    st.write(f"**Humedad:** {humedad}%")
    st.write(f"**Lluvia:** {'Sí' if llueve else 'No'}")
