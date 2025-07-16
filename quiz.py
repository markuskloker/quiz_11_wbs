import streamlit as st

# --- Initialisierung ---
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

# --- Reset-Button ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state["beantwortet"] = {}
    st.session_state["ausgewählte_frage"] = None
    st.session_state["punkte_A"] = 0
    st.session_state["punkte_B"] = 0
    st.success("Quiz wurde zurückgesetzt.")

# --- Gruppenanzeige ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")

# --- Gruppenauswahl ---
st.radio("👥 Wer beantwortet gerade?", ["A", "B"], key="aktive_gruppe", horizontal=True)

# --- Fragenstruktur (jede Frage hat genau 4 Antworten) ---
fragen = {
    ("Wirtschaftssysteme", 20): {"frage": "Was kennzeichnet die soziale Marktwirtschaft?", "antworten": ["Planwirtschaft", "Freie Marktwirtschaft", "Staatliche Eingriffe", "Subsistenzwirtschaft"], "richtig": 2},
    ("Wirtschaftssysteme", 40): {"frage": "Wer gilt als Begründer der sozialen Marktwirtschaft?", "antworten": ["Adam Smith", "Karl Marx", "Ludwig Erhard", "John Keynes"], "richtig": 2},
    ("Wirtschaftssysteme", 60): {"frage": "Was ist das Ziel des Stabilitätsgesetzes?", "antworten": ["Wirtschaftswachstum", "Preissteigerung", "Arbeitslosigkeit erhöhen", "Sozialabbau"], "richtig": 0},
    ("Wirtschaftssysteme", 80): {"frage": "Was bedeutet Angebot und Nachfrage?", "antworten": ["Steuermechanismus", "Importregelung", "Produktionskosten", "Konsumsteuer"], "richtig": 0},

    ("Arbeitswelt", 20): {"frage": "Was versteht man unter dualer Ausbildung?", "antworten": ["Nur Schule", "Nur Betrieb", "Kombination Schule und Betrieb", "Selbststudium"], "richtig": 2},
    ("Arbeitswelt", 40): {"frage": "Welche Rechte haben Auszubildende?", "antworten": ["Kündigungsschutz", "Mindestlohn", "Urlaubsanspruch", "Beförderung"], "richtig": 2},
    ("Arbeitswelt", 60): {"frage": "Was ist eine Tarifverhandlung?", "antworten": ["Verhandlung über Preise", "Verhandlung über Gehälter", "Verhandlung mit Kunden", "Private Vereinbarung"], "richtig": 1},
    ("Arbeitswelt", 80): {"frage": "Was bedeutet Work-Life-Balance?", "antworten": ["Mehr Arbeit", "Weniger Freizeit", "Ausgewogenes Verhältnis", "Nur Freizeit"], "richtig": 2},

    ("Berufsorientierung", 20): {"frage": "Was gehört in eine vollständige Bewerbung?", "antworten": ["Liebesbrief", "Steuererklärung", "Lebenslauf & Anschreiben", "Geldschein"], "richtig": 2},
    ("Berufsorientierung", 40): {"frage": "Was ist ein Assessment-Center?", "antworten": ["Freizeitcamp", "Testverfahren zur Personalauswahl", "Sportkurs", "Online-Shop"], "richtig": 1},
    ("Berufsorientierung", 60): {"frage": "Was zählt zu Soft Skills?", "antworten": ["Excel", "Teamfähigkeit", "Mathematik", "Word-Kenntnisse"], "richtig": 1},
    ("Berufsorientierung", 80): {"frage": "Was macht ein gutes Vorstellungsgespräch aus?", "antworten": ["Frechheit", "Unpünktlichkeit", "Vorbereitung", "Lügen"], "richtig": 2},

    ("Verbraucherverhalten", 20): {"frage": "Was bedeutet nachhaltiger Konsum?", "antworten": ["Viel kaufen", "Gar nichts kaufen", "Billig einkaufen", "Umweltbewusst konsumieren"], "richtig": 3},
    ("Verbraucherverhalten", 40): {"frage": "Was ist Fair Trade?", "antworten": ["Warenhandel im Einkaufszentrum", "Faire Bedingungen für Produzent:innen", "Preisregulierung", "Online-Shopping"], "richtig": 1},
    ("Verbraucherverhalten", 60): {"frage": "Wie beeinflussen Werbungen das Verhalten?", "antworten": ["Gar nicht", "Manipulation", "Steuererklärung", "Baupläne"], "richtig": 1},
    ("Verbraucherverhalten", 80): {"frage": "Was beschreibt den ökologischen Fußabdruck?", "antworten": ["CO₂-Bilanz einer Person", "Fußspuren im Wald", "Reifenprofil", "Verbraucherzertifikat"], "richtig": 0},
}

# --- Anzeige: vier nebeneinanderliegende breite Spalten ---
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]
punkte_liste = [20, 40, 60, 80]
spalten = st.columns([2, 2, 2, 2])  # Breiter, aber alle sichtbar

for i, kat in enumerate(kategorien):
    with spalten[i]:
        st.subheader(kat)
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

# --- Frage anzeigen & Punktesystem anwenden ---
if st.session_state["ausgewählte_frage"]:
    kategorie, punkte = st.session_state["ausgewählte_frage"]
    frage_daten = fragen.get((kategorie, punkte))

    if frage_daten:
        st.markdown("---")
        st.subheader(f"📝 Frage aus {kategorie} – {punkte} Punkte")
        auswahl = st.radio(frage_daten["frage"], frage_daten["antworten"], key=f"radio_{kategorie}_{punkte}")
        if st.button("Antwort bestätigen", key=f"bestätigen_{kategorie}_{punkte}"):
            index = frage_daten["antworten"].index(auswahl)
            frage_id = f"{kategorie}_{punkte}"
            gruppe = st.session_state["aktive_gruppe"]

            if index == frage_daten["richtig"]:
                st.success("✅ Richtig!")
                st.session_state["beantwortet"][frage_id] = "richtig"
                if gruppe == "A":
                    st.session_state["punkte_A"] += punkte
                else:
                    st.session_state["punkte_B"] += punkte
            else:
                st.error("❌ Leider falsch.")
                st.session_state["beantwortet"][frage_id] = "falsch"

            st.session_state["ausgewählte_frage"] = None
