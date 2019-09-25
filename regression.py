#get the module
import matplotlib.pyplot as plt

#performs the function value call
def f(w2, w1, w0, x):
    return (w2*(x**2))+(w1*x)+w0

#want to replace this with file
data = [[-10, 91], [-3, 7], [0, 1], [1, 3],
        [2, 7], [3, 13], [4, 21], [10, 111]]

#values to help the regression
alpha, w0, w1, w2, epochs = 1e-06, 0, 0, 0, 100000

#setting the x and y values of the data
xs, ys = list(map(lambda x:x[0], data)), list(map(lambda x:x[1], data))

#making the graph
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xs,ys,'ro')
line1, = ax.plot(xs,ys,linestyle='dashed')

#performing the regression
for i in range(epochs):
    for j in range(len(data)):
        x, y = data[j][0], data[j][1]
        p = w2 * (x**2) + (w1 * x) + w0

        w2 += alpha * (y - p) * (x**2)
        w1 += alpha * (y - p) * x
        w0 += alpha * (y - p)

    #updating the graph
    line1.set_ydata(list(map(lambda x:f(w2,w1,w0,x),xs)))
    fig.canvas.draw()
