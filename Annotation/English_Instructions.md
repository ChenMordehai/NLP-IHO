# Doccano Annotation Tool Setup and Usage Guide

This guide provides a step-by-step process to install, configure, and use Doccano for annotation tasks. Follow the instructions below to set up the environment, create users, launch the services, and start annotating.

---

## Table of Contents
- [Installation](#installation)
  - [Option 1: Using Provided Environment](#option-1-using-provided-environment)
  - [Option 2: Creating a New Virtual Environment](#option-2-creating-a-new-virtual-environment)
- [Initialize the Doccano Services](#Initialize-the-doccano-services)
- [Accessing the Web Interface](#accessing-the-web-interface)
- [Project Setup](#project-setup)
- [Adding Members](#adding-members)
- [Importing Labels](#importing-labels)
- [Uploading the Dataset](#uploading-the-dataset)
- [Annotating the Records](#annotating-the-records)
- [Exporting Annotations](#exporting-annotations)
- [Stopping the Services](#stopping-the-services)

---

## Installation

### Option 1: Using Provided Conda Environment
[Link to environment directory](https://drive.google.com/file/d/1tG4jZjARH6H29paLDeCvn7B4muejV4KH/view?usp=drive_link)
1. Unpack the doccano_env.zip directory to **C:\Users\..\Anaconda3\envs**
2. Open a anaconda prompt.
2. Activate doccano_env:
    
bash
   conda activate doccano_env


### Option 2: Creating a New Virtual Environment
1. Open a command prompt.
2. Create a new virtual environment:
   
bash
   python -m venv doccano_env

3. Activate the environment:
   - **On Windows:**
     
bash
     doccano_env\Scripts\activate

   - **On Unix or macOS:**
     
bash
     source doccano_env/bin/activate

4. Install Doccano using pip:
   
bash
   pip install doccano


---

## Initialize the Doccano Services

1. In the activated environment, run the following commands in the **first anaconda prompt**:

   - Initialize Doccano:
     
bash
     doccano init

   - Create two users:
     
bash
     doccano createuser --username user1 --password nlpiho && doccano createuser --username user2 --password nlpiho

   - Start the web server on port 8080:
     
bash
     doccano webserver --port 8080


2. Open a **second anaconda prompt** (keep the first one running) and start the task service:
   
bash
   doccano task


### Re-accessing the Services (After Initialization)
- To launch the web server again:
  
bash
  doccano webserver --port 8080

- In a **new command prompt**, start the task service:
  
bash
  doccano task


---

## Accessing the Web Interface

1. Open your web browser and go to: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
2. Log in using one of the created users (either user1 or user2) with the password nlpiho.

---

## Project Setup

If a project is not yet initialized:

1. Click on **Projects** in the sidebar.
2. Click on **Create**.
3. Select **Sequence Labeling**.
4. Fill in the project name and description.
5. Check the box for **Allow overlapping spans**.
6. Click **Create**.

---

## Adding Members

1. Navigate to **Members**.
2. Click **Add**.
3. Select **User Search APIs**.
4. Choose the other user (user1 or user2).
5. Set the role to **Project Admin**.
6. Click **Save**.

---

## Importing Labels

1. Go to **Labels**.
2. Click **Actions**.
3. Select **Import Labels**.
4. Use the file input to select the provided labels file.
5. Click **Import**.

---

## Uploading the Dataset

1. Go to **Dataset**.
2. Click **Actions**.
3. Select **Import Dataset**.
4. Choose **JSONL** as the file format.
5. Select your dataset file (processed by our script).
6. Click **Import**.

---

## Annotating the Records

1. Once the dataset is uploaded, click **Start Annotation**.
2. For each record, after finishing the annotation, press **ENTER** or click the **V** button to approve the annotation.

---

## Exporting Annotations

After both annotators have completed their work:

1. Go to **Dataset**.
2. Click **Actions**.
3. Select **Export Dataset**.
4. Choose **JSONL** as the file format.
5. Check the box for **Export only approved documents**.
6. Click **Export** to download the annotations.

---

## Stopping the Services

- To stop the running services, press CTRL+C in both command prompt windows.

---
