from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._rock = rock
        self._gem = gem
        
    def get_rock(self):
        """Gets the rocks position.
        
        Returns:
            string: The rocks position.
        """
        return self._rock
        
    def get_gem(self):
        """Gets the gem position.
        
        Returns:
            string: The gems position.
        """
        return self._gem
    
    def set_rock(self, rock):
        """Updates the rocks position.
        
        Args:
            rock (string): The rocks position.
        """
        self._rock = rock
    
    def set_gem(self, gem):
        """Updates the gems position.
        
        Args:
            gem (string): The gems position.
        """
        self._gem = gem