# 🚀 Quick Setup Guide

Complete installation guide for the Facial Emotion Detection project.

---

## ⏱️ Estimated Setup Time

- **Basic Setup:** 10-15 minutes
- **With Dataset Download:** 30-45 minutes
- **Full Training:** 2-4 hours (depending on hardware)

---

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.7 or higher installed ([Download Python](https://www.python.org/downloads/))
- [ ] Git installed ([Download Git](https://git-scm.com/downloads))
- [ ] 5+ GB free disk space
- [ ] Webcam (for real-time detection)
- [ ] Internet connection (for downloads)
- [ ] (Optional) NVIDIA GPU with CUDA support

**Verify Python Installation:**

```bash
python --version
# or
python3 --version
```

---

## 🔧 Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/YourUsername/facial_emotion.git
cd facial_emotion
```

### Step 2: Create Virtual Environment

**Why?** Isolates project dependencies from system Python packages.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify activation:** Your terminal prompt should show `(venv)`

### Step 3: Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**This will install:**

- TensorFlow (Deep Learning)
- OpenCV (Computer Vision)
- NumPy, Pandas (Data Processing)
- Matplotlib, Seaborn (Visualization)
- Jupyter (Interactive Notebooks)
- And more...

**Installation may take 5-10 minutes**

### Step 5: Download Required Assets

**Download Haar Cascade:**

```bash
python download_assets.py
```

This downloads the face detection classifier (~900 KB).

### Step 6: Setup Environment File

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

**Edit `.env` file** if you need to customize paths or settings.

### Step 7: Download Training Dataset

**Option A: Kaggle API (Recommended)**

1. Setup Kaggle API credentials:
   - Go to [kaggle.com](https://www.kaggle.com) → Account → API
   - Click "Create New API Token"
   - Save `kaggle.json` to:
     - Windows: `C:\Users\YourName\.kaggle\`
     - Linux/Mac: `~/.kaggle/`

2. Download dataset:

```bash
pip install kaggle
kaggle datasets download -d msambare/fer2013
```

3. Extract:

```bash
# Windows (PowerShell)
Expand-Archive fer2013.zip -DestinationPath Training/images/

# Linux/Mac
unzip fer2013.zip -d Training/images/
```

**Option B: Manual Download**

1. Visit [FER-2013 on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)
2. Click "Download" button
3. Extract to `Training/images/` folder
4. Ensure folder structure matches:
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

---

## ✅ Verify Installation

Run this verification script:

```python
# verify_setup.py
import sys
import os

def check_python_version():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print("✓ Python version:", sys.version.split()[0])
        return True
    else:
        print("✗ Python 3.7+ required")
        return False

def check_imports():
    packages = {
        'tensorflow': 'TensorFlow',
        'cv2': 'OpenCV',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'keras': 'Keras',
        'PIL': 'Pillow'
    }

    all_good = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name} installed")
        except ImportError:
            print(f"✗ {name} not found")
            all_good = False
    return all_good

def check_files():
    required_files = [
        'haarcascade_frontalface_default.xml',
        'requirements.txt',
        'Facedetection.ipynb',
        'FinalDetection.ipynb',
        '.env.example'
    ]

    all_good = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} not found")
            all_good = False
    return all_good

def check_dataset():
    train_path = 'Training/images/images/train'
    emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    if not os.path.exists(train_path):
        print(f"⚠ Dataset not found at {train_path}")
        print("  Run: kaggle datasets download -d msambare/fer2013")
        return False

    all_good = True
    for emotion in emotions:
        emotion_path = os.path.join(train_path, emotion)
        if os.path.exists(emotion_path):
            count = len(os.listdir(emotion_path))
            print(f"✓ {emotion}: {count} images")
        else:
            print(f"✗ {emotion} folder not found")
            all_good = False
    return all_good

if __name__ == '__main__':
    print("\n=== Facial Emotion Detection - Setup Verification ===\n")

    print("📌 Checking Python version...")
    py_ok = check_python_version()

    print("\n📦 Checking installed packages...")
    pkg_ok = check_imports()

    print("\n📁 Checking required files...")
    files_ok = check_files()

    print("\n📊 Checking dataset...")
    data_ok = check_dataset()

    print("\n" + "="*50)
    if py_ok and pkg_ok and files_ok:
        print("✅ Setup complete! Ready to train.")
        if not data_ok:
            print("⚠  Dataset not found - download before training")
    else:
        print("❌ Setup incomplete - fix issues above")
    print("="*50)
```

**Run verification:**

```bash
python verify_setup.py
```

---

## 🎓 Quick Start Tutorial

### Option 1: Use Pre-trained Model (Fast)

1. Download pre-trained model (if available):

```bash
python download_assets.py --model-url <MODEL_URL>
```

2. Open detection notebook:

```bash
jupyter notebook FinalDetection.ipynb
```

3. Run all cells (Shift+Enter)
4. Press 'q' to quit camera view

### Option 2: Train Your Own Model

1. Open training notebook:

```bash
jupyter notebook Facedetection.ipynb
```

2. Run cells sequentially:
   - Import libraries
   - Load dataset
   - Visualize data
   - Build model
   - Train model (this takes 1-3 hours)
   - Save model

3. Model will be saved as `best_model.h5`

4. Then use Option 1 for detection

---

## 🎯 Next Steps

After successful setup:

1. **Explore the notebooks:**
   - `Facedetection.ipynb` - Training pipeline
   - `FinalDetection.ipynb` - Real-time detection

2. **Customize the model:**
   - Adjust hyperparameters in `.env`
   - Modify model architecture
   - Experiment with data augmentation

3. **Test with your own images:**
   - Place images in a test folder
   - Modify detection script

4. **Deploy the model:**
   - Create Flask/FastAPI endpoint
   - Build a web interface
   - Mobile app integration

---

## 🐛 Common Issues & Solutions

### Issue 1: "ModuleNotFoundError: No module named 'tensorflow'"

**Solution:**

```bash
pip install tensorflow
```

### Issue 2: "Could not find haarcascade file"

**Solution:**

```bash
python download_assets.py
```

### Issue 3: "Camera not detected"

**Solution:**

- Check if camera is connected
- Try different camera index in code: `cv2.VideoCapture(1)`
- Grant camera permissions in OS settings

### Issue 4: "Out of memory during training"

**Solution:**

- Reduce batch size in `.env`: `BATCH_SIZE=64` or `32`
- Close other applications
- Use data generators instead of loading all data

### Issue 5: "ImportError: DLL load failed" (Windows)

**Solution:**

```bash
pip uninstall opencv-python
pip install opencv-python-headless
```

### Issue 6: Virtual environment issues

**Solution:**

```bash
# Deactivate current environment
deactivate

# Delete and recreate
rm -rf venv  # or rmdir /s venv on Windows
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
```

---

## 💡 Performance Tips

### For Training:

- Use GPU if available (40-50x faster)
- Start with fewer epochs to test
- Use data augmentation for better accuracy
- Monitor training with TensorBoard

### For Detection:

- Reduce camera resolution for faster FPS
- Use threading for parallel processing
- Optimize face detection parameters
- Consider using lighter models (MobileNet)

---

## 📚 Additional Resources

- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Keras Guide](https://keras.io/guides/)
- [FER-2013 Paper](https://arxiv.org/abs/1307.0414)

---

## 🆘 Getting Help

If you encounter issues:

1. **Check Documentation:**
   - README.md
   - DOWNLOADS.md
   - This guide

2. **Search Existing Issues:**
   - GitHub Issues tab
   - Stack Overflow

3. **Ask for Help:**
   - Open a new GitHub issue
   - Provide error messages
   - Include system info

---

## ✅ Setup Complete!

You're now ready to:

- ✨ Train emotion detection models
- 🎥 Detect emotions in real-time
- 🔬 Experiment with different architectures
- 🚀 Deploy your own applications

**Happy coding! 🎉**

---

**Last Updated:** May 9, 2026
