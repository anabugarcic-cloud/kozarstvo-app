import streamlit as st

# Podešavanje stranice
st.set_page_config(
    page_title="Kozarstvo - Vodič i Kalkulator",
    page_icon="🐐",
    layout="wide"
)

# Custom CSS za diskretnu zelenu pozadinu i lep izgled
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f9f4;
    }
    
    .slogan-box {
        text-align: center;
        padding: 16px;
        margin-top: 15px;
        margin-bottom: 25px;
        background-color: #d8ebd9;
        border-radius: 12px;
        border: 2px solid #82c486;
    }
    
    .slogan-text {
        font-size: 26px;
        font-weight: bold;
        color: #1e4d2b;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🐐 Kozarstvo: Vodič za uzgoj, proizvodnju i kalkulator")

# Galerija slika - 4 jednake kolone u jednom redu
col1, col2, col3, col4 = st.columns(4)

with col1:
    try:
        st.image("koza.jpg", caption="Naša koza", use_container_width=True)
    except Exception:
        st.info("Slika koza.jpg")

with col2:
    try:
        st.image("milka 1.jpg", caption="Koza Milka", use_container_width=True)
    except Exception:
        st.info("Slika milka 1.jpg")

with col3:
    try:
        st.image("jarici.jpg", caption="Jarići na pašnjaku", use_container_width=True)
    except Exception:
        st.info("Slika jarici.jpg")

with col4:
    st.image(
        "https://images.unsplash.com/photo-1452195100486-9cc805987862?auto=format&fit=crop&w=800&q=80", 
        caption="Domaći kozji sir", 
        use_container_width=True
    )

# Slogan ispod galerije
st.markdown("""
    <div class="slogan-box">
        <span class="slogan-text">🐐 JEDITE SIR SREĆNIH KOZA 🧀</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tabovi za navigaciju kroz aplikaciju
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Rase i Osnove", 
    "2. Ishrana i Nega", 
    "3. Kalkulator Mleka i Sira", 
    "4. Prerada i Recepti", 
    "5. Sirenje i Čuvanje Sira"
])

with tab1:
    st.header("1. Rase koza i osnove uzgoja")
    st.write("""
    Kozarstvo je izuzetno isplativa i održiva grana stočarstva. Pravilan izbor rase zavisi od vaših ciljeva:
    - **Alpina (Francuska alpina):** Odlična mlekulja, prilagodljiva terenima, stabilna proizvodnja.
    - **Sanska koza:** Šampion u količini mleka, idealna za intenzivan uzgoj i štalske uslove.
    - **Balkanska koza:** Skromnih zahteva, izuzetno otporna, odlična za brdska i planinska područja.
    """)

with tab2:
    st.header("2. Ishrana i dnevna nega")
    st.write("""
    Pravilna ishrana direktno utiče na kvalitet mleka i procenat mlečne masti:
    - **Kabasta hrana:** Kvalitetno seno (lucerka, livadsko seno) čini osnovu obroka.
    - **Koncentrovana hrana:** Kukuruz, ječam, zob i mekinje za visoku mlečnost.
    - **Čista voda i mineralni kamen:** Uvek dostupni za pravilno varenje i zdravlje stada.
    """)

with tab3:
    st.header("3. Kalkulator prerade mleka u sir")
    st.write("Izračunajte očekivanu količinu sira na osnovu ulazne količine mleka:")
    
    mleko_litara = st.number_input("Unesite količinu mleka u litrima (L):", min_value=1.0, value=10.0, step=1.0)
    tip_sira = st.selectbox("Izaberite tip sira:", ["Meki / Sveži sir (~12-15% prinos)", "Polutvrdi / Tvrdi sir (~10-12% prinos)"])
    
    if "Meki" in tip_sira:
        prinos = mleko_litara * 0.14
    else:
        prinos = mleko_litara * 0.11
        
    st.success(f"Očekivana količina sira: **{prinos:.2f} kg**")

with tab4:
    st.header("4. Prerada mleka i tradicionalne recepture za sir")
    st.write("Tri proverene i vrhunske recepture za dodatu vrednost vaših proizvoda:")
    
    col_r1, col_r2, col_r3 = st.columns(3)
    
    with col_r1:
        st.subheader("🫒 1. Sir u maslinovom ulju")
        st.write("""
        **Sastojci:** Kockice dobro oceđenog i prosušenog čvrstog kozjeg sira, devičansko maslinovo ulje, ruzmarin, majčina dušica, biber u zrnu.
        
        **Priprema:**
        1. Sir prosušiti 24h na rešetki.
        2. Ređati u sterilisanu teglu sa začinima.
        3. Potpuno prelijte uljem da nema vazdušnih džepova.
        4. Odležati minimum 10 dana na hladnom.
        """)
        
    with col_r2:
        st.subheader("🌿 2. Sir sa bosiljkom i začinskim biljem")
        st.write("""
        **Sastojci:** Sveži ili polutvrdi kozji sir, svež ili sušeni bosiljak, beli luk u granulama, maslinovo ulje.
        
        **Priprema:**
        1. Formirane rolice ili kriške sira uvaljati u sitno seckani bosiljak i beli luk.
        2. Ostaviti u hladnjači/frižideru 12–24h da sir upije aromu bilja.
        3. Pakovati u vakuum foliju ili preliti laganim uljem za produženu svežinu.
        """)
        
    with col_r3:
        st.subheader("🪵 3. Sir u pepelu (ili pikantni sa paprikom)")
        st.write("""
        **Sastojci:** Meki/sveži kozji sir, prosejani drveni pepeo (od hrasta/bukve) ili slatka/ljuta tucana paprika.
        
        **Priprema:**
        1. Sir nakon ceđenja blagim posipanjem obložiti tankim slojem čistog drvenog pepela (ili tucane paprike).
        2. Pepeo smanjuje kiselost na površini i podstiče stvaranje fine, kremaste kore.
        3. Ostaviti na zrenju na 12°C oko 7 do 14 dana.
        """)

with tab5:
    st.header("5. Sirenje i detaljno uputstvo za čuvanje sira")
    
    st.subheader("🧀 Proces sirenja")
    st.write("""
    Sirenje je ključna faza u kojoj se mleko pod uticajem sirila i kontrole temperature zgrušava i pretvara u gruš:
    - Održavajte temperaturu mleka stabilnom (obično između 32°C i 35°C u zavisnosti od recepture).
    - Nakon dodavanja sirila, ostavite mleko u mirovanju dok se ne formira čvrst gruš čistog loma.
    - Gruš se seče na kockice odgovarajuće veličine kako bi se izdvojila surutka.
    """)
    
    st.subheader("🧊 Čuvanje i zrenje sira nakon podsoljavanja / salamurenja")
    st.info("""
    Mnogi proizvođači prave greške upravo nakon soljenja! Pravilno čuvanje određuje teksturu, ukus i trajnost sira.
    """)
    
    st.markdown("""
    #### 1. Prosušivanje sira (nakon vađenja iz salamure ili suvog soljenja)
    - **Ocedjivanje:** Sir se mora dobro ocediti od viška tečnosti.
    - **Formiranje kore:** Ostavite sir na proji/rešetki na temperaturi od **12°C do 15°C** uz blago strujanje vazduha 24–48 sati dok se površina ne osuši i ne formira zaštitna pokožica.

    #### 2. Uslovi zrenja (Podrum / Zrenionica)
    - **Temperatura:** Optimalna temperatura za zrenje većine kozjih sireva je **10°C – 13°C**.
    - **Vlažnost vazduha:** Relativna vlažnost mora biti **80% – 85%**. Ako je vazduh presuv, sir puca; ako je previše vlažan, hvata se nepoželjna buđ.
    - **Okretanje:** Prvih dve nedelje sir se okreće svakodnevno, a kasnije 2-3 puta nedeljno radi ravnomernog sušenja i formiranja strukture.

    #### 3. Skladištenje i dugotrajno čuvanje
    - **Čuvanje u ulju:** Za produženo trajanje bez gubitka vlage, sir se pakuje u staklene tegle sa maslinovim ili suncokretovim uljem uz dodatak lekovitog bilja.
    - **Čuvanje u salamuri:** Za meke i polutvrde bele sireve, čuvati u blagoj salamuri (6–8% soli) na temperaturi od **4°C do 8°C** u frižideru ili hladnom podrumu.
    """)
