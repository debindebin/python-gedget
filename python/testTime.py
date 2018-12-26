#/usr/bin/env python
#__*__coding: utf-8 __*__

import os.path 

def file_extension(path): 
  return os.path.splitext(path)[1] 
print file_extension('C:\Users\huazai\Desktop\数据统计.txt')