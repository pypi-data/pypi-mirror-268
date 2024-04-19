from dataclasses import dataclass

@dataclass
class JenkinsPlugin:
    shortName: str
    longName: str
    url: str
    version: str
    hasUpdate: bool
    enabled: bool
    detached: bool
    downgradable: bool
    
    def __post_init__(self):
        self.version = str(self.version)
