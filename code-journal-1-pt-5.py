import numpy as np

def numbers():
	x = np.linspace(0,2*np.pi,1000)
	y = np.sin(x)
	xy = np.meshgrid(x,y)
	XY = np.array(xy).transpose()
	print("x, sinx")
	print(XY)

def main():
	numbers()

if __name__=="__main__":
	main()
