# Day 17 – Fashion MNIST CNN Image Classification Web App

## 1. Project Overview

On Day 17 of my Machine Learning internship, I worked on a Deep Learning project using a Convolutional Neural Network (CNN). The project classifies clothing images into different categories using the Fashion MNIST dataset.

I trained a CNN model, evaluated its performance, saved the trained model, and developed a web application using Gradio. I then ran the application in Google Colab and tested it by uploading clothing images through a public demo link.

## 2. Objectives

- Understand the basic concepts of Deep Learning and CNNs.
- Use the Fashion MNIST dataset for image classification.
- Train and evaluate a CNN model.
- Save the trained model for reuse.
- Create a web interface using Gradio.
- Load the saved model into the web application.
- Run the application in Google Colab.
- Generate a public link for testing.
- Upload clothing images and analyze prediction results.
- Document the project and prepare a demonstration.

## 3. Technologies and Tools Used

- Python
- TensorFlow
- Keras
- NumPy
- Pillow (PIL)
- Gradio
- Google Colab
- GitHub
- Visual Studio Code
- Command Prompt / PowerShell

## 4. Dataset

I used the Fashion MNIST dataset, which contains 70,000 grayscale images of clothing items. It includes 60,000 training images and 10,000 testing images.

Each image has a size of 28 × 28 pixels and belongs to one of ten clothing categories.

The categories are:

1. T-shirt / Top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle Boot

## 5. CNN Model Training

I developed and trained a Convolutional Neural Network using TensorFlow and Keras.

The model learns visual patterns from the training images and uses these patterns to classify clothing categories.

Training details:

- Model type: Convolutional Neural Network (CNN)
- Dataset: Fashion MNIST
- Number of epochs: 5
- Test accuracy: 89.20%
- Saved model file: `fashion_mnist_cnn.keras`

After training, I evaluated the model on the test dataset and saved it in Keras format. This allowed me to reuse the trained model without training it again.

## 6. Saving and Uploading the Model

I saved the trained model as:

`fashion_mnist_cnn.keras`

I uploaded the required project files to my GitHub repository so that the model and application code could be accessed for deployment and demonstration.

GitHub repository:

https://github.com/18-muskan/fashion-mnist-cnn-app

The repository contains:

- `app.py` – Gradio application code
- `fashion_mnist_cnn.keras` – Trained CNN model
- `requirements.txt` – Required Python packages
- `README.md` – Project documentation

## 7. Creating the Web Application

I used Gradio to create a simple interface for image classification.

The application allows users to upload a clothing image and view the model's predicted categories and confidence scores.

The application performs these steps:

1. Accepts an image from the user.
2. Corrects the image orientation when required.
3. Converts the image to grayscale.
4. Resizes it to 28 × 28 pixels.
5. Converts pixel values to floating-point numbers.
6. Normalizes pixel values between 0 and 1.
7. Reshapes the image into the format required by the CNN.
8. Sends the processed image to the trained model.
9. Displays the top three predicted categories with confidence scores.

The model was loaded from the saved Keras file, so retraining was not required to run the application.

## 8. Running the Application in Google Colab

I used Google Colab to run the web application without needing to configure a local web server.

The steps completed were:

1. Opened Google Colab.
2. Created a new notebook named `Fashion_MNIST_CNN_App.ipynb`.
3. Installed Gradio using pip.
4. Downloaded `fashion_mnist_cnn.keras` from my GitHub repository.
5. Imported the required Python libraries.
6. Loaded the trained CNN model using TensorFlow/Keras.
7. Created the image preprocessing and prediction function.
8. Built the Gradio interface with an image upload component and prediction output.
9. Launched the application using `demo.launch(share=True)`.
10. Received a public Gradio URL.
11. Opened the link in a browser and tested the application.

The model loaded successfully in Google Colab, and the Gradio application started without a model-loading error.

## 9. Public Demo

I generated a temporary public link using Gradio's sharing feature.

Live demo:

https://e5a355d548a7a6987c.gradio.live

This link was generated during the Google Colab session. It is temporary and may stop working when the session ends or the sharing link expires.

The public link allowed me to test the application in a web browser without running the interface locally.

## 10. Image Upload Testing

I tested the application by uploading clothing images downloaded from Google Images.

### Test 1: Bag Image

The model returned the following results:

- Bag: 100%
- T-shirt / Top: 0%
- Pullover: 0%

The model correctly predicted the uploaded bag image.

### Test 2: Sneaker Image

The model returned the following results:

- Bag: 95%
- Sneaker: 5%
- Sandal: 0%

The model incorrectly classified the uploaded sneaker image as a bag.

This showed that although the application runs successfully, prediction accuracy can vary when real-world images are used instead of images similar to the Fashion MNIST dataset.

These confidence scores represent the model's output and do not guarantee that a prediction is correct.

## 11. Troubleshooting and Deployment Attempts

During the project, I explored options for running the application online.

- I attempted to run the application using Hugging Face Spaces.
- I also attempted deployment using Streamlit Community Cloud.
- I explored Render as another hosting option.
- These attempts did not provide a working public application during my testing.
- I then used Google Colab with Gradio's sharing feature to run and demonstrate the application successfully.

Google Colab provided a practical way to demonstrate the trained model without completing a permanent hosting setup.

## 12. Challenges and Limitations

- Real-world clothing images may look different from the training images.
- Image backgrounds, colors, cropping, and resizing can affect predictions.
- The model may incorrectly classify images downloaded from the internet.
- A high confidence score does not guarantee a correct result.
- The Gradio public link is temporary rather than permanent hosting.
- Google Colab sessions have usage limits and may disconnect.

Further improvements could include better image preprocessing, testing on more samples, and training or fine-tuning a model using a dataset closer to real-world product photographs.

## 13. Screen Recording and Demonstration

I prepared the application for a screen-recorded demonstration.

The demonstration can include:

1. Showing the GitHub repository and project files.
2. Showing the Google Colab notebook.
3. Demonstrating successful model loading.
4. Opening the public Gradio application.
5. Uploading a bag image and showing its prediction.
6. Uploading a sneaker image and showing its prediction.
7. Explaining that real-world images can sometimes be misclassified.

The recording can be used as supporting evidence of the application's functionality.

## 14. Learning Outcomes

During this task, I learned how to:

- Understand the role of CNNs in image classification.
- Train and evaluate a deep learning model.
- Interpret model test accuracy.
- Save and reload a trained Keras model.
- Preprocess images before prediction.
- Build a web interface using Gradio.
- Run Python applications in Google Colab.
- Download model files from GitHub.
- Generate a temporary public demo link.
- Test an AI application using uploaded images.
- Identify prediction errors and explain model limitations.
- Explore different deployment platforms.

## 15. Conclusion

On Day 17, I trained a CNN model using the Fashion MNIST dataset and achieved 89.20% test accuracy after five epochs. I saved the trained model and developed a Gradio web application for clothing image classification.

I uploaded the project files to GitHub, loaded the model in Google Colab, and generated a temporary public demo link. I tested the application using bag and sneaker images. The bag image was classified correctly, while the sneaker image was misclassified, helping me understand the limitations of using a model trained on a specific dataset for real-world photographs.

Overall, this task helped me practice deep learning, model saving and loading, image preprocessing, web application development, testing, and deployment exploration.

## 16. Project Links

- GitHub Repository: https://github.com/18-muskan/fashion-mnist-cnn-app
- Google Colab Notebook: Saved in my Google Colab account.
- Gradio Demo: https://e5a355d548a7a6987c.gradio.live

Note: The Gradio demo link is temporary and may expire.
