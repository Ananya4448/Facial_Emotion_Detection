# Downloads and Assets Guide

This document provides detailed information about all the required downloads and assets for the Facial Emotion Detection project.

---

## Required Downloads

### 1. Haar Cascade Classifier

**File:** `haarcascade_frontalface_default.xml`

**Purpose:** Face detection in images and video streams

**Download Options:**

#### Option A: Automatic Download (Recommended)

```bash
python download_assets.py
```

#### Option B: Manual Download

- **Direct Link:** [haarcascade_frontalface_default.xml](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml)
- **Source:** OpenCV GitHub Repository
- **Location:** Place in project root directory

**File Details:**

- Format: XML
- Size: ~900 KB
- Version: OpenCV 4.x compatible

---

### 2. Training Dataset

**Dataset:** FER-2013 (Facial Expression Recognition)

**Purpose:** Training and validation data for the emotion detection model

**Download Options:**

#### Option A: Kaggle (Recommended)

1. Create a Kaggle account at [kaggle.com](https://www.kaggle.com)
2. Download from: [FER-2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013)
3. Alternative: [FER Challenge](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge)

#### Option B: Kaggle API

```bash
# Install Kaggle CLI
pip install kaggle

# Download dataset
kaggle datasets download -d msambare/fer2013

# Unzip
unzip fer2013.zip -d Training/images/
```

**Dataset Details:**

- **Size:** ~300 MB (compressed)
- **Images:** 35,887 grayscale images
- **Resolution:** 48x48 pixels
- **Classes:** 7 emotions (angry, disgust, fear, happy, neutral, sad, surprise)
- **Format:** JPG/PNG

**Dataset Structure:**

```
Training/images/images/
├── train/
│   ├── angry/
│   ├── disgust/
│   ├── fear/
│   ├── happy/
│   ├── neutral/
│   ├── sad/
│   └── surprise/
└── validation/
    ├── angry/
    ├── disgust/
    ├── fear/
    ├── happy/
    ├── neutral/
    ├── sad/
    └── surprise/
```

---

### 3. Pre-trained Model (Optional)

**File:** `best_model.h5`

**Purpose:** Skip training and use pre-trained weights for immediate testing

**Download Options:**

#### Option A: Using download script

```bash
python download_assets.py --model-url <YOUR_MODEL_URL>
```

#### Option B: Google Drive

If the model is hosted on Google Drive:

1. Get the shareable link
2. Use `gdown` to download:

```bash
pip install gdown
gdown https://drive.google.com/uc?id=YOUR_FILE_ID
```

#### Option C: Train Your Own (Recommended)

Run the training notebook `Facedetection.ipynb` to generate your own model

**Model Details:**

- **Format:** HDF5 (.h5)
- **Size:** ~10-50 MB (depending on architecture)
- **Framework:** TensorFlow/Keras
- **Input Shape:** (48, 48, 1)
- **Output:** 7 classes

---

## Python Dependencies

**Install all dependencies:**

```bash
pip install -r requirements.txt
```

**Core Dependencies:**

- TensorFlow >= 2.9.0
- OpenCV >= 4.6.0
- NumPy >= 1.21.0
- Keras >= 2.9.0
- Matplotlib >= 3.4.3
- Pillow >= 8.3.0

**See `requirements.txt` for complete list**

---

## Additional Tools (Optional)

### 1. CUDA Toolkit (For GPU Acceleration)

**Purpose:** Faster model training using NVIDIA GPU

**Requirements:**

- NVIDIA GPU with CUDA Compute Capability >= 3.5
- CUDA Toolkit 11.2 or higher
- cuDNN 8.1 or higher

**Download:**

- [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
- [cuDNN](https://developer.nvidia.com/cudnn)

**Installation Guide:**

- [TensorFlow GPU Setup](https://www.tensorflow.org/install/gpu)

### 2. Kaggle API Credentials

**Purpose:** Automated dataset download from Kaggle

**Setup:**

1. Go to Kaggle.com → Account → API → Create New Token
2. Download `kaggle.json`
3. Place in:
   - Windows: `C:\Users\<YourUsername>\.kaggle\kaggle.json`
   - Linux/Mac: `~/.kaggle/kaggle.json`
4. Set permissions (Linux/Mac):
   ```bash
   chmod 600 ~/.kaggle/kaggle.json
   ```

---

## Download Verification Checklist

After downloading all required files, verify:

- [ ] `haarcascade_frontalface_default.xml` exists in project root
- [ ] Training dataset is extracted to `Training/images/`
- [ ] Dataset has 7 emotion folders with images
- [ ] `best_model.h5` exists (or you're ready to train)
- [ ] All pip dependencies installed (`pip list`)
- [ ] Python version is 3.7+ (`python --version`)
- [ ] Virtual environment is activated (recommended)

**Quick Verification Script:**

```python
import os

files_to_check = [
    'haarcascade_frontalface_default.xml',
    'best_model.h5',  # Optional if training from scratch
    'requirements.txt',
    'Facedetection.ipynb',
    'FinalDetection.ipynb'
]

for file in files_to_check:
    status = "✓" if os.path.exists(file) else "✗"
    print(f"{status} {file}")
```

---

## External Resources

### Datasets

- [FER-2013 Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)
- [AffectNet](http://mohammadmahoor.com/affectnet/)
- [RAF-DB](http://www.whdeng.cn/raf/model1.html)
- [CK+ Dataset](http://www.jeffcohn.net/Resources/)

### Pre-trained Models

- [Keras Model Zoo](https://keras.io/api/applications/)
- [TensorFlow Hub](https://www.tensorflow.org/hub)
- [Model Gardens](https://github.com/tensorflow/models)

### Haar Cascades

- [OpenCV Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- [Face Detection Models](https://github.com/opencv/opencv/tree/master/data)

---

## Quick Start Download Script

**Complete Setup:**

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download Haar Cascade
python download_assets.py

# Download dataset (requires Kaggle API setup)
kaggle datasets download -d msambare/fer2013
unzip fer2013.zip -d Training/images/

# Verify installation
python -c "import tensorflow as tf; import cv2; print('Setup complete!')"
```

---

## Download Troubleshooting

### Issue: Download fails / Timeout

**Solution:**

- Check internet connection
- Try manual download from browser
- Use download manager for large files
- Check firewall settings

### Issue: Kaggle API not working

**Solution:**

- Verify `kaggle.json` is in correct location
- Check file permissions (Linux/Mac)
- Ensure Kaggle account is verified
- Accept competition/dataset rules on Kaggle website

### Issue: Model file corrupted

**Solution:**

- Re-download the file
- Verify file size matches expected size
- Check MD5/SHA hash if provided
- Train a new model using the notebook

### Issue: Dataset extraction fails

**Solution:**

- Ensure sufficient disk space (~2-3 GB)
- Use appropriate extraction tool
- Check file integrity
- Download in smaller chunks if available

---

## Support

For download issues or questions:

- Open an issue on GitHub
- Check existing issues for solutions
- Contact: [Your Email/Support Channel]

---

**Last Updated:** May 9, 2026
