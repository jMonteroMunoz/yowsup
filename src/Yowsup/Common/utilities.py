'''
Copyright (c) <2012> Tarek Galal <tare2.galal@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR 
A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import hashlib, string
class Utilities:

	Version="2.11.23"
	Resource="Android-"+Version+"-443"
	UserAgent = "WhatsApp/"+Version+" Android/4.2.1 Device/GalaxyS3"

	@staticmethod
	def processIdentity(identifier):
		if (len(identifier) == 0):
			return "abcdef0123456789"
		else:
			identifier = identifier[::-1]

			digest = hashlib.sha1(identifier)
			return digest.hexdigest()
	
	@staticmethod
	def decodeString(encoded):
		return "".join(map(chr,  map(lambda x: x ^ 19, encoded)))

	@staticmethod
	def str( number, radix ):
		"""str( number, radix ) -- reverse function to int(str,radix) and long(str,radix)"""

		if not 2 <= radix <= 36:
			raise ValueError("radix must be in 2..36")

		abc = string.digits + string.ascii_letters

		result = ''

		if number < 0:
			number = -number
			sign = '-'
		else:
			sign = ''

		while True:
			number, rdigit = divmod( number, radix )
			result = abc[rdigit] + result
			if number == 0:
				return sign + result
