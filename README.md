# BCOG-200-Final-Project

1. This project aims to simulate neural activity using the NeuroSynth library and assess various signal detection and classification methods.
   Firstly, a function will utilize NeuroSynth to create a synthetic fMRI image based on specified terms and coordinates.
   Subsequently, another function will apply signal detection or classification techniques, such as thresholding, clustering, or decoding, to the generated image and produce a result.
   Finally, a function will compare and visually plot the outcome against the ground truth, evaluating the accuracy and error rate of the chosen method.
   This project facilitates exploration and assessment of different approaches in analyzing neural signals for research or diagnostic purposes.


2. a) create_neurosynth_object: This function creates a NeuroSynth object with a given set of terms and coordinates, enabling the generation of synthetic fMRI images.
   b) generate_synthetic_fmri_image: This function generates a synthetic fMRI image based on the provided NeuroSynth dataset and a specified number of voxels.
   c) apply_signal_detection: This function applies a signal detection method (such as thresholding or clustering) to the synthetic fMRI image, producing a detection result.
