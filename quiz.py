import streamlit as st

# --- Session-State ---
if "beantwortet" not in st.session_state:
    st.session_state["beantwortet"] = {}
if "ausgewählte_frage" not in st.session_state:
    st.session_state["ausgewählte_frage"] = None
if "punkte_A" not in st.session_state:
    st.session_state["punkte_A"] = 0
if "punkte_B" not in st.session_state:
    st.session_state["punkte_B"] = 0
if "aktive_gruppe" not in st.session_state:
    st.session_state["aktive_gruppe"] = "A"

# --- Reset ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state["beantwortet"] = {}
    st.session_state["ausgewählte_frage"] = None
    st.session_state["punkte_A"] = 0
    st.session_state["punkte_B"] = 0
    st.session_state["aktive_gruppe"] = "A"
    st.success("Quiz wurde zurückgesetzt.")

# --- Punktestand & aktive Gruppe ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragenstruktur (4×4 Fragen à 4 Antworten) ---
fragen = {
    ("Wirtschaftssysteme", 20): {
        "frage": "Was ist ein typisches Merkmal der freien Marktwirtschaft?",
        "antworten": ["Preisbindung", "Staatliche Planung", "Angebot und Nachfrage", "Subventionen"],
        "richtig": 2
    },
    ("Wirtschaftssysteme", 40): {
        "frage": "Wie unterscheidet sich die soziale von der freien Marktwirtschaft?",
        "antworten": ["Durch staatlichen Sozialausgleich", "Durch Preisbindung", "Durch höhere Steuern", "Durch Monopole"],
        "richtig": 0
    },
    ("Wirtschaftssysteme", 60): {
        "frage": "Was gehört zum magischen Viereck?",
        "antworten": ["Inflation, Migration, Export, Zinsniveau", "Preisniveaustabilität, Vollbeschäftigung, außenwirtschaftliches Gleichgewicht, Wirtschaftswachstum", "Subvention, Steuern, Löhne, Rente", "Handel, Bildung, Sicherheit, Umwelt"],
        "richtig": 1
    },
    ("Wirtschaftssysteme", 80): {
        "frage": "Welche Auswirkung haben Subventionen?",
        "antworten": ["Sie senken die Produktivität", "Sie fördern bestimmte Branchen gezielt", "Sie erhöhen die Mehrwertsteuer", "Sie führen zu weniger Konsum"],
        "richtig": 1
    },
    ("Arbeitswelt", 20): {
        "frage": "Was ist eine duale Ausbildung?",
        "antworten": ["Nur Schule", "Nur Betrieb", "Kombination von Schule und Betrieb", "Fernstudium"],
        "richtig": 2
    },
    ("Arbeitswelt", 40): {
        "frage": "Was ist ein Berichtsheft?",
        "antworten": ["Gehaltsnachweis", "Nachweis über Ausbildungsinhalte", "Urlaubsübersicht", "Steuerbescheid"],
        "richtig": 1
    },
    ("Arbeitswelt", 60): {
        "frage": "Was regelt das Berufsbildungsgesetz?",
        "antworten": ["Steuerrecht", "Pflichten von Auszubildenden und Ausbildenden", "Krankenkassenbeiträge", "Arbeitszeiten für Beamte"],
        "richtig": 1
    },
    ("Arbeitswelt", 80): {
        "frage": "Was passiert bei einem Verstoß gegen Ausbildungsvorgaben?",
        "antworten": ["Nichts", "Abmahnung durch Schule", "Bußgeld und Entzug der Ausbildungsbefugnis", "Verlängerung der Ausbildung"],
        "richtig": 2
    },
    ("Berufsorientierung", 20): {
        "frage": "Was gehört zu einer Bewerbung?",
        "antworten": ["Abizeugnis & Steuererklärung", "Lebenslauf & Anschreiben", "Liebesbrief", "Mietvertrag"],
        "richtig": 1
    },
    ("Berufsorientierung", 40): {
        "frage": "Was ist ein Assessment-Center?",
        "antworten": ["Ein Freizeitcamp", "Ein Auswahlinstrument mit Tests und Gruppenaufgaben", "Ein Verkaufslager", "Ein Bewerbungskurs"],
        "richtig": 1
    },
    ("Berufsorientierung", 60): {
        "frage": "Was zählt zu Soft Skills?",
        "antworten": ["Excel-Kenntnisse", "Teamfähigkeit", "Mathematikkenntnisse", "Technisches Wissen"],
        "richtig": 1
    },
    ("Berufsorientierung", 80): {
        "frage": "Wie geht man im Bewerbungsgespräch mit Schwächen um?",
        "antworten": ["Ignorieren", "Übertreiben", "Reflektiert benennen und Umgang damit zeigen", "Frech kommentieren"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 20): {
        "frage": "Was bedeutet nachhaltiger Konsum?",
        "antworten": ["Spontankäufe", "Billig einkaufen", "Ökologisch und sozial bewusst einkaufen", "Konsumverzicht"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 40): {
        "frage": "Was ist das Ziel von Fair Trade?",
        "antworten": ["Produkte schneller liefern", "Höherer Gewinn für Händler", "Faire Bedingungen für Produzent:innen", "Rabattaktionen"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 60): {
        "frage": "Wie wirkt Werbung?",
        "antworten": ["Sie hat keinen Einfluss", "Sie informiert neutral", "Sie beeinflusst emotional und durch Suggestion", "Sie erhöht Preise"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 80): {
        "frage": "Was ist der ökologische Fußabdruck?",
        "antworten": ["CO₂-Bilanz eines Menschen", "Schuhgröße", "Ressourcenverbrauch der Industrie", "Steuerklasse für Ökoprodukte"],
        "richtig": 0
    }
}

# --- Spaltenlayout ---
spalten = st.columns([2, 2, 2, 2])
for i, kat in enumerate(["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kat}</b></div>", unsafe_allow_html=True)
        for p in [20, 40, 60, 80]:
            frage_id = f"{kat}_{p}"
            status = st.session_state["beantwortet"].get(frage_id)
            label = f"{p} Punkte"

            if status == "richtig":
                st.button(f"~~{label}~~ ✔️", key=frage_id, disabled=True)
            elif status == "falsch":
                st.button(f"~~{label}~~ ❌", key=frage_id, disabled=True)
            else:
                if st.button(label, key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kat, p)

# --- Frageanzeige ---
if st.session_state["ausgewählte_frage"]:
    kategorie, punkte = st.session_state["ausgewählte_frage"]
    frage_daten = fragen.get((kategorie, punkte))
    if frage_daten:
        st.markdown("---")
        st.subheader(f"📝 Frage aus {kategorie} – {punkte} Punkte")
        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"radio_{kategorie}_{punkte}")
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✅ Antwort bestätigen", key=f"bestätigen_{kategorie}_{punkte}"):
                index = frage_daten["antworten"].index(auswahl)
                frage_id = f"{kategorie}_{punkte}"
                gruppe = st.session_state["aktive_gruppe"]

                if index == frage_daten["richtig"]:
                    st.success("Richtig!")
                    st.session_state["beantwortet"][frage_id] = "richtig"
                    if gruppe == "A":
                        st.session_state["punkte_A"] += punkte
                    else:
                        st.session_state["punkte_B"] += punkte
                else:
                    st.error("Leider falsch.")
                    st.session
