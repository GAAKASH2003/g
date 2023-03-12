f=open('file.txt','w+')
f.write('this is verypreccious to me')
f.close()
import os
import zipfile
comp=zipfile.ZipFile('comp.zip','w')
comp.write('file.txt',compress_type=zipfile.ZIP_DEFLATED)
zip_obj=zipfile.ZipFile('comp.zip','r')
zip_obj.extractall("heloo")
