import streamlit as st

# 📚 Quiz-Daten
quiz_data = {
    "Wirtschaft": [...],  # Unverändert – siehe vorheriger Code
    "Recht": [...],
    "Globalisierung": [...],
    "Nachhaltigkeit": [...]
}

st.set_page_config(page_title="WBS Quiz", layout="wide")
st.title("📊 Quiz – WBS Klasse 11")

if "answered" not in st.session_state:
    st.session_state["answered"] = set()
if "selected_question" not in st.session_state:
    st.session_state["selected_question"] = None

# 🧮 Matrix-Ansicht
col1, col2, col3, col4 = st.columns(len(quiz_data))

for col, category in zip([col1, col2, col3, col4], quiz_data.keys()):
    with col:
        st.subheader(category)
        for item in quiz_data[category]:
            key = f"{category}_{item['score']}"
            label = f"~~{item['score']} Punkte~~" if key in st.session_state["answered"] else f"{item['score']} Punkte"
            if st.button(label, key=key):
                if key not in st.session_state["answered"]:
                    st.session_state["selected_question"] = (key, item)

# 💡 Frage anzeigen
if st.session_state["selected_question"]:
    key, q = st.session_state["selected_question"]
    st.markdown(f"### ❓ {q['question']}")
    selected_option = st.radio("Antwortmöglichkeiten:", q["options"], index=None)
    if selected_option is not None:
        if q["options"].index(selected_option) == q["answer"]:
            st.success("✅ Richtig!")
        else:
            st.error("❌ Leider falsch.")
        st.session_state["answered"].add(key)
        st.session_state["selected_question"] = None  # Frage schließen
        st.rerun()  # Seite neu laden, um das UI zu aktualisieren
