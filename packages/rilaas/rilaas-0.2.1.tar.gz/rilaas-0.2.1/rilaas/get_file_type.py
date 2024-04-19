import mimetypes

def get_mime_type(file_name: str) -> str:
    """
    Returns the MIME type for a provided file name with an extension.

    Args:
    file_name (str): The name of the file including its extension.

    Returns:
    str: The MIME type of the file, or an empty string if the MIME type cannot be determined.
    """
    # Ensure the mimetype database is initialized (usually not necessary, but safe to do)
    mimetypes.init()

    # Guess the MIME type and encoding (we only need the MIME type here)
    mime_type, _ = mimetypes.guess_type(file_name)

    # If the mime_type is None (unknown), we return an empty string
    return mime_type if mime_type is not None else ""