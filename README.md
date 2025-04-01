# 🤖 Next-Gen AI Chatbot

A modern web-based chatbot application powered by Google's Gemini 1.5 Pro API, featuring customizable AI personalities.

## ✨ Features

- **🎨 Multiple AI Personalities:** Choose from 25+ pre-configured personality options across different categories:
  - 🎭 Tech Innovators (Steve Jobs, Elon Musk, etc.)
  - 👨‍🎓 Scientists & Thinkers (Einstein, Tesla, etc.)
  - 🇺🇸 World Leaders (Lincoln, Churchill, etc.)
  - 🎮 Fictional Characters (Sherlock Holmes, Yoda, etc.)
  - 🎬 Celebrities & Artists (Shakespeare, Morgan Freeman, etc.)
- **💀 Custom Personalities:** Define your own unique AI personality
- **💡 Modern UI:** Sleek, responsive dark-themed interface with animations
- **⏳ Real-time Interaction:** Immediate AI responses with typing indicators

## 🛠️ Tech Stack

- **💪 Backend:** Flask (Python)
- **💡 Frontend:** HTML, CSS, JavaScript
- **🔮 AI Model:** Google Gemini 1.5 Pro

### 🔧 Prerequisites

- 📝 Python 3.8+
- ✨ Any AI API key

### 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/next-gen-ai-chatbot.git
   cd next-gen-ai-chatbot
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
    Modify the `.env` file in the project root with:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### 🌐 Running the Application

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/` by default.

## 📚 Usage

1. When you open the app, you'll see the personality selection screen
2. Either:
   - Choose a pre-configured personality from the available categories
   - Enter a custom personality description and click "Set Custom Personality"
3. Once a personality is selected, the chat interface will appear
4. Type your message and press Enter or click Send
5. The AI will respond according to the chosen personality

## 📂 Project Structure

```
AIChatBot/
├── app.py              # Flask application main file
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not included in repo)
└── templates/
    └── index.html      # Frontend interface
```

## 🎨 Customization

### 👩‍🔧 Adding New Personalities

Add new personality buttons to `index.html` by following the existing pattern:

```html
<button class="personality-btn" data-value="Personality Name, key traits">
    <span class="personality-name">Personality Name</span>
    <span class="personality-desc">Key traits</span>
</button>
```

### 🌈 Modifying the UI

The UI is styled using custom CSS variables in the `:root` selector. Modify these to change the color scheme:

```css
:root {
    --primary-color: #8B5CF6;  /* Main accent color */
    --bg-dark: #0F0F0F;        /* Background color */
    --bg-darker: #1A1A1A;      /* Secondary background */
    --text-primary: #FFFFFF;   /* Main text color */
    --text-secondary: #A0AEC0; /* Secondary text color */
}
```

## 📞 Acknowledgements

- [🔮 Google Generative AI](https://ai.google/discover/generative-ai/) for the Gemini API
- [📝 Flask](https://flask.palletsprojects.com/) for the web framework
- All the personalities that inspired this project
