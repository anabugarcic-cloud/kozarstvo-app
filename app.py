import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Kozarstvo Vodič & Kalkulator", 
    page_icon="🐐", 
    layout="wide"
)

st.title("🐐 Vodič, Kalendar i Kalkulator za Kozarstvo")

# --- SLIKA NA VRHU ---
try:
    st.image("koza.jpg", caption="Naša akrobatkinja na imanju 🐐✨", use_container_width=True)
except Exception:
    st.info("💡 Proverite da li je fajl 'koza.jpg' otpremljen na GitHub.")

meni = [
    "📋 Rase koza",
    "🥗 Ishrana",
    "🥛 Povećanje mlečnosti",
    "📅 Kalendar jarenja",
    "🧮 Kalkulator obroka",
    "🧀 Pravljenje sira & Saveti"
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

elif izbor == "🧀 Pravljenje sira & Saveti":
    st.header("🧀 Vodič za pravljenje sira & Kalkulator prinosa")
    
    tab1, tab2, tab3 = st.tabs(["🧮 Kalkulator sira", "📖 Korak-po-korak vodič", "💡 Zlatna pravila i greške"])
    
    with tab1:
        st.subheader("Proračun količine sira iz mleka")
        litara_mleka = st.number_input("Unesite količinu mleka (Litara):", min_value=1.0, value=10.0, step=0.5)
        vrsta_sira = st.selectbox("Vrsta sira koju pravite:", ["Meki / Mladi / Sveži sir (veći randman)", "Polutvrdi / Kriška sir", "Tvrdi odležali sir"])
        
        if vrsta_sira == "Meki / Mladi / Sveži sir (veći randman)":
            randman = 0.15  # 15%
            opis = "Za 1 kg mladog sira potrebno je oko 6.5–7 litara kozjeg mleka."
        elif vrsta_sira == "Polutvrdi / Kriška sir":
            randman = 0.11  # 11%
            opis = "Za 1 kg polutvrdog sira potrebno je oko 9 litara kozjeg mleka."
        else:
            randman = 0.08  # 8%
            opis = "Za 1 kg tvrdog zrelog sira potrebno je oko 12 litara kozjeg mleka."
            
        procenjen_sir = litara_mleka * randman
        st.success(f"Očekivani prinos sira: **{procenjen_sir:.2f} kg**")
        st.caption(f"ℹ️ {opis}")

    with tab2:
        st.subheader("Osnove tehnologije izrade kozjeg sira")
        
        st.markdown("### 1. Priprema i Pasterizacija")
        st.write("• Sveže pomuženo mleko je najbolje odmah procediti kroz višekratnu sterilnu gazu.")
        st.write("• **Pasterizacija:** Zahrejte mleko na **63°C–65°C** i držite na toj temperaturi 30 minuta (ili na **72°C** na 15 sekundi), a zatim ga brzo ohladite na temperaturu sirištenja (32°C–35°C).")
        
        st.markdown("### 2. Sirištenje (Ukotvljavanje)")
        st.write("• Na temperaturi mleka od **33°C–35°C** dodaje se sirilo (maja) razblaženo u malo mlake nehlorisane vode sa prstohvatom soli.")
        st.write("• Poklopite posudu i ostavite **40–60 minuta** na toplom mestu dok se ne formira čvrst gruš (koagulum).")

        st.markdown("### 3. Sečenje i obrada gruša")
        st.write("• Kada je gruš čvrst (puca ravno pod prstom), isecite ga nožem ili rešetkom na kockice veličine 1–2 cm.")
        st.write("• Ostavite 5–10 minuta da se surutka počne odvajati, pa lagano mešajte 10-15 minuta da se zrna malo zategnu.")

        st.markdown("### 4. Ceđenje i Kalupljenje")
        st.write("• Prebacite gruš u kalupe obložene gazom ili u sirarske cediljke.")
        st.write("• Ostavite da se samoceđivanjem odvaja surutka nekoliko sati, uz povremeno okretanje sira u kalupu.")

        st.markdown("### 5. Soljenje")
        st.write("• **Suvo soljenje:** Posipanje morske soli po površini sira tokom preklapanja/okretanja.")
        st.write("• **Soljenje u salamuri:** Potapanje sira u 18-20% rastvor soli na nekoliko sati (u zavisnosti od veličine sira).")

    with tab3:
        st.subheader("💡 Najčešće greške i kako ih izbeći")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.error("❌ Sir je gorak")
            st.write("Najčešći razlog je **previše sirila**, prljava oprema ili neadekvatna temperatura tokom zrenja (previsoka temperatura).")
            
            st.error("❌ Sir se mrvi i jako je tvrd")
            st.write("Razlog je previše kiselo mleko, previše sitno isečen gruš ili presušivanje tokom ceđenja.")
        
        with col_b:
            st.warning("⚠️ Miris štale u siru")
            st.write("Potiče od nedovoljne higijene prilikom muže ili od prisustva jarca blizu koza koje se muzu.")
            
            st.success("✅ Savet za puniji ukus")
            st.write("Ostavite sir u čistom i prohladnom prostoru (12–15°C) sa vlažnošću vazduha oko 80–85% ako želite da razvije bogatu aromu i lepu koricu.")
