from typing import Tuple
from pathlib import Path
import os

import semver

from xmltest import build_schema

def semver_to_tuple(version: dict):
    return (version['major'], version['minor'], version['patch'])

def tuple_to_str(version: Tuple[int, int, int]):
    return f"{version[0]}.{version[1]}.{version[2]}"

class SchemaCatalog():
    def __init__(self):
        self._data_path = Path(os.path.abspath(os.path.dirname(__file__))) / "data"
        self._path_dict = { semver_to_tuple(semver.parse(dir.name)) : dir for dir in self._data_path.iterdir() }
        self._sorted_keys = sorted(self._path_dict.keys())
        self._cache = {}
    
    def build_all_schemas(self):
        for version in self._sorted_keys:
            try:
                schema = self.get_schema_for(tuple_to_str(version))
                print(version, schema)
            except Exception as ex:
                print(version, ex)

    def get_latest_schema(self, format_xsd = True):
        return self.get_schema_for(tuple_to_str(self._sorted_keys[-1]), format_xsd)

    def get_schema_for(self, version: str, format_xsd = True):
        sv = semver.parse(version)
        sv_t = semver_to_tuple(sv)
        if not (sv_t in self._cache.keys()):
            if not (sv_t in self._path_dict.keys()):
                raise Exception(f"No schema for {version}")
            schema_path = self._path_dict[sv_t]
            if format_xsd:
                schema_path = schema_path / "xsd"
            else:
                schema_path = schema_path / "json"
            if not schema_path.exists():
                raise Exception("No schema in correct format under {schema_path}")
            core_schema_path = ""
            supporting_schemas = []
            for file in schema_path.glob("*.*"):
                if "120_core" in file.name.lower():
                    core_schema_path = file.resolve()
                else:
                    supporting_schemas.append(file.resolve())
            schema, _ = build_schema(core_schema_path, supporting_schemas)
            if not schema:
                raise Exception(f"Could not build schema for version {version}")
            self._cache[sv_t] = schema
        return self._cache[sv_t]
