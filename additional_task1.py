from json2xml import json2xml
from json2xml.utils import readfromjson
xmlf = open('file1.xml','w+',encoding='utf-8')
data = readfromjson("file.json")
print(data)
xmlf.write(json2xml.Json2xml(data,wrapper='root',attr_type=False).to_xml())
xmlf.close()


