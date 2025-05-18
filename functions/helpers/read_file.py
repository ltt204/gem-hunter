def read_file(path):
    """
    Reads a file and returns its content as a string.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    with open(path, "r") as file:
        content = file.read()
    return content
