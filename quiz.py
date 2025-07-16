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

# --- Fragenstruktur (4 Kategorien × 4 Fragen mit je 4 Antwortmöglichkeiten) ---
fragen = {
    ("Wirtschaftssysteme", 20): {
        "frage": "Was beschreibt das Prinzip der freien Marktwirtschaft?",
        "antworten": ["Der Staat legt Preise fest", "Angebot & Nachfrage regeln Preise", "Waren sind kostenlos", "Monopole kontrollieren Märkte"],
        "richtig": 1
    },
    ("Wirtschaftssysteme", 40): {
        "frage": "Was kennzeichnet die soziale Marktwirtschaft?",
        "antworten": ["Staat greift sozial ausgleichend ein", "Preise sind fixiert", "Es existieren keine Unternehmen", "Planung durch Behörden"],
        "richtig": 0
    },
    ("Wirtschaftssysteme", 60): {
        "frage": "Was ist Ziel des magischen Vierecks?",
        "antworten": ["Vier Ministerien kontrollieren Steuern", "Gleichzeitige Verwirklichung wirtschaftlicher Hauptziele", "Inflation senken", "Vollbeschäftigung abschaffen"],
        "richtig": 1
    },
    ("Wirtschaftssysteme", 80): {
        "frage": "Wie beeinflussen Subventionen den Markt?",
        "antworten": ["Erhöhung der Inflation", "Förderung gezielter Branchen", "Einschränkung der Produktion", "Abschaffung von Wettbewerb"],
        "richtig": 1
    },

    ("Arbeitswelt", 20): {
        "frage": "Was versteht man unter dualer Ausbildung?",
        "antworten": ["Nur Betrieb", "Nur Schule", "Selbststudium", "Ausbildung im Betrieb & Berufsschule"],
        "richtig": 3
    },
    ("Arbeitswelt", 40): {
        "frage": "Was ist das Berichtsheft?",
        "antworten": ["Rechnung", "Stundenplan", "Ausbildungsnachweis", "Gehaltserklärung"],
        "richtig": 2
    },
    ("Arbeitswelt", 60): {
        "frage": "Was ist im Berufsbildungsgesetz geregelt?",
        "antworten": ["Pflichten des Ausbildenden", "Steuern", "Versicherungen", "Urlaubsrecht für alle Beschäftigten"],
        "richtig": 0
    },
    ("Arbeitswelt", 80): {
        "frage": "Was passiert bei Verstoß gegen Ausbildungsverpflichtungen?",
        "antworten": ["Bußgeld & Entzug der Ausbildungsbefugnis", "Gehaltskürzung", "Bonuszahlung", "Nichts"],
        "richtig": 0
    },

    ("Berufsorientierung", 20): {
        "frage": "Was gehört zu einer vollständigen Bewerbung?",
        "antworten": ["Liebesbrief", "Lebenslauf & Anschreiben", "Steuererklärung", "Abizeugnis ohne weitere Dokumente"],
        "richtig": 1
    },
    ("Berufsorientierung", 40): {
        "frage": "Was ist das Ziel eines Assessment-Centers?",
        "antworten": ["Teamverhalten und Problemlösen beurteilen", "Bewerber in Gruppen unterhalten", "Firmenpräsentation zeigen", "Einkaufsverhalten analysieren"],
        "richtig": 0
    },
    ("Berufsorientierung", 60): {
        "frage": "Was zählt zu Soft Skills?",
        "antworten": ["Excel-Kenntnisse", "Pünktlichkeit", "Teamfähigkeit", "Technisches Know-how"],
        "richtig": 2
    },
    ("Berufsorientierung", 80): {
        "frage": "Wie geht man im Vorstellungsgespräch mit Schwächen um?",
        "antworten": ["Übertreiben", "Verheimlichen", "Reflektiert benennen & Umgang zeigen", "Lustig machen"],
        "richtig": 2
    },

    ("Verbraucherverhalten", 20): {
        "frage": "Was bedeutet nachhaltiger Konsum?",
        "antworten": ["Schnäppchenjagd", "Spontaneinkauf", "Bewusster, umweltfreundlicher Konsum", "Luxusgüter kaufen"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 40): {
        "frage": "Was ist Fair Trade?",
        "antworten": ["Handel unter Freunden", "Fairer Handel mit Produzenten weltweit", "Online-Shopping-Plattform", "Rabatt-Aktion"],
        "richtig": 1
    },
    ("Verbraucherverhalten", 60): {
        "frage": "Wie beeinflusst Werbung das Kaufverhalten?",
        "antworten": ["Kaum", "Neutral", "Emotional & psychologisch", "Nur bei digitalen Produkten"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 80): {
        "frage": "Was ist der ökologische Fußabdruck?",
        "antworten": ["CO₂-Bilanz der Lebensweise", "Fußgröße", "Verbrauch von Schuhen", "Finanzverhalten"],
        "richtig": 0
    }
}

# --- Layout mit 4 gleichmäßigen Spalten ---
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]
punkte_liste = [20, 40, 60, 80]
spalten = st.columns([2, 2, 2, 2])

for i, kat in enumerate(kategorien):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kat}</b></div>", unsafe_allow_html=True)
        for p in punkte_liste:
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

# --- Frageanzeige mit Antwort- & Zurück-Button ---
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
                    st.success("Richtig")
