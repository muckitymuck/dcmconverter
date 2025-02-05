# DICOM to PNG Converter

A Python script that converts DICOM (.dcm) medical image files to PNG format. The script processes multiple files in batch, automatically handles different bit depths, and skips already converted files.

## Features

- Batch conversion of DICOM files to PNG format
- Automatic directory creation
- Handles different bit depths and normalizes pixel values
- Skips already converted files to avoid duplicates
- Progress tracking and conversion summary
- Error handling for corrupted or invalid DICOM files

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone or download this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Create a directory named `files` (if it doesn't exist) in the same location as the script
2. Place your DICOM (.dcm) files in the `files` directory
3. Run the script:
```bash
python dcm_converter.py
```

The script will:
- Create a `converted` directory if it doesn't exist
- Process all DICOM files from the `files` directory
- Save converted PNG images in the `converted` directory
- Skip any files that have already been converted
- Display progress and a summary of the conversion

## Directory Structure

```
.
├── dcm_converter.py     # Main conversion script
├── requirements.txt     # Python dependencies
├── files/              # Place your DICOM files here
└── converted/          # Converted PNG files will be saved here
```

## Output

The script provides feedback during conversion:
- Number of DICOM files found
- Progress updates for each file (converting or skipping)
- Final summary showing:
  - Number of successfully converted files
  - Number of skipped files
  - Location of output directory

## Dependencies

- pydicom==2.4.3
- Pillow==10.2.0
- numpy==1.26.3

## Error Handling

The script includes error handling for:
- Missing or invalid DICOM files
- File access issues
- Conversion failures

Any errors during conversion will be printed to the console, and the script will continue processing the remaining files. 