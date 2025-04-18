import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁 File Convertor & Cleaner", layout="wide")

st.title("📁 File Convertor & Cleaner")
st.write("Upload your CSV and Excel files to clean the data and convert formats effortlessly. 🚀")

# File uploader 
files = st.file_uploader("Upload CSV Or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

processed_files = {}  

if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()
        
        file_bytes = file.read()
        data = BytesIO(file_bytes)

        if ext == "csv":
            df = pd.read_csv(BytesIO(file_bytes))
        elif ext == "xlsx":
            df = pd.read_excel(data)
        else:
            st.error("Unsupported file format.")
            continue

        processed_files[file.name] = df

        st.subheader(f"🔍 {file.name} - preview")
        st.dataframe(df.head())

  # Checkbox for filling missing values
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("Missing Values filled successfully!")
            st.dataframe(df.head())

        # Column selection
        select_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns.tolist())
        df = df[select_columns]
        processed_files[file.name] = df  
        st.dataframe(df.head())

for file_name, df in processed_files.items():
    if st.checkbox(f"📊 Show Chart - {file_name}") and not df.select_dtypes(include="number").empty:
        st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        format_choice = st.radio(f"Convert {file_name} to:", ["CSV", "Excel"], key=file_name)
        if st.button(f"⬇ Download {file_name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file_name.rsplit(".", 1)[0] + ".csv"
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file_name.rsplit(".", 1)[0] + ".xlsx"
            
            output.seek(0)
            st.download_button("📥 Download File", file_name=new_name, data=output, mime=mime)

            st.success("Processing Completed! 🎉")
