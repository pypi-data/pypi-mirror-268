from pathlib import Path
from commitizen.providers import VersionProvider
import re

class LRPluginVersionProvider(VersionProvider):
    file = Path() / "Info.lua"
    search_re = r'(\s*)VERSION\s*=\s*{\s*major\s*=\s*(\d+),\s*minor\s*=\s*(\d+),\s*revision\s*=\s*(\d+),?\s*},?'

    def get_version(self) -> str:
        """
        Reads a version string from the Info.lua file in the format
            VERSION = { major = 1, minor = 1, revision = 0, },
        """

        contents = self.file.read_text()
        match = re.search(self.search_re, contents)
        if match:
            return ".".join(match.group(2,3,4))

        return ""

    def set_version(self, version: str):
        """
        Writes a new Info.lua replacing the version line.
        """
        v = map(int, version.split("."))

        old_content = self.file.read_text()
        new_content = re.sub(
            self.search_re,
            r'\1VERSION = { major = %d, minor = %d, revision = %d, },' % tuple(v),
            old_content
        )

        self.file.write_text(new_content)
