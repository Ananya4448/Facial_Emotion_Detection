# Facial Emotion Detection

A real-time facial emotion detection system using deep learning with TensorFlow/Keras and OpenCV. This project detects and classifies facial expressions into seven emotion categories: angry, disgust, fear, happy, neutral, sad, and surprise.

**Author:** AnanyaSaha

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Documentation Files

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete step-by-step setup instructions with troubleshooting
- **[DOWNLOADS.md](DOWNLOADS.md)** - Detailed guide for all required downloads and assets
- **[requirements.txt](requirements.txt)** - Python package dependencies
- **[.env.example](.env.example)** - Environment configuration template
- **[verify_setup.py](verify_setup.py)** - Automated setup verification script

---

## Quick Start

```bash
# 1. Clone and navigate to repository
git clone https://github.com/YourUsername/facial_emotion.git
cd facial_emotion

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download required assets
python download_assets.py

# 5. Verify installation
python verify_setup.py

# 6. Start Jupyter and run detection
jupyter notebook FinalDetection.ipynb
```

For detailed instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md).

---

## Features

- **Real-time Emotion Detection**: Detects emotions from webcam feed in real-time
- **7 Emotion Categories**: Classifies expressions into angry, disgust, fear, happy, neutral, sad, and surprise
- **Deep Learning Model**: Trained CNN model for accurate emotion classification
- **Face Detection**: Uses Haar Cascade for efficient face detection
- **Image Preprocessing**: Automated image augmentation and preprocessing pipeline
- **Jupyter Notebooks**: Interactive notebooks for training and testing

---

## Project Structure

```
facial_emotion/
├── Training/
│   └── images/
│       └── images/
│           └── train/
│               ├── angry/
│               ├── disgust/
│               ├── fear/
│               ├── happy/
│               ├── neutral/
│               ├── sad/
│               └── surprise/
├── Facedetection.ipynb          # Training notebook
├── FinalDetection.ipynb         # Real-time detection notebook
├── best_model.h5                # Trained model weights
├── haarcascade_frontalface_default.xml  # Face detection classifier
├── download_assets.py           # Script to download required files
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment configuration template
└── README.md                    # Project documentation
```

---

## Prerequisites

- Python 3.7 or higher
- Webcam (for real-time detection)
- CUDA-compatible GPU (optional, for faster training)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ananyasaha4448/facial_emotion.git
cd facial_emotion
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Required Assets

Run the download script to get the Haar Cascade classifier:

```bash
python download_assets.py
```

If you need to download a pre-trained model from a URL:

```bash
python download_assets.py --model-url YOUR_MODEL_URL
```

### 5. Configure Environment Variables

Copy the example environment file and configure as needed:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

---

## Dataset

The project uses the **FER-2013** (Facial Expression Recognition) dataset or similar emotion datasets. The training images should be organized in the following structure:

```
Training/images/images/train/
├── angry/
├── disgust/
├── fear/
├── happy/
├── neutral/
├── sad/
└── surprise/
```

Each folder should contain grayscale images (48x48 pixels) of faces expressing the corresponding emotion.

**Dataset Sources:**

- [FER-2013 on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)
- [Facial Expression Recognition Dataset](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge)

---

## Usage

### Training the Model

1. Open the training notebook:

   ```bash
   jupyter notebook Facedetection.ipynb
   ```

2. Run all cells to:
   - Load and preprocess the dataset
   - Build the CNN architecture
   - Train the model
   - Save the trained model as `best_model.h5`

### Real-time Emotion Detection

1. Open the detection notebook:

   ```bash
   jupyter notebook FinalDetection.ipynb
   ```

2. Run the cells to start webcam-based emotion detection

3. Press `q` to quit the detection window

**Or run directly from Python:**

```python
from keras.models import load_model
import cv2
import numpy as np
from keras.preprocessing.image import img_to_array

# Load the model
classifier = load_model('best_model.h5')
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)
# ... (emotion detection loop)
```

---

## Model Architecture

The model is a Convolutional Neural Network (CNN) with the following characteristics:

- **Input**: 48x48 grayscale images
- **Architecture**:
  - Multiple Conv2D layers with BatchNormalization
  - MaxPooling layers for downsampling
  - Dropout layers for regularization
  - Dense layers for classification
- **Output**: 7 emotion categories (softmax activation)
- **Optimizer**: Adam/SGD/RMSprop
- **Loss Function**: Categorical Crossentropy

---

## Results

The trained model achieves:

- **Validation Accuracy**: ~XX% (update with your results)
- **Training Accuracy**: ~XX% (update with your results)

**Emotion Categories Performance:**
| Emotion | Precision | Recall | F1-Score |
|-----------|-----------|--------|----------|
| Angry | - | - | - |
| Disgust | - | - | - |
| Fear | - | - | - |
| Happy | - | - | - |
| Neutral | - | - | - |
| Sad | - | - | - |
| Surprise | - | - | - |

_(Update these values after training)_

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- FER-2013 Dataset contributors
- OpenCV for face detection capabilities
- TensorFlow/Keras team for the deep learning framework
- The open-source community

---

## Contact

**AnanyaSaha**

- GitHub: [@AnanyaSaha](https://github.com/AnanyaSaha)
- Project Link: [https://github.com/ananyasaha4448/facial_emotion](https://github.com/ananyasaha4448/facial_emotion)

---

## 🐛 Troubleshooting

**Issue: Webcam not detected**

- Ensure your webcam is connected and not being used by another application
- Check camera permissions in your OS settings

**Issue: Model file not found**

- Run the training notebook first to generate `best_model.h5`
- Or download a pre-trained model using `download_assets.py --model-url <URL>`

**Issue: Import errors**

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version compatibility (3.7+)

**Issue: Low accuracy**

- Increase training epochs
- Add more training data
- Adjust model hyperparameters
- Use data augmentation techniques
