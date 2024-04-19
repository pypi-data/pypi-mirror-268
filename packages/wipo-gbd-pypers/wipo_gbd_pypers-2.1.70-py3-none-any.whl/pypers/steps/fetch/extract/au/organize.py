import os
import shutil
import copy
import json

from datetime import datetime

from pypers.steps.fetch.common.organize import Organize as BaseOrganize

class Organize(BaseOrganize):
    archive_splitter_nb = 20

    def process(self):
        # nothing to do
        if not len(self.manifest['data_files'].keys()):
            return
        archive_date = self.manifest['archive_date']
        archive_name = self.manifest['archive_name']
        archive_file = self.manifest['archive_file']

        # STAGE the original files
        ori_gen_path = os.path.join(os.environ.get('ORIFILES_DIR'), # mandatory ENV VARIABLE - we do not want to make defaults
                                    self.run_id,
                                    self.pipeline_type,
                                    self.collection,
                                    archive_date,
                                    "%s_%s" % (archive_name, "%s"))
        manifests = []
        for i in range(0, self.archive_splitter_nb):
            os.makedirs(ori_gen_path % i, exist_ok=True)
            manifests.append({'files': {}})

        # -- move the data files to ori stage
        for appnum, item in self.manifest['data_files'].items():
            ori_path = ori_gen_path % (int(appnum) % self.archive_splitter_nb)
            if os.path.exists(os.path.join(self.manifest['extraction_dir'], item.get('ori'))):
                self._move_object(ori_path, item.get('ori'))

        # -- move the image files to ori stage
        for appnum, item in self.manifest['img_files'].items():
            for img in item:
                ori_path = ori_gen_path % (int(appnum) % self.archive_splitter_nb)
                if os.path.exists(os.path.join(self.manifest['extraction_dir'], img.get('ori', ''))):
                    self._move_object(ori_path, img.get('ori', None))
        # -- create manifest file in ori stage

        for key in self.manifest['data_files'].keys():
            manifest = manifests[(int(key) % self.archive_splitter_nb)]
            if key not in manifest['files']:
                manifest['files'][key] = {}
            manifest['files'][key]['data'] = self.manifest['data_files'][key]
        for key in self.manifest['img_files'].keys():
            manifest = manifests[(int(key) % self.archive_splitter_nb)]
            if key not in manifest['files']:
                manifest['files'][key] = {}
            manifest['files'][key]['imgs'] = self.manifest['img_files'][key]
        for i in range(0, self.archive_splitter_nb):
            manifest = manifests[i]
            for key in manifest['files'].keys():
                manifest['files'][key].update({
                    'gbd_extraction_date': datetime.now().strftime('%Y-%m-%d'),
                    'archive_date' : self.manifest['archive_date'],
                    'archive_name' : self.manifest['archive_name'],
                    'archive_file' : self.manifest['archive_file'],
                })
            ori_path = ori_gen_path % i
            tmp = os.path.join(ori_path, 'manifest.json')
            with open(tmp, 'w') as f:
                json.dump(manifest, f, indent=2)
        self.manifest = []
        for i in range(0, self.archive_splitter_nb):
            ori_path = ori_gen_path % i
            self.manifest.append(os.path.join(ori_path, 'manifest.json'))

    def postprocess(self):
        pass
