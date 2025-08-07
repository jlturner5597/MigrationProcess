#!/usr/bin/env python3
import subprocess
import sys

def test_mmdc():
    print("Testing mermaid-cli detection...")
    
    # Test npx
    try:
        result = subprocess.run(['npx', '@mermaid-js/mermaid-cli', '--version'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        print(f"npx test - returncode: {result.returncode}")
        print(f"npx test - stdout: {result.stdout}")
        print(f"npx test - stderr: {result.stderr}")
    except Exception as e:
        print(f"npx test - exception: {e}")
    
    # Test mmdc
    try:
        result = subprocess.run(['mmdc', '--version'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        print(f"mmdc test - returncode: {result.returncode}")
        print(f"mmdc test - stdout: {result.stdout}")
        print(f"mmdc test - stderr: {result.stderr}")
    except Exception as e:
        print(f"mmdc test - exception: {e}")

if __name__ == "__main__":
    test_mmdc() 