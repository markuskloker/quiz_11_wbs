import streamlit as st

# Datenstruktur: Kategorien, Fragen, Antworten und Punkte
quiz_data = {
    "Wirtschaftssysteme": [
        {"frage": "Was kennzeichnet die soziale Marktwirtschaft?", "antworten": ["Planwirtschaft", "Freie Marktwirtschaft", "Staatliche Eingriffe", "Subsistenzwirtschaft"], "richtig": 2, "punkte": 20},
        {"frage": "Wer gilt als Begründer der sozialen Marktwirtschaft?", "antworten": ["Adam Smith", "Karl Marx", "Ludwig Erhard", "John Keynes"], "richtig": 2, "punkte": 40},
        {"frage": "Was ist das Ziel des Stabilitätsgesetzes?", "antworten": ["Wirtschaftswachstum", "Preissteigerung", "Arbeitslosigkeit erhöhen", "Sozialabbau"], "richtig": 0, "punkte": 60},
        {"frage": "Was bedeutet Angebot und Nachfrage?", "antworten": ["Steuermechanismus", "Importregelung", "Produktionskosten", "Konsumsteuer"], "richtig": 0, "punkte": 80}
    ],
    "Arbeitswelt": [
        {"frage": "Was versteht man unter dualer Ausbildung?", "antworten": ["Nur Schule", "Nur Betrieb", "Kombination Schule und Betrieb", "Selbststudium"], "richtig": 2, "punkte": 20},
        {"frage": "Welche Rechte haben Auszubildende?", "antworten": ["Kündigungsschutz", "Mindestlohn", "Urlaubsanspruch", "Beförderung"], "richtig": 2, "punkte": 40},
        {"frage": "Was ist eine Tarifverhandlung?", "antworten": ["Verhandlung über Preise", "Verhandlung über Gehälter", "Verhandlung mit Kunden", "Private Vereinbarung"], "richtig": 1, "punkte": 60},
        {"frage": "Was bedeutet Work-Life-Balance?", "antworten": ["Mehr Arbeit", "Weniger Freizeit", "Ausgewogenes Verhältnis", "Nur Freizeit"], "richtig": 2, "punkte": 80}
    ],
    "Berufsorientierung": [
        {"frage": "Was gehört in eine Bewerbung?", "antworten": ["Lebenslauf", "Zeugnisse", "Liebesbrief", "Bewerbungsschreiben"], "richtig": 2, "punkte": 20},
        {"frage": "Was ist ein Assessment-Center?", "antworten": ["Sportkurs", "Testverfahren zur Personalauswahl", "Freizeitcamp", "Wahlveranstaltung"], "richtig": 1, "punkte": 40},
        {"frage": "Was zählt zu Soft Skills?", "antworten": ["Word-Kenntnisse", "Kommunikationsfähigkeit", "Excel", "Mathematik"], "richtig": 1, "punkte": 60},
        {"frage": "Was macht ein gutes Vorstellungsgespräch aus?", "antworten": ["Spontanität", "Unpünktlichkeit", "Vorbereitung", "Frechheit"], "richtig": 2, "punkte": 80}
    ],
    "Verbraucherverhalten": [
        {"frage": "Was ist nachhaltiger Konsum?", "antworten": ["Viel kaufen", "Billig einkaufen", "Umweltbewusst kaufen", "Gar nichts kaufen"], "richtig": 2, "punkte": 20},
        {"frage": "Was bedeutet Fair Trade?", "antworten": ["Handel unter Freunden", "Faire Bedingungen für Produzenten", "Keine Steuern", "Schneller Versand"], "richtig": 1, "punkte": 40},
        {"frage": "Wie beeinflussen Werbungen das Verhalten?", "antwort
