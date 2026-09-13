import streamlit as st
import os

# 1. Postavljanje fiksnih boja za Light/Dark mode
st.set_page_config(
    page_title="Kozarstvo: Vodič i Kalkulator",
    page_icon="🐐",
    layout="wide"
)

# CSS stil koji fiksira tamnu boju teksta na telefonu i u Dark Mode-u
st.markdown("""
    <style>
    /* Fiksiranje pozadine cele aplikacije */
    .stApp {
        background-color: #f9fbf9;
    }
    
    /* Fiksiranje boje teksta za sve elemente da se uvek vide */
    html, body, [class*="css"], p, h1, h2, h3, h4, h5, h6, li, span, label {
        color: #1a1a1a !important;
    }

    /* Stil za kartice i kontejnere */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 8px;
    }
    
    /* ZELENI SLOGAN NA DNU */
    .slogan-box {
        background-color: #e8f5e9;
        border: 1px solid #c8e6c9;
        padding: 15px;
        text-align: center;
        border-radius: 10px;
        margin-top: 30px;
        font-weight: bold;
        color: #2e7d32 !important;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# NASLOV I SLIKE 
# ---------------------------------------------------------
st.title("🐐 Kozarstvo: Vodič za uzgoj, proizvodnju i kalkulator")
st.write("Dobrodošli na digitalni vodič namenjen malim poljoprivrednim gazdinstvima i početnicima u kozarstvu.")

col1, col2, col3 = st.columns(3)

with col1:
    if os.path.exists("milka 1.jpg"):
        st.image("milka 1.jpg", caption="Koza Milka")
    else:
        st.image("https://images.unsplash.com/photo-1524024973431-2ad916746881?w=500", caption="Koza Milka")

with col2:
    st.image("https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=500", caption="Domaći kozji sir")

with col3:
    st.image("https://images.unsplash.com/photo-1559561853-08451507cbe7?w=500", caption="Delikatesni sir sa biljem")

st.markdown("---")

# ---------------------------------------------------------
# TABOVI SA SADRŽAJEM
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📚 1. Osnove uzgoja", "🧀 2. Kalkulator sira", "🌿 3. Delikatesni recepti"])

with tab1:
    st.header("Rase koza i detaljan vodič o ishrani")
    st.markdown("""
    * **Mlečne rase:** Alpina i Sanska koza su najzastupljenije na našem podneblju zbog visoke mlečnosti i otpornosti.
    * **Higijena:** Čistoća staje i vimena pre i posle muže je ključna za bezbednost i vrhunski kvalitet sira.
    """)
    
    st.subheader("⚖️ Detaljne dnevne količine u ishrani (po jednoj mliječnoj kozi)")
    st.markdown("""
    Pravilno balansiran obrok utiče direktno na količinu i kvalitet mleka:
    * **Kvalitetno seno (leguminoze/detelina ili livadsko):** **1.5 do 2.5 kg** dnevno. Koza uvek treba da ima dostupno suvo seno.
    * **Koncentrovana smeša (žitarice - kukuruz, ječam, stočni grašak):** **0.3 do 0.6 kg** dnevno (količina se prilagođava količini mleka koju koza daje, otprilike 300g bazično + 100g za svaki litar mleka).
    * **Sveža kabasta hrana / Sočna hrana:** U sezoni 2 do 3 kg zelene paše ili bundeve/šargarepe kao dodatak.
    * **Mineralno-vitaminski dodaci i so:** Kamen lizalac uvek u štali + 15-20g stočne soli i minerala umešanih u hranu.
    * **Voda:** Kozi je dnevno potrebno **od 5 do 10 litara** čiste, sveže vode (naročito tokom laktacije).
    """)
    
    st.subheader("🩺 Zdravstvena zaštita i vakcinacija")
    st.markdown("""
    * **Vakcinacija:** Redovna preventiva obuhvata vakcinaciju protiv klostridijalnih infekcija (enterotoksemija) i zaraznog šepavca u dogovoru sa nadležnim veterinarom.
    * **Čišćenje od parazita:** Obavezna dehelmintizacija (čišćenje od unutrašnjih parazita) sprovodi se u proleće pre izlaska na pašu i u jesen po završetku pašne sezone.
    """)
    
    st.warning("⚠️ **VAŽNO UPOZORENJE O ISHRANI:** Izbegavajte davanje svežeg ili plesnivog hleba kozama. Velike količine hleba i skroba mogu izazvati opasnu acidozu ruma i teške digestivne probleme!")
    
    st.info("🧊 **ČUVANJE MLEKA:** Sveže pomuženo mleko mora se što pre ohladiti na temperaturu od 4°C kako bi se sprečio razvoj bakterija i očuvao prirodan, blag ukus. Ne mešati toplo tek pomuženo mleko sa već ohlađenim mlekom!")

with tab2:
    st.header("Napredni kalkulator prinosa sira")
    st.write("Izračunajte okvirnu količinu različitih vrsta sira koju možete dobiti od unete količine mleka.")
    
    mleko_litara = st.number_input("Unesite količinu mleka u litrima (L):", min_value=1.0, value=10.0, step=0.5)
    
    vrsta_sira = st.selectbox(
        "Izaberite vrstu sira koju želite da pravite:",
        [
            "Mladi meki sir (kremastiji, veći prinos)", 
            "Polutvrdi / Zreli domaći sir (standardni)", 
            "Feta / Beli sir u salamuri"
        ]
    )
    
    if "Mladi meki" in vrsta_sira:
        prinos_min = mleko_litara * 0.15
        prinos_max = mleko_litara * 0.18
        opis_sira = "Mladi meki sir zadržava više vlage, pa je i prinos veći (oko 15-18%)."
    elif "Polutvrdi" in vrsta_sira:
        prinos_min = mleko_litara * 0.10
        prinos_max = mleko_litara * 0.12
        opis_sira = "Polutvrdi i zreli sir se duže cede i suše, pa je prinos oko 10-12%."
    else:
        prinos_min = mleko_litara * 0.13
        prinos_max = mleko_litara * 0.15
        opis_sira = "Beli sir za salamuru (feta tip) ima specifičan prinos oko 13-15% pre zrenja u slanoj vodi."
    
    st.success(f"Od **{mleko_litara} L** mleka za **{vrsta_sira}**, očekivani prinos je **{prinos_min:.2f} kg do {prinos_max:.2f} kg** sira.")
    st.info(f"💡 {opis_sira}")

with tab3:
    st.header("Receptura: Sir u maslinovom ulju sa biljem")
    st.markdown("""
    ### Ključni koraci u pripremi (5 koraka):
    1. **Priprema sira:** Koristiti punomasni kozji sir odceđen od surutke.
    2. **Sečenje:** Sir iseći na jednake kockice veličine oko 2x2 cm.
    3. **Prethodno sušenje (Obavezno):** Nakon sečenja na kockice, ostavite ih na rešetki u frižideru **24–48h** da se prosuše. Ovo sprečava izdvajanje surutke u ulju.
    4. **Sterilisanje teglica:** Staklene teglice dobro operite i osušite u rerni na 100°C.
    5. **Pakovanje i prelivanje:** Slagati red sira, red začina, pa sve zaliti uljem tako da sir bude potpuno potopljen.
    
    ---
    
    #### 🌿 Varijanta 1: Mediteranski klasik
    * **Sastojci:** Kockice sira, sušeni bosiljak, ruzmarin, crni biber u zrnu, hladno ceđeno maslinovo ulje.
    * **Priprema:** Slagati red sira, red začina, pa sve preliti maslinovim uljem do vrha.
    
    #### 🧄 Varijanta 2: Pikantni delikates
    * **Sastojci:** Kockice sira, sušeni beli luk u listićima, tucana crvena paprika, kombinacija maslinovog i suncokretovog ulja.
    * **Priprema:** Izmešati začine sa sirom i zaliti uljem.
    """)

# SLOGAN NA DNU
st.markdown('<div class="slogan-box">🐐 JEDITE SIR SREĆNIH KOZA 🏡</div>', unsafe_allow_html=True)
