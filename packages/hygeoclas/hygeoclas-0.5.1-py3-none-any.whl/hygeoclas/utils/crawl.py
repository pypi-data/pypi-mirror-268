import numpy as np
import re

def get_last_class_name(filePath: str):
    """Gets the name of the last class defined in a file.

    Args:
        filePath (str): The path of the file.

    Returns:
        lastClass (str): The name of the last class defined in the file.
        "FileNotFoundError": If the file is not found.

    Raises:
        IndexError: If no classes are found in the file.
    """
    try:
        with open(filePath, 'r') as file:
            content = file.read()
            definedClasses = re.findall(r"class\s+(\w+)", content)
            lastClass = definedClasses[-1]
            return lastClass    
    except FileNotFoundError:
        return "FileNotFoundError"
    except IndexError:
        raise IndexError(f"No classes were found in {filePath}.")

def get_udf_record(filePath: str, recordName: str, **kwargs) -> np.array:
    """
    Extracts a specific record from a UDF file.

    Args:
        filePath (str): The path to the UDF file.
        recordName (str): The name of the record to extract.

    Kwargs:
        cleaned (bool): If True, removes zero values from the record. Default is False.

    Returns:
        np.array: An array containing the values of the specified record.

    Note:
        This function will print the number of records with incomplete values that were not imported.
    """
    filePath = filePath
    with open(filePath, 'r') as content:
        lines = content.readlines()

    headerRecordIndex = next(i for i, line in enumerate(lines) if recordName in line)
    recordIndex = next(i for i, record in enumerate(lines[headerRecordIndex].split(" ")[1:-1]) if recordName in record)
    
    record = []
    headerRecordLength = len(lines[headerRecordIndex].split(" ")[1:-1])
    errors = 0
    for recordLine in lines[headerRecordIndex+1:]:
        if recordLine == "0\n":
            break
        else:
            if len(recordLine.split("\t")) != headerRecordLength:
                errors += 1
                continue
            else:
                record.append(float(recordLine.split("\t")[recordIndex]))

    if errors > 0:
        print(f"Number of records with incomplete values and that were not imported: {errors}")

    if kwargs.get("cleaned", False):
        record = [value for value in record if value != 0.0] 

    return np.array(record)