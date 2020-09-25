x=1
y=1
z=1
n=2
xx= [[x_index,y_index,z_index] for x_index in range (x+1) for y_index in range(y+1) for z_index in range (z+1) if x_index+y_index+z_index!=n]
print(xx)
