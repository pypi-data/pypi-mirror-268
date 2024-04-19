import yaml
from pydantic import BaseModel

class GpuSpec(BaseModel):
    minGpusPerNode: int
    minVramPerGPU: int
    totalGpuCount: int


class JobSpec(BaseModel):
    name: str
    command: list[str]
    gpuSpec: GpuSpec | None = None
    
    @classmethod
    def from_file(cls, filename: str) -> 'JobSpec':
        """
        Load a ClusterSpec from a file
        """
        with open(filename, 'r') as file:
            y = yaml.load(file, Loader=yaml.FullLoader)
            return cls(**y)
    