# check for general terms
extend=0
reg=0
unwanted=0
count=0
text2=[]
with io.open(directory+file_list[2],'rb') as f:
        for line in f:
            
            try: 
                status = json.loads(line) 
                if 'extended_tweet' not in str(status):
                    text=status['text']
                    reg+=1
                else:
                    text=status['extended_tweet']['full_text']
                    
                    extend+=1
                
                if 'midterm' not in str(status).lower() and 'election' not in str(status).lower():
                    unwanted+=1
                    text2.append(text)
                    
                else:
                    print(count,'good')
            
#                     with open('general_tweet_id.txt', 'a') as f:
#                         f.write("%s\n" % status['id_str'])
            
            except:
                continue
            count+=1    
#             if count == 21: break
            
            
