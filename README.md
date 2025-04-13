# Arnold Transform Image Encryption Application

A Streamlit-powered web application for image encryption and decryption utilizing the Arnold Transform (Cat Mapping) algorithm.


## Installation

Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Operation process:
   - Upload an image file in the sidebar (supports png, jpg, jpeg, gif, webp formats)
   - Click "Run Encryption" button to encrypt the image
   - Click "Run Decryption" button to decrypt the image

Note:
- Input image must be square, otherwise an error will occur
- The encryption and decryption process is based on the reversible property of Arnold Transform, ensuring full restoration of the original image
