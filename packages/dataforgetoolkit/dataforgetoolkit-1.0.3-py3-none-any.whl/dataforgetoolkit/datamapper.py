import pandas as pd
import json
from dataforgetoolkit.common_utils import *


def map(report_file_path, transformation_file_path):
    """
    Map a CSV or Excel file based on a JSON transformation mapping.

    Args:
        report_file_path (str): Path to the CSV or Excel file.
        transformation_file_path (str): Path to the JSON transformation file.

    Returns:
        dict: Mapped data in dictionary format.
    """
    df = df = pd.read_csv(report_file_path)
    df = df.fillna('')
    try:
        with open(transformation_file_path, "r") as json_file:
            transformations = json.load(json_file)['transformation_mapping']
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format for transformations."}

    if transformations is None:
        transformations = {}

    # Update column names and values
    df = transform_model(df, transformations)
    return df.to_dict(orient='records')


def transform_model(df, transformation):
    """
    Transform the DataFrame based on the provided transformation mapping.

    Args:
        df (DataFrame): Input DataFrame.
        transformation (dict): Transformation mapping.

    Returns:
        DataFrame: Transformed DataFrame.
    """
    # List of column names to keep
    column_names = [transformation["column"]
                    for transformation in transformation]

    # Drop columns not in the column_names list
    columns_to_drop = [col for col in df.columns if col not in column_names]
    df.drop(columns=columns_to_drop, inplace=True)

    # Update column names and values as per the transformation
    for transformation in transformation:
        old_name = transformation["column"]
        new_name = transformation["new_name"]
        value_mappings = transformation["value_mappings"]

        if old_name in df.columns:
            print(f"Updating column '{old_name}' to '{new_name}'")
            df.rename(columns={old_name: new_name}, inplace=True)

            print(f"Updating values in column '{new_name}'")
            for value_mapping in value_mappings:
                for old_value, new_value in value_mapping.items():
                    df = apply_mapping_criteria(
                        df, new_name, old_value, new_value)
                    df[new_name] = df[new_name].replace(old_value, new_value)

    return df


def apply_mapping_criteria(df, column_name, old_value, new_value):
    """
    Apply mapping criteria to the DataFrame.

    Args:
        df (DataFrame): Input DataFrame.
        column_name (str): Column name to apply mapping criteria.
        old_value (str): Old value to be replaced.
        new_value (str): New value.

    Returns:
        DataFrame: Transformed DataFrame.
    """
    if old_value == DEFAULT_VALUE:
        df[column_name] = new_value
    elif old_value == FILTER_VALUE:
        df = df[df[column_name] != new_value]
    elif old_value.startswith(REPLACE_VALUE):
        # Replace substrings in column values
        substring = old_value.split("_", 1)[1]
        df[column_name] = df[column_name].str.replace(substring, new_value)
    elif old_value == CONCAT_VALUE:
        # Concatenate column values with a delimiter
        delimiter = new_value
        df[column_name] = df[column_name].apply(
            lambda x: delimiter.join(x) if isinstance(x, list) else x)
    elif old_value == UPPERCASE_VALUE:
        # Convert column values to uppercase
        df[column_name] = df[column_name].str.upper()
    elif old_value == LOWERCASE_VALUE:
        # Convert column values to lowercase
        df[column_name] = df[column_name].str.lower()
    # Add more conditions for other aggregations if needed
    return df
