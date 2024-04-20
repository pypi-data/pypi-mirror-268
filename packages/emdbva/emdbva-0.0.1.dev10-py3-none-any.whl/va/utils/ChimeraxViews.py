import json
import os
import re
import sys
import subprocess
from distutils.spawn import find_executable
from va.utils.misc import scale_image, out_json
try:
    from va.PATHS import CHIMERA
except ImportError:
    CHIMERA = None

class ChimeraxViews:

    def __init__(self, input_json):
        self.input_json = input_json
        self.va_dir = os.path.dirname(self.input_json)
        if self.input_json:
            with open(input_json, 'r') as f:
                self.json_data = json.load(f)
        else:
            self.json_data = None
            print('There is no json file data.')


    def get_root_data(self, data_type):
        """
            Get the root json data based on the input json file and the data type

        :param data_type: a string of full path name of the json file
        """

        root_data = None
        if data_type in self.json_data.keys():
            root_data = self.json_data[data_type]
            try:
                del root_data['err']
            except:
                print('There is/are %s model(s).' % len(root_data))
        else:
            print(f'{data_type} json result is')

        return root_data

    def write_residue_cxc(self, colors, residues, map_name, model_name, data_type):
        """
            Write a ChimeraX cxc file for generating surfaces with model cases
        :param colors: list of colors
        :param residues: list of residues e.g., A:321 THR
        :param map_name: a string of input file name
        :param model_name: a string of input model name
        :param data_type: a string of surface type, e.g., residue_local_resolution
        """

        if data_type:
            cur_type = data_type.replace('_', '')
            chimerax_file_name = f'{map_name}_{model_name}_{cur_type}_chimerax.cxc'
        else:
            cur_type = ''
            chimerax_file_name = f'{map_name}_{model_name}_chimerax.cxc'

        surface_file_name = '{}/{}_{}'.format(self.va_dir, map_name, model_name)
        model = f'{self.va_dir}/{model_name}'
        with open(f'{self.va_dir}/{chimerax_file_name}', 'w') as fp:
            fp.write(f'open {model} format mmcif\n')
            fp.write('show selAtoms ribbons\n')
            fp.write('hide selAtoms\n')

            for (color, residue) in zip(colors, residues):
                chain, restmp = residue.split(':')
                # Not sure if all the letters should be replaced
                # res = re.sub("\D", "", restmp)
                res = re.findall(r'-?\d+', restmp)[0]
                fp.write(
                    f'color /{chain}:{res} {color}\n'
                )
            fp.write(
                'set bgColor white\n'
                'lighting soft\n'
                'view cofr True\n'
                f'save {str(surface_file_name)}_z{cur_type}.jpeg supersample 3 width 1200 height 1200\n'
                'turn x -90\n'
                'turn y -90\n'
                'view cofr True\n'
                f'save {str(surface_file_name)}_y{cur_type}.jpeg supersample 3 width 1200 height 1200\n'
                'view orient\n'
                'turn x 90\n'
                'turn z 90\n'
                'view cofr True\n'
                f'save {str(surface_file_name)}_x{cur_type}.jpeg supersample 3 width 1200 height 1200\n'
                'close all\n'
                'exit'
            )

            return chimerax_file_name

    def chimerax_envcheck(self):
        """
            Get the ChimeraX executable full path
            Either from PATH or in environment variables
        """

        chimerax_app = None
        try:
            if CHIMERA is not None:
                chimerax_app = CHIMERA
                print(chimerax_app)
            else:
                assert find_executable('ChimeraX') is not None
                chimerax_app = find_executable('ChimeraX')
                print(chimerax_app)

        except AssertionError:
            sys.stderr.write('ChimeraX executable is not there.\n')

        return chimerax_app

    def run_chimerax(self, chimerax_file_name):
        """
            Run ChimeraX to produce the surface views

        :param chimerax_file_name: a string of ChimeraX cxc file
        """
        errs = []
        chimerax = self.chimerax_envcheck()
        model_name = chimerax_file_name.split('_')[1]
        bin_display = os.getenv('DISPLAY')
        try:
            if not bin_display:
                subprocess.check_call(f'{chimerax} --offscreen --nogui {self.va_dir}/{chimerax_file_name}',
                                      cwd=self.va_dir, shell=True)
                print('Colored models were produced.')
            else:
                subprocess.check_call(f'{chimerax}  {self.va_dir}/{chimerax_file_name}', cwd=self.va_dir, shell=True)
                print('Colored models were produced.')

            return None
        except subprocess.CalledProcessError as e:
            err = 'Saving model {} fit surface view error: {}.'.format(model_name, e)
            errs.append(err)
            sys.stderr.write(err + '\n')

            return errs

    def rescale_view(self, map_name, model_name=None, data_type=None):
        """
            Scale views and produce corresponding dictionary

        :param map_name: a string of input map name
        :param model_name: a string of input model name
        :param data_type: a string of view type
        """

        original = {}
        scaled = {}
        result = {}
        used_data_type = data_type.replace('_', '')
        for i in 'xyz':
            if model_name is None:
                image_name = f'{map_name}_{i}{used_data_type}.jpeg'
            else:
                image_name = f'{map_name}_{model_name}_{i}{used_data_type}.jpeg'
            full_image_path = f'{self.va_dir}/{image_name}'
            if os.path.isfile(full_image_path):
                scaled_image_name = scale_image(full_image_path, (300, 300))
                original[i] = image_name
                scaled[i] = scaled_image_name
        result['original'] = original
        result['scaled'] = scaled

        return result

    def get_views(self, root_data, map_name, data_type=None):
        """
            Based on the information produce views and save to json file

        :param root_data: root data from input json file
        :param map_name: a string of input map nanme
        :param data_type: a string of view type
        """

        num_model = len(root_data)

        for i in range(num_model):
            output_json = {}
            json_dict = {}
            cur_model = root_data[str(i)]
            keylist = list(cur_model.keys())
            colors = None
            residues = None
            model_name = None
            for key in keylist:
                if key != 'name':
                    colors = cur_model[key]['color']
                    residues = cur_model[key]['residue']
                else:
                    model_name = cur_model[key]
            chimerax_file_name = self.write_residue_cxc(colors, residues, map_name, model_name, data_type)
            out = self.run_chimerax(chimerax_file_name)
            surfaces_dict = self.rescale_view(map_name, model_name, data_type)
            json_dict[model_name] = surfaces_dict
            output_json[f'{data_type}_views'] = json_dict

            output_json_file = f"{map_name}_{model_name}_{data_type.replace('_', '')}.json"
            output_json_fullpath = f'{self.va_dir}/{output_json_file}'
            out_json(output_json, output_json_fullpath)




