import re
import logging
import argparse
from fpdf import FPDF
import chardet  # Install with: pip install chardet

class BhagavadGitaAssistant:
    def __init__(self, file_path):
        self.verses = self.load_verses(file_path)

    def detect_encoding(self, file_path):
        """Detects the encoding of a file."""
        try:
            with open(file_path, 'rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                return result['encoding']
        except Exception as e:
            logging.error(f"Error detecting encoding: {e}")
            return None

    def load_verses(self, file_path):
        """Loads verses from the file with detected encoding."""
        encoding = self.detect_encoding(file_path)
        if not encoding:
            logging.warning("Could not detect encoding. Defaulting to 'utf-8'.")
            encoding = 'utf-8'

        try:
            with open(file_path, 'r', encoding=encoding, errors='replace') as file:
                text = file.read()
            verses = text.splitlines()
            if not verses:
                logging.warning("The input file is empty or contains no valid verses.")
            return verses
        except Exception as e:
            logging.error(f"An error occurred while loading the file: {e}")
            return []

    def search_verses(self, query):
        results = []
        for verse in self.verses:
            if re.search(query, verse, re.IGNORECASE):
                results.append(verse)
        return results

    def get_answer(self, question):
        keywords = re.findall(r'\w+', question)
        if not keywords:
            return []

        combined_pattern = '|'.join(re.escape(keyword) for keyword in keywords)
        return self.search_verses(combined_pattern)

def create_pdf(input_file, output_file):
    try:
        # Detect the encoding of the input file
        with open(input_file, 'rb') as file:
            raw_data = file.read()
            detected = chardet.detect(raw_data)
            encoding = detected.get('encoding', 'utf-8')  # Default to 'utf-8' if detection fails
            logging.info(f"Detected file encoding: {encoding}")

        # Read the input file with the detected encoding and handle decoding errors
        with open(input_file, 'r', encoding=encoding, errors='replace') as file:
            text = file.read()

        # Clean text to ensure compatibility with 'latin-1' (used by FPDF)
        clean_text = text.encode('latin-1', 'ignore').decode('latin-1')

        # Create the PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.multi_cell(0, 10, clean_text)
        pdf.output(output_file)
        logging.info(f"PDF created successfully: {output_file}")
    except Exception as e:
        logging.error(f"Error while creating PDF: {e}")

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Argument parser setup
    parser = argparse.ArgumentParser(description="Bhagavad Gita Assistant: Create PDF and search verses.")
    parser.add_argument('--input', type=str, default='/home/rudddyy/Desktop/bhagavad_geeta.txt',
                        help="Path to the input text file")
    parser.add_argument('--output', type=str, default='/home/rudddyy/Desktop/bhagavad_gita.pdf',
                        help="Path to save the generated PDF")
    args = parser.parse_args()

    # File paths
    input_file = args.input
    pdf_output_file = args.output

    # Create a PDF from the text file
    create_pdf(input_file, pdf_output_file)

    assistant = BhagavadGitaAssistant(input_file)
    print("Welcome to the Bhagavad Gita Assistant!")
    print("Ask your question (type 'exit' to quit):")

    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            print("Assistant: Thank you for using the Bhagavad Gita Assistant. Goodbye!")
            break

        answers = assistant.get_answer(question)
        if answers:
            print("Assistant: Here are some relevant verses:")
            for answer in answers:
                print(f"- {answer}")
        else:
            print("Assistant: Sorry, I couldn't find any relevant verses.")

if __name__ == "__main__":
    main()
