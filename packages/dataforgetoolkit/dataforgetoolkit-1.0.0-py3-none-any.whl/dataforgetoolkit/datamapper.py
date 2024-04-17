import pandas as pd
import json
from dataforgetoolkit.common_utils import *

def map(report_file_path, transformation_file_path):
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
                    df = mapping_criteria(df, new_name, old_value, new_value)
                    df[new_name] = df[new_name].replace(old_value, new_value)

    return df


def mapping_criteria(df, new_name, old_value, new_value):
    if old_value == DAFULT_VALUE:
        df[new_name] = new_value
        pass
    if old_value == FILTER_VALUE:
        df = df[df[new_name] != new_value]
    return df