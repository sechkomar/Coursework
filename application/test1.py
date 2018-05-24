# # import matplotlib.pyplot as plt
# # import numpy as np
# #
# # data = np.random.random(size=(20, 20))
# #
# # plt.imshow(data, interpolation='nearest')
# # # plt.xticks(np.arange(0.0, 2.5, 1), np.arange(0.5, 2, 0.5))
# # # plt.yticks(np.arange(2, -0.5, -1), np.arange(0.5, 2, 0.5))
# #
# # plt.show()
# # #
# # # cmap = colors.ListedColormap(['white', 'red'])
# # # bounds = [0, 5, 10]
# # #
# # # make a color bar
# # # plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0, 5, 10])
# # # plt.show()
#
# """
# Show how to modify the coordinate formatter to report the image "z"
# value of the nearest pixel given x and y
# """
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.cm as cm
#
# X = 10 * np.random.rand(5, 3)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.imshow(X, cmap=cm.jet, interpolation='nearest')
#
# numrows, numcols = X.shape
#
#
# def format_coord(x, y):
#     col = int(x + 0.5)
#     row = int(y + 0.5)
#     if 0 <= col < numcols and 0 <= row < numrows:
#         z = X[row, col]
#         return 'x=%1.4f, y=%1.4f, z=%1.4f' % (x, y, z)
#     else:
#         return 'x=%1.4f, y=%1.4f' % (x, y)
#
#
# ax.format_coord = format_coord
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import mpldatacursor
#
# data = np.random.random((100, 100))
#
# fig, ax = plt.subplots()
# # ax.imshow(data, interpolation='none', extent=[0, 1.5 * np.pi, 0, np.pi])
# ax.imshow(data, interpolation='none')
#
# mpldatacursor.datacursor(hover=True, bbox=dict(alpha=0.7, fc='w'),
#                          formatter='i, j = {i}, {j}\nz = {z:.02g}'.format)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# data = 10 * np.random.rand(100, 100)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.imshow(data)
#
# numrows, numcols = data.shape
#
#
# def format_coord(x, y):
#     col = int(x + 0.5)
#     row = int(y + 0.5)
#     return 'x={}, y={}'.format(col, row)
#
#
# ax.format_coord = format_coord
#
# plt.show()
"""
compute the mean and stddev of 100 data sets and plot mean vs stddev.
When you click on one of the mu, sigma points, plot the raw data from
the dataset that generated the mean and stddev
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(100, 1000)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=5)  # 5 points tolerance


# def onpick(event):
#     if event.artist != line:
#         return True
#
#     N = len(event.ind)
#     if not N:
#         return True
#
#     figi = plt.figure()
#     for subplotnum, dataind in enumerate(event.ind):
#         ax = figi.add_subplot(N, 1, subplotnum + 1)
#         ax.plot(X[dataind])
#         ax.text(0.05, 0.9, 'mu=%1.3f\nsigma=%1.3f' % (xs[dataind], ys[dataind]),
#                 transform=ax.transAxes, va='top')
#         ax.set_ylim(-0.5, 1.5)
#     figi.show()
#     return True
#
#
# fig.canvas.mpl_connect('pick_event', onpick)
#
# plt.show()
