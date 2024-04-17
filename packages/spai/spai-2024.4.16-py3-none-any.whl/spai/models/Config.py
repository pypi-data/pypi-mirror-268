from pydantic import BaseModel
from typing import Union, List, Any, Dict
from pathlib import Path
from typing import Optional
import json

from .StorageConfig import LocalStorageConfig, S3StorageConfig


class ScriptConfig(BaseModel):
    name: str
    run_on_start: bool = True
    command: Optional[str] = None
    run_every: Optional[int] = None  # seconds (in cloud minutes)
    storage: Optional[str] = None  # folder to bind in cloud
    type: str = "script"


class NotebookConfig(BaseModel):
    name: str
    command: Union[str, None] = None
    storage: Union[str, None] = None  # folder to bind in cloud
    port: int = 8888
    host: str = "0.0.0.0"
    type: str = "notebook"


class APIConfig(BaseModel):
    name: str
    command: Union[str, None] = None
    port: int = 8000
    host: str = "0.0.0.0"
    storage: Union[str, None] = None  # folder to bind in cloud
    type: str = "api"


class UIConfig(BaseModel):
    name: str
    command: str  # steamlit, javascript, ...
    port: int = 3000
    host: str = "0.0.0.0"
    env: dict = {}  # can accept the name of another service as a url placeholder
    type: str = "ui"


class Config(BaseModel):
    dir: Path
    project: str
    scripts: List[ScriptConfig] = []
    notebooks: List[NotebookConfig] = []
    apis: List[APIConfig] = []
    uis: List[UIConfig] = []
    storage: List[Union[LocalStorageConfig, S3StorageConfig]] = []

    # iterator for all the services
    def __iter__(self):
        # if self.storage:
        #     for storage in self.storage:
        #         yield storage
        if self.scripts:
            for script in self.scripts:
                yield script
        if self.notebooks:
            for notebook in self.notebooks:
                yield notebook
        if self.apis:
            for api in self.apis:
                yield api
        if self.uis:
            for ui in self.uis:
                yield ui
        if self.storage:
            for storage in self.storage:
                yield storage

    def type2folder(self, type):
        return type + "s"


# class Config:

#     def __init__(self, dir, config_filename="spai.config.json"):
#         self.dir = Path(dir)
#         self.config_path = self.dir / config_filename
#         self.config = self.load_config(self.config_path)
#         self.project = self.config.get('project', None)
#         self.scripts = [ScriptConfig(**script) for script in self.config.get('scripts', [])]
#         self.notebooks = [NotebookConfig(**notebook) for notebook in self.config.get('notebooks', [])]
#         self.apis = [APIConfig(**api) for api in self.config.get('apis', [])]
#         self.uis = [UIConfig(**ui) for ui in self.config.get('uis', [])]
#         self.storage = [LocalStorageConfig(**storage) if storage['type'] == 'local' else S3StorageConfig(**storage) for storage in self.config.get('storage', [])]

#     def load_config(self, config_path):
#         if config_path.exists():
#             with open(config_path, "r") as f:
#                 try:
#                     return json.load(f)
#                 except json.JSONDecodeError as e:
#                     print(f"Error loading JSON from {config_path}: {e}")
#         else:
#             print(f"Config file not found: {config_path}")
#         return {}
