import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load the GeoTIFF file
file_path = r"D:\AllProjects\SIH_SAR_img_Col\S1A_EW_SLC__1SDH_20240830T070441_20240830T070547_055439_06C332_1A98.SAFE\measurement\s1a-ew2-slc-hv-20240830t070442-20240830t070546-055439-06c332-007.tiff"
base_name = os.path.splitext(os.path.basename(file_path))[0]
output_file_name = f'{base_name}.png'
with rasterio.open(file_path) as src:
    # Read the first band (assuming it's single-band SAR data)
    image = src.read(1)

# Calculate the magnitude of the complex numbers
magnitude_image = np.abs(image)

# Check for the minimum and maximum values
print(f"Pixel value range before log scaling: {magnitude_image.min()} to {magnitude_image.max()}")

# Apply logarithmic scaling
log_magnitude_image = 10 * np.log10(magnitude_image + 1)  # Add 1 to avoid log(0)

# Check for the minimum and maximum values after log scaling
print(f"Pixel value range after log scaling: {log_magnitude_image.min()} to {log_magnitude_image.max()}")

# Normalize the image to 0-255 for better visualization
normalized_image = (255 * (log_magnitude_image - log_magnitude_image.min()) / 
                    (log_magnitude_image.max() - log_magnitude_image.min())).astype(np.uint8)

# Save as PNG
plt.imsave(output_file_name, normalized_image, cmap='gray')




