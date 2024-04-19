from pydantic import Field, BaseModel
import yaml

class ProviderSpec(BaseModel):
    """
    Cloud Provider specification object
    """

    name: str = Field(description="Cloud Provider Instance Name")
    provider_type: str = Field(description="Cloud Provider Type")
    credentials: str = Field(description="Cloud Provider Credentials File")
    
    @classmethod
    def from_file(cls, filename: str) -> 'ProviderSpec':
        """
        Load a ProviderSpec from a file
        """
        with open(filename, 'r') as file:
            y = yaml.load(file, Loader=yaml.FullLoader)
            return cls(**y)
