# Skull-Stripping
Method for stripping the skull of MRI Brain images.<br>
![Screenshot 2023-04-02 at 9 00 12 AM](https://user-images.githubusercontent.com/34732790/229357737-e180779e-9575-410f-bc05-f498588209e2.png)


SynthStrip Dataset and Model Instructions: https://surfer.nmr.mgh.harvard.edu/docs/synthstrip/ 

Steps to running on Macbook (.PKG):
1. Open terminal
2. export FREESURFER_HOME="/Applications/freesurfer/7.3.2"
3. source $FREESURFER_HOME/SetUpFreeSurfer.sh
4. which freeview  (check if it installed correctly)
5. Load Jupyter Notebook in same session
6. Us os.system to run the following
   "mri_synthstrip -i input_path.nii.gz -o outpu_path.nii.gz"


Synthstrip is a software that is part of a big software packaged for the analysis and visualization of structural and functionall neuroimaging data.
It was developed by the Laboratory for computational neuroimaging at the Athinoula A. Martinos Centor for Biomedical Imagings

References:<br>

arXiv: https://arxiv.org/abs/2203.09974

SynthStrip: Skull-Stripping for Any Brain Image.
A Hoopes, JS Mora, AV Dalca, B Fischl, M Hoffmann.
NeuroImage 206 (2022), 119474.

