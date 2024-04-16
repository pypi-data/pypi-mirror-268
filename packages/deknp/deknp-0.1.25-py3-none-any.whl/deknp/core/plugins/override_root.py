import os
import tempfile
from distutils.dir_util import copy_tree
from dektools.file.operation import write_file
from .base import Plugin


class PluginOverrideRoot(Plugin):
    dek_overrides_dir_name = 'dek-override'

    def run(self):
        dir_temp = tempfile.mkdtemp()
        dir_temp_final = os.path.join(dir_temp, 'final')
        os.makedirs(dir_temp_final)
        file_ignore_content = ''
        file_ignore_temp_final = os.path.join(dir_temp_final, self.template_full.file_ignore_override[0])
        for i, dir_dek in enumerate(self.dek_dir_list):
            dir_target = os.path.join(dir_temp, str(i))
            src = os.path.join(dir_dek, self.dek_overrides_dir_name)
            if os.path.exists(src):
                os.makedirs(dir_target)
                self.template_full.render_dir(dir_target, src, open_ignore_override=False)
                file_ignore_override = os.path.join(src, self.template_full.file_ignore_override[0])
                if os.path.isfile(file_ignore_override):
                    file_ignore_content += '\n' + self.load_text(file_ignore_override)
                template_file_ignore_override = os.path.join(src, self.template_full.file_ignore_override[1])
                if os.path.isfile(template_file_ignore_override):
                    file_ignore_content += '\n' + self.template_full.render_string(template_file_ignore_override)
        for x in os.listdir(dir_temp):
            path = os.path.join(dir_temp, x)
            if path != dir_temp_final:
                copy_tree(path, dir_temp_final)
        write_file(file_ignore_temp_final, sb=file_ignore_content)
        self.template_full.render_dir(self.project_dir, dir_temp_final, force_close_tpl=True)
