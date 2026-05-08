#!/usr/bin/env python3
"""
Setup Verification Script for Facial Emotion Detection Project

This script verifies that all required dependencies, files, and datasets
are properly installed and configured.

Usage:
    python verify_setup.py [--verbose]
"""

import sys
import os
from pathlib import Path

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print a formatted header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print("=" * 60)

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓{Colors.END} {text}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗{Colors.END} {text}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠{Colors.END} {text}")

def check_python_version():
    """Check if Python version meets requirements"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 7:
        print_success(f"Python version: {version_str}")
        return True
    else:
        print_error(f"Python {version_str} found, but 3.7+ required")
        return False

def check_package_imports():
    """Check if required Python packages are installed"""
    print_header("Checking Required Packages")
    
    packages = {
        'tensorflow': 'TensorFlow',
        'cv2': 'OpenCV',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'keras': 'Keras',
        'PIL': 'Pillow',
        'pandas': 'Pandas',
        'seaborn': 'Seaborn',
        'sklearn': 'Scikit-learn',
        'h5py': 'H5Py',
        'requests': 'Requests'
    }
    
    all_installed = True
    for package, name in packages.items():
        try:
            mod = __import__(package)
            version = getattr(mod, '__version__', 'unknown')
            print_success(f"{name:15} - version {version}")
        except ImportError:
            print_error(f"{name:15} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_required_files():
    """Check if required project files exist"""
    print_header("Checking Required Files")
    
    required_files = [
        'haarcascade_frontalface_default.xml',
        'requirements.txt',
        'Facedetection.ipynb',
        'FinalDetection.ipynb',
        '.env.example',
        'download_assets.py',
        'README.md',
        'DOWNLOADS.md',
        'SETUP_GUIDE.md'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            size_kb = size / 1024
            print_success(f"{file:40} ({size_kb:.1f} KB)")
        else:
            print_error(f"{file:40} - NOT FOUND")
            all_exist = False
    
    return all_exist

def check_optional_files():
    """Check for optional files"""
    print_header("Checking Optional Files")
    
    optional_files = {
        'best_model.h5': 'Trained model (needed for detection)',
        '.env': 'Environment configuration',
        '.gitignore': 'Git ignore file'
    }
    
    for file, description in optional_files.items():
        if os.path.exists(file):
            size = os.path.getsize(file)
            size_mb = size / (1024 * 1024)
            print_success(f"{file:20} - {description} ({size_mb:.2f} MB)")
        else:
            print_warning(f"{file:20} - {description} - NOT FOUND")

def check_dataset():
    """Check if training dataset exists and is properly structured"""
    print_header("Checking Training Dataset")
    
    train_path = Path('Training/images/images/train')
    emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    
    if not train_path.exists():
        print_error(f"Dataset not found at {train_path}")
        print_warning("Download with: kaggle datasets download -d msambare/fer2013")
        return False
    
    all_found = True
    total_images = 0
    
    for emotion in emotions:
        emotion_path = train_path / emotion
        if emotion_path.exists():
            images = list(emotion_path.glob('*.jpg')) + list(emotion_path.glob('*.png'))
            count = len(images)
            total_images += count
            print_success(f"{emotion:10} - {count:5} images")
        else:
            print_error(f"{emotion:10} - folder not found")
            all_found = False
    
    if all_found:
        print(f"\n{Colors.BOLD}Total training images: {total_images}{Colors.END}")
    
    # Check validation set
    val_path = Path('Training/images/images/validation')
    if val_path.exists():
        print_success(f"\nValidation dataset found")
    else:
        print_warning(f"\nValidation dataset not found (optional)")
    
    return all_found

def check_webcam():
    """Check if webcam is accessible"""
    print_header("Checking Webcam Access")
    
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                height, width = frame.shape[:2]
                print_success(f"Webcam detected - Resolution: {width}x{height}")
                cap.release()
                return True
            else:
                print_error("Webcam detected but cannot read frames")
                cap.release()
                return False
        else:
            print_error("Cannot open webcam (index 0)")
            print_warning("Try different camera index or check permissions")
            return False
    except Exception as e:
        print_error(f"Error accessing webcam: {e}")
        return False

def check_gpu_availability():
    """Check if GPU is available for TensorFlow"""
    print_header("Checking GPU Availability")
    
    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices('GPU')
        
        if gpus:
            print_success(f"GPU(s) detected: {len(gpus)}")
            for i, gpu in enumerate(gpus):
                print(f"  GPU {i}: {gpu.name}")
            return True
        else:
            print_warning("No GPU detected - will use CPU (slower training)")
            return False
    except Exception as e:
        print_error(f"Error checking GPU: {e}")
        return False

def check_disk_space():
    """Check available disk space"""
    print_header("Checking Disk Space")
    
    try:
        import shutil
        total, used, free = shutil.disk_usage(".")
        
        free_gb = free / (1024**3)
        total_gb = total / (1024**3)
        
        if free_gb > 5:
            print_success(f"Free space: {free_gb:.2f} GB / {total_gb:.2f} GB")
            return True
        elif free_gb > 2:
            print_warning(f"Low disk space: {free_gb:.2f} GB (recommend 5+ GB)")
            return True
        else:
            print_error(f"Insufficient disk space: {free_gb:.2f} GB (need 5+ GB)")
            return False
    except Exception as e:
        print_warning(f"Could not check disk space: {e}")
        return True

def test_model_loading():
    """Test if model can be loaded"""
    print_header("Testing Model Loading")
    
    if not os.path.exists('best_model.h5'):
        print_warning("best_model.h5 not found - skipping model load test")
        print_warning("Train model using Facedetection.ipynb first")
        return True
    
    try:
        from keras.models import load_model
        model = load_model('best_model.h5')
        print_success("Model loaded successfully")
        print(f"  Input shape: {model.input_shape}")
        print(f"  Output shape: {model.output_shape}")
        return True
    except Exception as e:
        print_error(f"Error loading model: {e}")
        return False

def generate_summary(results):
    """Generate and print summary of verification"""
    print_header("Verification Summary")
    
    total = len(results)
    passed = sum(results.values())
    failed = total - passed
    
    print(f"\n{Colors.BOLD}Total Checks: {total}{Colors.END}")
    print(f"{Colors.GREEN}Passed: {passed}{Colors.END}")
    print(f"{Colors.RED}Failed: {failed}{Colors.END}")
    
    percentage = (passed / total) * 100
    
    print("\n" + "="*60)
    if percentage == 100:
        print(f"{Colors.GREEN}{Colors.BOLD}✅ ALL CHECKS PASSED!{Colors.END}")
        print(f"{Colors.GREEN}Your setup is complete and ready to use!{Colors.END}")
    elif percentage >= 75:
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠ SETUP MOSTLY COMPLETE{Colors.END}")
        print(f"{Colors.YELLOW}Some optional components missing - review above{Colors.END}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}❌ SETUP INCOMPLETE{Colors.END}")
        print(f"{Colors.RED}Please fix the errors listed above{Colors.END}")
    print("="*60 + "\n")
    
    # Provide next steps
    if not results.get('model', False):
        print("📝 Next step: Train the model using Facedetection.ipynb")
    else:
        print("🚀 Next step: Run FinalDetection.ipynb for real-time detection")

def main():
    """Main verification function"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   FACIAL EMOTION DETECTION - SETUP VERIFICATION          ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}")
    
    results = {}
    
    # Run all checks
    results['python'] = check_python_version()
    results['packages'] = check_package_imports()
    results['files'] = check_required_files()
    check_optional_files()  # Not counted in results
    results['dataset'] = check_dataset()
    results['webcam'] = check_webcam()
    results['gpu'] = check_gpu_availability()  # Not critical
    results['disk'] = check_disk_space()
    results['model'] = test_model_loading()  # Optional
    
    # Generate summary
    generate_summary(results)
    
    return all(results.values())

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Verification interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
