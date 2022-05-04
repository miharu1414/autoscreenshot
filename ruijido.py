from PIL import Image 
import imagehash 

def judge(path1,path2) -> bool:
    hash = imagehash.average_hash(Image.open('path1')) 
    print(hash) 
    
    otherhash = imagehash.average_hash(Image.open('path2')) 
    print(otherhash) 
    
    print(hash == otherhash) 
    print(hash - otherhash)
    return hash == otherhash
