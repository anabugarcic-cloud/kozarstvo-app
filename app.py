import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Kozarstvo Vodič & Kalkulator", 
    page_icon="🐐", 
    layout="wide"
)

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
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🥛 Mlečne rase")
        st.markdown("**Sanska koza:** Najpoznatija mlečna rasa (750–1000L mleka po laktaciji). Izuzetno mirna.")
        st.markdown("**Alpina (Francuska alpina):** Otporna, prilagodljiva, odlična mlečnost i visok kvalitet mleka.")
    with col2:
        st.subheader("🥩 Kombinovane i mesne rase")
        st.markdown("**Balkanska rasa:** Domaća rasa, izuzetno otporna na vremenske uslove, mleko sa visokim % masti.")
        st.markdown("**Burska koza:** Specijalizovana rasa primarno za proizvodnju mesa.")

elif izbor == "🥗 Ishrana":
    st.header("🥗 Osnovi ishrane koza")
    st.info("Pravilna ishrana je ključ zdravlja stada i visoke mlečnosti.")
    
    st.error("⚠️ **STRIKTNO UPOZORENJE:** Koze **ne smeju da jedu hleb** (naročito svež ili u većim količinama)! Hleb izaziva opasnu acidozu buraga, nadutost i može biti smrtonosan.")
    
    st.markdown("""
    * **Kabasta hrana:** Kvalitetno seno (lucerka, livadsko) čini 60-70% obroka.
    * **Koncentrat:** Smese kukuruza, ječma, mekinja i soje za faze laktacije i bremenitosti.
    * **Voda i minerali:** Sveža voda (5–10L dnevno) i mineralni kamen moraju biti stalno dostupni.
    """)

elif izbor == "🥛 Povećanje mlečnosti":
    st.header("🥛 Saveti za povećanje mlečnosti")
    st.success("Mali saveti za optimalan prinos mleka:")
    st.markdown("""
    1. **Redovna muža:** Muža uvek u isto vreme smanjuje stres kod koza.
    2. **Balansirani proteini:** Dodavanje sojine ili suncokretove sačme u fazi pune laktacije.
    3. **Hidratacija:** Topla voda zimi značajno povećava unos vode i proizvodnju mleka.
    """)

elif izbor == "📅 Kalendar jarenja":
    st.header("📅 Kalendar jarenja")
    datum_pripusta = st.date_input("Izaberite datum pripusta (parenja):", datetime.today())
    if datum_pripusta:
        datum_jarenja = datum_pripusta + timedelta(days=150)
        st.success(f"Očekivani datum jarenja (prosečno 150 dana): **{datum_jarenja.strftime('%d.%m.%Y.')}**")

elif izbor == "🧮 Kalkulator obroka":
    st.header("🧮 Kalkulator dnevnog obroka")
    
    st.warning("🚫 **Napomena:** U kalkulator obroka nikada ne uračunavajte hleb ili pekarne otpatke!")
    
    broj_koza = st.number_input("Broj koza u stadu:", min_value=1, value=5, step=1)
    status = st.selectbox("Faza laktacije / status:", ["Mlečne koze u laktaciji", "Bremenite koze (zasušene)", "Koze u mirovanju"])
    
    if status == "Mlečne koze u laktaciji":
        seno_po_kozi = 2.5
        koncentrat_po_kozi = 0.8
    elif status == "Bremenite koze (zasušene)":
        seno_po_kozi = 2.0
        koncentrat_po_kozi = 0.4
    else:
        seno_po_kozi = 1.8
        koncentrat_po_kozi = 0.2
        
    st.write("---")
    st.metric("Potrebno sena dnevno (kg)", f"{seno_po_kozi * broj_koza:.1f} kg")
    st.metric("Potrebno koncentrata dnevno (kg)", f"{koncentrat_po_kozi * broj_koza:.1f} kg")

elif izbor == "🧀 Kalkulator sira":
    st.header("🧀 Kalkulator prinosa sira")
    litara_mleka = st.number_input("Unesite količinu mleka (Litar):", min_value=1.0, value=10.0, step=0.5)
    vrsta_sira = st.selectbox("Vrsta sira:", ["Meki / Sveži sir", "Polutvrdi sir"])
    
    if vrsta_sira == "Meki / Sveži sir":
        randman = 0.15  # oko 15%
    else:
        randman = 0.10  # oko 10%
        
    procenjen_sir = litara_mleka * randman
    st.success(f"Očekivani prinos sira: **{procenjen_sir:.2f} kg**")
