
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot(x_data, y_data, x_label='', y_label='', title=''):
  plt.scatter(x_data, y_data)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.title(title)
  plt.show()

def box_plot(data, labels=None, title=''):
  plt.boxplot(data, labels=labels)
  plt.title(title)
  plt.show()
