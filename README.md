# COVICO System 🌟  
**COmputer VIsion COntrol System**  

A touch-free, gesture-based system that leverages computer vision to control presentations seamlessly. Navigate slides, annotate, and interact effortlessly using hand gestures.

---

## Features ✨  

- **Gesture-Based Slide Navigation**:  
  - Swipe right to move to the next slide.  
  - Swipe left to go back to the previous slide.  

- **Annotation Capabilities**:  
  - Point to specific areas using gestures.  
  - Draw annotations on slides.  
  - Erase annotations when needed.  

- **Webcam Feed Overlay**:  
  - Integrates a live webcam feed within your presentation for a dynamic, interactive experience.  

- **Touch-Free Interface**:  
  - No need for remotes or keyboards — control everything with your hands!  

---

## Demo 🎥  

![Demo](path-to-demo-gif-or-screenshot)  

---

## Installation 🛠️  

### Prerequisites  
- Python 3.8 or later  
- A working webcam  

### Steps  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/rajeshkumar-niet/COVICO
   cd COVICO-System  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Add Your Presentation Images**:  
   - Place the images of your slides (in `.jpg` or `.png` format) inside the `PPT/img` folder.  

4. **Run the Application**:  
   ```bash  
   python main.py  
   ```  

---

## Usage 🚀  

1. **Prepare Slides**:  
   - Add slides (as images) to the `PPT/img` folder.  

2. **Start the Program**:  
   - Run the application and ensure your webcam is active.  

3. **Gesture Controls**:  
   - Control the slides and annotate them with predefined gestures (see below).  

4. **Exit**:  
   - Press the `q` key to exit the application.  

---

## Gesture Controls 🕹️  

| Gesture                   | Action                     |  
|---------------------------|----------------------------|  
| Thumb Up                  | Previous slide            |  
| Pinky Up                  | Next slide                |  
| Index Finger Up           | Pointer mode              |  
| Index + Middle Fingers Up | Draw annotations          |  
| Three Fingers Up          | Erase annotations         |  

---

## File Structure 📂  

```
COVICO-System/  
├── PPT/  
│   └── img/               # Folder for storing presentation images  
├── main.py                # Main application script  
├── requirements.txt       # Python dependencies  
└── README.md              # Project documentation  
```  

---

## Requirements 📋  

- **Python Libraries**:  
  - `OpenCV` (`cv2`)  
  - `numpy`  
  - `cvzone`  

Install all dependencies via:  
```bash  
pip install -r requirements.txt  
```  

---

## Future Enhancements 🛠️  

- **Slide Import from Files**: Add support for `.pptx` and `.pdf` files.  
- **Save and Load Annotations**: Store annotations to resume later.  
- **Voice Commands**: Integrate voice control for a hybrid interface.  
- **Custom Gestures**: Allow users to define their own gestures.  

---

## Contributing 🤝  

Contributions are welcome! If you'd like to contribute:  
1. Fork the repository.  
2. Create a new branch for your feature/bug fix.  
3. Submit a pull request.  

---

## License 📜  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## Acknowledgments 🙌  

- **OpenCV**: For robust computer vision tools.  
- **cvzone**: For simplified hand-tracking modules.  
