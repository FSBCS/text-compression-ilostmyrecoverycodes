from friendsbalt.acs import MinPQ


class HuffmanEncoding:
    def __init__(self, src=None, encoded_text=None, root=None):
        """
        Initializes a new Huffman Encoding. Either source text or encoded text and root must be provided.
        If source text is provided, it builds the Huffman tree and dictionary, and encodes the text.
        If encoded text and root are provided, it decodes the text.
        Args:
            src (str, optional): The source text to be encoded.
            encoded_text (str, optional): The encoded text to be decoded.
            root (Node, optional): The root node of the Huffman tree for decoding.
        """
        if src:
            self.buildTree()
        else:
            self.encoded_text = encoded_text
            self.root = root
            self.source_text = self.decode()
            self.dictionary = self._build_dictionary()
            

            


    
    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def is_leaf(self):
            return self.char is not None

    def encoding(self):
        """
        Returns the encoded text.
        Returns:
            str: The encoded text as a string of 0s and 1s.
        """
        return self.encoded_text

    def source_text(self):
        """
        Returns the original source text.
        Returns:
            str: The original source text.
        """
        return self.source_text

    def root(self):
        """
        Returns the root node of the Huffman tree.
        Returns:
            Node: The root node of the Huffman tree.
        """
        return self.root
    
    def buildTree(self):

        #create a list for frequencies to be counted
        frequency_list = {}
        #runs through source text and if a character is
        #in the list already add 1 to it, if not create
        #a new index for it.
        for n in self.source_text:
            if n in frequency_list:
                frequency_list[n] += 1
            else:
                frequency_list[n] = 1
        #build tree based off of this
        priorityQueue = MinPQ()
        for a, b in frequency_list.items():
            priorityQueue.insert(self.Node(b, a))
        while priorityQueue.length > 1:
            #gets frequencies in the list and puts it in the tree
            lNode = priorityQueue.del_min()
            rNode = priorityQueue.del_min()
            #big tree
            tree = self.Node(lNode.b + rNode.b, left = lNode, right= rNode)
            priorityQueue.insert(tree)

        self.root = priorityQueue.del_min()
        self.dictionary = self._build_dictionary()
        return self.root
        


    def _build_dictionary(self, node=None, prefix=''):
        """
        Recursively builds a dictionary that maps characters to their corresponding
        Huffman codes based on the Huffman tree.
        Args:
            node (Node, optional): The current node in the Huffman tree. Defaults to None,
                                   which means the function will start from the root node.
            prefix (str, optional): The current Huffman code prefix. Defaults to an empty string.
        Returns:
            dict: A dictionary where keys are characters and values are their corresponding
                  Huffman codes.
        """
        if node is None:
            node = self.root
        
        if node.char is not None:
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary