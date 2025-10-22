from google.cloud import vision
import os
import matplotlib.pyplot as plt

# Set Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\ovaiz\OneDrive\Desktop\PROJECTS\MAJOR\Codes\Transcend\sonic-ivy-459106-k0-6cb4ddafd2c4.json"

# Initialize Google Vision API client
client = vision.ImageAnnotatorClient()

# List of test images for accuracy validation
test_images = [
    r"C:\Users\ovaiz\OneDrive\Desktop\PROJECTS\MAJOR\Images\Test.png",
    r"C:\Users\ovaiz\OneDrive\Desktop\PROJECTS\MAJOR\Images\1.jpg",
    r"C:\Users\ovaiz\OneDrive\Desktop\PROJECTS\MAJOR\Images\2.jpg"
]

# Lists to store results
image_names = []
char_counts = []

# Process each image
for img_path in test_images:
    with open(img_path, "rb") as image_file:
        content = image_file.read()
        image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    extracted_text = response.full_text_annotation.text.strip()

    # Log the results
    print(f"\n🖼️ Image: {os.path.basename(img_path)}")
    print(f"📄 Extracted Text:\n{extracted_text}")
    print(f"🔢 Character Count: {len(extracted_text)}")

    image_names.append(os.path.basename(img_path))
    char_counts.append(len(extracted_text))

# Plotting the OCR accuracy graph
plt.figure(figsize=(10, 5))
plt.bar(image_names, char_counts, color='cornflowerblue')
plt.title("OCR Accuracy: Characters Extracted per Image", fontsize=14)
plt.xlabel("Image Files", fontsize=12)
plt.ylabel("Number of Characters Extracted", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the graph
graph_path = r"C:\Users\ovaiz\OneDrive\Desktop\PROJECTS\MAJOR\Images\ocr_accuracy_graph.png"
plt.savefig(graph_path)
plt.show()

print(f"\n✅ OCR accuracy graph saved at: {graph_path}")
