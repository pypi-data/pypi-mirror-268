import os
import json
from dektools.dict import dict_merge
from dektools.file import write_file
from .base import Plugin
from ..base.env_vars import EnvVars


class PluginDv3EnvVars(Plugin):
    env_key = 'vars.env'
    env_path_data = 'deknp.env.log'
    env_path_src = 'index.html'

    def run(self):
        result = {}
        for data in self.dek_info_list:
            env_set = data.get(self.env_key)
            if env_set:
                dict_merge(result, env_set)
        write_file(
            os.path.join(self.project_dir, self.env_path_data),
            json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True)
        )
        ev = EnvVars(os.path.join(self.project_dir, self.env_path_src))
        ev.update('envBase', result.get('base'))
        ev.update('envEnv', result.get('dev'))
