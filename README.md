# Nf-as-a-metric-for-quantifying-and-improving-super-resolution-microscopy-image-reconstruction
We trained a Conditional Variational Diffusion Model (CVDM) (G. Della Maggiora, 2023) using the BioSR dataset (Qiao & Li, 2020) (DOI: 10.6084/m9.figshare.13264793.v9). To evaluate if the model can generate natural images similar to the gtound truth, we assessed the Naturalness Factor(Gong, Y., & Sbalzarini, I. F. 2014) at two stages: prior learning (before training) and post-processing (after applying the model's output enhancements).

The model is trained for 10 epochs with a batch size of 2. Overall, the model is trained for 500,000 iterations, with generation time step T = 200, learning rate 0.0001. 
During theinference, generation time steps are set to T = 500. The naturalization of images is donewith the ImageJ Mosaic Suite plugin. 
The implementation of CVDM can be found on the GitHub page (G. Della Maggiora, L. A. Croquevielle, N. Deshpande, H. Horsley, T. Heinis, A. Yaki-movich, Conditional variational diffusion models, https://github.com/casus/cvdm)2023. 
The Naturalness Factor information and documentation (including a guide on installation of the Mosaic Suite plugin) can be found in  MOSAIC group, MosaicSuite documentation, https://sbalzarinilab.org/MosaicSuiteDoc/index.html.

