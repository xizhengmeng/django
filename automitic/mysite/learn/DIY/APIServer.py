import os,subprocess,shutil,json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getfilecontent():
    f = open('/Users/wxg/Desktop/text2.txt','r')
    text = f.read()
    f.close()
    return text

def writecontent(string):
    data = json.loads(string)
    if data:
        f = open('/Users/wxg/Desktop/text3.txt','w')
        f.write(string)
        f.close()
        return 'done'
    else:
        return 'error for json'