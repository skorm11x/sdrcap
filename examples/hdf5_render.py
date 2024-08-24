"""
    Example showing hdf5 datasets and attributes in CLI
"""

import h5py


def print_hdf5_structure(filepath):
    """Print out basic information on HDF5 file.

    Args:
        filepath (str): string of location of hdf5 file.
    """
    with h5py.File(filepath, "r") as f:
        print("Root Group Attributes:")
        for attr_name, attr_value in f.attrs.items():
            print(f"  {attr_name}: {attr_value}")

        print("\nDatasets:")

        def print_datasets(name, obj):
            if isinstance(obj, h5py.Dataset):
                print(f"Dataset: {name}")
                print(f"  Shape: {obj.shape}")
                print(f"  Dtype: {obj.dtype}")
                for attr_name, attr_value in obj.attrs.items():
                    print(f"  Dataset Attribute: {attr_name} = {attr_value}")

        f.visititems(print_datasets)


if __name__ == "__main__":
    FILEPATH = "outputs/test.hdf5"
    print_hdf5_structure(FILEPATH)
