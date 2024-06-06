from llama2_stat_analysis.stats import load_csv, basic_statistics
from llama2_stat_analysis.plots import generate_plots
from llama2_stat_analysis.llama2_integration import query_llama

def main():
    file_path = 'data/sample.csv'
    data = load_csv(file_path)
    stats = basic_statistics(data)
    generate_plots(data)
    question = "Provide a detailed analysis of the data."
    response = query_llama(question)
    print(response)

if __name__ == '__main__':
    main()
