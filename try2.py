import io
import pandas as pd
import streamlit as st
import plotly.express as px
## python -m streamlit run try2.py
Categorii_pentru_cheltuieli={
    "Alimente si bucatarie":
    ["Lidl", 
     "Carrefour",
       "Mega Image", 
       "Kaufland", 
       "Auchan", 
       "Profi",
       "Unicarm",
       "Selgros",
       "Penny",
       "Minimarket",
       "La noi pasi",
       "Piata",
       "ABC",
       "Magazin de cartier",
       "Magazin alimentar"
       ],

       "Haine si cumparaturi personale":

    ["Zara",
        "H&M",
        "Bershka",
        "Stradivarius",
        "Pull&Bear",
        "Mango",
        "Reserved",
        "C&A",
        "Deichmann",
        "CCC",
        "Sportisimo",
        "Decathlon",
        "Intersport"
        "Sinsay",
        "New Yorker",
        "Pepco",
        "LC Waikiki",
        "Tommy Hilfiger"
        ],

        "Placeri si relaxare":

    ["Cinema",
        "Teatru",
        "Concert",
        "Festival",
        "Parc de distractii",
        "Escape room",
        "Bowling",
        "Laser tag",
        "Mini golf",
        "Aqua park",
        "Spa",
        "Masaj",
        "Salon de infrumusetare"
    ],

    "Mancare cumparata si fast food":

    ["McDonald's",
        "KFC",
        "Pizza Hut",
        "Subway",
        "Burger King",
        "Domino's Pizza",
        "Taco Bell",
        "Starbucks",
        "Dunkin' Donuts",
        "Five Guys",
        "Wendy's"
    ],

    "Cafele si bauturi":

    ["Starbucks",
        "Costa Coffee",
        "Dunkin' Donuts",
        "Gloria Jean's Coffees",
        "Tim Hortons",
        "Peet's Coffee",
        "Caribou Coffee",
        "Dutch Bros Coffee",
        "Lavazza",
        "Nespresso",
        "Meron"
    ],

    "Facturi si abonamente":

    ["Electricitate",
        "Apa",
        "Gaz",
        "Internet",
        "Telefonie mobila",
        "Cablu TV",
        "Streaming (Netflix, Spotify, etc.)",
        "Asigurari (auto, locuinta, sanatate)",
        "Abonamente la sali de sport",
        "Servicii de curatenie",
        "Servicii de intretinere a locuintei",
        "Netflix",
        "Spotify",
        "HBO Max",
        "Disney+",
        "Amazon Prime Video"
    ],

    "Sanatate si farmacii":
    ["Farmacie",
        "Medicamente",
        "Consultatii medicale",
        "Analize medicale",
        "Tratament stomatologic",
        "Tratament oftalmologic",
        "Tratament dermatologic",
        "Tratament fizioterapie",
        "Tratament psihologic",
        "Analize de laborator",
        "Vaccinuri",
        "Dr Max",
        "Catena",
        "Sensiblu",
        "Help Net",
        "Farmacia Tei",
        "Farmacia Dona",
        "Farmacia Ardealul"
    ],

    "Combustibil si transport":
    ["Benzina",
        "Motorina",
        "GPL",
        "Transport public (autobuz, tramvai, metrou)",
        "Taxi",
        "Ridesharing (Uber, Bolt)",
        "Parcare",
        "Intretinere auto (revizii, schimb ulei, etc.)",
        "Asigurare auto",
        "Inmatriculare auto"
        "OMV",
        "Petrom",
        "Lukoil",
        "Rompetrol"
    ],

    "Transferuri si donatii":
    ["Transfer bancar",
        "Plata facturi online",
        "Donatii caritabile",
        "Plata impozite si taxe",
        "Plata chirie",
        "Plata rate la credite",
        "Plata pensii alimentare",
        "Plata abonamente la servicii online"
    ],

    "Investitii si economii":
    ["Investitii in actiuni",
        "Investitii in obligatiuni",
        "Investitii in fonduri mutuale",
        "Investitii in criptomonede",
        "Economii la banca",
        "Economii la fonduri de pensii private",
        "Economii la asigurari de viata"
    ],

     "Casa si intretinere":
    ["Mobilier",
     "Electrocasnice",
        "Decoratiuni interioare",
        "Curatenie si intretinere",
        "Reparatii si renovari",
        "Servicii de intretinere a locuintei"
    ],

    "Alte cheltuieli":
    ["Cadouri",
        "Evenimente speciale (nunti, botezuri, aniversari)",
        "Vacante si calatorii",
        "Hobby-uri si activitati recreative",
        "Educatie si cursuri",
        "Servicii profesionale (avocat, contabil, etc.)",
        "Alte cheltuieli neprevazute"
    ]

}
def identifica_categorie(descriere):
 
  descriere = str(descriere).upper()

def identifica_categorie(descriere):
    descriere = descriere.upper()
    for categorie, magazine in Categorii_pentru_cheltuieli.items():
        for magazin in magazine:
            if magazin.upper() in descriere:
                return categorie
    for categorie in st.session_state["categorii_personalizate"]:
        if categorie.upper() in descriere:
           return categorie

    return "Alte cheltuieli"


st.title("Gestionare Cheltuieli");
st.write("Acesta este un exemplu de aplicație Streamlit pentru gestionarea cheltuielilor.") ;

# Initializam lista categoriilor personalizate
if "categorii_personalizate" not in st.session_state:
    st.session_state["categorii_personalizate"] = []
    
# Initializam limitele de buget
if "limite_categorii" not in st.session_state:
    st.session_state["limite_categorii"] = {}

# Construim lista actuala de categorii
toate_categoriile = list(Categorii_pentru_cheltuieli.keys())

# Adaugam si categoriile personalizate
for categorie in st.session_state["categorii_personalizate"]:
    if categorie not in toate_categoriile:
        toate_categoriile.append(categorie)

# Fiecare categorie noua primeste initial limita 0 RON
for categorie in toate_categoriile:
    if categorie not in st.session_state["limite_categorii"]:
        st.session_state["limite_categorii"][categorie] = 0.0

# Eliminam limitele categoriilor care nu mai exista
for categorie in list(st.session_state["limite_categorii"].keys()):
    if categorie not in toate_categoriile:
        del st.session_state["limite_categorii"][categorie]

# Interfata pentru setarea bugetelor
st.divider()
st.subheader("Seteaza limitele de buget (RON)")
st.write(
    "Introdu suma maxima lunara pentru fiecare categorie. "
    "Lasa 0 daca nu doresti o limita."
)

df_limite = pd.DataFrame({
    "Categorie": toate_categoriile,
    "Buget lunar (RON)": [
        st.session_state["limite_categorii"][cat]
        for cat in toate_categoriile
    ]
})

tabel_limite = st.data_editor(
    df_limite,
    hide_index=True,
    disabled=["Categorie"],
    use_container_width=True,
    column_config={
        "Buget lunar (RON)": st.column_config.NumberColumn(
            "Buget lunar (RON)",
            min_value=0.0,
            step=50.0,
            format="%.2f RON"
        )
    },
    key="editor_bugete"
)

# Salvam valorile introduse de utilizator in sesiunea curenta
for _, rand in tabel_limite.iterrows():
    categorie = rand["Categorie"]
    buget = pd.to_numeric(
        rand["Buget lunar (RON)"],
        errors="coerce"
    )

    if pd.notna(buget) and buget >= 0:
        st.session_state["limite_categorii"][categorie] = float(buget)

st.divider()



fisier_csv = st.file_uploader("Încarcă fișierul CSV cu cheltuielile tale", type=["csv"]);



if fisier_csv is not None:
    df = pd.read_csv(fisier_csv)

    # Convertim sumele in numere
    df["Suma"] = pd.to_numeric(
        df["Suma"].astype(str).str.replace(",", ".", regex=False),
        errors="coerce"
    )

    st.write("Fisierul CSV a fost incarcat cu succes!")
    st.subheader("Vizualizare date")
    st.dataframe(df)

    # Identificam categoriile
    if "Descriere" in df.columns:
        df["Categorie"] = df["Descriere"].apply(
            identifica_categorie
        )
        st.write("Categorii atribuite cu succes!")
        st.dataframe(df)
    else:
        st.error("Coloana 'Descriere' nu a fost gasita.")
        st.stop()

    # Verificam daca exista coloana Data
    if "Data" not in df.columns:
        st.error("CSV-ul trebuie sa contina o coloana numita 'Data'.")
        st.stop()

    # Convertim datele calendaristice
    df["Data"] = pd.to_datetime(
        df["Data"],
    
        errors="coerce"
    )

    # Selectam luna curenta
    azi = pd.Timestamp.today()
    inceput_luna = azi.replace(day=1).normalize()
    inceput_luna_viitoare = (
        inceput_luna + pd.offsets.MonthBegin(1)
    )

    df_luna = df[
        (df["Data"] >= inceput_luna) &
        (df["Data"] < inceput_luna_viitoare)
    ].copy()

    # Selectam doar cheltuielile
    cheltuieli_luna = df_luna[
        df_luna["Suma"] < 0
    ].copy()

    cheltuieli_luna["Suma"] = (
        cheltuieli_luna["Suma"].abs()
    )

    # Calculam cheltuielile pentru fiecare categorie
    total_cheltuieli = (
        cheltuieli_luna.groupby("Categorie")["Suma"]
        .sum()
        .reindex(toate_categoriile, fill_value=0)
        .reset_index()
    )

    st.subheader("Total cheltuieli pe categorii")
    st.bar_chart(
        total_cheltuieli,
        x="Categorie",
        y="Suma"
    )

    # Adaugam limitele de buget
    total_cheltuieli["Buget alocat"] = (
        total_cheltuieli["Categorie"]
        .map(st.session_state["limite_categorii"])
        .fillna(0.0)
    )

    # Calculam diferenta dintre buget si cheltuieli
    total_cheltuieli["Suma ramasa"] = (
        total_cheltuieli["Buget alocat"]
        - total_cheltuieli["Suma"]
    )

    st.subheader("Analiza bugetului lunar")
    st.caption(f"Luna analizata: {azi.strftime('%B %Y')}")

    st.dataframe(
        total_cheltuieli,
        hide_index=True,
        use_container_width=True
    )

    # Afisam avertizarile, fara a restrictiona cheltuielile
    for _, rand in total_cheltuieli.iterrows():
        categorie = rand["Categorie"]
        buget = rand["Buget alocat"]
        cheltuit = rand["Suma"]
        ramas = rand["Suma ramasa"]

        if buget <= 0:
            continue

        if cheltuit > buget:
            st.error(
                f"DEPASIRE: {categorie}. Ai cheltuit "
                f"{cheltuit:.2f} RON din {buget:.2f} RON. "
                f"Ai depasit limita cu {abs(ramas):.2f} RON."
            )
        elif cheltuit >= 0.8 * buget:
            st.warning(
                f"ATENTIE: {categorie}. Ai folosit "
                f"{cheltuit / buget * 100:.1f}% din buget. "
                f"Mai ai {ramas:.2f} RON pana la limita."
            )
        else:
            st.success(
                f"IN GRAFIC: {categorie}. "
                f"Mai ai {ramas:.2f} RON din buget."
            )



# Lista categoriilor personalizate de utilizator
if "categorii_personalizate" not in st.session_state:
    st.session_state["categorii_personalizate"] = []

st.subheader("Personalizeaza categoriile")

categorie_noua = st.text_input(
    "Introdu numele noii categorii"
)

if st.button("Adauga categoria"):
    categorie_noua = categorie_noua.strip()

    if categorie_noua == "":
        st.warning("Introdu un nume pentru categorie.")

    elif categorie_noua in Categorii_pentru_cheltuieli:
        st.warning("Aceasta categorie exista deja.")

    elif categorie_noua in st.session_state["categorii_personalizate"]:
        st.warning("Ai adaugat deja aceasta categorie.")

    else:
        st.session_state["categorii_personalizate"].append(
            categorie_noua
        )
        st.success("Categoria a fost adaugata!")


st.write("Categorii implicite:")
st.write(list(Categorii_pentru_cheltuieli.keys()))

st.write("Categoriile tale:")
st.write(st.session_state["categorii_personalizate"])

