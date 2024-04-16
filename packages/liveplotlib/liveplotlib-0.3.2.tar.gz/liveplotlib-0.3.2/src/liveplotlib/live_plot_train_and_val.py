import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from .if_ipynb import IfIPYNBHandler


class LivePlotTrainAndVal():
    """
    `J` - cost/loss function \n
    `val` - validation (aka cv/dev) \n

    Renders 4 subplots:
    -------------------
    - [0, 0] - J_train_history and J_val_history together
    - [0, 1] - slice of [0, 0]

    - [1, 0] - slice of train
    - [1, 1] - slice of val

    
    `slice_size = slice_fraction * len(J_train_history) + slice_bias`

    Usage
    -------------------
    ```python
    # STEP 1: IMPORT

    from liveplotlib import LivePlotTrainAndVal 



    # ...............
    # Some operations with data
    # ................



    # STEP 2: CREATE HISTORY LISTS

    # Along with model initialization, create empty J_train_history and J_val_history as well
    model = FooSomeModelClass() 
    J_train_history = []
    J_val_history = []



    # STEP 3: INITIALIZE LIVE PLOT (START SESSION)

    # Right before training
    live_plot = LivePlotTrainAndVal()



    # STEP 4: UPDATE DURING TRAINING

    # -----Inside train function loop-----
    # ...
    # new_J_train = ...
    # new_J_val = ...
    # ...
    J_train_history.append(new_J_train)
    J_val_history.append(new_J_val)
    # ...
    live_plot.update(J_train_history, J_val_history)
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



        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

        self.line1_1, = self.ax1.plot([], [])
        self.line1_2,  = self.ax1.plot([], [])

        self.line2_1, = self.ax2.plot([], [])
        self.line2_2, = self.ax2.plot([], [])

        self.line3, = self.ax3.plot([], [])
        self.line4, = self.ax4.plot([], [], c='orange')

        self.ax1.set_title('J_train_history and J_val_history')
        self.ax2.set_title('J_train_history and J_val_history (last {slice_size} steps)')
        self.ax3.set_title('J_train_history (last {slice_size} steps)')
        self.ax4.set_title('J_val_history (last {slice_size} steps)')


        self.ax1.set_ylabel('J')
        self.ax3.set_ylabel('J')
        self.ax3.set_xlabel('# Step')
        self.ax4.set_xlabel('# Step')

        self.ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        self.ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        self.ax3.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        self.ax4.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

    def update(self, J_train_history: list, J_val_history: list):
        if len(J_train_history) != len(J_val_history):
            raise ValueError(f"Given J_train_history and J_val_history are not the same length ({len(J_train_history)} != {len(J_val_history)})! Please, ensure, that you append elements to them synchronously")


        slice_size = int(len(J_train_history) * self.slice_fraction) + self.slice_bias

        self.ax2.set_title(f"J_train_history and J_val_history (last {slice_size} steps)")
        self.ax3.set_title(f"J_train_history (last {slice_size} steps)")
        self.ax4.set_title(f"J_val_history (last {slice_size} steps)")


        train_slice = J_train_history[-slice_size:]
        val_slice = J_val_history[-slice_size:]



        self.line1_1.set_data(range(len(J_train_history)), J_train_history)
        self.line1_2.set_data(range(len(J_val_history)), J_val_history)

        self.line2_1.set_data(range(len(J_train_history) - len(train_slice), len(J_train_history)), train_slice)
        self.line2_2.set_data(range(len(J_val_history) - len(val_slice), len(J_val_history)), val_slice)

        self.line3.set_data(range(len(J_train_history) - len(train_slice), len(J_train_history)), train_slice)
        self.line4.set_data(range(len(J_val_history) - len(val_slice), len(J_val_history)), val_slice)


        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]:
            ax.relim()
            ax.autoscale_view()
        plt.pause(0.01)

    def close(self):
        plt.close()
        self.if_ipynb_handler.end()
