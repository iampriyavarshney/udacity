import os
def rename_files():
	#get file name from a folder
	file_list=os.listdir(r"C:\Users\Priya Varshney\Downloads\Compressed\photos")
	#print(file_list)
	saved_path=os.getcwd()
	print("current working directory is"+saved_path)
	os.chdir(r"C:\Users\Priya Varshney\Downloads\Compressed\photos")
	#for each file , rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
	os.chdir(saved_path)
rename_files()  