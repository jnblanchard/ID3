import DTree
import sys
import Node

''' 
	Execution: 
	python id3.py </trainData.csv> </testData.csv> </MFN> 
	trainData - csv file contating training data
	testData - csv file contatining test data
	MFN - model file name (all one word ex: XORmodel)
'''

def main():
	print "training data file: " + str(sys.argv[1]) 
	file = open(str(sys.argv[1]))
	"""
	IMPORTANT: Change this variable too change target attribute 
	"""
	target = "Class"
	#extract training data
	data = [[]]
	for line in file:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	attributes = data[0]
	data.remove(attributes)
	#ID3 DTree
	tree = DTree.makeTree(data, attributes, target, 0)
	file.close()
	print "generated decision tree"
	f = open(str(sys.argv[3])+ ".model", 'w')
	DTree.DFTreePrint(tree, 0, f)
	f.close()
	data = [[]]
	print "test data file: " + str(sys.argv[2])
	f = open(str(sys.argv[2]))
	#extract test data
	for line in f:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	count = 0
	hits = 0
	total = 0
	for entry in data:
		count += 1
		if str(entry[len(entry)-1]) != target:
			total += 1
			tempDict = tree.copy()
			result = ""
			while(isinstance(tempDict, dict)):
				root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
				oldDict = tempDict
				tempDict = tempDict[tempDict.keys()[0]]
				index = attributes.index(root.value)
				value = entry[index]
				if str(index) == str(value):
					if str(value) == str(entry[len(entry)-1]):
						hits+=1
						break
			
				child = Node.Node(value, tempDict[value])
				result = tempDict[value]
				tempDict = tempDict[value]
				break
					
	print "hits: " + str(hits)
	print "total: " + str(total)
	accuracy = float(hits)/total * 100
	print str(accuracy) + '%' + ' accuracy on test set'
	
if __name__ == '__main__':
	main()