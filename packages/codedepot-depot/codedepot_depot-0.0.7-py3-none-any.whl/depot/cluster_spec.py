from pydantic import Field, BaseModel
import yaml

class ClusterSpec(BaseModel):
    """
    Cluster specification object
    """

    name: str = Field(description="Cluster Name")
    provider: str = Field(description="Cloud Provider Name")
    nodes: list[str] = Field(description="List of node IPs")
    key_file: str = Field(description="SSH Key File")
    
    @classmethod
    def from_file(cls, filename: str) -> 'ClusterSpec':
        """
        Load a ClusterSpec from a file
        """
        with open(filename, 'r') as file:
            y = yaml.load(file, Loader=yaml.FullLoader)
            return cls(**y)
