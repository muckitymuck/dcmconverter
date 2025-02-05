import os
import pydicom
from PIL import Image
import numpy as np

def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def convert_dcm_to_png(dcm_file_path, png_file_path):
    """Convert a single DICOM file to PNG format."""
    try:
        # Read the DICOM file
        dicom = pydicom.dcmread(dcm_file_path)
        
        # Get the pixel array from the DICOM file
        pixel_array = dicom.pixel_array
        
        # Normalize the pixel values if needed
        if pixel_array.dtype != np.uint8:
            pixel_min = pixel_array.min()
            pixel_max = pixel_array.max()
            if pixel_max - pixel_min != 0:
                scaled_array = ((pixel_array - pixel_min) / (pixel_max - pixel_min) * 255).astype(np.uint8)
            else:
                scaled_array = np.zeros_like(pixel_array, dtype=np.uint8)
        else:
            scaled_array = pixel_array
        
        # Convert the pixel array to a PIL Image
        image = Image.fromarray(scaled_array)
        
        # Save the image as a PNG file
        image.save(png_file_path)
        return True
    except Exception as e:
        print(f"Error converting {dcm_file_path}: {str(e)}")
        return False

def convert_directory():
    """Convert all DICOM files in the 'files' directory to PNG format."""
    # Setup directories
    input_dir = 'files'
    output_dir = 'converted'
    
    # Ensure both directories exist
    ensure_directory_exists(input_dir)
    ensure_directory_exists(output_dir)
    
    # Get list of files in input directory
    files = os.listdir(input_dir)
    dcm_files = [f for f in files if f.lower().endswith('.dcm')]
    
    if not dcm_files:
        print("No DICOM files found in the 'files' directory.")
        return
    
    print(f"Found {len(dcm_files)} DICOM files to process.")
    
    # Convert each file
    successful = 0
    skipped = 0
    for dcm_file in dcm_files:
        input_path = os.path.join(input_dir, dcm_file)
        output_filename = f"{os.path.splitext(dcm_file)[0]}.png"
        output_path = os.path.join(output_dir, output_filename)
        
        # Check if the file already exists in the converted folder
        if os.path.exists(output_path):
            print(f"Skipping: {dcm_file} (already converted)")
            skipped += 1
            continue
        
        print(f"Converting: {dcm_file}")
        if convert_dcm_to_png(input_path, output_path):
            successful += 1
    
    print(f"\nConversion complete!")
    print(f"Successfully converted: {successful}/{len(dcm_files)} files")
    print(f"Skipped {skipped} already converted files")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    convert_directory() 