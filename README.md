# ME-Chatbot
MockExam Chatbot is an AI-powered assistant designed to help students prepare for the Institute of Technology of Cambodia (ITC) entrance exam. It provides answers to common questions about exam preparation, subjects, and scholarships using a trained NLP model.

## Features
- Answer student queries about ITC exams, subjects, and scholarships
- AI-powered response generation based on trained data
- NLP-based question matching using vectorization
- Easy integration with a frontend and backend (NestJS)

## File Structure
```
mockexam-chatbot/
│── ai-model/                   # AI Model for training and inference
│   ├── src/
│   │   ├── train.py            # Training script for chatbot model
│   │   ├── inference.py        # Handles chatbot responses
│   │   ├── preprocess.py       # Text preprocessing functions
│   │   ├── vetorize.py         # Convert text to numerical data
│   │   ├── server.py           # Connect the between inference.py to backend
│   ├── data/
│   │   ├── intents.json        # Training data (questions and responses)
│   ├── model/
│   │   ├── label_map.pkl       # Mapped labels
│   │   ├── model.pkl           # Saved trained model
│   │   ├── responses.pkl       # Saved responses
│   │   ├── vectorizer.pkl      # TF-IDF vectorizer
│   ├── requirements.txt        # Python dependencies
│
│── backend/                    # Backend using NestJS
│   ├── src/
│   ├── ├── chatbot/
│   │   │   ├── chatbot.controller.ts   # Handle the chatbot endpoint
│   │   │   ├── chatbot.module.ts       # verify the the controllers and providers 
│   │   │   ├── chatbot.service.ts      # Handle the logic
│   │   ├── main.ts             # Main server file
│   │   ├── app.controller.ts   # API endpoint
│   │   ├── app.service.ts      # Handles logic
│   │   ├── app.module.ts       # Handles chatbot
│   ├── package.json            # Backend dependencies
│
│── frontend/                   # Frontend for user interaction
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── App.js              # Main React app file
│   │   ├── components/         # UI components
│   │   ├── pages/              # Homepage components
│   ├── package.json            # Frontend dependencies
│   ├── src/
│
│── .gitignore                   # Git ignored files
│── README.md                    # Project documentation
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
Gmail: [mailto:]("chantharith77@gmail.com")