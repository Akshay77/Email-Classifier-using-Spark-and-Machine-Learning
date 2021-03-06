import os

def makeDataFileFromEmails( dir_path, out_file_path ):
	"""
	Iterate over files converting them to a single line
	then write the set of files to a single output file
	"""

	with open( out_file_path, 'w' ) as out_file:

		# Iterate over the files in directory 'path'
		for file_name in os.listdir( dir_path ):

			# Open each file for reading
			with open( dir_path + file_name ) as in_file:

				# Reformat emails as a single line of text
				text = in_file.read().replace( '\n',' ' ).replace( '\r', ' ' )
				text = text + "\n"
				# Write each email out to a single file
				out_file.write( text )


def main():
	"""
	Driver program for a spam filter using Spark and MLLib
	"""

	# Consolidate the individual email files into a single spam file
	# and a single ham file
	makeDataFileFromEmails( "D:\\Softwares\spark-2.1.0-bin-hadoop2.7\\spark-2.1.0-bin-hadoop2.7\\bin\\My_Examples\\Spam-Ham\\20050311_spam_2.tar\\20050311_spam_2\\spam_2\\", 
		"D:\\Softwares\spark-2.1.0-bin-hadoop2.7\\spark-2.1.0-bin-hadoop2.7\\bin\\My_Examples\\Spam-Ham\\20050311_spam_2.tar\\20050311_spam_2\\spam.txt")
	makeDataFileFromEmails( "D:\\Softwares\\spark-2.1.0-bin-hadoop2.7\\spark-2.1.0-bin-hadoop2.7\\bin\\My_Examples\\Spam-Ham\\20030228_easy_ham.tar\\20030228_easy_ham\\easy_ham\\", 
		"D:\\Softwares\\spark-2.1.0-bin-hadoop2.7\\spark-2.1.0-bin-hadoop2.7\\bin\\My_Examples\\Spam-Ham\\20030228_easy_ham.tar\\20030228_easy_ham\\ham.txt" )

if __name__ == "__main__":
	main()