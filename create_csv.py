import sys,os
#### Enter the path of your dataset folder here
root = "/My/Path/To/dataset/İmages/FOLDER"
path = os.path.join(root)
#Create CSV file
csv = open('dataset.csv', 'w')
#This reads everything in that folder
for r,d,f in os.walk(path):
    for file in f:
        print(os.path.join(root,file))
        #Create initial csv entries. My initial default label is 0
        csv.write(os.path.join(root,file)+",0,0,0,0,0,0\n")
csv.close() 
