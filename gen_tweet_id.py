import pandas as pd
import numpy as np
import json
import gzip
import os
import io




def get_files(directory,file_ext):
    file_list = []
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(file_ext):
                file_list.append(file)
    file_list.sort()
    return file_list

directory = './data/'
file_ext = '.txt'

file_list=get_files(directory,file_ext)


for filename in file_list:
   



    with io.open(directory+filename,'rb') as f:
        count=0
        for line in f:
            
            try: 
                status = json.loads(line) 
                if 'extended_tweet' not in str(status):
                    text=status['text']
                
                else:
                    text=status['extended_tweet']['full_text']
                
                if 'midterm' not in str(status).lower() and 'election' not in str(status).lower():
                    continue
                    
                else:
                    with open('general_tweet_id.txt', 'a') as f:
                        f.write("%s\n" % status['id_str'])
            
            except:
                continue
            count+=1    
#             if count == 21: break
            
    print(filename)
