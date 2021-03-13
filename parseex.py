#!/usr/bin/env python

import optparse
import requests


parser = optparse.OptionParser()


parser.add_option("-u", "--url", dest="url", type="str", help="here you need to past url of img")
parser.add_option("-i", "--img", dest="img", type="str", help="here you need to penter type of img you want to convert to")

(opt, arg) = parser.parse_args()


def convert(url, toType):



	geturl = requests.get(url)
	try:

		with open(f'img.{toType}', 'wb') as f:
			f.write(geturl.content)

		return "The picture converted seccessfuly!"

	except:
		return "error! type not found!"

l = opt.url
imgT = opt.img

print(convert(l, imgT))