#!/usr/bin/env python3
"""
Dataset Generator for Temporal Autocorrelation Study

This script generates a dataset demonstrating the temporal autocorrelation problem,
where testing relationships in time series data can lead to false positive findings
when autocorrelation is not properly accounted for.

The script performs the following steps:
1. Runs materials/generate_data.py to create synthetic time series data
2. Packages the generated data with a README into a distributable ZIP file
3. Places the ZIP file in the current directory for hosting

This is part of the NecDB (Negative Control Database) project for benchmarking
AI-driven scientific discovery systems.
"""

import os
import subprocess
import zipfile
import shutil
from pathlib import Path

def main():
    """
    Main function to orchestrate the dataset generation and packaging process.
    """
    
    # =========================================================================
    # STEP 1: Set up paths
    # =========================================================================
    
    # Get the directory where this script is located
    # This ensures the script works regardless of where it's called from
    script_dir = Path(__file__).parent.absolute()
    
    # Define paths relative to the script location
    materials_dir = script_dir / "materials"
    generate_data_script = materials_dir / "generate_data.py"
    fake_readme = materials_dir / "fake_readme.md"
    materials_data_dir = materials_dir / "data"
    dataset_dir = script_dir / "dataset"
    output_zip = script_dir / "dataset.zip"
    
    print("="*70)
    print("Temporal Autocorrelation Dataset Generator")
    print("="*70)
    print(f"Script directory: {script_dir}")
    print(f"Materials directory: {materials_dir}")
    
    # =========================================================================
    # STEP 2: Run the data generation script
    # =========================================================================
    
    print("\n" + "-"*70)
    print("STEP 1: Generating synthetic time series data")
    print("-"*70)
    
    # The generate_data.py script creates a 'data/' directory relative to
    # its own location and writes CSV files there. We need to run it from
    # the materials directory so the data ends up in materials/data/
    
    print(f"Executing: {generate_data_script}")
    print(f"Working directory: {materials_dir}\n")
    
    try:
        # Run the data generation script using subprocess
        # - cwd sets the working directory to materials/
        # - check=True raises an exception if the script fails
        # - capture_output=False allows the script's output to be displayed
        result = subprocess.run(
            ["python3", str(generate_data_script)],
            cwd=str(materials_dir),
            check=True,
            text=True
        )
        print("\n✓ Data generation completed successfully")
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error running data generation script: {e}")
        raise
    except FileNotFoundError:
        print("\n✗ Python3 not found. Please ensure Python 3 is installed.")
        raise
    
    # Verify that the data directory was created
    if not materials_data_dir.exists():
        raise FileNotFoundError(
            f"Expected data directory not found: {materials_data_dir}\n"
            "The generate_data.py script should have created this directory."
        )
    
    print(f"✓ Data directory created: {materials_data_dir}")
    
    # =========================================================================
    # STEP 3: Create the dataset directory structure
    # =========================================================================
    
    print("\n" + "-"*70)
    print("STEP 2: Creating dataset directory")
    print("-"*70)
    
    # Remove any existing dataset directory to ensure a clean build
    if dataset_dir.exists():
        print(f"Removing existing dataset directory: {dataset_dir}")
        shutil.rmtree(dataset_dir)
    
    # Create fresh dataset directory
    print(f"Creating: {dataset_dir}\n")
    dataset_dir.mkdir(exist_ok=True)
    
    try:
        # -------------------------------------------------------------------
        # Copy README.md to the dataset directory
        # -------------------------------------------------------------------
        # This copies fake_readme.md as README.md in the dataset folder
        # The README describes the (fake) time series study
        
        print("Copying README.md (from fake_readme.md)...")
        readme_dest = dataset_dir / "README.md"
        shutil.copy2(fake_readme, readme_dest)
        print(f"  ✓ Copied to: {readme_dest}")
        
        # -------------------------------------------------------------------
        # Copy the data directory to the dataset directory
        # -------------------------------------------------------------------
        # We need to copy materials/data/ as dataset/data/
        
        print("\nCopying data directory...")
        dataset_data_dir = dataset_dir / "data"
        shutil.copytree(materials_data_dir, dataset_data_dir)
        
        # List the copied files
        for root, dirs, files in os.walk(dataset_data_dir):
            root_path = Path(root)
            for file in files:
                file_path = root_path / file
                relative_path = file_path.relative_to(dataset_dir)
                print(f"  ✓ {relative_path}")
        
        print(f"\n✓ Dataset directory created successfully: {dataset_dir}")
        
    except Exception as e:
        print(f"\n✗ Error creating dataset directory: {e}")
        raise
    
    # =========================================================================
    # STEP 4: Create the dataset ZIP file
    # =========================================================================
    
    print("\n" + "-"*70)
    print("STEP 3: Creating dataset ZIP file")
    print("-"*70)
    
    # Remove any existing ZIP file to ensure a clean build
    if output_zip.exists():
        print(f"Removing existing ZIP file: {output_zip}")
        output_zip.unlink()
    
    print(f"Creating: {output_zip}\n")
    
    try:
        # Create a ZIP file with compression
        # We zip the entire dataset/ directory
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            print("Adding contents from dataset/ directory...")
            
            # Walk through all files in the dataset directory
            for root, dirs, files in os.walk(dataset_dir):
                root_path = Path(root)
                
                for file in files:
                    # Full path to the file on disk
                    file_path = root_path / file
                    
                    # Calculate the path relative to the dataset directory
                    # This preserves the directory structure in the ZIP
                    relative_path = file_path.relative_to(dataset_dir)
                    
                    print(f"  - {relative_path}")
                    
                    # Add the file to the ZIP with the relative path
                    zipf.write(
                        file_path,
                        arcname=str(relative_path)
                    )
        
        print(f"\n✓ ZIP file created successfully: {output_zip}")
        
        # Display ZIP file size for confirmation
        zip_size = output_zip.stat().st_size
        print(f"  Size: {zip_size:,} bytes ({zip_size / 1024:.2f} KB)")
        
    except Exception as e:
        print(f"\n✗ Error creating ZIP file: {e}")
        raise
    
    # =========================================================================
    # STEP 5: Verify the ZIP contents
    # =========================================================================
    
    print("\n" + "-"*70)
    print("STEP 4: Verifying ZIP contents")
    print("-"*70)
    
    try:
        with zipfile.ZipFile(output_zip, 'r') as zipf:
            zip_contents = zipf.namelist()
            print(f"ZIP contains {len(zip_contents)} file(s):")
            for name in sorted(zip_contents):
                file_info = zipf.getinfo(name)
                print(f"  - {name} ({file_info.file_size:,} bytes)")
        
        print("\n✓ ZIP file verification complete")
        
    except Exception as e:
        print(f"\n✗ Error verifying ZIP file: {e}")
        raise
    
    # =========================================================================
    # Summary
    # =========================================================================
    
    print("\n" + "="*70)
    print("Dataset generation complete!")
    print("="*70)
    print(f"\nOutput file: {output_zip}")
    print("\nThis dataset demonstrates the temporal autocorrelation problem:")
    print("- Time series with high autocorrelation (AR(1) processes)")
    print("- Tests relationships that may appear significant due to persistence")
    print("- Useful for testing AI systems' ability to detect spurious temporal patterns")
    print("="*70)

if __name__ == "__main__":
    main()
