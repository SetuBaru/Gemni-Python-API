# Gemni-Python-API
<img width="1600" alt="Screenshot 2023-12-14 at 04 46 39" src="https://github.com/SetuBaru/Gemni-Python-API/assets/78774159/d77d5160-30a6-4694-be2b-c7dc9918ea41">

## An Unofficial Wrapper for the Gemini API's python SDK

### This repository demonstrates using Google's GenerativeAI (GenAI) API with the Gemini Pro model to generate content based on prompts.
<br><br>

## Getting Started

### Prerequisites

- Python 3.9+ installed
- Access to the Google GenerativeAI API
- API key stored in a `.env` file
<br>

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SetuBaru/Gemni-Python-API.git
   cd your_repository
   ```
   
2. Install the Gemni Python SDK
  ```bash
  pip install -q -U google-generativeai
  ```

3. Install python-dotenv

```bash
pip install python-dotenv
```

4. Get your API key from
  ```bash
 https://makersuite.google.com/app/apikey
```

5. Add your key to the .venv files GOOGLE_API_KEY VARIABLE
   ```bash
   GOOGLE_API_KEY=[PUT YOUR API KEY HERE]
   ```
6. Run the main.py file
   
  <img width="476" alt="Screenshot 2023-12-14 at 05 24 02" src="https://github.com/SetuBaru/Gemni-Python-API/assets/78774159/00dd790c-e685-4355-ae95-1d57c055b20e">

<br>

#### Special thanks to the people at https://ai.google.dev/tutorials/python_quickstart for their guidance! This project is mostly based of their implementation!
