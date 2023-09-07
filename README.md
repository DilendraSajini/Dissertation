<p align="center">
  <img  src="./static/background.png">
</p>

<h1 align="center">
Leveraging Deep Learning and Medical Image Analysis for Enhanced Breast Cancer Diagnosis </h1>

<p align="justify">
Deep learning has brought remarkable advancements to the field of medical image analysis, introducing algorithms like convolutional neural networks (CNNs), recurrent neural networks (RNNs), generative adversarial networks (GANs), etc. These sophisticated algorithms can be utilised with the objective of augmenting the precision and efficiency of cancer diagnostics while concurrently diminishing errors. Focusing on the domain of breast cancer histopathological images, this study delves into a diverse array of strategies with the intent of elevating the accuracy and efficiency of classification.
</p></p><p align="justify">
The intricacies embedded within high-resolution images hold a pivotal role in ensuring the precise detection and characterization of cancer. Nevertheless, the inherent complexity of these images gives rise to challenges, necessitating the development of specialised methodologies tailored for resource-conscious, cost-effective, and efficient processing. This study introduces a novel approach tailored for high-resolution histopathology image analysis, aiming to enhance both accuracy and performance in medical image classification
</p></p><p align="justify">
The architecture put forth harnesses the advantages of patch-based image analysis through the seamless integration of a transfer learning Visual Geometry Group (VGG) 16 model with an LSTM (Long Short-Term Memory) classifier. This combination results in a powerful solution for the precise classification of high-resolution histology images. By utilising pre-trained models as feature extractors, the system gains the ability to capture intricate image features that contribute to accurate diagnoses. The LSTM classifier goes a step further in augmenting accuracy by capturing temporal dependencies among image patches. This addresses the challenge of losing global context for structures or features that are frequently disregarded in traditional approaches.
</p><p align="justify">
The effectiveness of this strategy becomes unmistakably clear from its results. Attaining an impressive accuracy of 90.05%, coupled with elevated precision, recall, and AUC values at 100X magnifications, underscores the model's proficiency in high-resolution analysis. The patch-based approach optimally processes large-dimensional tumour regions without the need for resource-intensive whole slide image (WSI) analysis and showcasing its prowess in capturing intricate details for precise classification. This scalability contributes to quicker processing times, allowing for swift predictions and efficient utilisation of computational resources.
<p align="center">
  <img  src="./static/architecture.PNG">
</p>


## Application Overview

This web application allows users to perform histopathology binary classification using above  deep learning model. Follow these steps to use the app:

1. **Access the Web App**

   - Open the [Breast Cancer Classification Web App](https://dissertation-zejrc29dctwmetafszbaaw.streamlit.app/) using your web browser.

2. **Upload Histopathology WSI (100X)**

   - On the app's interface, you will find an option to upload a histopathology Whole Slide Image (WSI) captured at 100X magnification. Use the file uploader to select and upload your image.

3. **Patch Extraction**

   - After uploading the image, the app will perform patch extraction. It will divide the WSI into smaller patches, allowing you to view the details of different areas of the image.

4. **Preprocessed Patches**

   - The app will also display preprocessed versions of the patches, which have been prepared for classification.

5. **Classification Output**

   - The most critical step is the classification of the uploaded image. The deep learning model will analyze the patches and provide a binary classification output:
      - If the model determines that the histopathology is "Benign," it will display "Benign."
      - If the model determines that the histopathology is "Malignant," it will display "Malignant."

## Usage

1. Clone the repository:
   ```bash
   git https://github.com/DilendraSajini/Dissertation.git
