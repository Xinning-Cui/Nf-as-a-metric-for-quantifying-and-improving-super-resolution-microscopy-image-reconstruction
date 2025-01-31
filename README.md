# Nf-as-a-metric-for-quantifying-and-improving-super-resolution-microscopy-image-reconstruction
We trained a Conditional **Variational Diffusion Model (CVDM)** (G. Della Maggiora, 2023) using the **BioSR dataset** (Qiao & Li, 2020) (DOI: 10.6084/m9.figshare.13264793.v9). To evaluate if the model can generate natural images similar to the gtound truth, we assessed the **Naturalness Factor**(Gong, Y., & Sbalzarini, I. F. 2014) at two stages: prior learning (before training) and post-processing (after applying the model's output enhancements). 

The model is trained for 10 epochs with a batch size of 2. Overall, the model is trained for 500,000 iterations, with generation time step T = 200, learning rate 0.0001. 
During theinference, generation time steps are set to T = 500. The naturalization of images is donewith the ImageJ Mosaic Suite plugin. 
The implementation of CVDM can be found on the GitHub page (G. Della Maggiora, L. A. Croquevielle, N. Deshpande, H. Horsley, T. Heinis, A. Yaki-movich, Conditional variational diffusion models, https://github.com/casus/cvdm)2023. 
The Naturalness Factor information and documentation (including a guide on installation of the Mosaic Suite plugin) can be found in  MOSAIC group, MosaicSuite documentation, https://sbalzarinilab.org/MosaicSuiteDoc/index.html.

##How to use the images?

Every folder contains 100 TIFF images representing four biological structures from the **BioSR dataset**, 25 images for each structure.

- **CCP** (Clathrin-Coated Pits) from image_1 to image_25 
- **ER** (Endoplasmic Reticulum)  from image_26 to image_50 
- **F-actin** (Filamentous Actin)  from image_51 to image_75 
- **MT** (Microtubules) from image_76 to image_100 

The **BioSR_low_resolution_images** folder contains low-resolution images.

The **BioSR_high_resolution_images** folder contains the high-resolution grond truth images.

The **naturalized_BioSR_high_resolution_images** folder contains the naturalized high-resolution ground truth images, which are obtained by naturalizing the images in **BioSR_high_resolution_images** using ImageJ Mosaic Suite plugin.

The **CVDM_inference** folder contains CVDM generated images during inference, using images from **BioSR_low_resolution_images** as input.

The **CVDM+N_inference** folder contains images obtained by natrualizing all images in the **CVDM_inference** folder using ImageJ Mosaic Suite plugin.

The **NCVDM_inference** folder contains images generated by NCVDM model.

##How to use the metric code?

To calculate **CVDM experiment metrics**:

- Use images from the **BioSR_high_resolution_images** folder and the **CVDM_inference** folder as pairs to compute **MS-SSIM, MAE, and PSNR**.
- Use images from the **CVDM_inference** folder to compute **RMS Contrast** and **Naturalness Factor**.

To calculate **CVDM+N experiment metrics**:

- Use images from the **naturalized_BioSR_high_resolution_images** folder and the **CVDM+N_inference** folder as pairs to compute **MS-SSIM, MAE, and PSNR**.
- Use images from the **CVDM+N_inference** folder to compute **RMS Contrast** and **Naturalness Factor**.

To calculate **NCVDM experiment metrics**:

- Use images from the **naturalized_BioSR_high_resolution_images** folder and the **NCVDM_inference** folder as pairs to compute **MS-SSIM, MAE, and PSNR**.
- Use images from the **NCVDM_inference** folder to compute **RMS Contrast** and **Naturalness Factor**.



