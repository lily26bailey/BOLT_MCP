import json
import matplotlib.pyplot as plt
import os

def plot_utterance_length_histogram(client_input_path, therapist_input_path, output_path):
    all_utterance_lengths = []

    # Process client utterances
    with open(client_input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            utterance = data.get('utterance', '')
            word_count = len(utterance.split())
            all_utterance_lengths.append(word_count)

    # Process therapist utterances
    with open(therapist_input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            utterance = data.get('utterance', '')
            word_count = len(utterance.split())
            all_utterance_lengths.append(word_count)

    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(all_utterance_lengths, bins=50, edgecolor='black')
    plt.title('Distribution of Utterance Lengths (Word Count)')
    plt.xlabel('Utterance Length (Words)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    print(f"Histogram saved to: {output_path}")

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    
    client_input = os.path.join(script_dir, '..', 'sample_dataset', 'sample_client_input.jsonl')
    therapist_input = os.path.join(script_dir, '..', 'sample_dataset', 'sample_therapist_input.jsonl')
    output_file = os.path.join(script_dir, 'utterance_length_histogram.png')

    plot_utterance_length_histogram(client_input, therapist_input, output_file)
