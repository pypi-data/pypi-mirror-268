# CoastSeg

<!--  [![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/2320sharon/CoastSeg/blob/main/coastseg_for_google_colab.ipynb) -->

[![image](https://img.shields.io/pypi/v/coastseg.svg?color=%23ec3dc8)](https://pypi.python.org/pypi/coastseg)
</br>
[![image](https://github.com/SatelliteShorelines/CoastSeg/actions/workflows/pip_install_e.yml/badge.svg)](https://github.com/SatelliteShorelines/CoastSeg/actions)

[![Last Commit](https://img.shields.io/github/last-commit/SatelliteShorelines/CoastSeg)](https://github.com/Doodleverse/segmentation_gym/commits/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/SatelliteShorelines/CoastSeg/graphs/commit-activity)
[![Wiki](https://img.shields.io/badge/wiki-documentation-forestgreen)](https://github.com/SatelliteShorelines/CoastSeg/wiki)
![GitHub](https://img.shields.io/github/license/Doodleverse/segmentation_gym)
[![Wiki](https://img.shields.io/badge/discussion-active-forestgreen)](https://github.com/SatelliteShorelines/CoastSeg/discussions)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)


<img src="https://user-images.githubusercontent.com/61564689/212394936-263ec9fc-fb82-45b8-bc79-bc57dafdae73.gif" width="350" height="350">

### Table of Contents

- [Installation Instructions](#installation-instructions)
- [Getting Started](#getting-started)
- [CoastSeg Update Guide](#coastseg-update-guide)

### Useful Links

- [Wiki](https://github.com/SatelliteShorelines/CoastSeg/wiki)
- [Discussion](https://github.com/SatelliteShorelines/CoastSeg/discussions)
- [Contribution Guide](https://github.com/Doodleverse/CoastSeg/wiki/13.-%5BADVANCED%5D-Contribution-Guide)

## What is CoastSeg?

Coastseg stands for Coastal Segmentation, it is an interactive jupyter notebook for downloading satellite imagery with [CoastSat](https://github.com/kvos/CoastSat) and applying Doodleverse/[Zoo](https://github.com/Doodleverse/segmentation_zoo) image segmentation models to satellite imagery. CoastSeg provides an interactive interface for drawing Regions of Interest (ROIs) on a map, downloading satellite imagery, loading geojson files, extracting shorelines from satellite imagery, and much more. In a nutshell, it is ...

- ... an easy way to download time-series of cloud-masked and post-processed satellite imagery anywhere in the world
- ... a mapping extension for [CoastSat](https://github.com/kvos/CoastSat) using [Segmentation Zoo](https://github.com/Doodleverse/segmentation_zoo) models.
- ... an interactive interface to download satellite imagery using CoastSat from Google Earth Engine
- ... an interactive interface for extracting shorelines from satellite imagery
- ... an interactive interface to apply segmentation models to satellite imagery

In more detail, CoastSeg represents the following advances in satellite-derived shoreline workflows:

1. An emulation of the CoastSat methodology for defining a shoreline extraction project, image downloading, shoreline extraction, shoreline filtering, and tide correction, all within a single jupyter notebook that can be accessed online
2. A pip-installable package for CoastSat workflows
3. Use of concurrency for image downloads from Google Earth Engine
4. A faster and more convenient API-based methodology for tidal height estimation, using pyTMD
5. An initial implementation of an alternative shoreline mapping workflow using Zoo models from the Doodleverse
6. A conda environment that can work on secure networks
7. Script-based data wrangling utilities
8. Hyperparameter experimentation and tracking using an organizational workflow idea called ‘Sessions’
9. Supporting databases for transects, reference shorelines, beach slopes, and other useful metadata variables
10. A deep-learning based shoreline extraction workflow (still in development)

Version 1 is now stable, and we have a lot of planned new features for version 2.

![coastseg_main_flow_updated](https://github.com/Doodleverse/CoastSeg/assets/61564689/ac9076bd-bf40-44c5-a686-0fdc1acf8656)


- Create ROIs(regions of interest) along the coast and automatically load shorelines on the map.
- Use Google Earth Engine to automatically download satellite imagery for each ROI clicked on the map.
- Coastseg can automatically extract shorelines from downloaded satellite imagery.


## Installation Instructions

We recommend that you use Windows 10, Windows 11, or Ubuntu Linux. Mac users, please see [here](https://github.com/Doodleverse/CoastSeg/wiki/01.-How-to-Install-CoastSeg#mac-users)

In order to use Coastseg you need to install Python packages in an environment. We recommend you use [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) to install the python packages in an environment for Coastseg. 

After you install miniconda/Anaconda on your PC, open the Anaconda prompt or Terminal in Mac and Linux and use the `cd` command (change directory) to go the folder where you have downloaded the Coastseg repository.

We highly recommend you install CoastSeg using `conda` following the instructions in [Install from conda-forge](#install-from-conda-forge).

## Install from conda-forge
1. Create an miniconda/Anaconda environment and Activate it
- This command creates an anaconda environment named `coastseg` and installs `python 3.10` in it.
  ```bash
  conda create --name coastseg python=3.10 -y
  conda activate coastseg
  ```

2. Install coastseg 

   ```bash
   conda install -c conda-forge coastseg
   ```
3. (Optional) Install Optional Dependencies
    - Only install these dependencies if you plan to use CoastSeg's Zoo workflow notebook. 
    ```bash
   pip install tensorflow
   pip install transformers
   ```  

## Install from Pypi
1. Create an miniconda/Anaconda environment
- This command creates an anaconda environment named `coastseg` and installs `python 3.10` in it.
  ```bash
  conda create --name coastseg python=3.10 -y
  ```

2. Activate your conda environment

   ```bash
   conda activate coastseg
   ```

- If you have successfully activated coastseg you should see that your terminal's command line prompt should now start with `(coastseg)`.

<img src="https://user-images.githubusercontent.com/61564689/184215725-3688aedb-e804-481d-bbb6-8c33b30c4607.png" 
     alt="coastseg activated in anaconda prompt" width="350" height="150">

3. Install Conda Dependencies
   - CoastSeg requires `jupyterlab` and `geopandas` to function properly so they will be installed in the `coastseg` environment.
   - [Geopandas](https://geopandas.org/en/stable/) has [GDAL](https://gdal.org/) as a dependency so its best to install it with conda.
   - Make sure to install geopandas from the `conda-forge` channel to ensure you get the latest version.
   - Make sure to install both jupyterlab and geopandas from the conda forge channel to avoid dependency conflicts
     ```bash
     conda install -c conda-forge geopandas -y
     ```
4. Install the CoastSeg from PyPi
   ```bash
   pip install coastseg
   ```
5. Uninstall the h5py installed by pip and reinstall with conda-forge
   - `pip install jsonschema==4.19.0` is a temporary command you have to run until issue https://github.com/stac-utils/pystac/issues/1214 is resolved
   ```bash
   pip install jsonschema==4.19.0 --user  
   pip uninstall h5py -y
   conda install -c conda-forge h5py -y
   ```
## **Having Installation Errors?**

Use the command `conda clean --all` to clean old packages from your anaconda base environment. Ensure you are not in your coastseg environment or any other environment by running `conda deactivate`, to deactivate any environment you're in before running `conda clean --all`. It is recommended that you have Anaconda prompt (terminal for Mac and Linux) open as an administrator before you attempt to install `coastseg` again.

#### Conda Clean Steps

```bash
conda deactivate
conda clean --all
```

# Getting Started
Check out the rest of the [wiki](https://github.com/Doodleverse/CoastSeg/wiki) for more tutorials

## Prerequisites
1. Sign up to use Google Earth Engine Python API

-Request access to Google Earth Engine at https://signup.earthengine.google.com/

-It takes about 1 day for Google to approve requests.

## Installation & SetUp
1. Activate the coastseg conda environment
   ```bash
   conda activate coastseg
   ```
- If you have successfully activated coastseg you should see that your terminal's command line prompt should now start with `(coastseg)`.

<img src="https://user-images.githubusercontent.com/61564689/184215725-3688aedb-e804-481d-bbb6-8c33b30c4607.png" 
     alt="coastseg activated in anaconda prompt" width="350" height="150">

2. Download CoastSeg from GitHub
```
git clone coastseg --depth 1 https://github.com/Doodleverse/CoastSeg.git
```
## Extract Shorelines
1. Launch Jupyter Lab

- Run this command in the coastseg directory to launch the notebook `SDS_coastsat_classifier`
  ```bash
  conda activate coastseg
  jupyter lab SDS_coastsat_classifier.ipynb
  ```
2. Authenticate with Google Earth Engine
![auth_cell_cropped](https://github.com/Doodleverse/CoastSeg/assets/61564689/642c8353-bfab-4458-a248-a8efce01f1ee)
4. Draw an Bounding Box
6. Generate ROI (Region of Interest)
7. Load Transects
![load_rois_then_transects_on_map_demo](https://github.com/Doodleverse/CoastSeg/assets/61564689/d53154b0-7a63-470f-91ec-dabdf7d4a100)

8. Modify the Settings
   - Change the satellites to L8 and L9
   - Change the dates to 12/01/2023 - 03/01/2024
   - Change the size of the reference shoreline buffer
   - Click `Save Settings`
9. Name the Session
10. Extract Shorelines
![save_settings_download_extract](https://github.com/Doodleverse/CoastSeg/assets/61564689/3548a9ce-a190-4c95-b495-0ff75484fdb2)

## Apply Tidal Correction to Extracted Shorelines (Optional) 
  1. Download the tide model
      - Before tidal correction can be applied the tide model must be downloaded
      - Follow the tutorial: [How to Download Tide Model](https://github.com/Doodleverse/CoastSeg/wiki/09.-How-to-Download-Tide-Model)
  2. Load the Session with Extracted Shorelines
      - Re-open the jupyter notebook
      - Under the Kernal menu Click 'restart and clear outputs of all cells'
      - Click Load Session and load the same we made before ''
  3. Click Correct Tides
    - Click the ROI ID from the dropdown
    - Enter Beach Slope
    - Enter Beach Elevation relative to Mean Sea Level
![load_session_correct_tides_demo](https://github.com/Doodleverse/CoastSeg/assets/61564689/d7a34d13-7c01-4a30-98b3-706a63195aa7)



# CoastSeg Update Guide

This guide is designed to help you easily update CoastSeg, whether you're updating to a specific version, the latest version, applying a patch, or updating code and notebooks from GitHub.

## Step 1: Install CoastSeg from PyPi

### Option 1:  Update to the latest version
1. **Install CoastSeg from PyPi**
   - To ensure you have the latest features and fixes, use this command:
   ```bash
     pip install coastseg --upgrade
   ```
  - Don't worry if you see the warning message below. This is normal
  ```bash
    "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts."
  ```

2. **Install jsonschema**
   - This is necessary to run coastseg in a jupyter notebook. 
  ```bash
   pip install jsonschema==4.19.0 --user
  ```

### Option 2:  Update to a Specific Version
1. **Install CoastSeg from PyPi**
   - If you need a specific version of CoastSeg, use this command:
   -  Replace <version> with the desired version number (e.g., 1.1.26).
   ```bash
    pip install coastseg==<version>
   ```
  - Don't worry if you see the warning message below. This is normal
  ```bash
    "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts."
  ```
2. **Install jsonschema**
   - This is necessary to run coastseg in a jupyter notebook. 
  ```bash
   pip install jsonschema==4.19.0 --user
  ```

## Step 2: Update Code and Notebooks from GitHub</h2>
(Optional) Follow these steps if you want the latest notebooks or code updates from the CoastSeg GitHub repository.
<details>
  <summary><strong>Click to expand instructions</strong></strong></summary>
    
  ### Step 1: Open CoastSeg in Anaconda
   1. Open Anaconda Prompt
   2. Activate the coastseg environment
   ```bash
     conda activate coastseg
   ```
3. Go to your coastseg location
```bash
cd <coastseg location>
```
### Step 2: Check for a Remote Connection to CoastSeg Repository
-Run the command below. In the output of this command you should see `origin  https://github.com/Doodleverse/CoastSeg.git (fetch)`
```
git remote -v
```
![git remote output](https://github.com/Doodleverse/CoastSeg/assets/61564689/adbb9783-0f0e-4081-ad3f-cbfb00964a9d)
- If you don't see this output, then run the following command
  ```bash
   git remote add origin  https://github.com/Doodleverse/CoastSeg.git
   git pull origin main
  ```
### Step 3: Pull the Latest Changes
   1. Run the command below
      ```
       git pull origin main
      ```
   2. If you recieve an error message like the one shown below then proceed to 3, otherwise go to [Go to Step 4: Verify Update Success](#step-4-verify-update-success)
      
       ```
           Please commit your changes or stash them before you merge
           Aborting
       ```
       
      <img width="437" alt="git_pull_fail" src="https://github.com/Doodleverse/CoastSeg/assets/61564689/fd7ebceb-11f4-4c68-8aad-19f4d5f85030">

   3.  Run the command below:

  - **WARNING** This will clear out anything you have written to the `certifications.json` make sure to save that file to a new location then move it back when you're done upgrading
       
  ```
         git fetch origin
         git reset --hard origin/main
         git pull origin main
  ```
### Step 4: Verify Update Success
```
git status
```
- This command should return the following message
- ```
  On branch main
  Your branch is up to date with 'origin/main'.
  ```

</details>
<br>

# Authors

Package maintainers:

- [@dbuscombe-usgs](https://github.com/dbuscombe-usgs)  Contracted to USGS Pacific Coastal and Marine Science Center.
- [@2320sharon](https://github.com/2320sharon) : Lead Software Developer / Contracted to USGS Pacific Coastal and Marine Science Center.

Contributions:

- [@ebgoldstein](https://github.com/ebgoldstein)
- [@venuswku](https://github.com/venuswku)
- [@robbibt](https://github.com/robbibt)
- [@edlazarus](https://github.com/edlazarus)
- Beta testers: Catherine Janda, Ann Gibbs, Jon Warrick, Andrea O’Neill, Kathryn Weber, Julia Heslin (USGS)
- We would like to express our gratitude to all the contributors who made this release possible. Thank you to everyone who tested the beta versions of coastseg and provided us with the feedback we needed to improve coastseg. Thanks also to the developers and maintainers of pyTMD, DEA-tools, xarray, and GDAL, without which this project would be impossible

## Citations

Thank you to all the amazing research who contributed their transects to coastseg.

1. Hawaii small islands https://pubs.usgs.gov/of/2011/1009/data.html
2. Barter Island, Alaska https://www.sciencebase.gov/catalog/item/5fa1f10ad34e198cb793cee4
3. Pacific Northwest, Gulf, and SE USA: Dr Sean Vitousek, USGS-PCMSC, based on DSAS transects
4. Atlantic barrier islands: https://www.sciencebase.gov/catalog/item/5d5ece47e4b01d82ce961e36
5. Mexico, New Zealand, Japan, Chile, Peru all from: https://zenodo.org/record/7758183#.ZCXZMcrMJPY
6. Snyder, A.G., and Gibbs, A.E., 2019, National assessment of shoreline change: A GIS compilation of updated vector shorelines and associated shoreline change data for the north coast of Alaska, Icy Cape to Cape Prince of Wales: U.S. Geological Survey data release, https://doi.org/10.5066/P9H1S1PV.
7. Gibbs, A.E., Ohman, K.A., Coppersmith, R., and Richmond, B.M., 2017, National Assessment of Shoreline Change: A GIS compilation of updated vector shorelines and associated shoreline change data for the north coast of Alaska, U.S. Canadian border to Icy Cape: U.S. Geological Survey data release, https://doi.org/10.5066/F72Z13N1.
8. Himmelstoss, E.A., Kratzmann, M., Hapke, C., Thieler, E.R., and List, J., 2010, The National Assessment of Shoreline Change: A GIS Compilation of Vector Shorelines and Associated Shoreline Change Data for the New England and Mid-Atlantic Coasts: U.S. Geological Survey Open-File Report 2010-1119, available at https://pubs.usgs.gov/of/2010/1119/.
9. Kilian Vos. (2023). Time-series of shoreline change along the Pacific Rim (v1.4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7758183
10. Vos, Kilian, Wen, Deng, Harley, Mitchell D., Turner, Ian L., & Splinter, Kristen D. (2022). Beach-face slope dataset for Australia (Version 2) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7272538
11. Gibbs, A.E., Jones, B.M., and Richmond, B.M., 2020, A GIS compilation of vector shorelines and coastal bluff edge positions, and associated rate-of-change data for Barter Island, Alaska: U.S. Geological Survey data release, https://doi.org/10.5066/P9CRBC5I.

To compile into a pdf use
```
pandoc paper.md -o paper.pdf --bibliography paper.bib
```
