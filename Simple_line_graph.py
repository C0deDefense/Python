import matplotlib.pyplot as plt
squares = [1,4,9,16,15]

fig, ax = plt.subplots() #using subplot to generate a plot
ax.plot(squares) #sending our plot list to the plot method

plt.show() #here will call plt and the show method
