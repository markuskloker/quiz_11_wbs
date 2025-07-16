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

# --- Reset ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state["beantwortet"] = {}
    st.session_state["ausgewählte_frage"] = None
    st.session_state["punkte_A"] = 0
    st.session_state["punkte_B"] = 0
    st.session_state["aktive_gruppe"] = "A"
    st.success("Quiz wurde zurückgesetzt.")

# --- Punktestand ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragenstruktur: 4 Kategorien × 4 Fragen (je 4 Antworten) ---
fragen = {
    # Wirtschaftssysteme
    ("Wirtschaftssysteme", 20): {"frage": "Was kennzeichnet eine freie Marktwirtschaft?", "antworten": ["Staatliche Kontrolle", "Angebot & Nachfrage regeln den Markt", "Zentrale Planung", "Preisbindung durch Regierung"], "richtig": 1},
    ("Wirtschaftssysteme", 40): {"frage": "Was unterscheidet die soziale von der freien Marktwirtschaft?", "antworten": ["Mehr Wettbewerb", "Sozialer Ausgleich durch Staat", "Privatbesitz wird verboten", "Preise sind festgelegt"], "richtig": 1},
    ("Wirtschaftssysteme", 60): {"frage": "Welche Ziele enthält das Stabilitätsgesetz?", "antworten": ["Hohe Inflation", "Vollbeschäftigung", "Preisanstieg", "Exportsteigerung"], "richtig": 1},
    ("Wirtschaftssysteme", 80): {"frage": "Wie wirken sich staatliche Subventionen auf die Marktregulierung aus?", "antworten": ["Konsum wird eingeschränkt", "Markt wird destabilisiert", "Bestimmte Branchen werden gefördert", "Nachfrage sinkt stark"], "richtig": 2},

    # Arbeitswelt
    ("Arbeitswelt", 20): {"frage": "Was versteht man unter dualer Ausbildung?", "antworten": ["Nur Berufsschule", "Nur Betrieb", "Kombination von Schule und Betrieb", "Selbststudium"], "richtig": 2},
    ("Arbeitswelt", 40): {"frage": "Wer darf einen Ausbildungsvertrag abschließen?", "antworten": ["Nur über 21", "Nur mit Abi", "Jede Person mit Schulabschluss", "Nur mit Studium"], "richtig": 2},
    ("Arbeitswelt", 60): {"frage": "Welche Aufgabe hat ein Ausbildungsnachweis (Berichtsheft)?", "antworten": ["Beurteilung durch Kunden", "Nachweis über erbrachte Urlaubszeiten", "Dokumentation der Lerninhalte", "Berechnung der Ausbildungsvergütung"], "richtig": 2},
    ("Arbeitswelt", 80): {"frage": "Welche rechtliche Grundlage regelt Pflichten von Ausbildenden?", "antworten": ["Grundgesetz", "Arbeitsrecht", "Berufsbildungsgesetz (BBiG)", "Gewerbeordnung"], "richtig": 2},

    # Berufsorientierung
    ("Berufsorientierung", 20): {"frage": "Was gehört in ein Bewerbungsschreiben?", "antworten": ["Rechnung", "Selbstbeschreibung & Motivation", "Mietvertrag", "Abschlusszeugnis"], "richtig": 1},
    ("Berufsorientierung", 40): {"frage": "Was ist ein Assessment-Center?", "antworten": ["Urlaubszentrum", "Auswahlverfahren mit Gruppenübungen", "Online-Bewerbung", "Bewerbungsgespräch per Telefon"], "richtig": 1},
    ("Berufsorientierung", 60): {"frage": "Welche Eigenschaft zählt zu Soft Skills?", "antworten": ["Teamfähigkeit", "Programmierkenntnisse", "Führerschein", "Abschlussnote"], "richtig": 0},
    ("Berufsorientierung", 80): {"frage": "Wie kann man im Vorstellungsgespräch mit eigenen Schwächen umgehen?", "antworten": ["Leugnen", "Reflektiert und lösungsorientiert benennen", "Ignorieren", "Übertreiben"], "richtig": 1},

    # Verbraucherverhalten
    ("Verbraucherverhalten", 20): {"frage": "Was bedeutet nachhaltiger Konsum?", "antworten": ["Billig einkaufen", "Ökologisch und sozial bewusst einkaufen", "Spontankäufe", "Viel kaufen"], "richtig": 1},
    ("Verbraucherverhalten", 40): {"frage": "Was ist das Ziel von Fair Trade?", "antworten": ["Rabatte sichern", "Faire Arbeitsbedingungen für Produzenten", "Produkte schneller liefern", "Einkäufe bewerben"], "richtig": 1},
    ("Verbraucherverhalten", 60): {"frage": "Wie beeinflusst Werbung unser Konsumverhalten?", "antworten": ["Gar nicht", "Sie informiert neutral", "Sie beeinflusst Entscheidungen emotional", "Sie unterbindet Kaufentscheidungen"], "richtig": 2},
    ("Verbraucherverhalten", 80): {"frage": "Was beschreibt der ökologische Fußabdruck?", "antworten": ["Größe der Schuhe", "CO₂-Bilanz des eigenen Lebensstils", "Einkommen", "Verbrauch von Elektrogeräten"], "richtig": 1},
}

# --- Layout: 4 gleichmäßige Spalten ---
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

# --- Frageanzeige mit Antwortlogik & „Zurück“-Button ---
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
                    st.session_state["beantwortet"][frage_id] = "falsch"

                # Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️
