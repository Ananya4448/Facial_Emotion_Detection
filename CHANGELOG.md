# Changelog

All notable changes to the Facial Emotion Detection project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features

- [ ] Web-based user interface for emotion detection
- [ ] REST API for model inference
- [ ] Support for video file input (not just webcam)
- [ ] Multi-face detection in single frame
- [ ] Export detection results to CSV/JSON
- [ ] Model ensemble for improved accuracy
- [ ] Mobile app integration
- [ ] Real-time emotion statistics dashboard
- [ ] Support for additional emotion datasets
- [ ] Model quantization for faster inference

---

## [1.0.0] - 2026-05-09

### Added

- Initial release of Facial Emotion Detection project
- CNN model for 7 emotion classification (angry, disgust, fear, happy, neutral, sad, surprise)
- Real-time webcam-based emotion detection
- Training pipeline in Jupyter notebook (`Facedetection.ipynb`)
- Detection pipeline in Jupyter notebook (`FinalDetection.ipynb`)
- Haar Cascade face detection integration
- Automated asset download script (`download_assets.py`)
- Comprehensive documentation:
  - `README.md` - Project overview and documentation
  - `SETUP_GUIDE.md` - Step-by-step installation guide
  - `DOWNLOADS.md` - Assets and dataset download guide
  - `CHANGELOG.md` - Project version history
- Environment configuration template (`.env.example`)
- Setup verification script (`verify_setup.py`)
- Project `.gitignore` file
- MIT License

### Dataset

- Support for FER-2013 dataset
- Training/validation data structure
- Image preprocessing and augmentation pipeline

### Model Features

- 48x48 grayscale image input
- Convolutional Neural Network architecture
- Batch normalization and dropout for regularization
- Model checkpointing and best model saving
- Configurable hyperparameters via environment variables

### Dependencies

- TensorFlow >= 2.9.0
- OpenCV >= 4.6.0
- Keras >= 2.9.0
- NumPy, Pandas, Matplotlib, Seaborn
- Jupyter Notebook support
- Python 3.7+ compatible

---

## Version History Summary

- **v1.0.0** (2026-05-09) - Initial release with core functionality

---

## Contributing

When contributing to this project, please update this CHANGELOG.md file with your changes under the [Unreleased] section. Follow these guidelines:

### Categories for Changes

- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Vulnerability fixes

### Example Entry

```markdown
## [1.1.0] - 2026-XX-XX

### Added

- Feature description here

### Fixed

- Bug fix description here
```

---

**Note:** Dates are in YYYY-MM-DD format.
