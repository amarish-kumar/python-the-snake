# import os

# def list_all(root):
# 	# print os.listdir(root)
# 	for f in os.listdir(root):
# 		# print f, 
# 		# print os.path.isdir(f)
# 		print os.path.abspath(f)
# 		if os.path.isdir(os.path.abspath(f)):
# 			list_all(os.path.abspath(f))
# 		else:
# 			print f

# list_all("/Users/admin/projects/Web/")


def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print sChildPath
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents("/Users/admin/projects/Web/")