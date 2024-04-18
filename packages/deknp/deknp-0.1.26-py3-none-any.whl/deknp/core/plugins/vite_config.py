import os
import json
from .base import PluginVue, PluginUniapp


class PluginViteConfig(PluginVue, PluginUniapp):
    vite_config_standard_name = 'vite.config.js'
    dek_config_marker = '//@marker-dek-config-add'

    @property
    def all_vite_imports(self):
        result = []

        for data_dek in self.dek_info_list:
            items = (data_dek.get(self.vite_config_standard_name) or {}).get('imports') or []
            result.extend(items)

        return result

    @property
    def all_vite_plugins(self):
        result = []

        for data_dek in self.dek_info_list:
            items = (data_dek.get(self.vite_config_standard_name) or {}).get('plugins') or []
            result.extend(items)

        return result

    @property
    def all_vite_alias(self):
        result = {}

        for data_dek in self.dek_info_list:
            items = (data_dek.get(self.vite_config_standard_name) or {}).get('alias') or {}
            result.update(items)

        return result

    @property
    def all_vite_scssheader(self):
        result = []

        for data_dek in self.dek_info_list:
            items = (data_dek.get(self.vite_config_standard_name) or {}).get('scssHeader') or []
            result.extend(items)

        return result

    def run(self):
        if self.is_uniapp_project():
            if self.get_uniapp_vue_version() != 3:
                return
        else:
            version = self.get_vue_version()
            if not version or version[0] != 3:
                return
        if not os.path.isfile(self.vue_config_standard_filepath):
            return
        s = self.load_text(self.vue_config_standard_filepath)
        str_list = []

        for item in sorted(set(self.all_vite_plugins)):
            mk = f'marker--addPlugin--{self.get_data_uid(item)}'
            if mk not in s:
                str_list.append(f'dekConfig.addPlugin({json.dumps(mk)}, {item})')

        for key in sorted(self.all_vite_alias):
            value = self.all_vite_alias[key]
            mk = f'marker--addAlias--{self.get_data_uid([key, value])}'
            if mk not in s:
                str_list.append(f'dekConfig.addAlias({json.dumps(mk)}, {json.dumps(key)}, {value})')

        for item in sorted(set(self.all_vite_scssheader)):
            mk = f'marker--addScssHeader--{self.get_data_uid(item)}'
            if mk not in s:
                str_list.append(f'dekConfig.addScssHeader({json.dumps(mk)}, {json.dumps(item)})')

        index = s.find(self.dek_config_marker)
        ss = ''.join([
            s[:index], '\n',
            '\n'.join([x for x in self.all_vite_imports if x not in s]), '\n',
            '\n'.join(str_list), '\n',
            s[index:]
        ])
        self.save_text(self.vue_config_standard_filepath, ss)

    @property
    def vue_config_standard_filepath(self):
        return os.path.join(self.project_dir, self.vite_config_standard_name)
