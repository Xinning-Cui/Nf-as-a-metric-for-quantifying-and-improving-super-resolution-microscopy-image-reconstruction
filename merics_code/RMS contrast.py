#RMS contrast
import os
import cv2
import numpy as np
import pandas as pd

# Function to normalize image to [0, 255] using Min-Max normalization
def min_max_normalize(image):
    return ((image - np.min(image)) / (np.max(image) - np.min(image)))*255

# Function to calculate RMS contrast
def calculate_rms_contrast(image):

    # Calculate the mean intensity
    mean_intensity = np.mean(image)

    # Calculate RMS contrast
    rms_contrast = np.sqrt(np.mean((image - mean_intensity) ** 2))

    return rms_contrast


#Vanilla CVDM
image_folder = r'path to\images\VanillaCVDM_inference'  # Replace with your folder path
output_csv = r"path to \RMS_contrast_CVDM.csv"

#CVDM+N
# image_folder = =r'path to\images\CVDM+N_inference'  # Replace with your folder path
# output_csv = r"path to\RMS_contrast_CVDM+N.csv"

#NCVDM
# image_folder = r'path to\images\NCVDM_inference'  # Replace with your folder path
# output_csv = r"path to \RMS_contrast_NCVDM.csv"




# List to store results
results = []

# Loop through all files in the folder
for filename in os.listdir(image_folder):
    file_path = os.path.join(image_folder, filename)

    # Check if the file is an image (optional: add specific extensions if needed)
    if filename.lower().endswith(( ".tif", ".tiff")):
        try:
            # Read the image
            image = cv2.imread(file_path,cv2.IMREAD_UNCHANGED)
            image=image.astype('float32')
            image=min_max_normalize(image)
            # Ensure the image was loaded successfully
            if image is not None:
                # Calculate RMS contrast
                rms_contrast = calculate_rms_contrast(image)

                # Append the result to the list
                results.append({"filename": filename, "RMS Contrast": rms_contrast})
            else:
                print(f"Could not read image: {filename}")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Save results to a CSV file
if results:
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"RMS contrast results saved to {output_csv}")
else:
    print("No valid images found in the folder.")
