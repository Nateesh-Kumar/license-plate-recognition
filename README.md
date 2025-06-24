# 🚗 License Plate Detection & Recognition

This project performs automatic license plate detection using **YOLOv8** and character recognition using a **CRNN + CTC Loss** pipeline. The goal is to identify license plates from car images and extract the first 7 digits, which are then formatted into a one-hot encoded submission format.

---

## 📁 Project Structure

📦 project/

├── License_Plate_Recognition_Nateesh.ipynb # Main notebook

├── final_submission(1).csv # Predicted license plate texts

├── final_submission_onehot.csv # One-hot encoded final output

├── truth_final_submission.csv # Ground truth values for validation

└── README.md # This file


---

## 📌 Problem Statement

> Given a set of vehicle and license plate images:
> - 🔍 Detect the license plate using bounding box
> - 🔠 Recognize characters using OCR
> - 🧾 Format predictions into 7-digit one-hot vectors for each image

Evaluation is based on **character recognition accuracy**.

---

## 🛠️ Tools & Frameworks

- [PyTorch](https://pytorch.org/)
- [YOLOv8](https://docs.ultralytics.com/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- Albumentations (data augmentation)
- CTC Loss for sequence modeling

---

## 🧠 Model Architecture

- **Detection**: YOLOv8 fine-tuned on bounding boxes of plates
- **OCR**: CRNN (Convolution + Bidirectional LSTM + Linear) trained with CTC Loss
- **Postprocessing**: Extract digits, pad to 7, ignore characters like `T`

---

## ✅ Results

- **Full Match Accuracy**: 90.00%
- **Character-Level Accuracy**: 98.07%
- Performance validated using `truth_final_submission.csv`

---

## 📄 Key Files

| File | Description |
|------|-------------|
| [📒 Jupyter Notebook](./License_Plate_Recognition_Nateesh.ipynb) | Main codebase with all logic |
| [🧾 final_submission(1).csv](./final_submission(1).csv) | Detected text per image |
| [✅ Ground Truth](./truth_final_submission.csv) | Used to calculate accuracy |
| [📊 One-Hot Output](./final_submission_onehot.csv) | Final formatted output for submission |

---

## 📨 Submission Instructions

All files listed above were submitted via email to `hr@soulpageit.com` as part of the evaluation process.

---

## 🙋‍♂️ Author

**Nateesh Kumar**  
[GitHub Profile](https://github.com/Nateesh-Kumar) | [LinkedIn](http://www.linkedin.com/in/ninaniya-nateesh-kumar-8841b62a4)  


