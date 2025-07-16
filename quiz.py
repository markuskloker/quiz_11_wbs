import streamlit as st

# --- Session-State Initialisierung ---
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
if "antwortende_gruppen" not in st.session_state:
    st.session_state["antwortende_gruppen"] = {}

# --- Reset-Button ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state.clear()
    st.experimental_rerun()

# --- Punktestand ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragenstruktur: 4 Kategorien × 4 Fragen mit Erklärung ---
fragen = {
    # (Kategorie, Punkte): {...}
    ("Soziale Marktwirtschaft", 20): {
        "frage": "Welche Rolle spielt der Staat in der sozialen Marktwirtschaft?",
        "antworten": ["Er greift nicht ein.", "Er plant zentral.", "Er sorgt für Ausgleich und reguliert Wettbewerb.", "Er kontrolliert alle Unternehmen."],
        "richtig": 2,
        "erklärung": "Der Staat schafft sozialen Ausgleich und schützt den Wettbewerb."
    },
    ("Soziale Marktwirtschaft", 40): {
        "frage": "Was versteht man unter 'Ordnungspolitik'?",
        "antworten": ["Preisbindung", "Staatliche Rahmengestaltung", "Produktionssteuerung", "Wettbewerbsabschaffung"],
        "richtig": 1,
        "erklärung": "Sie legt die rechtlichen Rahmenbedingungen für den Markt fest."
    },
    ("Soziale Marktwirtschaft", 60): {
        "frage": "Welche Maßnahme gehört NICHT zur sozialen Marktwirtschaft?",
        "antworten": ["Subventionen", "Mindestlöhne", "Zentrale Planung", "Sozialversicherungen"],
        "richtig": 2,
        "erklärung": "Zentrale Planung ist ein Merkmal der Planwirtschaft."
    },
    ("Soziale Marktwirtschaft", 80): {
        "frage": "Was ist ein Ziel der sozialen Marktwirtschaft?",
        "antworten": ["Wettbewerb abschaffen", "Monopole fördern", "Freiheit und soziale Sicherheit verbinden", "Planwirtschaft einführen"],
        "richtig": 2,
        "erklärung": "Sie verbindet wirtschaftliche Freiheit mit sozialem Ausgleich."
    },
    ("Wirtschaftswachstum", 20): {
        "frage": "Welche Kennzahl misst das Wirtschaftswachstum?",
        "antworten": ["Inflation", "BIP", "Arbeitslosenquote", "Außenhandel"],
        "richtig": 1,
        "erklärung": "Das BIP zeigt die Wirtschaftsleistung eines Landes."
    },
    ("Wirtschaftswachstum", 40): {
        "frage": "Was ist qualitatives Wachstum?",
        "antworten": ["Produktionssteigerung", "Nachhaltiges Wachstum", "Subventioniertes Wachstum", "Industriewachstum"],
        "richtig": 1,
        "erklärung": "Es setzt auf Nachhaltigkeit und Ressourcenschonung."
    },
    ("Wirtschaftswachstum", 60): {
        "frage": "Was beschreibt ein Problem des Wirtschaftswachstums?",
        "antworten": ["Mehr Arbeitslosigkeit", "Umweltzerstörung und Ressourcenverbrauch", "Branchenübergreifende Gleichverteilung", "Innovationsverlust"],
        "richtig": 1,
        "erklärung": "Wachstum kann die Umwelt und Ressourcen stark belasten."
    },
    ("Wirtschaftswachstum", 80): {
        "frage": "Was ist ein Merkmal von nachhaltigem Wirtschaftswachstum?",
        "antworten": ["Ressourcenverschwendung", "Soziale und ökologische Verantwortung", "Konsummaximierung", "Verzicht auf Zukunftsperspektive"],
        "richtig": 1,
        "erklärung": "Es berücksichtigt auch die Bedürfnisse zukünftiger Generationen."
    },
    ("Konjunktur", 20): {
        "frage": "Welche Phase gehört NICHT zum Konjunkturzyklus?",
        "antworten": ["Aufschwung", "Boom", "Deflation", "Rezession"],
        "richtig": 2,
        "erklärung": "Deflation ist ein Preisphänomen, keine Konjunkturphase."
    },
    ("Konjunktur", 40): {
        "frage": "Was passiert in der Boom-Phase?",
        "antworten": ["Hohe Arbeitslosigkeit", "Sinkende Nachfrage", "Überhitzung & Preissteigerungen", "Investitionsrückgang"],
        "richtig": 2,
        "erklärung": "Vollauslastung der Ressourcen führt zu Preisanstieg."
    },
    ("Konjunktur", 60): {
        "frage": "Maßnahme gegen Rezession?",
        "antworten": ["Steuern erhöhen", "Ausgaben senken", "In Infrastruktur investieren", "Zinsen erhöhen"],
        "richtig": 2,
        "erklärung": "Investitionen kurbeln Nachfrage und Beschäftigung an."
    },
    ("Konjunktur", 80): {
        "frage": "Was bedeutet antizyklische Fiskalpolitik?",
        "antworten": ["Zölle einführen", "Steuern in Rezession erhöhen", "Staatsausgaben gegen Konjunkturverlauf steuern", "Konsum reduzieren"],
        "richtig": 2,
        "erklärung": "Der Staat gleicht konjunkturelle Schwankungen aktiv aus."
    },
    ("Europäische Wirtschaftsunion", 20): {
        "frage": "Was ist das Ziel der EWWU?",
        "antworten": ["Zölle einführen", "Freier Handel & gemeinsame Währung", "Wettbewerb abschaffen", "Zentralplan für Europa"],
        "richtig": 1,
        "erklärung": "Sie erleichtert Handel und stärkt Integration durch den Euro."
    },
    ("Europäische Wirtschaftsunion", 40): {
        "frage": "Welche Institution steuert die Geldpolitik der EU?",
        "antworten": ["EU-Kommission", "EuGH", "EZB", "Europäischer Rat"],
        "richtig": 2,
        "erklärung": "Die EZB sorgt für Preisstabilität und geldpolitische Steuerung."
    },
    ("Europäische Wirtschaftsunion", 60): {
        "frage": "Voraussetzung für Euro-Beitritt?",
        "antworten": ["NATO-Mitglied", "Exportüberschuss", "Stabiles Preisniveau und geringe Staatsverschuldung", "Bevölkerung über 10 Mio."],
        "richtig": 2,
        "erklärung": "Konvergenzkriterien sichern wirtschaftliche Stabilität im Euroraum."
    },
    ("Europäische Wirtschaftsunion", 80): {
        "frage": "Was ist ein Vorteil des Euro?",
        "antworten": ["Mehr Wechselkursrisiken", "Erleichterung des Handels", "Nationale Geldpolitik", "Weniger Integration"],
        "richtig": 1,
        "erklärung": "Der Euro schafft stabile Handelsbeziehungen und Preisvergleichbarkeit."
    },
}

# --- Layout: 4 Spalten mit stabilen Buttonpositionen ---
punkte_liste = [20, 40, 60, 80]
kategorien = ["Soziale Marktwirtschaft", "Wirtschaftswachstum", "Konjunktur", "Europäische Wirtschaftsunion"]
spalten = st.columns([2, 2, 2, 2])

for i, kategorie in enumerate(kategorien):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kategorie}</b></div><br>", unsafe_allow_html=True)

        for punkte in punkte_liste:
            frage_id = f"{kategorie}_{punkte}"
            status = st.session_state["beantwortet"].get(frage_id)
            gruppe = st.session_state["antwortende_gruppen"].get(frage_id)
            label = f"{punkte} Punkte"
            icon = ""
            group_label = ""

            if status == "richtig":
                icon = "✔️"
                group_label = f"(Gruppe {gruppe})"
            elif status == "falsch":
                icon = "❌"
                group_label = f"(Gruppe {gruppe})"

            button_text = f"{label} {icon} {group_label}".strip()

            # Fixierte Anzeige mit fester Größe – egal ob beantwortet oder nicht
            button_placeholder = st.empty()
            if status:
                with button_placeholder.container():
                    st.markdown(
                        f"<div style='height:50px; display:flex; align-items:center; justify-content:center; border:1px solid #ccc; border-radius:4px; font-size:14px;'>{button_text}</div>",
                        unsafe_allow_html=True)
            else:
                if button_placeholder.button(label, key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kategorie, punkte)

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
                    st.success("Richtig! 🎉")
                    st.session_state["beantwortet"][frage_id] = "richtig"
                    if gruppe == "A":
                        st.session_state["punkte_A"] += punkte
                    else:
                        st.session_state["punkte_B"] += punkte
                else:
                    st.error("Leider falsch.")
                    st.session_state["beantwortet"][frage_id] = "falsch"

                st.session_state["antwortende_gruppen"][frage_id] = gruppe

                # 📚 Erklärung anzeigen
                richtige_antwort = frage_daten["antworten"][frage_daten["richtig"]]
                erklärung = frage_daten.get("erklärung", "")
                st.info(f"👉 Richtige Antwort: **{richtige_antwort}**\n\n📚 **Warum?** {erklärung}")

                # 🔁 Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️ Zurück", key=f"zurueck_{kategorie}_{punkte}"):
                st.session_state["ausgewählte_frage"] = None
