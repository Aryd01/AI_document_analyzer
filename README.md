# NOTE :- If you are using Jio as your ISP(either network or Jiofiber) either use a VPN or change your ISP as photos donot render in Jio network it is a known issue
# AI_document_analyzerDocument Analyzer

The Document Analyzer is a Python-based repository that utilizes the OpenAI API key and LangChain repository to analyze documents. It leverages the power of OpenAI's language models to provide answers to user queries based on the content of the document.

![Document Analyzer](https://github.com/Aryd01/AI_document_analyzer/blob/master/results/output.JPG)

## Installation

1. Clone the repository:

```shell
git clone https://github.com/Aryd01/AI_document_analyzer.git
```

2. Chage into project directory
 ``` 
 cd AI_document_analyzer
 ```
 3.Create and activate a virtual environment (optional but recommended):
 
 ```
 python3 -m venv venv
source venv/bin/activate
```
4. Install the dependencies using pip:

```
pip install -r requirements.txt
```
## Configuration
To use the Document Analyzer, you need to set up your OpenAI API key and configure the LangChain repository. Follow the steps below to configure the necessary settings:

1. Obtain an OpenAI API key by signing up on the OpenAI website (https://openai.com/).

2. Copy the API key and create a new file named .env in the project's root directory as shown in .sample_env.

## Usage

1. Place your document in the root directory with the name document.txt
2. Run
 ```
 python app.py
 ```
 3. Enter the prompt to get the desired output
