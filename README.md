# FTCS_Model_Sol_Rad
Model that uses FTCS to predict latitudinal solar radiation on Earth over time.

First, constants and variables are defined. Then, a loop runs through the designated number of timesteps, calculating all of the new latitudinal solar radiation values as a column. After that, the new column is appended to the initial solar radiation values. Eventually, this creates a 20x838 matrix that holds all of the latitudinal solar radiation values for all 838 timesteps. Finally, a plot is produced that shows the temporal evolution of the latitudinal solar radiation, specifically the initial, an intermediate, and the final timesteps.
