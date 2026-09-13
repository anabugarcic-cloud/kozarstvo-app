import streamlit as st

# 1. Postavljanje fiksnih boja za Light/Dark mode (Fiksira beli tekst na svetloj pozadini)
st.set_page_config(
    page_title="Kozarstvo: Vodič i Kalkulator",
    page_icon="🐐",
    layout="wide"
)

# CSS stil koji force-uje tamnu boju teksta na telefonu i računaru
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
# NASLOV I GLAVNE SLIKE
# ---------------------------------------------------------
st.title("🐐 Kozarstvo: Vodič za uzgoj, proizvodnju i kalkulator")
st.write("Dobrodošli na digitalni vodič namenjen malim poljoprivrednim gazdinstvima i početnicima u kozarstvu.")

# Prikaz 3 lokalne slike u redu
col1, col2, col3 = st.columns(3)
with col1:
    st.image("milka 1.jpg", caption="Koza Milka")
with col2:
    st.image("sir 1.jpg", caption="Domaći kozji sir")
with col3:
    st.image("sir u ulju.jpg", caption="Delikatesni sir sa biljem")

st.markdown("---")

# ---------------------------------------------------------
# TABOVI SA SADRŽAJEM
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📚 1. Osnove uzgoja", "🧀 2. Kalkulator sira", "🌿 3. Delikatesni recepti"])

with tab1:
    st.header("Rase koza i osnove uzgoja")
    st.markdown("""
    * **Mlečne rase:** Alpina i Sanska koza su najzastupljenije na našem podneblju zbog visoke mlečnosti.
    * **Ishrana:** Osnovu ishrane čine kvalitetna paša, seno i balansirane koncentrovane smeše.
    * **Higijena:** Čistoća staje i vimea pre i posle muže je ključna za kvalitet i ukus sira.
    """)
    
    st.warning("⚠️ **VAŽNO UPOZORENJE O ISHRANI:** Izbegavajte davanje svežeg ili plesnivog hleba kozama. Velike količine hleba i skroba mogu izazvati opasnu acidozu ruma i teške digestivne probleme!")
    
    st.info("🧊 **ČUVANJE MLEKA:** Sveže pomuženo mleko mora se što pre ohladiti na temperaturu od 4°C kako bi se sprečio razvoj bakterija i očuvao prirodan, blag ukus.")

with tab2:
    st.header("Kalkulator prinosa sira")
    st.write("Izračunajte okvirnu količinu sira koju možete dobiti od dnevne muže.")
    
    mleko_litara = st.number_input("Unesite količinu mleka u litrima (L):", min_value=1.0, value=2.5, step=0.5)
    
    # Okvirna procena: 10-12% prinosa za polutvrdi/zreli sir
    sir_min = mleko_litara * 0.10
    sir_max = mleko_litara * 0.12
    teglice = int(sir_min // 0.120)  # Teglice od ~120g sira
    
    st.success(f"Od **{mleko_litara} L** mleka očekivani prinos sušenog sira je **{sir_min:.2f} kg do {sir_max:.2f} kg**.")
    st.info(f"💡 To je dovoljno za otprilike **{teglice} do {teglice+1} delikatesne teglice** sira u ulju!")

with tab3:
    st.header("Receptura: Sir u maslinovom ulju sa biljem")
    st.markdown("""
    ### Ključni koraci u pripreme (5 koraka):
    1. **Priprema sira:** Koristiti punomasni kozji sir odceđen od surutke.
    2. **Sečenje:** Sir iseći na jednake kockice veličine oko 2x2 cm.
    3. **Prethodno sušenje (Obavezno):** Nakon sečenja na kockice, ostavite ih na rešetki u frižideru **24–48h** da se prosuše. Ovo sprečava izdvajanje surutke i mućenje ulja.
    4. **Sterilisanje teglica:** Staklene teglice dobro operite i osušite u rerni na 100°C.
    5. **Pakovanje i prelivanje:** Slagati red sira, red začina, pa sve zaliti uljem tako da sir bude potpuno potopljen.
    
    ---
    
    #### 🌿 Varijanta 1: Mediteranski klasik
    * **Sastojci:** Kockice sira, sušeni bosiljak, ruzmarin, crni biber u zrnu, hladno ceđeno maslinovo ulje.
    
    #### 🧄 Varijanta 2: Pikantni delikates
    * **Sastojci:** Kockice sira, sušeni beli luk u listićima, tucana crvena paprika, kombinacija maslinovog i suncokretovog ulja.
    """)

# ---------------------------------------------------------
# SLOGAN NA DNU
# ---------------------------------------------------------
st.markdown('<div class="slogan-box">🐐 JEDITE SIR SREĆNIH KOZA 🏡</div>', unsafe_allow_html=True)
