from .get_file_format import get_file_format


class IfIPYNBHandler():
    """
    Handles all operations, that must be done if caller file's format is `.ipynb`
    """

    def __init__(self, print_reports: bool = True):
        # These reports are turned on by default, because it helps beginner-user to understand what happend (for example, why matplotlib starts to plot everything outside of notebook)
        self.print_reports = print_reports

    def start(self):
        self.file_format = get_file_format()
        if self.print_reports:
            print('Detected file format: ', self.file_format)

        if self.file_format == 'ipynb':
            import IPython

            IPython.get_ipython().run_line_magic('matplotlib', 'qt5')

            if self.print_reports:
                print('matplotlib is in "separated window" (PyQt5) mode now')
                print('To return to "inline" mode later, just run live_plot.close()')

    def end(self):
        if self.file_format == 'ipynb':
            import IPython

            IPython.get_ipython().run_line_magic('matplotlib', 'inline')

            if self.print_reports:
                print('matplotlib is in inline mode now')