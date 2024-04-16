
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot(x_data, y_data, x_label='', y_label='', title=''):
   """주어진 x와 y 데이터에 대한 산점도를 그리는 함수
    :param x데이터: x 축 데이터 (리스트 또는 배열)
    :param y데이터: y 축 데이터 (리스트 또는 배열)
    :param x축레이블: x 축 레이블 (기본값: '')
    :param y축레이블: y 축 레이블 (기본값: '')
    :param 제목: 그래프 제목 (기본값: '')
    """
    plt.scatter(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def box_plot(data, labels=None, title=''):
    """
    주어진 데이터에 대한 상자 그림을 그리는 함수
    :param data: 상자 그림을 그릴 데이터 리스트의 리스트
    :param labels: 각 상자에 대한 레이블 (기본값: None)
    :param title: 그래프 제목 (기본값: '')
    """
    plt.boxplot(data, labels=labels)
    plt.title(title)
    plt.show()
