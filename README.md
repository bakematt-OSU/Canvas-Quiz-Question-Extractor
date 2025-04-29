# Canvas Quiz Question Extractor

A Python tool designed to extract and organize quiz questions, answers, and scoring details from Canvas LMS HTML quiz reports. This utility is particularly useful for instructors and students aiming to analyze quiz performance or archive assessments.

## Features

- **Class Management**: Select from predefined classes listed in `CurrentClasses.txt` or input new class details manually.
- **Quiz Parsing**: Process Canvas-generated HTML quiz reports to extract questions, student responses, correct answers, and points awarded.
- **Structured Output**: Generate a neatly formatted text file summarizing each question, the student's answer, correctness, and scoring.
- **Batch Processing**: Handle multiple quiz reports efficiently by placing them in the `Input/` directory.

## Prerequisites

- Python 3.6 or higher
- Required Python packages listed in `requirements.txt`

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bakematt-OSU/Canvas-Quiz-Question-Extractor.git
   cd Canvas-Quiz-Question-Extractor
   ```

2. **Install Dependencies**:

   It's recommended to use a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare HTML Files**:

   - Export the quiz report from Canvas as an HTML file.
   - Place the HTML file(s) into the `Input/` directory.

2. **Run the Extractor**:

   ```bash
   python CanvasQuizExtractor.py
   ```

   - You'll be prompted to select a class from `CurrentClasses.txt` or enter a new class name.
   - The script will process each HTML file in the `Input/` directory.

3. **View Output**:

   - Processed results will be saved in the `Output/` directory.

### Example Output

Example of output file content:

```
Quiz 1 - CS-101 - 2025-04-29
----------------------------------------
----------------------------------------
Question 1:
✔ CORRECT - 1.66/1.66pts
What is the IP address of the client computer (source) that is transferring the file to google.com? Enter the IP address in dotted decimal notation (include each dot, and omit any leading zeros for any byte, e.g., 10.1.216.54):
   ✔ - CORRECT: Text 1: 192.168.86.68
----------------------------------------
----------------------------------------
Question 2:
✔ CORRECT - 1.66/1.66pts
What is the client-side port number of the Server computer (source) that is transferring the file to google.com? Enter the port integer port number (digits only, no commas), with no leading 0's:
   ✔ - CORRECT: Text 1: 55639
----------------------------------------
----------------------------------------
Incorrect Question 3:
✖ INCORRECT - 0.0/1.66pts
What is the value in the Acknowledgment field of the TCP SYNACK segment that is used to initiate the TCP connection between the client computer and google.com? [Note: this is the "raw" value carried in the ACK number field within the segment, not the "abs ack number" displayed in Wireshark's TCP protocol window.] Enter the acknowledgment number (digits only, no commas), with no leading 0's:
   ✖ Text Box 1: 778
----------------------------------------
```

## File Structure

```
Canvas-Quiz-Question-Extractor/
├── ARCHIVE/                # Archived or old files
├── Input/                  # Place HTML quiz reports here
├── Output/                 # Processed output files
├── __pycache__/            # Python cache files
├── CanvasQuizExtractor.py  # Main script to run
├── CurrentClasses.txt      # List of predefined classes
├── FileProcess.py          # Module for file handling
├── HTML_Extract.py         # Module for HTML parsing
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Notes

- Ensure that the HTML files exported from Canvas retain their original formatting for accurate parsing.
- The script is tailored for the structure of Canvas quiz reports; modifications may be necessary for other formats.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

