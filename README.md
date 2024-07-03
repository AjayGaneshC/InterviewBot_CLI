# AI Interviewer

AI Interviewer is an automated interview simulation tool for software developer positions. It uses the Ollama language model to conduct interviews, ask relevant questions, and provide feedback on candidate responses.

## Features

- Conducts a simulated job interview for software developer positions
- Uses predefined questions covering various aspects of software development
- Provides real-time feedback and evaluation of candidate responses
- Generates a summary of the candidate's overall performance at the end of the interview

## Requirements

- Python 3.6+
- Ollama
- LangChain

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-interviewer.git
   cd ai-interviewer
   ```

2. Install the required packages:
   ```
   pip install langchain
   ```

3. Ensure you have Ollama set up and running. The code assumes Ollama is accessible at the specified base URL.

## Usage

1. Make sure your Ollama instance is running and accessible.

2. Run the script:
   ```
   python main.py
   ```

3. Follow the prompts to answer the interview questions.

4. After answering all questions, you'll receive a summary of your performance.

## Customization

You can customize the interview questions by modifying the `questions` list in the script. Add, remove, or change questions as needed to suit your specific interview requirements.

## How It Works

1. The script initializes an Ollama language model instance.
2. It defines a list of interview questions covering various aspects of software development.
3. A PromptTemplate is used to structure the interviewer's responses and questions.
4. The `conduct_interview()` function runs the interview process:
   - It presents each question to the candidate.
   - The candidate's answer is fed into the LLMChain.
   - The AI interviewer evaluates the response and asks the next question.
   - After the final question, it provides an overall summary of the candidate's performance.

## Limitations

- The quality of the AI's responses depends on the underlying Ollama model (llama3,mistral etc.,).
- The interview questions are predefined and not dynamically generated.
- The system does not verify the technical accuracy of the candidate's responses.

## Contributing

Contributions to improve AI Interviewer are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

[MIT License](LICENSE)

---

Created by AJAY C with ❤️
