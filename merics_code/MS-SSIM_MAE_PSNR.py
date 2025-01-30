import os
import cv2
import tensorflow as tf
import pandas as pd
import numpy as np

#Vanilla CVDM
folder_a = r'path to\images\VanillaCVDM_inference'
folder_b = r'path to\images\BioSR_high_resolution_images'


#CVDM+N
# folder_a=r'path to\images\naturalized_BioSR_high_resolution_images'
# folder_b=r'path to\images\CVDM+N_inference'

#NCVDM
# folder_a=r'path to\images\naturalized_BioSR_high_resolution_images'
# folder_b=r'path to\images\NCVDM_inference'


metrics = []

# Loop through the images in the first folder
for filename in os.listdir(folder_a):

    img_path_a = os.path.join(folder_a, filename)
    img_path_b = os.path.join(folder_b, filename)

    if os.path.isfile(img_path_b):
        # Read the grayscale TIFF images
        img_a = cv2.imread(img_path_a, cv2.IMREAD_UNCHANGED)
        img_b = cv2.imread(img_path_b, cv2.IMREAD_UNCHANGED)
        if img_a is None:
            print(f"Error: Could not load {img_path_a}")
            continue
        if img_b is None:
            print(f"Error: Could not load {img_path_b}")
            continue

        img_a = img_a.astype('float32')
        img_b = img_b.astype('float32')

        # Min-Max normalization
        img_a_min, img_a_max = img_a.min(), img_a.max()
        img_b_min, img_b_max = img_b.min(), img_b.max()
         #normalize image to [0, 255] 
        img_a = ((img_a - img_a_min) / (img_a_max - img_a_min)) * 255  
        img_b = ((img_b - img_b_min) / (img_b_max - img_b_min)) * 255
        # Adds a channel dimension
        img_a = tf.expand_dims(img_a, axis=-1)  
        img_b = tf.expand_dims(img_b, axis=-1)  

        # Calculate MS-SSIM, PSNR and MAE
        msssim_value = tf.image.ssim_multiscale(img_a, img_b, max_val=255.0).numpy()
        psnr_value = tf.image.psnr(img_a, img_b, max_val=255).numpy()
        mae_value = np.mean(np.abs(img_a - img_b))
        # Append the result to the list
        metrics.append({
            "filename": filename,
            "MS-SSIM": msssim_value,
            "MAE": mae_value,
            "PSNR": psnr_value
        })

# Create a DataFrame from the results
results_df = pd.DataFrame(metrics)

# Save results to a CSV file
results_df.to_csv(r"path to\CVDM+N.csv", index=False)
