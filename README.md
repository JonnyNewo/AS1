TUTORIAL - AS1 Model Parse Script 
_______________________________________________________________________________________________________________________________________________
DETAILS:

The AS1 Model Parse Script: 'MODEL_PARSE.py', was written to organize the various components of a typical .gltf file, including the associated 
nodes, materials and meshes. Using arguments, the script can also be directed to open the model in Blender after being organized. There are
also additional options, such as to automatically export from Blender. Please read the 'STEPS' section carefully, as it will help you identify 
which method for running the script aligns most closely with your intended workflow (primarily for how you intend to use Blender, if at all).

_______________________________________________________________________________________________________________________________________________
PREREQUISITES:

1) It is assumed that you have Python installed on your machine. The AS1 script has been tested up to version 3.13.2. If you do not have
Python installed, then please download it from: 'https://www.python.org/downloads/release/python-3132/', and then reboot before using the AS1
script. 

2) For Blender usage, it is assumed that you have Blender installed in it's default location: C:\Program Files\Blender Foundation\Blender 4.3;
if you do not, then please download it from: 'https://www.blender.org/download/release/Blender4.3/blender-4.3.2-windows-x64.msi/', and then
install it before running the AS1 script.

3) For Blender usage, it is assumed that you are using Blender 4.3.2. Earlier versions of Blender may be less stable, so please ensure your
installation is up to date.

_______________________________________________________________________________________________________________________________________________
PURPOSE:

The structure of a .gltf file may differ depending on the source you got it from, such as Quixel Meganscans (Fab), Artstation, TurboSquid, 
etc. As such, the AS1 script organizes nodes into a standardized format to avoid discrepencies.

_______________________________________________________________________________________________________________________________________________
USE:

There are several ways to run the AS1 script, depending on your needs. The 'STEPS' section below outlines several scenarios for usage. 

_______________________________________________________________________________________________________________________________________________
STEPS:

STEP A) Download the model you wish to work with to your local machine.
 
STEP B) After you have your model downloaded locally, place the desired model's directory in the 'SAMPLE_MODEL' directory.

STEP C) Decide which scenario fits your needs and/or workflow requirements:
    
___________1) Run organization pass on model only. (non-Blender)
    
___________2) Run organization pass on model, then open in Blender to begin a workflow. (no export included)
    
___________3) Run organization pass on model, then export from Blender using standard export settings. 
    
___________4) Run organization pass on model, export from Blender using standard export settings and output to specified directory.

STEP D) Run the 'MODEL_PARSE.py' script either with, or without, arguments (which are described below):


____#1) Standard Organization Pass:
  Type: Non-Blender Use-Case (Vanilla)

  Argument: N/A

  Details: The 'Standard Organization Pass' includes *no* arguments, and only organizes the model's structure (both .gltf itself, as well as
  the .json file).
    
EXAMPLE: 
    's:/DOPPLE/AS1/MODEL_PARSE.py'

____#2) Standard Organization Pass *with* Blender Launch:
  Type: Blender Workflow Use-Case
  
  Argument: '-b'
  
  Details: The 'Standard Pass with Blender Launch' first organizes your .gltf model files, opens the model in Blender, and then halts so that
  you may begin a workflow within Blender (which could include the use of a specific plugin or toolset). It is assumed that you will choose 
  your own export options later, since they will differ depending on your workflow(s) and/or any plugins used. 
    
  NOTE: If *only* want to export from within Blender after the organization and do *not* want to run a workflow, 
          then use scenario #3), which is: 'Standard Organizaiton Pass with Blender Export'.   

____#3) Standard Organizaiton Pass *with* Blender Export:
  Type: Blender Export Only Use-Case
  Argument: '-be'
  Details: 'Standard Organizaiton Pass with Blender Export' will open the model in Blender, perform a few helpful viewport toggles, and then
  export using default settings for .gltf. It's worth noting that Blender does not exit after the export if finished, but stays open until
  you close it.

____#4) Custom Output Location:
  Type: Blender Export Custom Location Use-Case
  Argument: '-r'
  Details: This argument is not intended to be run by itself, but in combination with a proceeding argument related to Blender usage. After 
  opening in Blender, the '-r' argument will export the newly organized .gltf to a custom location of your choice, rather than the default 
  directory it came from. 

_______________________________________________________________________________________________________________________________________________
ARGUMENTS LIST:

Blender Launch: '-b'
    
EXAMPLE:  s:/DOPPLE/AS1/MODEL_PARSE.py -b'

Blender Export: '-be'

EXAMPLE:  's:/DOPPLE/AS1/MODEL_PARSE.py -be'

Custom Output Destination: '-d [your desired system path]'
    
EXAMPLE:  's:/DOPPLE/AS1/MODEL_PARSE.py -d s:/OTHER_PROJECT_LOCATION'


_______________________________________________________________________________________________________________________________________________
QUALITY OF LIFE NOTES:

The AS1 Model Parse Script has a few built in things it does that are (hopefully) helpful to you. As an example, after the desired model is
seen Blender, the script both scales the model up to 1.0 from the default (which is quite small), and it also toggles on the 'Material Preview'
so that you see the model and it's corresponding texture immediately after Blender is opened, rather than having to toggle it of yourself. 
Another action the script takes automatically is to remove the default cube that's part of a default Blender scene. These are just a few 
examples, and again, they are actions carried out by the script automatically to better align with how a typical user interacts with Blender
in a creative capacity. 

_______________________________________________________________________________________________________________________________________________
SCREENSHOTS:

- Example Blender Screenshot following .gltf model organization, XYZ scale up to 1.0, default cube removal, and toggle on of Material Preview).
<img width="1920" alt="image" src="https://github.com/user-attachments/assets/a8836e33-107a-48bd-81d1-5891ad9bbadc" />


