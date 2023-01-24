
from papahana.models.observation_block import ObservationBlock
from papahana.controllers import instrument_controller as inst_cont


class ValidateOB:

    def __init__(self, obs_block):
        self.ob_obj = ObservationBlock.from_dict(obs_block)
        self.ob = obs_block
        self.inst = self.ob_obj.metadata.instrument
        self.err_dict = {'target': {}, 'acquisition': {}, 'common_parameters': {}}

    def get_errors(self):
        return self.err_dict

    def is_valid(self):
        # State values (0=partial, 1=ready, 2=ongoing, 3=complete, 4=aborted)
        if self.ob_obj.status.state < 1:
            return True, {'msg': 'Observation Block in state=0 '
                                 '(Partially Complete).  No validation required.'}

        return self.validate()

    def validate(self):
        components = {'acquisition':  self.ob['acquisition'],
                      'target': self.ob['target'],
                      'common_parameters': self.ob['common_parameters'],
                      'observations': self.ob['observations']}

        valid = True
        for component_name, component_info in components.items():
            if component_name == 'observations':
                if not self._loop_observation_list(component_name, component_info):
                    valid = False
                continue

            if not self.validate_component(component_name, component_info):
                valid = False

        return valid

    def _loop_observation_list(self, component_name, component_info):
        valid =True
        for iter, obs in enumerate(component_info):
            seq_n = obs['metadata']['sequence_number']
            component_name_new = component_name + f'_{seq_n}'
            self.err_dict[component_name_new] = {}
            if not self.validate_component(component_name_new, obs):
                valid = False

        return valid

    def validate_component(self, component_name, component_info):
        ptype = component_name
        temp_name = component_info['metadata']['name']
        comp_temp = inst_cont.instrument_packages_template(
            self.inst.upper(), template_name=temp_name)

        if 'common_parameters' not in temp_name:
            comp_params = component_info['parameters']
            tmplt_params = comp_temp[temp_name]["parameters"]
            return self.check_ob_vs_template(comp_params, tmplt_params, ptype, temp_name)

        # common parameters has different types of parameters
        common_valid = True
        for val in ('instrument_parameters', 'detector_parameters',
                    'guider_parameters', 'tcs_parameters'):
            comp_params = component_info[val]
            tmplt_params = comp_temp[temp_name][val]

            if not self.check_ob_vs_template(comp_params, tmplt_params, ptype, temp_name):
                common_valid = False

        return common_valid

    def check_ob_vs_template(self, comp_params, tmplt_params, ptype, temp_name):
        valid = True
        for pname, pval in dict(comp_params).items():
            if pname not in tmplt_params:
                self.add_error(ptype, pname, pval,
                               f'parameter is not in template: {temp_name}.')
                valid = False

            pdscrp = tmplt_params[pname]

            if not self.check_parameter(ptype, pname, pdscrp, pval):
                valid = False

                # skip further checks with the same parameter, if already failed
                continue

        return valid

    def check_parameter(self, ptype, pname, pdscrp, pval):
        """
        Check the parameter for the first failure.  Only one error
        per parameter,  as fixing one error may fix any further errors.

        :param ptype:
        :param pname:
        :param pdscrp:
        :param pval:
        :return: False if any check fails
        """
        if not self.check_for_required(ptype, pname, pdscrp, pval):
            return False

        if not self.check_type(ptype, pname, pdscrp, pval):
            return False

        if not self.check_allowed(ptype, pname, pdscrp, pval):
            return False

        return True

    def check_for_required(self, ptype, pname, pdscrp, pval):
        if not pval and pdscrp['optionality'] == 'required':
            self.add_error(ptype, pname, pval,
                           'parameter required,  no value defined.')
            return False

        return True

    def check_type(self, ptype, pname, pdscrp, pval):
        # check for null values,  cannot be null if optionality = required
        if not pval:
            if 'optionality' == 'required':
                self.add_error(ptype, pname, pval,
                               'parameter required,  no value defined.')
                return False

            return True


        # string, float, integer, bool, array, file
        js_to_py_type = {
            'string': 'str',
            'integer': 'int',
            'boolean': 'bool',
            'array': 'list'
        }
        if pdscrp['type'] in js_to_py_type:
            pytype_str = js_to_py_type[pdscrp['type']]
        else:
            pytype_str = pdscrp['type']

        pytype = self.string_to_pytype(pytype_str)

        try:
            if not pytype == type(pval):
                self.add_error(ptype, pname, pval,
                               f"parameter value is not of type: {pdscrp['type']}")
                return False
        except:
            return False

        return True

    def check_allowed(self, ptype, pname, pdscrp, pval):
        if "allowed" not in pdscrp:
            return True

        option = pdscrp['option']

        # array, file, open, range, regex, set, static
        if option in ('file', 'open', 'static', 'array'):
            return True

        allowed = pdscrp['allowed']

        if option == 'range':
            if allowed[0] < pval < allowed[1]:
                return True
            self.add_error(ptype, pname, pval,
                           f'value is outside the allowed range: {allowed}')

            return False

        if option == 'set':
            if pval in allowed:
                return True

            self.add_error(ptype, pname, pval,
                           f'value is outside the allowed set: {allowed}')

            return False

        # TODO add regex checks
        if option == 'regex':
            return True

        return False

    def string_to_pytype(self, type_str):
        """
        Convert a variable type written as a string to a python type class

        :param type_str: string defining the variable type
        :return: python type class,  or None
        """
        # remove any spaces
        type_str = type_str.strip()

        try:
            pytype = eval(type_str)
        except (NameError, SyntaxError):
            return None

        return pytype

    def add_error(self, ptype, pname, pval, msg):
        if pname not in self.err_dict[ptype]:
            self.err_dict[ptype][pname] = {pval: msg}
