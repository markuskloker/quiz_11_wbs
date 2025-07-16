import streamlit as st

# --- Quizdaten ---
fragen = {
    ("Wirtschaftssysteme", 20): {
        "frage": "Was kennzeichnet die soziale Marktwirtschaft?",
        "antworten": ["Planwirtschaft", "Freie Marktwirtschaft", "Staatliche Eingriffe", "Subsistenzwirtschaft"],
        "richtig": 2
    },
    ("Wirtschaftssysteme", 40): {
        "frage": "Wer gilt als Begründer der sozialen Marktwirtschaft?",
        "antworten": ["Adam Smith", "Karl Marx", "Ludwig Erhard", "John Keynes"],
        "richtig": 2
    },
    ("Wirtschaftssysteme", 60): {
        "frage": "Was ist das Ziel des Stabilitätsgesetzes?",
        "antworten": ["Wirtschaftswachstum", "Preissteigerung", "Arbeitslosigkeit erhöhen", "Sozialabbau"],
        "richtig": 0
    },
    ("Wirtschaftssysteme", 80): {
        "frage": "Was bedeutet Angebot und Nachfrage?",
        "antworten": ["Steuermechanismus", "Importregelung", "Produktionskosten", "Konsumsteuer"],
        "richtig": 0
    },

    ("Arbeitswelt", 20): {
        "frage": "Was versteht man unter dualer Ausbildung?",
        "antworten": ["Nur Schule", "Nur Betrieb", "Kombination Schule und Betrieb", "Selbststudium"],
        "richtig": 2
    },
    ("Arbeitswelt", 40): {
        "frage": "Welche Rechte haben Auszubildende?",
        "antworten": ["Kündigungsschutz", "Mindestlohn", "Urlaubsanspruch", "Beförderung"],
        "richtig": 2
    },
    ("Arbeitswelt", 60): {
        "frage": "Was ist eine Tarifverhandlung?",
        "antworten": ["Verhandlung über Preise", "Verhandlung über Gehälter", "Verhandlung mit Kunden", "Private Vereinbarung"],
        "richtig": 1
    },
    ("Arbeitswelt", 80): {
        "frage": "Was bedeutet Work-Life-Balance?",
        "antworten": ["Mehr Arbeit", "Weniger Freizeit", "Ausgewogenes Verhältnis", "Nur Freizeit"],
        "richtig": 2
    },

    ("Berufsorientierung", 20): {
        "frage": "Was gehört in eine Bewerbung?",
        "antworten": ["Lebenslauf", "Zeugnisse", "Liebesbrief", "Bewerbungsschreiben"],
        "richtig": 3
    },
    ("Berufsorientierung", 40): {
        "frage": "Was ist ein Assessment-Center?",
        "antworten": ["Sportkurs", "Testverfahren zur Personalauswahl", "Freizeitcamp", "Wahlveranstaltung"],
        "richtig": 1
    },
    ("Berufsorientierung", 60): {
        "frage": "Was zählt zu Soft Skills?",
        "antworten": ["Word-Kenntnisse", "Kommunikationsfähigkeit", "Excel", "Mathematik"],
        "richtig": 1
    },
    ("Berufsorientierung", 80): {
        "frage": "Was macht ein gutes Vorstellungsgespräch aus?",
        "antworten": ["Spontanität", "Unpünktlichkeit", "Vorbereitung", "Frechheit"],
        "richtig": 2
    },

    ("Verbraucherverhalten", 20): {
        "frage": "Was ist nachhaltiger Konsum?",
        "antworten": ["Viel kaufen", "Billig einkaufen", "Umweltbewusst kaufen", "Gar nichts kaufen"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 40): {
        "frage": "Was bedeutet Fair Trade?",
        "antworten": ["Handel unter Freunden", "Faire Bedingungen für Produzenten", "Keine Steuern", "Schneller Versand"],
        "richtig": 1
    },
    ("Verbraucherverhalten", 60): {
        "frage": "Wie beeinflussen Werbungen das Verhalten?",
        "antworten": ["Gar nicht", "Durch Informationen", "Durch Manipulation", "Durch Preisänderung"],
        "richtig": 2
    },
    ("Verbraucherverhalten", 80): {
        "frage": "Was ist ein ökologischer Fußabdruck?",
        "antworten": ["Ein Schuhabdruck", "CO₂-Bilanz einer Person", "Umweltmarke", "Verbraucherzertifikat"],
        "richtig": 1
    },
}

# --- Session-State initialisieren ---
if "beantwortet" not in st.session_state:
    st.session_state["beantwortet"] = []

if "ausgewählte_frage" not in st.session_state:
    st.session_state["ausgewählte_frage"] = None

# --- Titel ---
st.title("📘 WBS Quiz – Klasse 11 (BW)")

# --- Spalten erstellen ---
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]
punkte_liste = [20, 40, 60, 80]
spalten = st.columns(4)

# --- Buttons in Spalten anzeigen ---
for i, kat in enumerate(kategorien):
    with spalten[i]:
        st.subheader(kat)
        for p in punkte_liste:
            frage_id = f"{kat}_{p}"
            if frage_id in st.session_state["beantwortet"]:
                st.button(f"~~{p} Punkte~~ ✅", key=frage_id, disabled=True)
            else:
                if st.button(f"{p} Punkte", key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kat, p)

# --- Wenn Frage ausgewählt ist, zeige sie ---
if st.session_state["ausgewählte_frage"]:
    kategorie, punkte = st.session_state["ausgewählte_frage"]
    frage_daten = fragen.get((kategorie, punkte))

    if frage_daten:
        st.markdown("---")
        st.subheader(f"📝 Frage aus {kategorie} – {punkte} Punkte")
        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"radio_{kategorie}_{punkte}")
        if st.button("Antwort bestätigen", key=f"bestätigen_{kategorie}_{punkte}"):
            if frage_daten["antworten"].index(auswahl) == frage_daten["richtig"]:
                st.success("✅ Richtig! Gute Arbeit. 🎉")
            else:
                st.error("❌ Leider falsch. Weiter geht's!")
            st.session_state["beantwortet"].append(f"{kategorie}_{punkte}")
            st.session_state["ausgewählte_frage"] = None
