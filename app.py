import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Kozarstvo Vodič & Kalkulator", page_icon="🐐", layout="wide")

st.title("🐐 Vodič, Kalendar i Kalkulator za Kozarstvo")

meni = [
    "📋 Rase koza", 
    "🥗 Ishrana", 
    "🥛 Povećanje mlečnosti", 
    "📅 Kalendar jarenja", 
    "🧮 Kalkulator obroka",
    "🧀 Kalkulator sira"
]
izbor = st.sidebar.selectbox("Meni / Navigacija", meni)

if izbor == "📋 Rase koza":
    st.header("📋 Pregled rasa koza")
    st.markdown("""
    * **Sanska koza:** Najpoznatija mlečna rasa (do 750–1000L mleka po laktaciji). Izuzetno mirne naravi.
    * **Alpina (Francuska alpina):** Otporna, prilagodljiva, odlična mlečnost i visok kvalitet mleka.
    * **Balkanska rasa:** Domaća rasa, izuzetno otporna na vremenske uslove, mleko sa visokim procentom masti.
    * **Burska koza:** Specijalizovana rasa primarno za proizvodnju mesa.
    """)

elif izbor == "🥗 Ishrana":
    st.header("🥗 Pravilna ishrana koza")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ Preporučeno i dobro")
        st.write("• Kvalitetno seno (lucerka, livadsko)")
        st.write("• Sveža paša, brst (žbunje, lišće)")
        st.write("• Zob (oves), kukuruz, ječam (umereno)")
        st.write("• So za lizanje i mineralni dodaci")
        st.write("• Čista voda (5–15L dnevno)")
    with col2:
        st.subheader("⚠️ Oprez i štetno")
        st.write("• Otrovne biljke (mrazovac, tisa, bujad, rododendron)")
        st.write("• Plesniva i buđava hrana")
        st.write("• Previše kukuruza odjednom (opasnost od acidoze)")
        st.write("• Sirov i zelen krompir")

elif izbor == "🥛 Povećanje mlečnosti":
    st.header("🥛 Saveti za veću mlečnost")
    st.write("1. **Proteini u hrani:** Kvalitetno seno lucerke u laktaciji direktno podiže proizvodnju mleka.")
    st.write("2. **Stalna voda:** Za 1L mleka kozi je potrebno 3 do 4 litra sveže vode.")
    st.write("3. **Redovna muža:** Muža u uvek isto vreme smanjuje stres i održava laktaciju.")
    st.write("4. **Higijena i mir:** Čist objekat bez promaje čuva zdravlje vimena.")

elif izbor == "📅 Kalendar jarenja":
    st.header("📅 Kalendar bremenitosti i zasušenja")
    datum_parenja = st.date_input("Izaberite datum parenja koze:", datetime.now())
    
    if st.button("Izračunaj datume", type="primary"):
        datum_jarenja = datum_parenja + timedelta(days=150)
        datum_zasusenja = datum_parenja + timedelta(days=90)
        
        st.success(f"🐐 **Očekivani datum jarenja:** {datum_jarenja.strftime('%d.%m.%Y.')}")
        st.info(f"🛑 **Preporučeni datum zasušenja (prestanak muže):** {datum_zasusenja.strftime('%d.%m.%Y.')}")
        st.caption("Gravidnost traje između 147 i 155 dana.")

elif izbor == "🧮 Kalkulator obroka":
    st.header("🧮 Kalkulator dnevnog obroka")
    tezina = st.number_input("Telesna masa koze (kg):", min_value=20.0, max_value=120.0, value=50.0)
    mleko = st.number_input("Dnevna proizvodnja mleka (L):", min_value=0.0, max_value=10.0, value=2.5)
    
    if st.button("Izračunaj obrok", type="primary"):
        seno_kg = tezina * 0.03
        koncentrat_g = mleko * 300
        voda_l = (tezina * 0.1) + (mleko * 3)
        
        st.success(f"🌾 **Seno (lucerka/livadsko):** {seno_kg:.2f} kg/dnevno")
        st.info(f"🥣 **Koncentrat / Žitarice:** {koncentrat_g:.0f} g/dnevno")
        st.info(f"💧 **Sveža voda:** {voda_l:.1f} L/dnevno")

elif izbor == "🧀 Kalkulator sira":
    st.header("🧀 Kalkulator prinosa sira i sirišta")
    litari = st.number_input("Količina kozjeg mleka (L):", min_value=1.0, max_value=500.0, value=10.0)
    
    if st.button("Izračunaj prinos sira", type="primary"):
        mladi = litari * 0.15
        stari = litari * 0.11
        siriste = litari * 0.5
        
        st.success(f"🧀 **Očekivana količina mladog sira:** oko {mladi:.2f} kg")
        st.info(f"🧀 **Očekivana količina prevrelog/tvrđeg sira:** oko {stari:.2f} kg")
        st.info(f"💧 **Orijentaciona količina tečnog sirišta:** oko {siriste:.1f} ml")
