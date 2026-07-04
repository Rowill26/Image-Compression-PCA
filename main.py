import numpy as np
from PIL import Image
import time

def manual_pca(channel_matrix, n_components):
    """
    Fungsi untuk melakukan kompresi PCA.
    """
    mean_val = np.mean(channel_matrix, axis=0)
    X_centered = channel_matrix - mean_val
    
    cov_matrix = np.cov(X_centered, rowvar=False)
    
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    sorted_index = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_index]
    
    eigenvector_subset = sorted_eigenvectors[:, 0:n_components]
    X_reduced = np.dot(X_centered, eigenvector_subset)
    X_reconstructed = np.dot(X_reduced, eigenvector_subset.T) + mean_val
    
    return X_reconstructed

def compress_image_pca(input_path, output_path, n_components):
    start_time = time.time()
    
    img = Image.open(input_path).convert('RGB')
    
    img.thumbnail((2000, 2000)) 
    
    img_array = np.array(img)
    H, W = img_array.shape[0], img_array.shape[1]
    
    max_possible_components = min(H, W)
    if n_components > max_possible_components:
        n_components = max_possible_components
    
    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]
    
    r_recon = manual_pca(r, n_components)
    g_recon = manual_pca(g, n_components)
    b_recon = manual_pca(b, n_components)
    
    img_reconstructed = np.dstack((r_recon, g_recon, b_recon))
    img_reconstructed = np.clip(img_reconstructed, 0, 255).astype(np.uint8)
    
    original_size = H * W * 3
    compressed_size = 3 * ((H * n_components) + (n_components * W))
    compression_percentage = (1 - (compressed_size / original_size)) * 100
    
    runtime = time.time() - start_time
    
    output_img = Image.fromarray(img_reconstructed)
    output_img.save(output_path)
    
    return runtime, compression_percentage