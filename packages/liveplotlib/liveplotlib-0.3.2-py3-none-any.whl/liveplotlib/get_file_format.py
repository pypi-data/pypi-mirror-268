def get_file_format():
    """
    To find out what is a caller file's format (`.py` or `.ipynb`)
    """

    try:
        # Attempt to make ipynb-specific actions

        import IPython

        # import IPynb is a good check, but may be not enough, because user could run a .py file using .venv, that have IPynb installed

        # This command works only if it is executed in .ipynb.
        # Because in .py files get_python() returns None. And Trying to get attribute of None raises an error
        IPython.get_ipython().cache_size
    except Exception:
        # Exception occurred. Assuming it is .py file
        file_format = 'py'
    else:
        # Runned successfully. Assuming it is .ipynb file
        file_format = 'ipynb'

    return file_format
