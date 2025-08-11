# Voice-to-Document AI Assistant

This Python script is a simple yet powerful tool that captures your spoken ideas, transcribes them into text, and then uses AI to format the text into a blog post, a professional email, or a concise summary. The final output is automatically saved as a Microsoft Word document (`.docx`).
## 🚀 Features
* **Voice Recording**: Captures up to 10 seconds of audio from your microphone.
* **Speech-to-Text**: Uses Google's Speech Recognition API to accurately transcribe your voice.
* **AI-Powered Formatting**: Leverages Hugging Face `transformers` to:
    * Generate a short blog post from your idea.
    * Draft a professional email.
    * Create a quick summary.
* **Automatic Document Creation**: Saves the final generated content into an `output.docx` file.
## 🛠️ Setup and Installation
Follow these steps to get the project running on your local machine.
### 1. Prerequisites
* Python 3.8+
* A working microphone
### 2. Installation
**a. Create a project directory and navigate into it:**
```bash
mkdir voice-assistant
cd voice-assistant
Create and activate a virtual environment:
Windows:
python -m venv venv
.\venv\Scripts\activate

Install the required libraries:
pip install speech_recognition pyaudio nltk spacy transformers torch python-docx

Download the necessary SpaCy language model:
python -m spacy download en_core_web_sm

### ## Complete Instructions to Execute From Scratch
Here is a step-by-step guide to get this project working on your computer, assuming you have nothing but the Python code.
#### **Step 1: Create Your Project Folder**
First, create a dedicated folder for this project to keep all files organized.
1.  Open your File Explorer (Windows) or Finder (macOS).
2.  Create a new folder and name it `voice_project`.

#### **Step 2: Save the Python Script**
1.  Copy the entire Python script.
2.  Open a basic text editor (like Notepad on Windows or TextEdit on macOS).
3.  Paste the code into the editor.
4.  Save the file as **`voice_processor.py`** inside the `voice_project` folder you just created.

#### **Step 3: Set Up the Command Line and Virtual Environment**
This is the most important technical step. It creates an isolated environment for the project.
1.  **Open a terminal** in your project folder.
    * **Windows**: Go into the `voice_project` folder, hold `Shift` and right-click the empty space, then select **"Open PowerShell window here"** or **"Open in Terminal"**.
    * **macOS/Linux**: Open the Terminal app, type `cd`, drag the `voice_project` folder onto the terminal window, and press **Enter**.
2.  **Create the virtual environment** by running this command:
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment**:
    * On **Windows**:
        ```cmd
        .\venv\Scripts\activate
        ```
    * On **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
    You will know it's working when you see **`(venv)`** at the start of your terminal prompt.
#### **Step 4: Install All Dependencies**
With the virtual environment active, install all the required Python packages.
1.  Run the main installation command:
    ```bash
    pip install speech_recognition pyaudio nltk spacy transformers torch python-docx
    ```
    This may take a few minutes.
2.  Next, download the required SpaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```
#### **Step 5: Run the Project**
Everything is now set up. You're ready to run the script.
1.  Make sure your terminal is in the `voice_project` directory and `(venv)` is visible.
2.  Run the script with this command:
    ```bash
    python voice_processor.py
    ```
3.  The program will start. Follow the on-screen prompts: speak your idea, then choose your desired output format.
#### **Step 6: Find Your Document**
Once the script finishes, go back to your `voice_project` folder. You will find a new file named **`output.docx`** containing your generated text.

