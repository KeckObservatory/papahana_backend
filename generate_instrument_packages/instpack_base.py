import sys
from papahana import util as papahana_util


class InstPackBase:
    def __init__(self, inst):
        self.inst = inst.upper()

    def generate_ip(self, template_list, recipe_list):
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def get_scripts(self):
        """

        @return: A dictionary (key=script name) of scripts.  Scripts are lists
                of two element lists.
                {'inst_acq': [['BEGIN_SLEW', 'Starts telescope slew'], ...]}
        @rtype: <dict/list/list>
        """
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def get_recipes(self):
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def acq_templates(self):
        """

        @return: list of dictionaries containing all acquisition templates
        @rtype: <list/dict>
        """
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def sci_templates(self):
        """

        @return: list of dictionaries containing all science templates
        @rtype: <list/dict>
        """
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def common_parameters_template(self):
        """

        @return: list of dictionaries containing all science templates
        @rtype: <list/dict>
        """
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def cal_templates(self):
        """

        @return: list of dictionaries containing all calibration templates
        @rtype: <list/dict>
        """
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def misc_templates(self):
        """

        @return: list of dictionaries containing all extra templates
        @rtype: <list/dict>
        """
        raise NotImplementedError(f"{sys._getframe().f_code.co_name} has not been implemented!")

    def get_all_templates(self):
        """

        @return: list of dictionaries containing all templates
        @rtype: <list/dict>
        """
        all_tmp = self.acq_templates() + self.sci_templates() + self.misc_templates() + \
        self.cal_templates() + self.common_parameters_template()

        return all_tmp

    def get_template_list(self, config):
        """

        @return: list of template names
        @rtype: <list>
        """
        coll_tmp = papahana_util.config_collection('templateCollect', conf=config)
        fields = {'metadata.name': 1, 'metadata.version': 1}
        query = {'metadata.instrument': self.inst}
        results = list(coll_tmp.find(query, fields))
        return results

    def get_inst_package(self, config, template_list):
        print("...generating instrument package")

        # add templates
        if not template_list:
            template_list = self.get_template_list(config)

        # add recipes
        coll_recipe = papahana_util.config_collection('recipeCollect', conf=config)
        fields = {'metadata.name': 1, '_id': 0}
        query = {'metadata.inst': self.inst}
        recipe_list = list(coll_recipe.find(query, fields))

        ip = self.generate_ip(template_list, recipe_list)

        return ip


    def generate_scripts(self, script_name, script_type, version):

        scripts = self.get_scripts()

        if script_name in scripts:
            script = scripts[script_name]
        else:
            script = {'TBD': 'TBD'}

        ui_name = script_name.replace('_', ' ').title()
        schema = {
            'metadata': {
                'name': script_name,
                'ui_name': ui_name,
                'version': version,
                'instrument': self.inst,
                'script_type': script_type,
                'comment': f'Script for template: {script_name}, {version}'
            },
            'script': script
        }

        return schema

    def generate_scripts_collection(self, coll, coll_inst, coll_tmp, inst):

        query = {'metadata.instrument': inst}
        fields = {'_id': 0, 'template_list': 1}

        results = list(coll_inst.find(query, fields))[0]

        for tmp in results['template_list']:
            query = {'metadata.instrument': inst,
                     'metadata.name': tmp['metadata']['name'],
                     'metadata.version': tmp['metadata']['version']}

            fields = {'_id': 0, 'metadata': 1}
            results = list(coll_tmp.find(query, fields))
            if not results:
                continue

            results = results[0]
            if not results or 'metadata' not in results:
                continue

            meta = results['metadata']
            if 'version' not in meta or 'template_type' not in meta \
                    or 'script' not in meta:
                print('skipping')
                continue

            script_name = results['metadata']['script']
            version = results['metadata']['version']
            script_type = results['metadata']['template_type']

            schema = self.generate_scripts(script_name, script_type, version)
            _ = coll.insert_one(schema)

        return coll

    def generate_recipes(self, config, replace=1):
        print("...generating recipes")
        coll = papahana_util.config_collection('recipeCollect', conf=config)

        recipes = self.get_recipes()

        if replace != 1:
            for name, schema in recipes.items():
                _ = coll.insert_one(schema)

            return

        for recipe_name, recipe in recipes.items():
            query = {'metadata.name': recipe_name}
            fields = {'_id': 1}

            result = list(coll.find(query, fields))
            if not result:
                coll.insert_one(recipe)
                continue

            query = result[0]

            _ = coll.replace_one(query, recipe)

        return

    def generate_templates(self, config, replace=1):
        print("...generating templates")
        coll = papahana_util.config_collection('templateCollect', conf=config)

        if replace != 1:
            templates = self.get_all_templates()

            _ = coll.insert_many(templates, ordered=False, bypass_document_validation=True)

            return

        tmp_list = self.get_all_templates()
        for tmp in tmp_list:
            ver = tmp['metadata']['version']
            name = tmp['metadata']['name']

            query = {'metadata.name': name, 'metadata.version': ver}
            fields = {'_id': 1}

            result = list(coll.find(query, fields))
            if not result:
                coll.insert_one(tmp)
                continue

            query = result[0]

            _ = coll.replace_one(query, tmp)

        return