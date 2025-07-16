import streamlit as st

# --- Session-State initialisieren ---
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
    st.success("Quiz wurde zurückgesetzt.")

# --- Punktestand & Gruppenauswahl ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.radio("👥 Aktive Gruppe", ["A", "B"], key="aktive_gruppe", horizontal=True)

# --- Fragen mit gestaffeltem Schwierigkeitsgrad ---
fragen = {
    ("Wirtschaftssysteme", 20): {"frage": "Was ist eine Marktwirtschaft?", "antworten": ["Der Staat lenkt Angebot", "Preise sind staatlich festgelegt", "Angebot und Nachfrage bestimmen den Markt", "Waren sind gratis"], "richtig": 2},
    ("Wirtschaftssysteme", 40): {"frage": "Was unterscheidet die soziale Marktwirtschaft von der freien?", "antworten": ["Mehr Wettbewerb", "Staat greift sozial ausgleichend ein", "Keine Privatunternehmen", "Preise werden festgelegt"], "richtig": 1},
    ("Wirtschaftssysteme", 60): {"frage": "Welches Ziel verfolgt das Stabilitätsgesetz?", "antworten": ["Steigende Inflation", "Steigende Arbeitslosigkeit", "Wirtschaftliches Gleichgewicht", "Verringerung der Nachfrage"], "richtig": 2},
    ("Wirtschaftssysteme", 80): {"frage": "Wie wirken sich Subventionen auf den Markt aus?", "antworten": ["Preis steigt", "Konkurrenz nimmt ab", "Produkte werden teurer", "Angebot wird gezielt gefördert"], "richtig": 3},

    ("Arbeitswelt", 20): {"frage": "Was ist eine Ausbildung?", "antworten": ["Eine Freizeitbeschäftigung", "Berufliche Qualifikation mit Theorie & Praxis", "Ein Studium", "Ein Ehrenamt"], "richtig": 1},
    ("Arbeitswelt", 40): {"frage": "Was ist der Unterschied zwischen dualer und schulischer Ausbildung?", "antworten": ["Duale Ausbildung findet im Betrieb & Schule statt", "Bei beiden wird studiert", "Nur die schulische Ausbildung ist bezahlt", "Keine Unterschiede"], "richtig": 0},
    ("Arbeitswelt", 60): {"frage": "Welche Pflichten hat der Ausbildende laut BBiG?", "antworten": ["Urlaub gewähren", "Auszubildende fördern & unterweisen", "Gehalt verdoppeln", "Beförderung zusichern"], "richtig": 1},
    ("Arbeitswelt", 80): {"frage": "Wie wirken Tarifverträge und Betriebsvereinbarungen zusammen?", "antworten": ["Tarifverträge gelten nie", "Betriebsvereinbarungen stehen über dem Gesetz", "Tarifverträge regeln Mindeststandards, Betriebe können ergänzen", "Tarifverträge gelten nur bei Beamten"], "richtig": 2},

    ("Berufsorientierung", 20): {"frage": "Was gehört in eine Bewerbung?", "antworten": ["Steuer-ID", "Liebesbrief", "Lebenslauf & Anschreiben", "Rechnungen"], "richtig": 2},
    ("Berufsorientierung", 40): {"frage": "Was ist das Ziel eines Assessment-Centers?", "antworten": ["Urlaub buchen", "Mitarbeiter motivieren", "Persönlichkeit & Fähigkeiten prüfen", "Kosten sparen"], "richtig": 2},
    ("Berufsorientierung", 60): {"frage": "Was zählt zu Soft Skills?", "antworten": ["Teamfähigkeit", "Technisches Wissen", "Sprachen", "Excel-Kenntnisse"], "richtig": 0},
    ("Berufsorientierung", 80): {"frage": "Wie bereitest du dich auf ein Vorstellungsgespräch optimal vor?", "antworten": ["Unpünktlich sein", "Unterlagen ignorieren", "Firma recherchieren & Selbstpräsentation üben", "Nur warten"], "richtig": 2},

    ("Verbraucherverhalten", 20): {"frage": "Was bedeutet nachhaltiger Konsum?", "antworten": ["Viel kaufen", "Spontan einkaufen", "Umweltbewusst & ressourcenschonend konsumieren", "Immer das Teuerste wählen"], "richtig": 2},
    ("Verbraucherverhalten", 40): {"frage": "Was ist das Ziel von Fair Trade?", "antworten": ["Schnell handeln", "Produzenten faire Bedingungen bieten", "Preise erhöhen", "Rabatte garantieren"], "richtig": 1},
    ("Verbraucherverhalten", 60): {"frage": "Wie beeinflusst Werbung unser Konsumverhalten?", "antworten": ["Gar nicht", "Manipulativ über Emotionen & Bedürfnisse", "Nur durch Logos", "Indirekt über TV-Zeit"], "richtig": 1},
    ("Verbraucherverhalten", 80): {"frage": "Was beinhaltet der ökologische Fußabdruck?", "antworten": ["Fußgröße", "CO₂-Ausstoß durch Lebensweise", "Haushaltsbudget", "Kleiderwahl"], "richtig": 1},
}

# --- Layout: 4 gleichmäßige breite Spalten + kleiner Kategorientitel ---
kategorien = ["Wirtschaftssysteme", "Arbeitswelt", "Berufsorientierung", "Verbraucherverhalten"]
punkte_liste = [20, 40, 60, 80]
spalten = st.columns([2, 2, 2, 2])  # Alle Spalten gleich breit

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

# --- Frage anzeigen und auswerten ---
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
