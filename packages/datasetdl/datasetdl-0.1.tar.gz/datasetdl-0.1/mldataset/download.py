import shutil
from pathlib import Path

def dataset(dataset_name):
    """
    Copies a dataset from the 'datasets' directory of the package to the current working directory.

    Parameters:
    dataset_name (str): The name of the dataset file to copy (e.g., 'data.json', 'data.csv')

    Returns:
    str: Path to the copied dataset in the current working directory.
    """

    datasets_dir = Path(__file__).resolve().parent / 'datasets'
    source_path = datasets_dir / dataset_name
    destination_path = Path.cwd() / dataset_name
    shutil.copy(source_path, destination_path)
    
    return str(destination_path)
