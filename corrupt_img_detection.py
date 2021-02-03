#!/usr/bin/env python
# coding: utf-8

# In[28]:


img_dir=r"C:\Users\Divyansh\Desktop\New folder\p0photo"

corrupt_img_dir=r"C:\Users\Divyansh\Desktop\currupt\currupt"

from PIL import Image
import os,time

count1=0
count=0

def verify_image(img_file):
     
    try:
        v_image = Image.open(img_file)
        v_image.verify()
        return True
       
    except OSError:
        return False


#main script
for root, dirs, files in os.walk(img_dir):
    for file in files:
        if file.endswith(".JPG"):
            currentFile=os.path.join(root, file)
            
            
            if verify_image(currentFile):
                print("good file ")
            else:
                new_file_name=corrupt_img_dir+os.path.basename(currentFile)
                print("corrupt file")
                os.rename(currentFile, new_file_name)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




