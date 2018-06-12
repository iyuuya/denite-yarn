# -*- coding: utf-8 -*-

from .base import Base
import subprocess
import json

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'yarn'
        self.kind = 'command'

    def gather_candidates(self, context):
        cmd = ['yarn', 'run', '--json']
        result = subprocess.run(cmd,
                                check=True,
                                universal_newlines=True,
                                stdout=subprocess.PIPE
                                ).stdout.split("\n")
        return [{'word': command, 'action__command': ':split term://yarn run ' + command}
                for command in json.loads(result[2])['data']['items']]
