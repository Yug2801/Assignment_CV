import streamlit as st
from llama2_stat_analysis.stats import load_csv, encode_data, basic_statistics
from llama2_stat_analysis.plots import generate_plot
from llama2_stat_analysis.llama2_integration import query_llama

def summarize_dataset(data):
    summary = ""
    summary += f"Number of rows: {data.shape[0]}\n"
    summary += f"Number of columns: {data.shape[1]}\n"
    summary += "Column names and types:\n"
    for col in data.columns:
        summary += f"- {col} ({data[col].dtype})\n"
    summary += "\n"
    summary += "First few rows:\n"
    summary += data.head().to_string()
    return summary

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

        st.write("Generate Plots")
        plot_type = st.selectbox('Select plot type', ['Histogram', 'Line Plot', 'Scatter Plot', 'Pie Chart'])
        columns = encoded_data.columns.tolist()
        selected_column = st.selectbox('Select column', columns)
        
        if st.button(f'Generate {plot_type} for {selected_column}'):
            generate_plot(encoded_data, selected_column, plot_type)

        question = st.text_input('Ask a question about the data:')
        if question:
            summary = summarize_dataset(data)
            prompt = f"Dataset Summary:\n{summary}\n\nQuestion: {question}"
            response = query_llama(prompt)
            st.write(response)

if __name__ == '__main__':
    main()
