import streamlit as st
from llama2_stat_analysis.stats import load_csv, encode_data, basic_statistics
from llama2_stat_analysis.plots import generate_plots
from llama2_stat_analysis.llama2_integration import query_llama

def main():
    st.title('CSV Statistical Analysis with Llama-2')
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = load_csv(uploaded_file)
        st.write("Original Data")
        st.write(data.head())

        encoded_data, encoders = encode_data(data)
        st.write("Encoded Data")
        st.write(encoded_data.head())

        if st.button('Show Statistics'):
            stats = basic_statistics(encoded_data, encoders)
            st.write("Statistics")
            for col, values in stats.items():
                st.write(f"{col}:")
                if isinstance(values, dict):
                    st.write("  Encoded:", values['encoded'])
                    st.write("  Decoded:", values['decoded'])
                else:
                    st.write("  ", values)

        if st.button('Generate Plots'):
            generate_plots(encoded_data)

        question = st.text_input('Ask a question about the data:')
        if question:
            response = query_llama(question)
            st.write(response)

if __name__ == '__main__':
    main()
