class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        def similiar(l1,l2):
            counter = 0
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    counter += 1
                if counter > 1:
                    break
            if counter == 1:
                return True
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []
        else:
            wordList.remove(endWord)
    # 首先逐级分层：
            possible = [endWord]
            layer = [possible]
            rest = wordList
            newpossible = [1]
            while newpossible != []:
                newpossible = []
                newrest = rest.copy()
                for i in possible:
                    for j in newrest:
                        if similiar(i,j):
                            if j not in newpossible:
                                newpossible.append(j)
                                rest.remove(j)
                possible = newpossible
                layer.append(newpossible)   
            print(layer)
    # 定位
            counter = 0
            for i in layer:
                if beginWord not in i:
                    counter += 1
                else:
                    break
    # 分层筛查  
        def recursion(layer,n,temp,result,beginWord):
            for i in layer[n - 1]:
                if similiar(i,temp[-1]):
                    newtemp = temp + [i]
                    if newtemp[-1] == endWord:
                        result.append(newtemp)
                    else:
                        recursion(layer,n - 1,newtemp,result,beginWord)
        result = []
        recursion(layer,counter,[beginWord],result,beginWord)
        return result  