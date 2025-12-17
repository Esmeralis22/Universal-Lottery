import streamlit as st

# ================== FUNCIÓN CLAVE ==================
def sumar_13_decimales_redondeados(valor):
    texto = f"{valor:.20f}"   # asegura suficientes decimales
    dec = texto.split(".")[1]

    primeros_13 = list(map(int, dec[:13]))
    dec_14 = int(dec[13])

    if dec_14 >= 5:
        primeros_13[-1] += 1

    return sum(primeros_13)

# ================== CONFIGURACIÓN ==================
st.set_page_config(
    page_title="Cálculo Numérico",
    layout="centered"
)

st.markdown("""
<style>
body {
    background-color: #1e1e1e;
}
.card {
    background-color: #333;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 12px;
    border: 2px solid #444;
}
.title {
    color: #00eaff;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
}
.subtitle {
    color: #bbb;
    text-align: center;
}
.label {
    color: #ccc;
    font-weight: bold;
}
.value {
    font-size: 26px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================== TÍTULO ==================
st.markdown(
    '<div class="title">Cálculo de 4 cifras con Fecha Manual</div>',
    unsafe_allow_html=True
)

# ================== ENTRADAS ==================
st.markdown("### 🔢 Cifras (xx-xx-xx-xx)")

c1, c2, c3, c4 = st.columns(4)
with c1: cifra1 = st.text_input(" ", max_chars=2, key="c1")
with c2: cifra2 = st.text_input(" ", max_chars=2, key="c2")
with c3: cifra3 = st.text_input(" ", max_chars=2, key="c3")
with c4: cifra4 = st.text_input(" ", max_chars=2, key="c4")

st.markdown("### 📅 Fecha (dd-mm-aaaa)")
f1, f2, f3 = st.columns([1, 1, 2])
with f1: dia = st.text_input("Día", max_chars=2)
with f2: mes = st.text_input("Mes", max_chars=2)
with f3: anio = st.text_input("Año", max_chars=4)

# ================== BOTÓN ==================
calcular = st.button("CALCULAR")

# ================== PROCESO ==================
if calcular:

    entradas = [cifra1, cifra2, cifra3, cifra4]

    # ---- Validación cifras ----
    if not all(x.isdigit() and len(x) == 2 for x in entradas):
        st.error("⚠️ Cada cifra debe ser un número de **dos dígitos**.")
        st.stop()

    cifras = list(map(int, entradas))
    total = sum(cifras)

    # ---- Validación fecha ----
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        st.error("⚠️ Fecha inválida. Usa formato dd-mm-aaaa.")
        st.stop()

    fecha_texto = f"{dia}-{mes}-{anio}"
    suma_fecha = sum(int(d) for d in fecha_texto if d.isdigit())
    suma_reducida = sum(int(d) for d in str(suma_fecha))

    st.markdown(
        f"<div class='subtitle'>"
        f"📅 Fecha: {fecha_texto} ➜ "
        f"Suma dígitos: <b>{suma_fecha}</b> ➜ "
        f"Suma reducida: <b>{suma_reducida}</b><br>"
        f"🔢 Suma de cifras: <b>{total}</b>"
        f"</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ================== RESULTADOS ==================
    divisores = [1110, 1220, 1330]

    for divisor in divisores:
        division = round(total / divisor, 13)

        # 🔥 AQUÍ SE USA LA FUNCIÓN CORRECTA
        suma_digitos = sumar_13_decimales_redondeados(division)

        extremo = suma_digitos + suma_fecha
        extra = suma_digitos + suma_reducida

        st.markdown(f"""
        <div class="card">
            <div class="label">División entre {divisor}</div>
            <div class="value" style="color:white;">{division}</div>
        </div>

        <div class="card" style="background:#222;">
            <div class="label">Número Directo</div>
            <div class="value" style="color:#FFD700;">{suma_digitos}</div>
        </div>

        <div class="card" style="background:#222;">
            <div class="label">Número Extremo</div>
            <div class="value" style="color:#00ff99;">{extremo}</div>
        </div>

        <div class="card" style="background:#222;">
            <div class="label">Número Extra</div>
            <div class="value" style="color:#00bfff;">{extra}</div>
        </div>
        """, unsafe_allow_html=True)
