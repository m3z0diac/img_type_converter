

try:

	import requests

except:

	print("librarys not found!, use (pip install requests)")

def ToType(to):
	'''
	chosing the type of pictur that what you want convert to
	'''

	typees = ['jpg', 'jpeg', 'png', 'webp']

	typees = ['jpg', 'jpeg', 'png', 'webp']

	return True if to in typees else False


def TypeAlreadyExest():

	'''
	if original type is the same what we chose functin will display the error
	'''

	error = """ The type of orignal image is the same of Type you have chosed! """
	print(error)



def isTypeTrue(link):
	'''
	#check if original type is not what we want to convert to
	# I comment it because there is a bug find it if you can

	types = ['jpg', 'jpeg', 'png', 'webp']

	for i in range(4):
		if link[-3:] == types[i] or link[-4:] == types[i]:
			break
			return True
	'''
	return True

def convert(url, toType):
	'''
	the must important function that convert jpg/jpeg/png/webp to other type of images
	'''

	if isTypeTrue(url):

		geturl = requests.get(url)
		try:

			with open(f'img.{toType}', 'wb') as f:
				f.write(geturl.content)

		except:
			print("error! type not found!")

		return "The picture converted seccessfuly!"

	else:
		return TypeAlreadyExest()

site = input("image url: ")
to_type = input("to jpg/jpeg/png/webp/gif : ")
if ToType(to_type):
	print(convert(site, to_type))
