import json
import os

def concatenate_files(directory, output_file, pattern='SXXPYY'):
    """
    Concatenate APL JSON files matching a pattern from a directory.

    Parameters
    ----------
    directory : str
        The directory to search for JSON files.
    output_file : str
        The file to write the concatenated JSON data.
    pattern : str, optional
        Pattern to match in file names (default is 'SXXPYY').

    Returns
    -------
    None
        This function does not return a value, it writes data to a file.
    """
    concatenated_activities = []

    # Walk through all subdirectories and find JSON files matching the pattern
    for root, dirs, files in os.walk(directory):
        if root != directory:  # Exclude top-level directory
            for file in files:
                if pattern in file and file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        try:
                            data = json.load(f)
                        except ValueError as e:
                            print(f'Invalid APL {file_path}: %s' % e)
                            return None  # or: raise
                        if "activities" in data:
                            concatenated_activities.extend(data["activities"])

    # Write the concatenated activities to the output file
    with open(output_file, 'w+') as f:
        json.dump({"activities": concatenated_activities}, f, indent=4)

    return


def check_duplicate_ids(apl_file):
    """
    Check for duplicate IDs in an APL JSON file.

    Parameters
    ----------
    apl_file : str
        The path to the JSON file to check for duplicate IDs.

    Returns
    -------
    None
        This function does not return a value, it prints duplicate IDs if found.
    """
    # Open the file containing JSON data
    with open(apl_file, 'r') as file:
        data = file.read()

    # Parse the JSON
    parsed_data = json.loads(data)

    # Extract the activities
    activities = parsed_data['activities']

    # Create a set to store unique IDs
    unique_ids = set()

    # List to store duplicate IDs
    duplicate_ids = []

    # Iterate through activities
    for activity in activities:
        activity_id = activity['id']
        # Check if ID is already in the unique set
        if activity_id in unique_ids:
            duplicate_ids.append(activity_id)
        else:
            unique_ids.add(activity_id)

    # Print duplicate IDs, if any
    if duplicate_ids:
        print("Duplicate IDs found:")
        for duplicate_id in duplicate_ids:
            print(duplicate_id)
    else:
        print("No duplicate IDs found.")

    return