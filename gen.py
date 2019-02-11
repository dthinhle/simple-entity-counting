import sys,os

TEST_DIR = os.path.join(".",os.path.join("test"))

class mapT:

    def __init__(self,wid,hei):
        self.wid = wid
        self.hei = hei
        self.firstNode = mapNode(None,None,None,None)
        self.genNode(wid,hei)
    def toStr(self):
        lineNode = self.firstNode
        tempNode = lineNode
        line = ""
        while True:
            while tempNode:
                line += (str(tempNode.value))
                tempNode = tempNode.rightNode
                  
            if lineNode.belowNode:
                line += "\n" 
                lineNode = lineNode.belowNode
                tempNode = lineNode
            else:
                break
        return line

    def convertMap(self, mapList):
        hNode = self.firstNode
        wNode = hNode 
        for x in mapList:
            if x == '1':
                wNode.value += 1
            if wNode.rightNode is None:
                wNode = hNode.belowNode
                hNode = wNode
            else:
                wNode = wNode.rightNode

        self.printMap()
    
    def printMap(self):
        # comment the line below to disable terminal output:
        return
        lineNode = self.firstNode
        tempNode = lineNode
        while True:

            line = str(tempNode.value)
            while tempNode.rightNode is not None:
                line += (str(tempNode.rightNode.value))
                tempNode = tempNode.rightNode
            print(line)
            if lineNode.belowNode:
                lineNode = lineNode.belowNode
                tempNode = lineNode
            else:
                break
        print('---')
        pass

    def genNode(self,wid,hei):
        self.firstNode = mapNode(None,None,None,None)
        abNode = self.firstNode
        # countH = 0
        for x in range(0,hei):
            
            #Gen first node in line:
            if x == 0:
                lineNode = abNode
                
            else:
                lineNode = mapNode(None,None,None,None)
                abNode.belowNode = lineNode
                lineNode.aboveNode = abNode
                abNode = lineNode
            # Gen every node next to the first:
            leftNode = lineNode
            countW=0
            for y in range(0,wid-1):
                newNode = mapNode(None,None,None,None)
                leftNode.rightNode = newNode
                newNode.leftNode = leftNode
                leftNode = newNode
        lineNode = self.firstNode
        tempNode = lineNode
        while lineNode.belowNode:
            while tempNode:
                if tempNode.belowNode is None:
                    tempNode.belowNode = tempNode.leftNode.belowNode.rightNode
                    tempNode.belowNode.aboveNode = tempNode
                tempNode = tempNode.rightNode
            lineNode = lineNode.belowNode
            tempNode = lineNode
        self.printMap()


    def countEntity(self):
        lineNode = self.firstNode
        tempNode = lineNode
        count = 0
        temp = 'A'
        while lineNode:
            while tempNode:
                check = mapNode.checkEntity(tempNode,count+1 if count < 9 else temp)
                if check == True:
                    count += 1
                    if count > 9:
                        temp = chr(ord(temp)+1)

                tempNode = tempNode.rightNode
            lineNode = lineNode.belowNode
            tempNode = lineNode
        return count
        


class mapNode:

    def __init__(self,below,right,above,left):
        self.value = 0
        self.tag = False
        self.belowNode = below
        self.aboveNode = above
        self.rightNode = right
        self.leftNode = left

    @staticmethod 
    def checkEntity(node, value):
        if node is None:
            return False
        elif node.value == 0:
            return False
           
        elif node.value == 1 and node.tag == False:
            node.tag = True
            node.value = value
            mapNode.checkEntity(node.aboveNode,value)
            mapNode.checkEntity(node.leftNode,value)
            mapNode.checkEntity(node.rightNode,value)
            mapNode.checkEntity(node.belowNode,value)
            return True
    pass
    
class genMap:
    @staticmethod 
    def test(dir,num):
        filename = os.path.join(TEST_DIR,str(num) + "_res.txt")
        checkfile =  os.path.join(TEST_DIR,str(num) + ".txt")
        file = open(checkfile,"r")
        # line = file.read()
        param = file.readline()
        ww = int(param[0:param.find(" ")])
        hh = int(param[param.find(" ")+1:])
        mapRes = []
        for x in range(0,hh):
            lineRead = file.readline()
            # lineRes = []
            for y in range(0,ww):
                mapRes.append(lineRead[y])
        file = open(filename,"w")
        # Generate object
        count = 1
        mapRet = mapT(ww,hh)
        mapRet.convertMap(mapRes)
        numEnt = mapRet.countEntity()
        ret = str(numEnt) + "\n" + mapRet.toStr()
        # Uncomment the line below to enable terminal output
        # print(ret)
        file.write(ret)
        # print(line)
        pass
    
