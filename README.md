TUTORIAL - AS1 Model Parse Script 

DETAILS:
The AS1 Model Parse Script: 'MODEL_PARSE.py', was written to organize the various components of a typical .gltf file, including the associated 
nodes, materials and meshes. Using arguments, the script can also be directed to open the model in Blender after being organized. There are
also additional options, such as to automatically export from Blender. Please read the 'STEPS' section carefully, as it will help you identify 
which method for running the script aligns most closely with your intended workflow (primarily for how you intend to use Blender, if at all).

PREREQUISITES:
1) It is assumed that you have Python installed on your machine. The AS1 script has been tested up to version 3.13.2. If you do not have
Python installed, then please download it from: 'https://www.python.org/downloads/release/python-3132/', and then reboot before using the AS1
script. 
2) For Blender usage, it is assumed that you have Blender installed in it's default location: C:\Program Files\Blender Foundation\Blender 4.3;
if you do not, then please download it from: 'https://www.blender.org/download/release/Blender4.3/blender-4.3.2-windows-x64.msi/', and then
install it before running the AS1 script.
3) For Blender usage, it is assumed that you are using Blender 4.3.2. Earlier versions of Blender may be less stable, so please ensure your
installation is up to date.

PURPOSE:
The structure of a .gltf file may differ depending on the source you got it from, such as Quixel Meganscans (Fab), Artstation, TurboSquid, 
etc. As such, the AS1 script organizes nodes into a standardized format to avoid discrepencies.

USE:
There are several ways to run the AS1 script, depending on your needs. The 'STEPS' section below outlines several scenarios for usage. 

STEPS:
A) Download the model you wish to work with to your local machine. 
B) After you have your model downloaded locally, place the desired model's directory in the 'SAMPLE_MODEL' directory.
C) Decide on your scenario:
    1) Run organization pass on model only.
    2) Run organization pass on model, then open in Blender to begin a workflow.
    3) Run organization pass on model, then export from Blender using standard export settings.
    4) Run organization pass on model, export from Blender using standard export settings and output to specified directory.
D) Run the 'MODEL_PARSE.py' script either with, or without, arguments (which are described below):


  #1) Standard Organization Pass:
  Type: Non-Blender Use-Case (Vanilla)
  Argument: N/A
  Details: The 'Standard Organization Pass' includes *no* arguments, and only organizes the model's structure (both .gltf itself, as well as
  the .json file).
    EXAMPLE: 
    's:/DOPPLE/AS1/MODEL_PARSE.py'

  #2) Standard Organization Pass *with* Blender Launch *Only*:
  Type: Blender Workflow Use-Case
  Arguemnt: '-b'
  Details: The 'Standard Pass with Blender Launch' first organizes your .gltf model files, opens the model in Blender, and then halts so that
  you may begin a workflow within Blender (which could include the use of a specific plugin or toolset). It is assumed that you will choose 
  your own export options later, since they will differ depending on your workflow(s) and/or any plugins used. 
    NOTE: If *only* want to export from within Blender after the organization and do *not* want to run a workflow, 
          then use scenario #3), which is: 'Standard Organizaiton Pass with Blender Export'.   

  #3) Standard Organizaiton Pass with Blender Export:
  Type: Blender Export Only Use-Case
  Arguemnt: '-b'
  Details: 'Standard Organizaiton Pass with Blender Export' will 

FULL ARGUMENTS LIST:
'-b' = Blender Launch
'-be' = Blender Export
'-d', '(specificed directory)'] = Specific Output Destination "s:\project\models"
