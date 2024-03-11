import mosspy

userid = 61861013

m = mosspy.Moss(userid, "python")

m.addFilesByWildcard("Submissions/*")

url = m.send()
 
print ("Report Url: " + url)
