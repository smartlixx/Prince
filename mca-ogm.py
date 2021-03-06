import matplotlib.pyplot as plt
import pandas as pd

import prince


df = pd.read_csv('examples/data/ogm.csv')

mca = prince.MCA(df, n_components=-1)

fig1, ax1 = mca.plot_cumulative_inertia()
fig2, ax2 = mca.plot_rows(show_points=True, show_labels=False,
                          color_by='Position Al A', ellipse_fill=True)
fig3, ax3 = mca.plot_rows_columns()
fig4, ax4 = mca.plot_relationship_square()

plt.show()
