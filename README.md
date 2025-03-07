# ME-Chatbot
MockExam Chatbot is an AI-powered assistant designed to help students prepare for the Institute of Technology of Cambodia (ITC) entrance exam. It provides answers to common questions about exam preparation, subjects, and scholarships using a trained NLP model.

## Features
- Answer student queries about ITC exams, subjects, and scholarships
- AI-powered response generation based on trained data
- NLP-based question matching using vectorization
- Easy integration with a frontend and backend (NestJS)

## File Structure
```
ME-Chatbot/
│── backend/                    # NestJS Backend (API)
│   ├── src/
│   │   ├── chatbot/
│   │   │   ├── chatbot.module.ts       # NestJS Module
│   │   │   ├── chatbot.controller.ts   # API Endpoint
│   │   │   ├── chatbot.service.ts      # Calls Python inference API
│   │   ├── main.ts                     # Entry Point for NestJS
│   ├── .env                            # API Configs (Python Server URL)
│   ├── package.json                     # Dependencies
│   ├── tsconfig.json                    # TypeScript Config
│── ai-model/                    # Python Chatbot (Training & Response)
│   ├── train.py                 # Train chatbot with PDF data
│   ├── inference.py             # Process user queries & return responses
│   ├── server.py                # Flask/FastAPI server to serve responses
│   ├── model/                    # Folder to store trained model
│   ├── data/
│   │   ├── raw_pdfs/             # Store original PDFs
│   │   ├── processed/            # Store processed text from PDFs
│   ├── requirements.txt           # Python Dependencies
│── frontend/                      # Chatbot UI (React/Vue)
│   ├── src/
│   │   ├── components/            # UI Components
│   │   ├── services/api.js        # Calls NestJS API
│   ├── package.json               # Frontend Dependencies
│── README.md                      # Documentation
```

## Installation & Setup
1. **Clone the Repository**
```
git clone https://github.com/chantharith-NY/ME-Chatbot.git
cd mockexam-chatbot
```

2. **Set Up the AI Model**
```
cd ai-model
python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

3. **Run the Preprocess**
```
python src/preprocess.py
```

4. **Run the Chatbot**
```
python src/inference.py
```

5. **Run the Server**
```
python src/server.py
```

## API Integration
Once the AI model is running, you can integrate it with a NestJS backend.
1. **Start the NestJS Backend**
```
cd backend
npm install
yarn run start
```

2. **Start the React Frontend**
```
npm start
```

## Technologies Used
- Python (NLP processing)
- NLTK (Text preprocessing)
- Scikit-learn (Vectorization & model training)
- NestJS (Backend API)
- React.js (Frontend interface)

## Future Improvements
- Improve response accuracy with deep learning (transformers)
- Add multilingual support (Khmer & English)
- Deploy chatbot as a web service

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the **MIT License**.

## Contact ME
Gmail: "chantharith77@gmail.com"