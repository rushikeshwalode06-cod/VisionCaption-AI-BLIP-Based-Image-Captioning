# 🌈 VisionCaption AI — BLIP-Based Image Captioning

VisionCaption AI is an AI-powered image captioning application built with Python, Streamlit, PyTorch, and BLIP. It analyzes uploaded RGB images and generates meaningful text descriptions. Features include image preview, adjustable caption settings, an attractive RGB-themed interface, and caption downloading for a smooth user experience.

# 🌈 VisionCaption AI — BLIP-Based Image Captioning

## 📌 Project Overview

VisionCaption AI is an AI-powered image captioning application that automatically generates meaningful natural-language descriptions from uploaded images. It uses the BLIP (Bootstrapping Language-Image Pre-training) model, fine-tuned on an inspiring Indian women image-captioning dataset.

The application is developed using Python, Streamlit, PyTorch, and Hugging Face Transformers. It features an interactive RGB-themed interface, image preview, adjustable caption generation settings, and downloadable text descriptions.

## ✨ Key Features

* 🤖 **AI Image Captioning:** Automatically generates text descriptions from images.
* 🎯 **Fine-Tuned BLIP Model:** Uses a custom model fine-tuned for Indian women-related image captioning.
* 🖼️ **Multiple Image Formats:** Supports JPG, JPEG, PNG, and WEBP formats.
* 🎨 **RGB Image Processing:** Converts uploaded images into RGB format for model processing.
* 🌈 **Interactive Web Interface:** Provides a modern, responsive, RGB-themed Streamlit UI.
* ⚙️ **Adjustable Caption Generation:** Allows users to configure maximum caption length and beam search.
* 👁️ **Image Preview:** Displays the uploaded image before generating a caption.
* 📥 **Caption Download:** Allows users to download generated descriptions as `.txt` files.
* 🚀 **GPU Support:** Uses CUDA when available and otherwise runs on the CPU.
* 📊 **Model Information:** Displays the model name and processing device.


## 🧠 AI Model

The project uses BLIP (Bootstrapping Language-Image Pre-training), a vision-language model designed for image understanding and text generation.

**Model Details:**

* 🏗️ **Model Architecture:** BLIP
* 🧩 **Base Model:** `Salesforce/blip-image-captioning-base`
* 🤗 **Fine-Tuned Model:** [Indian Women Image Captioning — Hugging Face](https://huggingface.co/rushikeshwalode/blip-image-captioning-base-Indian_celeb_womens-finetuned)
* 📝 **Task:** Image Captioning
* 🖼️ **Input:** RGB Image
* 💬 **Output:** Natural-Language Caption
* ⚙️ **Optimizer:** AdamW
* 📉 **Learning Rate:** `5e-5`
* 🔥 **Framework:** PyTorch
  
![ml](https://github.com/rushikeshwalode06-cod/VisionCaption-AI-BLIP-Based-Image-Captioning/blob/main/caption_model_image.png?raw=true)

## 📊 Dataset

The training script uses the following Hugging Face dataset:

**Dataset:** [Inspiring Indian Women BLIP](https://huggingface.co/datasets/dany0407/inspiring-indian-women-blip)

The dataset contains images and associated text captions. These image-caption pairs are used to train the model to generate relevant descriptions from visual inputs.

## ⚙️ Technologies Used

* 🐍 Python
* 🔥 PyTorch
* 🎈 Streamlit
* 🤗 Hugging Face Transformers
* 📚 Hugging Face Datasets
* 🖼️ BLIP (Bootstrapping Language-Image Pre-training)
* 🖼️ Pillow (PIL)
* 🌐 HTML
* 🎨 CSS


## 🔄 How It Works

1. 📤 **Upload Image:** The user uploads an image through the Streamlit interface.
2. 🎨 **Image Preprocessing:** The uploaded image is converted into RGB format.
3. 🤗 **Model Loading:** The application loads the fine-tuned BLIP model and its processor from Hugging Face.
4. 🔍 **Image Analysis:** The processor prepares the image for the model.
5. 🧠 **Caption Generation:** The model generates a textual description using its image-captioning capabilities.
6. 📝 **Display Output:** The generated caption appears in the application.
7. 📥 **Download Caption:** The user can download the generated description as a text file.

## 📈 Applications

* 📝 Image Caption Generation
* ♿ Assistive Technologies for Visually Impaired Users
* 🌐 Image Description and Accessibility
* 🎓 Educational AI Demonstrations
* 🤖 Computer Vision and Natural Language Processing (NLP) Projects
* 👁️ Visual Content Understanding

## 🔮 Future Enhancements

* 🌍 Support for Multiple Languages
* 🖼️ Batch Image Caption Generation
* 🎯 Improved Caption Accuracy Through Further Fine-Tuning
* 📊 Caption Evaluation Using Suitable Evaluation Metrics
* ♿ Image-to-Text Accessibility Integration
* ☁️ Deployment on a Public Cloud Platform
* 🤖 Support for Additional Vision-Language Models


## 🎯 Conclusion

VisionCaption AI demonstrates how computer vision and natural-language generation can work together to convert visual information into meaningful text. By combining a BLIP-based image captioning model with a modern Streamlit interface, the project provides an interactive solution for exploring AI-powered image understanding.

---
![ml](https://github.com/rushikeshwalode06-cod/VisionCaption-AI-BLIP-Based-Image-Captioning/blob/main/VisionCaption_image.png?raw=true)
