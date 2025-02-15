import json
import os
from pathlib import Path
import argparse
import subprocess
import time
import datetime

def sort_gltf_file(file_path):
    print(f"Starting to process file: {file_path}")
    
    # Read the GLTF file
    with open(file_path, 'r', encoding='utf-8') as f:
        gltf_data = json.load(f)
        print(f"File loaded successfully. Keys found: {list(gltf_data.keys())}")
    
    # Function to sort list
    def sort_list(input_list):
        if isinstance(input_list, list):
            print("Before sorting:", input_list)
            sorted_list = sorted(input_list, key=str.lower)
            print("After sorting:", sorted_list)
            return sorted_list
        return input_list
    
    # Sort materials if they exist
    if 'materials' in gltf_data:
        gltf_data['materials'] = sorted(gltf_data['materials'], key=lambda x: x.get('name', '').lower())
    
    # Sort meshes if they exist
    if 'meshes' in gltf_data:
        gltf_data['meshes'] = sorted(gltf_data['meshes'], key=lambda x: x.get('name', '').lower())
    
    # Sort nodes if they exist
    if 'nodes' in gltf_data:
        gltf_data['nodes'] = sorted(gltf_data['nodes'], key=lambda x: x.get('name', '').lower())
    
    # Check all possible locations for theme and tags
    for key in ['theme', 'tags']:
        # Check at root level
        if key in gltf_data:
            gltf_data[key] = sort_list(gltf_data[key])
        
        # Check in properties
        if 'properties' in gltf_data and isinstance(gltf_data['properties'], dict):
            if key in gltf_data['properties']:
                gltf_data['properties'][key] = sort_list(gltf_data['properties'][key])
        
        # Check in meta
        if 'meta' in gltf_data and isinstance(gltf_data['meta'], dict):
            if key in gltf_data['meta']:
                gltf_data['meta'][key] = sort_list(gltf_data['meta'][key])
        
        # Check in semanticTags
        if 'semanticTags' in gltf_data and isinstance(gltf_data['semanticTags'], dict):
            if key in gltf_data['semanticTags']:
                gltf_data['semanticTags'][key] = sort_list(gltf_data['semanticTags'][key])
    
    # Write the sorted data back to the file with 4-space indentation
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(gltf_data, f, indent=4, ensure_ascii=False)
        print(f"File saved successfully: {file_path}")

def open_in_blender(file_path):
    blender_path = r"C:\Program Files\Blender Foundation\Blender 4.3\blender-launcher.exe"
    if not Path(blender_path).exists():
        print(f"Error: Blender not found at {blender_path}")
        return False
    
    try:
        print(f"\nAttempting to open Blender...")
        print(f"Blender path: {blender_path}")
        print(f"File path: {file_path}")
        
        # Convert paths to absolute paths
        blender_path = str(Path(blender_path).resolve())
        file_path = str(Path(file_path).resolve())
        
        # Create a Python script to delete cube and import the GLTF
        import_script = [
            "import bpy",
            "# Delete default cube",
            "if 'Cube' in bpy.data.objects:",
            "    cube = bpy.data.objects['Cube']",
            "    bpy.data.objects.remove(cube, do_unlink=True)",
            "# Import GLTF file",
            "bpy.ops.import_scene.gltf(filepath=r'{}')".format(file_path),
            "# Set scale to 1.0 for all imported objects",
            "for obj in bpy.context.selected_objects:",
            "    obj.scale = (1.0, 1.0, 1.0)",
            "    # Apply scale",
            "    bpy.context.view_layer.objects.active = obj",
            "    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)",
            "# Switch to material preview mode",
            "for area in bpy.context.screen.areas:",
            "    if area.type == 'VIEW_3D':",
            "        for space in area.spaces:",
            "            if space.type == 'VIEW_3D':",
            "                space.shading.type = 'MATERIAL'"
        ]
        
        # Save the import script
        script_path = Path(file_path).parent / "temp_import.py"
        with open(script_path, 'w') as f:
            f.write("\n".join(import_script))
        
        # Run Blender with the Python script
        cmd = [blender_path, "--python", str(script_path)]
        print(f"Running command: {cmd}")
        
        subprocess.Popen(cmd, 
                        creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NO_WINDOW)
        print("Blender launch command executed")
        
        return True
    except Exception as e:
        print(f"Error opening Blender: {str(e)}")
        print(f"Error type: {type(e)}")
        return False

def open_in_blender_and_export(file_path, custom_dir=None):
    blender_path = r"C:\Program Files\Blender Foundation\Blender 4.3\blender-launcher.exe"
    if not Path(blender_path).exists():
        print(f"Error: Blender not found at {blender_path}")
        return False
    
    try:
        print(f"\nAttempting to open Blender...")
        print(f"Blender path: {blender_path}")
        print(f"File path: {file_path}")
        
        # Convert paths to absolute paths
        blender_path = str(Path(blender_path).resolve())
        file_path = str(Path(file_path).resolve())
        
        # Create timestamp and directory structure
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y_%d_%H_%M_%S")
        file_path_obj = Path(file_path)
        
        if custom_dir:
            # Use custom directory with timestamp subfolder
            export_dir = Path(custom_dir) / f"{timestamp}_{file_path_obj.stem}"
        else:
            # Use default ORGANIZED directory
            export_dir = file_path_obj.parent.parent / "ORGANIZED" / f"{timestamp}_{file_path_obj.stem}"
        
        export_dir.mkdir(parents=True, exist_ok=True)
        
        # Create export path with timestamp
        export_path = export_dir / f"{timestamp}_{file_path_obj.stem}AS1ORG.gltf"
        
        # Create a Python script for import and export
        import_script = [
            "import bpy",
            "# Delete default cube",
            "if 'Cube' in bpy.data.objects:",
            "    cube = bpy.data.objects['Cube']",
            "    bpy.data.objects.remove(cube, do_unlink=True)",
            "# Import GLTF file",
            "bpy.ops.import_scene.gltf(filepath=r'{}')".format(file_path),
            "# Set scale to 1.0 for all imported objects",
            "for obj in bpy.context.selected_objects:",
            "    obj.scale = (1.0, 1.0, 1.0)",
            "    # Apply scale",
            "    bpy.context.view_layer.objects.active = obj",
            "    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)",
            "# Switch to material preview mode",
            "for area in bpy.context.screen.areas:",
            "    if area.type == 'VIEW_3D':",
            "        for space in area.spaces:",
            "            if space.type == 'VIEW_3D':",
            "                space.shading.type = 'MATERIAL'",
            "# Select all objects and export",
            "bpy.ops.object.select_all(action='SELECT')",
            "bpy.ops.export_scene.gltf(filepath=r'{}', export_format='GLTF_SEPARATE')".format(export_path)
        ]
        
        # Save the import script
        script_path = Path(file_path).parent / "temp_import.py"
        with open(script_path, 'w') as f:
            f.write("\n".join(import_script))
        
        # Run Blender with the Python script
        cmd = [blender_path, "--python", str(script_path)]
        print(f"Running command: {cmd}")
        
        process = subprocess.Popen(cmd, 
                                 creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NO_WINDOW)
        
        print("Blender launch command executed")
        print(f"Exporting to: {export_path}")
        
        # Wait a bit before deleting the temp script
        time.sleep(2)
        
        # Delete the temporary script
        try:
            script_path.unlink()
            print("Temporary script file deleted")
        except Exception as e:
            print(f"Warning: Could not delete temporary script: {e}")
        
        return True
    except Exception as e:
        print(f"Error opening Blender: {str(e)}")
        print(f"Error type: {type(e)}")
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Sort GLTF and JSON files.')
    parser.add_argument('-b', action='store_true', help='Open in Blender after sorting')
    parser.add_argument('-be', action='store_true', help='Open in Blender, then export with AS1ORG suffix')
    parser.add_argument('-r', type=str, help='Specify custom export directory path')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get the directory containing the script
    script_dir = Path(__file__).parent
    sample_dir = script_dir / 'SAMPLE_MODEL'
    
    # Add debug information and directory check
    print(f"Looking for .gltf and .json files in: {sample_dir}")
    if not sample_dir.exists():
        print(f"Error: Directory '{sample_dir}' does not exist!")
        print("Please create the directory or update the path.")
        return
    
    # Find all .gltf and .json files in the SAMPLE_MODEL
    target_files = list(sample_dir.glob('*.gltf')) + list(sample_dir.glob('*.json'))
    print(f"Found files: {[f.name for f in target_files]}")
    
    if not target_files:
        print("No .gltf or .json files found in SAMPLE_MODEL")
        print("Files in directory:", list(sample_dir.iterdir()))
        return
    
    # Store .gltf file path for later if -b or -be flag is set
    gltf_file = None
    if args.b or args.be:
        gltf_files = [f for f in target_files if f.suffix.lower() == '.gltf']
        if gltf_files:
            gltf_file = gltf_files[0]
    
    # Process each file
    for file_path in target_files:
        try:
            print(f"\nProcessing {file_path.name}...")
            sort_gltf_file(file_path)
            print(f"Successfully sorted {file_path.name}")
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
    
    # Open in Blender after all files are processed
    if gltf_file:
        print("\nAll files processed. Opening GLTF in Blender...")
        if args.be:
            if args.r:
                # Create custom directory if it doesn't exist
                custom_dir = Path(args.r)
                try:
                    custom_dir.mkdir(parents=True, exist_ok=True)
                    print(f"Using custom export directory: {custom_dir}")
                    open_in_blender_and_export(str(gltf_file), custom_dir)
                except Exception as e:
                    print(f"Error creating custom directory {custom_dir}: {e}")
                    return
            else:
                open_in_blender_and_export(str(gltf_file))
        elif args.b:
            open_in_blender(str(gltf_file))

if __name__ == "__main__":
    main()
