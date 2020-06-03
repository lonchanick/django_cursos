def main():
	for x in range(1,11):
			xxr=x*x
			xxr=str(xxr)
			xxxr=x*x*x
			xxxr=str(xxxr)
			x=str(x)
			print('{0:2s} {1:3s} {2:4s}'.format(x,xxr,xxxr))

if __name__ == '__main__':
	main()