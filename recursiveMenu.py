menuItems = [
    {"id":"id-1", "level": 0, "title": "MainMenu1", "parentId": ""},
    {"id":"id-2", "level": 0, "title": "MainMenu2", "parentId": ""},
    {"id":"id-3", "level": 1, "title": "menu2_1", "parentId": "id-2"},
    {"id":"id-4", "level": 2, "title": "menu2_1_1", "parentId":"id-3"},
    {"id":"id-5", "level": 1, "title": "menu1_1", "parentId":"id-1"},
    {"id":"id-6", "level": 3, "title": "menu2_1_1_1", "parentId":"id-4"},
    {"id":"id-10", "level": 0, "title": "Main_új", "parentId":""},
    {"id":"id-11", "level": 1, "title": "Main_új_1", "parentId":"id-10"},
    {"id":"id-12", "level": 1, "title": "Main_új_2", "parentId":"id-10"},
    {"id":"id-15", "level": 1, "title": "menu2_2", "parentId": "id-2"},
]

class RecursiveMenu:
    class TreeNode:
        def __init__(self, object):
            self.id = object["id"]
            self.parentId = object["parentId"]
            self.title = object["title"]
            self.level = object["level"]
            self.children = []

        def toString(self):
            return self._printNode()

        def __str__(self) -> str:
            return self._prinNode()

        def _printNode(self) -> str:
             return "TreeNode: ( id={0}, title={1}, level={2}, childrenLenght={3}, parentId={4} )".format(self.id, self.title, self.level, len(self.children), self.parentId)

    # Visszad adja azokat az elemeket, ahol level szintjük egyforam, returns TreeNode[]
    # Pl: vissza adja csak level-1 elemeket
    def _getNodesFrom(self, nodes, level) -> [TreeNode]:
        retList = []
        for node in nodes:
            if (node.level == level):
                retList.append(node)

        return retList
    
    # Node elemeket csinált a megadott dict elemekeből, return TreeNode list
    def _createNodeFromDict(self, dictList) -> [TreeNode]:
        retNodes = []
        for item in dictList:
            retNodes.append(self.TreeNode(item))
        return retNodes

    # Vissza adja az adott parentNode if megtalálta node elemek között. return TreeNode
    def _getParentNode(self, parentNodes, parentId) -> TreeNode:
        for node in parentNodes:
            if (node.id == parentId):
                return node
        return None

    # Ősszerakra a childrenNodes(level-2 elemeket) az ők parentNodesba(level-1 elemekbe)
    def _mergeChildrenNodeIntoParent(self, parentNodes, childrenNodes):
        for childNode in childrenNodes:
            currentParent = self._getParentNode(parentNodes, childNode.parentId)
            if (currentParent):
                #print('parent=',currentParent.id)
                #print('parent children=', len(currentParent.children))
                #print(childNode)
                currentParent.children.append(childNode)

      
    def _makeTreeStructFrom(self, array, maxLevel):
        # Tartalmaz Tree elemeket
        retParentNodes = []

        # dict elemeket átalakítja treeNodes elemekké
        treeNodesList = self._createNodeFromDict(array)
            
        # végig megyek a nodes elemenein alulról felfele: level(3) --> level(0).ig 
        for level in range(maxLevel, 0, -1):
            parentNodes = self._getNodesFrom(treeNodesList, level-1)
            childrenNodes = self._getNodesFrom(treeNodesList, level)

            self._mergeChildrenNodeIntoParent(parentNodes, childrenNodes)

            # szintenkékt lépegetni és megniézni mit tartalmazt: parentNodes, childrenNodes
            #if (level == 1):
                #self._printNodes(parentNodes)
                #exit()

            # saving root parentNode reference
            if (level-1 == 0):
                retParentNodes = parentNodes
            
        #print('parentNode=', retParentNodes[0].children[0])
        #exit()
        return retParentNodes

    def _printNodes(self, nodes):
        retString = "[ \n"
        for node in nodes:
            retString += node.toString() + "\n"
        
        retString += "]"
        print(retString)
            
    # Kiirja az adott Node(csomopont) címét, ha van gyereke akkor belemegy megint
    def _printPreorderItem_rek(self, node):
        # Művelet végrehajtáse - Pre-order
        print('title=', node.title)
        #print('currentNode=', node)
        
        # in-order: Művelet feldolgozás
        
        # post-order: Művelet feldogolozás
        if (node.children != []):
            for child in node.children:
                self._printPreorderItem_rek(child)


    def show(self, menu_array):
        """
        Example
        treeMenu = {
            "title": "Test-1",
            "child": {"title": "Test-2", "child": [
                                            {"title":"Test-3", "children": []}
                                            ]}
        }"""

        maxDeepLevel = 3
        treeMainMenus = self._makeTreeStructFrom(menu_array, maxDeepLevel)
        
        print("TreeNodes:")
        print("------------")
        for treeItem in treeMainMenus:
            self._printPreorderItem_rek(treeItem)
        


menu = RecursiveMenu()
menu.show(menuItems)
