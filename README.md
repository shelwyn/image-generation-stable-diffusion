# Cyberpunk Themed Image Generator 🎨

A modern web application that generates images using Stable Diffusion with a cyberpunk-themed UI. Built with FastAPI, Hugging Face's Inference API, and modern web technologies.

![Project Demo](demo.gif)

## ✨ Features

- Image generation using Stable Diffusion (runwayml/stable-diffusion-v1-5)
- Real-time chat-like interface with animated typing indicators
- Cyberpunk-themed UI with neon effects and animations
- Download capability for generated images
- Responsive design for all devices
- FastAPI backend for efficient image generation

## 🛠️ Technologies Used

- **Backend**:
  - FastAPI
  - Python 3.8+
  - Hugging Face Inference API
  - Python-dotenv
  - Pillow

- **Frontend**:
  - HTML5
  - CSS3
  - Vanilla JavaScript
  - Anime.js for animations

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher installed
- A Hugging Face account and API token
- Node.js and npm (optional, for development)

## 🔧 Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/shelwyn/image-generation-stable-diffusion.git
cd image-generation-stable-diffusion
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```plaintext
HF_TOKEN=your_huggingface_token_here
```

5. Create the images directory:
```bash
mkdir generated_images
```

## 🚀 Running the Application

1. Start the FastAPI server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

2. Running the Frontend Server
```bash
python -m http.server 3000
```

The application will be running at:
- Backend: `http://localhost:8000`
- Frontend: Open `http://localhost:3000/index.html` directly in your browser

## 📁 Project Structure

```
image-generation-stable-diffusion/
├── main.py                # FastAPI backend
├── index.html            # Frontend interface
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables
├── generated_images/    # Directory for generated images
├── README.md           # Documentation
└── .gitignore         # Git ignore file
```

## 🔑 API Endpoints

- `POST /generate-image`
  - Generates an image from a text prompt
  - Request body: `{"prompt": "string"}`
  - Returns: `{"filename": "string"}`

- `GET /images/{filename}`
  - Retrieves a generated image
  - Returns: Image file

- `GET /health`
  - Health check endpoint
  - Returns: `{"status": "healthy"}`

## 🛡️ Environment Variables

The following environment variables are required:

- `HF_TOKEN`: Your Hugging Face API token

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Stable Diffusion model
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing backend framework
- [Anime.js](https://animejs.com/) for smooth animations
