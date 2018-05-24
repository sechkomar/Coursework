import matplotlib.pyplot as plt


class MyPlot(object):

    def makePlot(self):
        self.fig = plt.figure('Test', figsize=(10, 8))
        ax = plt.subplot(111)
        x = range(0, 100, 10)
        y = (5,) * 10
        ax.plot(x, y, '-', color='red')
        ax.plot(x, y, 'o', color='blue', picker=5)
        self.highlight, = ax.plot([], [], 'o', color='yellow')
        self.cid = plt.connect('pick_event', self.onPick)
        plt.show()

    def onPick(self, event=None):
        this_point = event.artist
        x_value = this_point.get_xdata()
        y_value = this_point.get_ydata()
        ind = event.ind
        self.highlight.set_data(x_value[ind][0], y_value[ind][0])
        self.fig.canvas.draw_idle()


if __name__ == '__main__':
    app = MyPlot()
    app.makePlot()


# import math
#
# import matplotlib.pyplot as plt
#
#
# class AnnoteFinder(object):
#     """callback for matplotlib to display an annotation when points are
#     clicked on.  The point which is closest to the click and within
#     xtol and ytol is identified.
#
#     Register this function like this:
#
#     scatter(xdata, ydata)
#     af = AnnoteFinder(xdata, ydata, annotes)
#     connect('button_press_event', af)
#     """
#
#     def __init__(self, xdata, ydata, annotes, ax=None, xtol=None, ytol=None):
#         self.data = list(zip(xdata, ydata, annotes))
#         if xtol is None:
#             xtol = ((max(xdata) - min(xdata)) / float(len(xdata))) / 2
#         if ytol is None:
#             ytol = ((max(ydata) - min(ydata)) / float(len(ydata))) / 2
#         self.xtol = xtol
#         self.ytol = ytol
#         if ax is None:
#             self.ax = plt.gca()
#         else:
#             self.ax = ax
#         self.drawnAnnotations = {}
#         self.links = []
#
#     def distance(self, x1, x2, y1, y2):
#         """
#         return the distance between two points
#         """
#         return (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
#
#     def __call__(self, event):
#
#         if event.inaxes:
#
#             clickX = event.xdata
#             clickY = event.ydata
#             if (self.ax is None) or (self.ax is event.inaxes):
#                 annotes = []
#                 # print(event.xdata, event.ydata)
#                 for x, y, a in self.data:
#                     # print(x, y, a)
#                     if ((clickX - self.xtol < x < clickX + self.xtol) and
#                             (clickY - self.ytol < y < clickY + self.ytol)):
#                         annotes.append(
#                             (self.distance(x, clickX, y, clickY), x, y, a))
#                 if annotes:
#                     annotes.sort()
#                     distance, x, y, annote = annotes[0]
#                     self.drawAnnote(event.inaxes, x, y, annote)
#                     for l in self.links:
#                         l.drawSpecificAnnote(annote)
#
#     def drawAnnote(self, ax, x, y, annote):
#         """
#         Draw the annotation on the plot
#         """
#         if (x, y) in self.drawnAnnotations:
#             markers = self.drawnAnnotations[(x, y)]
#             for m in markers:
#                 m.set_visible(not m.get_visible())
#             self.ax.figure.canvas.draw_idle()
#         else:
#             t = ax.text(x, y, " - %s" % (annote), )
#             m = ax.scatter([x], [y], marker='d', c='r', zorder=100)
#             self.drawnAnnotations[(x, y)] = (t, m)
#             self.ax.figure.canvas.draw_idle()
#
#     def drawSpecificAnnote(self, annote):
#         annotesToDraw = [(x, y, a) for x, y, a in self.data if a == annote]
#         for x, y, a in annotesToDraw:
#             self.drawAnnote(self.ax, x, y, a)
#
#
# x = range(10)
# y = range(10)
# annotes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# fig, ax = plt.subplots()
# ax.scatter(x, y)
# af = AnnoteFinder(x, y, annotes, ax=ax)
# fig.canvas.mpl_connect('button_press_event', af)
# plt.show()


# import numpy as np
#
#
# class PointBrowser(object):
#     """
#     Click on a point to select and highlight it -- the data that
#     generated the point will be shown in the lower axes.  Use the 'n'
#     and 'p' keys to browse through the next and previous points
#     """
#
#     def __init__(self):
#         self.lastind = 0
#
#         self.text = ax.text(0.05, 0.95, 'selected: none',
#                             transform=ax.transAxes, va='top')
#         self.selected, = ax.plot([xs[0]], [ys[0]], 'o', ms=12, alpha=0.4,
#                                  color='yellow', visible=False)
#
#     def onpress(self, event):
#         if self.lastind is None:
#             return
#         if event.key not in ('n', 'p'):
#             return
#         if event.key == 'n':
#             inc = 1
#         else:
#             inc = -1
#
#         self.lastind += inc
#         self.lastind = np.clip(self.lastind, 0, len(xs) - 1)
#         self.update()
#
#     def onpick(self, event):
#
#         if event.artist != line:
#             return True
#
#         N = len(event.ind)
#         if not N:
#             return True
#
#         # the click locations
#         x = event.mouseevent.xdata
#         y = event.mouseevent.ydata
#
#         distances = np.hypot(x - xs[event.ind], y - ys[event.ind])
#         indmin = distances.argmin()
#         dataind = event.ind[indmin]
#
#         self.lastind = dataind
#         self.update()
#
#     def update(self):
#         if self.lastind is None:
#             return
#
#         dataind = self.lastind
#
#         ax2.cla()
#         ax2.plot(X[dataind])
#
#         ax2.text(0.05, 0.9, 'mu=%1.3f\nsigma=%1.3f' % (xs[dataind], ys[dataind]),
#                  transform=ax2.transAxes, va='top')
#         ax2.set_ylim(-0.5, 1.5)
#         self.selected.set_visible(True)
#         self.selected.set_data(xs[dataind], ys[dataind])
#
#         self.text.set_text('selected: %d' % dataind)
#         fig.canvas.draw()
#
#
# if __name__ == '__main__':
#     import matplotlib.pyplot as plt
#
#     X = np.random.rand(100, 200)
#     xs = np.mean(X, axis=1)
#     ys = np.std(X, axis=1)
#
#     fig, (ax, ax2) = plt.subplots(2, 1)
#     ax.set_title('click on point to plot time series')
#     line, = ax.plot(xs, ys, 'o', picker=5)  # 5 points tolerance
#
#     browser = PointBrowser()
#
#     fig.canvas.mpl_connect('pick_event', browser.onpick)
#     fig.canvas.mpl_connect('key_press_event', browser.onpress)
#
#     plt.show()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()