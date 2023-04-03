import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import os


"""
strip all images in dataset
"""
csv_path = "./clinical data.csv"
df = pd.read_csv(csv_path)
patient_ids = list(df['Scan id']) # create list of files names ending in 'nii.gz'


for patient in tqdm(patient_ids):
    files = os.listdir(f"./{patient}/anat/")
    files = [file for file in files if 'nii.gz' in file] # only keep files that end in 'nii.gz'
    
    for file in files: 
        input_path = f"./{patient}/anat/{file}"
        save_path = f"../stripped/{patient}/anat/{file}"
        print(f"{patient} // input: {input_path} ---> Output: {save_path}")
        # Run SynthStrip Model && Save images in stripped folder
        os.system(f"mri_synthstrip -i {input_path} -o {save_path}")
        
"""
view stripped images
"""

path = "/path/to/stripped_image.nii.gz".   # (i.e. save_path)
img_obj = nib.load(path)
images = img_obj.get_fdata().T
images.shape

for count in range(num_slices):  # in my case I had 44 slices... (Height x Width x num_slices) or (num_slices x Height x Width)
  # Adds a subplot at the 1st position
  fig.add_subplot(rows, columns, count+1)
  # showing image
  x = images[count,:,:]
  plt.imshow(x)
  plt.axis('off')
