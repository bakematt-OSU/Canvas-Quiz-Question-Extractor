
# Canvas Quiz Question Extractor

This Python script processes an HTML file containing quiz questions and answers, extracts relevant information, and outputs it into a structured text file. The script is designed to work with a quiz data format and is useful for organizing quiz results, including correct/incorrect answers, awarded points, and more.

## Features

- **Class Selection**: Choose from predefined classes stored in `CurrentClasses.txt` or manually input class details.
- **Quiz Processing**: Extract questions, answers, and points awarded from the HTML file.
- **Formatted Output**: Save the results into a text file, including whether each answer was correct or incorrect, and points awarded.
- **Customizable File Handling**: You can select the input file to process and automatically generate an output file name based on the quiz number, class name, and date.

## Requirements

- Python 3.x
- **BeautifulSoup** library for HTML parsing

To install BeautifulSoup, run the following command:

```bash
pip install beautifulsoup4
```

## Usage
1. **Save/Copy HTML Quiz Results `Input.html`**:
   1. To use this script with Canvas Quiz results, first, export the quiz results from Canvas.
   2. Go to Canvas and open the quiz for which you want to extract results.
   3. Click on Quiz Results.
   4. Click on Download Results in CSV format.
   5. Open the CSV in a spreadsheet application (e.g., Excel or Google Sheets).
   6. Convert the CSV data into a structured HTML format that can be processed by this script.
   7. Save the quiz results as an HTML file in the root of the script directory.
   - The HTML file can then be selected by the script for processing.

2. **Prepare `CurrentClasses.txt`**:
   - The script will read class names from the `CurrentClasses.txt` file. Each line should contain a class name.

3. **Run the Script**:
   - The script will prompt you to select a file to process, choose the quiz number and class name, and generate the output.
   - The output file will be named in the format: `Quiz <quiz_number> - <class_name> - <current_date>.txt`.

4. **Process the File**:
   - The script reads the input HTML file, extracts quiz data, and formats the results into a structured text file.

### Example

```bash
$ python TakenQuizQuestionExtract.py
Available files in the current directory:
1. quiz_results.html
Enter the number of the file you want to process: 1
Available options:
0. Enter class info manually
1. CS-101 Intro to Computer Science
2. CS-201 Data Structures
Select a class by number: 1
Enter the quiz number: 3
Results have been saved to 'Quiz 3 - CS-101 Intro to Computer Science - 2025-04-14.txt'.
```

## How It Works

1. **File Selection**: The script lists files in the current directory and allows you to select one to process.
2. **Class and Quiz Selection**: Choose a class from `CurrentClasses.txt` or enter a class manually. Input the quiz number.
3. **Processing HTML**: The script reads the HTML file, finds all questions, and extracts relevant details:
   - Question text
   - Answer options
   - Points awarded and points possible
   - Whether the answer was correct or incorrect
4. **Output**: The results are written to a text file, with each question and its answers formatted with correctness indicators.

### Output Example

```
Quiz 3 - CS-101 Intro to Computer Science - 2025-04-14
----------------------------------------
Question 1:
✔CORRECT - 6 / 6pts
What is the time complexity of binary search?
   ✔ Option 1: O(log n) - CORRECT
   ❌ Option 2: O(n) - INCORRECT
   Option 3: O(n log n)
----------------------------------------
Question 2:
❌INCORRECT - 0 / 1pts
Which sorting algorithm is the most efficient in the worst case?
   ✔ Option 1: QuickSort - CORRECT
   ❌ Option 2: BubbleSort - SELECTED INCORRECT
   Option 3: MergeSort
----------------------------------------
```

## Contributing

Feel free to fork this repository, create a pull request, or report issues if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
