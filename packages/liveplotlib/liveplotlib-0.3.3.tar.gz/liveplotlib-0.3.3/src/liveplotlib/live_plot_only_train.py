import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from .if_ipynb import IfIPYNBHandler


class LivePlotOnlyTrain():
    """
    `J - cost/loss function` \n

    Renders 2 subplots:
    -------------------
    1) J_train_history
    2) J_train_history slice (last {slice_size} steps)
        `slice_size = slice_fraction * len(J_history) + slice_bias`

    Usage
    -------------------
    ```python
    
    # STEP 1: IMPORT

    from liveplotlib import LivePlotOnlyTrain  



    # ...............
    # Some operations with data
    # ................



    # STEP 2: CREATE HISTORY LIST

    # Along with model initialization, create empty J_train_history as well
    model = FooSomeModelClass() 
    J_train_history = []



    # STEP 3: INITIALIZE LIVE PLOT

    # Right before training
    live_plot = LivePlotOnlyTrain()



    # STEP 4: UPDATE DURING TRAINING

    # -----Inside train function loop-----
    # ...
    # new_J_train = ...
    # ...
    J_train_history.append(new_J_train)
    # ...
    live_plot.update(J_train_history)
    # ...
    # ------------------------------------



    # STEP 5: END SESSION

    # In the end (especially important in jupyter notebooks)
    live_plot.close()
    ```
    """

    def __init__(self, 
                 slice_bias: int = 10,
                 slice_fraction: float = 0,
                 print_reports: bool = True): 
        

        # Parameters checking 
        if not ( 0 <= slice_fraction < 1 ):
            raise ValueError(f"Slice fraction should be: 0 <= slice_fraction < 1  (in [0, 1)), but you gave {slice_fraction}")


        self.slice_bias = slice_bias
        self.slice_fraction = slice_fraction


        self.if_ipynb_handler = IfIPYNBHandler(print_reports=print_reports)
        self.if_ipynb_handler.start()

        
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, ncols=1, figsize=(7, 10))

        self.line1, = self.ax1.plot([], [])
        self.line2, = self.ax2.plot([], [])


        self.ax1.set_title('J_train_history')
        self.ax2.set_title("J_train_history (last {slice_size} steps)")

        self.ax1.set_ylabel('J')
        self.ax2.set_ylabel('J')
        self.ax2.set_xlabel('# Step')

        self.ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        self.ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))



    def update(self, J_history: list):
        slice_size = int(len(J_history) * self.slice_fraction) + self.slice_bias

        slice = J_history[-slice_size:]

        self.ax2.set_title(f"J_train_history - last {len(slice)} steps")

        self.line1.set_data(range(len(J_history)), J_history)
        self.line2.set_data(range(len(J_history) - len(slice), len(J_history)), slice)


        for ax in [self.ax1, self.ax2]:
            ax.relim()
            ax.autoscale_view()

        plt.pause(0.01)
    
    
    def close(self):
        plt.close()
        self.if_ipynb_handler.end()