import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ёвари Омӯзгор", layout="wide")
st.title("📊 Платформаи ҳисоби баҳо ва чорякҳо")

with st.sidebar:
    st.header("⚙️ Танзимот")
    miqdori = st.number_input("Миқдори хонандагон:", 1, 45, 30)

if 'df_data' not in st.session_state:
    st.session_state.df_data = pd.DataFrame({
        "№": range(1, miqdori + 1),
        "Ному Насаб": [""] * miqdori,
        "Баҳоҳои ҷорӣ": [""] * miqdori,
        "Санҷиш": [0] * miqdori
    })

edited_df = st.data_editor(st.session_state.df_data, use_container_width=True, hide_index=True)

if st.button("🚀 ҲИСОБ КАРДАН"):
    res = []
    for _, row in edited_df.iterrows():
        try:
            marks = [int(x) for x in str(row["Баҳоҳои ҷорӣ"]).split() if x.isdigit()]
            if marks:
                avg = sum(marks) / len(marks)
                sanjish = row["Санҷиш"]
                final = (avg + sanjish) / 2 if sanjish > 0 else avg
                baho = round(final)
            else:
                baho = "-"
        except:
            baho = "Хато"
        res.append({"№": row["№"], "Хонанда": row["Ному Насаб"], "Чоряк": baho})
    st.table(pd.DataFrame(res))
