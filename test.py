import neurosynth_simulation

def test_neurosynth_simulation():
    # Example test case
    dataset = neurosynth_simulation.create_neurosynth_object(["task", "emotion"], [(0, 0, 0), (1, 1, 1)])
    fMRI_image = neurosynth_simulation.generate_synthetic_fmri_image(dataset, 100)
    result = neurosynth_simulation.apply_signal_detection(fMRI_image, "thresholding")
    ground_truth = np.random.randint(0, 2, size=(100, 100, 100))  # Random ground truth for testing
    accuracy, error_rate = neurosynth_simulation.compare_results(result, ground_truth)
    assert accuracy >= 0 and accuracy <= 1
    assert error_rate >= 0 and error_rate <= 1

if __name__ == "__main__":
    test_neurosynth_simulation()