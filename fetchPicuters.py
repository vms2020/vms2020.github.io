import urllib.request
import urllib.response
import urllib.parse
import urllib
import json
import os


f =  open('docs/api/categories.json').read()
catsj = json.loads(f)
for o in catsj['categories']:
    ## print(o['image_url'])
    ##req = urllib.request.Request(o['image_url'])
    r = urllib.request.urlopen(o['image_url'])
    print(urllib.parse.unquote(r.info()['Content-Disposition'].split(';')[2].split("''")[1]))
    f=open(urllib.parse.unquote(r.info()['Content-Disposition'].split(';')[2].split("''")[1]),"bx")
    f.write(r.read())
    ## os.system("curl -J -O " + o['image_url'])


    
    
    
    



