class Wall:
    '''
    the Wall is used to connect the blocks
    '''
    def __init__(self) -> None:
        pass
    

class Block:
    '''
    the Block is the basic element for every room 
    consider the block as a node of a generation tree and each wall is a link
    '''
    def __init__(self, 
                 width: float,
                 height: float,
                 wallWidth: float) -> None:
        '''
        initialize a block with width, height, and wall width
        define the links
        return nothing
        '''
        self.width = width
        self.height = height
        self.wallWidth = wallWidth
        