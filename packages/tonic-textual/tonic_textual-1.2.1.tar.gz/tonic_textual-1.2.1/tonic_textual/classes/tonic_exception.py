from requests.exceptions import HTTPError

class DatasetNameAlreadyExists(Exception):
    """
        Raised when there is an attempt to create a dataset with a name that already exists.
    """
    def __init__(self, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__("The dataset name already exists. Dataset names must be unique. Choose a different name.")
        self.errors = errors

class DatasetFileMatchesExistingFile(HTTPError):
    """
        Raised when the content in a file to upload matches the content in an existing file in the dataset.
    """
    def __init__(self, errors):
        super().__init__(errors.response.content or "The file content matches content in an existing dataset file. Choose a different file.")
        self.errors = errors

class InvalidJsonForRedactionRequest(Exception):
    """
        Raised when the JSON redaction request contains invalid JSON
    """
    def __init__(self, msg):
        super().__init__(msg)

class LicenseInvalid(HTTPError):
    """
        Raised when either your license has expired OR you've exceeded your allowed word limit
    """
    def __init__(self, errors):
        super().__init__(str(errors.response.content) or "Invalid Textual license. Please reach out to textual@tonic.ai.")
        self.errors = errors

class FileNotReadyForDownload(Exception):
    """
        Raised when you make a reques to download a file that is not yet ready for download
    """
    def __init__(self, msg):
        super().__init__(msg)

class ErrorWhenDownloadFile(HTTPError):
    """
        Raised when server returns 500 when attempting to download file
    """
    def __init__(self, errors):
        super().__init__("Either error occured while downloading file or the file redaction job was cancelled.")
        self.errors = errors
        