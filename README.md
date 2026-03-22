# 😇Aura Scanner
 - Aura Scanner is an AI-powered chatbot that allows users to explore the public digital footprint of a professional using LinkedIn (and optionally Twitter) data.  
 - The system uses browser automation + RAG (Retrieval-Augmented Generation) to provide accurate, context-aware answers.

## ✨Demo Video
 https://youtu.be/rhfow0AsuP4

## 🔗Aura Scanner's Live Link
 - Currently not live on cloud as Aura Scanner uses Browser Automation(due to API Restrictions)

## 🧲Tech Stack
 - Python (Flask) for core feature implementation.
 - Selenium to do browser automation for LinkedIn scraping. (twitter optional)
 - LangChain for text processing & chunking.
 - FAISS as vector database.
 - Used llama-3.3-70b-versatile model via Groq API.
 - HTML, CSS, JavaScript for frontend.

## 🚀Workflow
 1. Input LinkedIn profile URL(twitter handle optional).
 2. Click "Load Button"
 3. Selenium will scrap and will request to login to linkedin account.
 4. Once the data is fetched, you can ask questions using chatbot.

## 🌀 Features

- AI chatbot powered by Groq LLM  
- Retrieval-Augmented Generation (RAG) for accurate, data-grounded answers  
- Multi-turn conversation (chat memory for context-aware responses)  

- LinkedIn Data Extraction via Browser Automation
  - Profile information (headline, experience, education, skills)
  - Real-time scraping using Selenium

- Posts & Comments Analysis
  - Fetches recent LinkedIn posts from activity feed  
  - Extracts comments made by the user  
  - Distinguishes between original posts and comments to avoid misclassification  
  - Enables deeper insights into user interests and engagement  

- Activity-Based Insights
  - Identifies topics the user posts about  
  - Analyzes engagement patterns through comments  
  - Generates intelligent summaries from combined activity  

- Clean UI/UX
  - Dark / Light mode toggle  
  - Chat-style interface  
  - Loader for async operations  

- Real-time Processing
  - Live scraping + instant AI responses  

- Error Handling
  - Invalid LinkedIn URLs  
  - Private or inaccessible profiles  
  - Missing or limited data scenarios  

- Advanced Scraping Logic
  - Implements smart scrolling to handle LinkedIn’s lazy loading  
  - Ensures consistent and complete activity extraction  

## 🌊Setup

1. Clone / Download repo into your local machine.

2. Install dependencies using command:
```bash
pip install -r requirements.txt
```

3. Create `.env` file the root folder and add your Groq API credentials.
```bash
GROQ_API_KEY=your_api_key
```

5. Run the python app.py using.
```bash
python app.py
```
