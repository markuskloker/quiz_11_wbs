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

# --- Reset-Funktion ---
if st.button("🔄 Quiz zurücksetzen"):
    st.session_state["beantwortet"] = {}
    st.session_state["ausgewählte_frage"] = None
    st.session_state["punkte_A"] = 0
    st.session_state["punkte_B"] = 0
    st.session_state["aktive_gruppe"] = "A"
    st.success("Quiz wurde zurückgesetzt.")

# --- Punktestand & Gruppenanzeige ---
st.markdown("### 🎯 Punktestand")
st.write(f"**Gruppe A**: {st.session_state['punkte_A']} Punkte")
st.write(f"**Gruppe B**: {st.session_state['punkte_B']} Punkte")
st.write(f"👥 Aktive Gruppe: **Gruppe {st.session_state['aktive_gruppe']}**")

# --- Fragenstruktur: 4 Kategorien × 4 Fragen mit Erklärung ---
fragen = {
    # Soziale Marktwirtschaft
    ("Soziale Marktwirtschaft", 20): {
        "frage": "Welche Rolle spielt der Staat in der sozialen Marktwirtschaft?",
        "antworten": ["Er greift nicht ein.", "Er plant die Produktion zentral.", "Er sorgt für Ausgleich und reguliert Wettbewerb.", "Er kontrolliert alle Unternehmen."],
        "richtig": 2,
        "erklärung": "Der Staat greift ein, um sozialen Ausgleich zu schaffen und Wettbewerb zu sichern."
    },
    ("Soziale Marktwirtschaft", 40): {
        "frage": "Was versteht man unter 'Ordnungspolitik'?",
        "antworten": ["Staatliche Preisbindung.", "Staatliche Gestaltung der Rahmenbedingungen.", "Direkte Produktionssteuerung.", "Abschaffung von Wettbewerb."],
        "richtig": 1,
        "erklärung": "Ordnungspolitik definiert rechtliche Rahmenbedingungen zur Sicherung des Marktes."
    },
    ("Soziale Marktwirtschaft", 60): {
        "frage": "Welche Maßnahme gehört NICHT zur sozialen Marktwirtschaft?",
        "antworten": ["Subventionen.", "Mindestlöhne.", "Zentrale Produktionsplanung.", "Sozialversicherungen."],
        "richtig": 2,
        "erklärung": "Zentrale Planung ist ein Element der Planwirtschaft."
    },
    ("Soziale Marktwirtschaft", 80): {
        "frage": "Was ist ein Ziel der sozialen Marktwirtschaft?",
        "antworten": ["Abschaffung des Wettbewerbs.", "Förderung von Monopolen.", "Verbindung von Freiheit und Sicherheit.", "Zentralisierung der Wirtschaft."],
        "richtig": 2,
        "erklärung": "Sie verbindet Marktfreiheit mit sozialem Ausgleich."
    },

    # Wirtschaftswachstum
    ("Wirtschaftswachstum", 20): {
        "frage": "Welche Kennzahl misst das Wirtschaftswachstum?",
        "antworten": ["Inflationsrate", "Bruttoinlandsprodukt (BIP)", "Arbeitslosenquote", "Handelsbilanz"],
        "richtig": 1,
        "erklärung": "Das BIP zeigt den Gesamtwert aller produzierten Güter und Dienstleistungen."
    },
    ("Wirtschaftswachstum", 40): {
        "frage": "Was bedeutet qualitatives Wachstum?",
        "antworten": ["Mehr Produktion.", "Wachstum mit Nachhaltigkeit.", "Wachstum durch Subventionen.", "Wachstum nur in Industrie."],
        "richtig": 1,
        "erklärung": "Es soll umweltverträglich und nachhaltig sein."
    },
    ("Wirtschaftswachstum", 60): {
        "frage": "Was ist ein Problem des Wirtschaftswachstums?",
        "antworten": ["Immer höhere Arbeitslosigkeit.", "Umweltzerstörung und Ressourcenverbrauch.", "Gleichmäßige Branchenverteilung.", "Weniger Innovation."],
        "richtig": 1,
        "erklärung": "Wachstum kann die Umwelt belasten und Ressourcen verbrauchen."
    },
    ("Wirtschaftswachstum", 80): {
        "frage": "Was fördert nachhaltiges Wachstum?",
        "antworten": ["Ausbeutung von Ressourcen.", "Soziale und ökologische Verantwortung.", "Kurzfristige Gewinne.", "Verzicht auf Zukunftsperspektive."],
        "richtig": 1,
        "erklärung": "Nachhaltigkeit bezieht zukünftige Generationen mit ein."
    },

    # Konjunktur
    ("Konjunktur", 20): {
        "frage": "Welche Phase gehört NICHT zum Konjunkturzyklus?",
        "antworten": ["Aufschwung", "Boom", "Deflation", "Rezession"],
        "richtig": 2,
        "erklärung": "Deflation beschreibt Preisverfall, keine Konjunkturphase."
    },
    ("Konjunktur", 40): {
        "frage": "Was geschieht in der Boom-Phase?",
        "antworten": ["Hohe Arbeitslosigkeit", "Sinkende Nachfrage", "Überhitzung und steigende Preise", "Rückgang der Investitionen"],
        "richtig": 2,
        "erklärung": "Die Wirtschaft läuft auf Hochtouren, Nachfrage und Preise steigen."
    },
    ("Konjunktur", 60): {
        "frage": "Was hilft gegen eine Rezession?",
        "antworten": ["Steuererhöhung", "Ausgabensenkung", "Investitionen in Infrastruktur", "Zinserhöhung"],
        "richtig": 2,
        "erklärung": "Öffentliche Investitionen kurbeln Nachfrage und Beschäftigung an."
    },
    ("Konjunktur", 80): {
        "frage": "Was bedeutet antizyklische Fiskalpolitik?",
        "antworten": ["Zölle einführen", "Steuern in Rezession erhöhen", "Ausgaben entgegen Konjunkturentwicklung steuern", "Konsum senken"],
        "richtig": 2,
        "erklärung": "Ausgaben werden antizyklisch angepasst, um Konjunktur zu stabilisieren."
    },

    # Europäische Wirtschaftsunion
    ("Europäische Wirtschaftsunion", 20): {
        "frage": "Was ist Ziel der Europäischen Wirtschafts- und Währungsunion?",
        "antworten": ["Zölle einführen", "Freier Handel und gemeinsame Währung", "Wettbewerb abschaffen", "Zentraler Wirtschaftsplan"],
        "richtig": 1,
        "erklärung": "Sie erleichtert Handel und stärkt Integration durch den Euro."
    },
    ("Europäische Wirtschaftsunion", 40): {
        "frage": "Welche Institution steuert die Geldpolitik der EU?",
        "antworten": ["EU-Kommission", "EuGH", "EZB", "Europäischer Rat"],
        "richtig": 2,
        "erklärung": "Die EZB ist zuständig für Preisstabilität und Geldpolitik."
    },
    ("Europäische Wirtschaftsunion", 60): {
        "frage": "Welche Voraussetzung gilt für Euro-Beitritt?",
        "antworten": ["NATO-Mitgliedschaft", "Hohe Exporte", "Stabiles Preisniveau und geringe Verschuldung", "Bevölkerung über 10 Mio."],
        "richtig": 2,
        "erklärung": "Die Konvergenzkriterien sichern finanzielle Stabilität im Euro-Raum."
    },
    ("Europäische Wirtschaftsunion", 80): {
        "frage": "Was ist ein Vorteil der gemeinsamen Währung?",
        "antworten": ["Mehr Wechselkursrisiken", "Erleichterung des Handels", "Nationale Geldpolitik", "Geringere Integration"],
        "richtig": 1,
        "erklärung": "Der Euro ermöglicht reibungslosen Handel ohne Wechselkursrisiken."
    },
}

# --- Frageauswahl-Layout ---
spalten = st.columns([2, 2, 2, 2])
kategorien = ["Soziale Marktwirtschaft", "Wirtschaftswachstum", "Konjunktur", "Europäische Wirtschaftsunion"]
punkte_liste = [20, 40, 60, 80]

for i, kategorie in enumerate(kategorien):
    with spalten[i]:
        st.markdown(f"<div style='font-size:16px;height:40px'><b>{kategorie}</b></div>", unsafe_allow_html=True)
        for p in punkte_liste:
            frage_id = f"{kategorie}_{p}"
            status = st.session_state["beantwortet"].get(frage_id)
            label = f"{p} Punkte"

            if status == "richtig":
                st.button(f"~~{label}~~ ✔️", key=frage_id, disabled=True)
            elif status == "falsch":
                st.button(f"~~{label}~~ ❌", key=frage_id, disabled=True)
            else:
                if st.button(label, key=frage_id):
                    st.session_state["ausgewählte_frage"] = (kategorie, p)

# --- Frageanzeige & Auswertung ---
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

                # ✅ Antwortbewertung
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

                # 📚 Erklärung anzeigen
                richtige_antwort = frage_daten["antworten"][frage_daten["richtig"]]
                erklärung = frage_daten.get("erklärung", "")
                st.info(f"👉 Richtige Antwort: **{richtige_antwort}**\n\n📚 **Warum?** {erklärung}")

                # 🔄 Gruppenwechsel
                st.session_state["aktive_gruppe"] = "B" if gruppe == "A" else "A"
                st.session_state["ausgewählte_frage"] = None

        with col2:
            if st.button("↩️ Zurück", key=f"zurueck_{kategorie}_{punkte}"):
                st.session_state["ausgewählte_frage"] = None
