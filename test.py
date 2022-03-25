import matplotlib.pyplot as plt  # 导入pyplot模块并设置别名为plt

squares = [0,1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)  # 函数linewidth设置绘制线条的粗细
# 设置图表标题，并给坐标轴加上标签
plt.title('Square number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()  # 打开matplotib查看器，并显示绘制的图形
