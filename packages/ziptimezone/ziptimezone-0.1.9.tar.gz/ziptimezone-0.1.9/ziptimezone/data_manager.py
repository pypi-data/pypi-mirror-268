import os
import requests
import zipfile
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_and_extract_zip_data(file_path, data_url):
    """
    Downloads a ZIP file from the specified URL and extracts its contents into a predefined path.

    Args:
        file_path (str): The full path where the extracted file will be stored. The ZIP file will be temporarily stored in the same location.
        data_url (str): The URL from which to download the ZIP file containing the data.

    Ensures that if the data file at the file_path does not exist, it is downloaded and extracted.
    If the data file already exists, no action is taken.
    """
    if not os.path.exists(file_path):
        zip_path = file_path + '.zip'
        logging.info("Downloading ZIP code data...")
        try:
            response = requests.get(data_url)
            response.raise_for_status()  # Ensure the download succeeded
            with open(zip_path, 'wb') as f:
                f.write(response.content)

            # Extract ZIP file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(file_path))
            os.remove(zip_path)  # Remove the zip file after extraction

            logging.info("Data downloaded and extracted successfully.")
        except requests.RequestException as e:
            logging.error(f"Failed to download the data: {e}")
        except zipfile.BadZipFile:
            logging.error("Failed to extract the ZIP file because it was corrupted.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
    else:
        logging.info("Data already exists.")

def get_data_file_path():
    """
    Constructs the file path for storing the data file within the package.

    Returns:
        str: The file path where the data file should be stored. This path points to a directory 'data' at the same level as this script.
    """
    data_directory = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_directory, exist_ok=True)
    return os.path.join(data_directory, 'US.txt')

def setup_zip_code_data():
    """Function can be called on demand to download and setup ZIP code data."""
    file_path = get_data_file_path()
    data_url = 'https://download.geonames.org/export/zip/US.zip'
    download_and_extract_zip_data(file_path, data_url)

if __name__ != '__main__':
    #file_path = get_data_file_path()
    #data_url = 'https://download.geonames.org/export/zip/US.zip'
    #download_and_extract_zip_data(file_path, data_url)
    setup_zip_code_data()
