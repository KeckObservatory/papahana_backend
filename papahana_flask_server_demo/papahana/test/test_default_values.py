import pymongo

from config import config_collection
from papahana import util


class ContainerTestDefaults:
    def __init__(self, mode):
        self.config = util.read_config(mode)
        coll = config_collection('containerCollect', conf=self.config)
        self.container_list = list(coll.find({}, sort=[('_id', pymongo.DESCENDING)]))

    def get_example_container(self, indx):
        if indx > len(self.container_list):
            indx = -1

        container = self.container_list[indx]

        if '_id' in container.keys():
            del container['_id']

        return container


class ObsBlocksTestDefaults:
    def __init__(self, mode):
        self.config = util.read_config(mode)
        coll = config_collection('obCollect', conf=self.config)
        self.ob_list = list(coll.find({"metadata.ob_type": 'science'},
                                      sort=[('_id', pymongo.DESCENDING)]))

        self.example_ob_id = []
        self.init_ob_keys()

    def init_ob_keys(self):
        self.example_ob_id.append(self.save_example_ob_id(0))
        self.example_ob_id.append(self.save_example_ob_id(-1))

    def get_example_ob_id(self, indx=0):
        if indx > len(self.example_ob_id):
            return self.example_ob_id[-1]
        return self.example_ob_id[indx]

    def get_example_ob(self, indx=0):
        if indx > len(self.ob_list):
            indx = -1

        ob = self.ob_list[indx]

        if '_id' in ob.keys():
            del ob['_id']

        return self.ob_list[indx]

    def save_example_ob(self, indx):
        ob = self.ob_list[indx]
        del ob['_id']
        return ob

    def save_example_ob_id(self, indx):
        ob = self.ob_list[indx]
        return str(ob['_id'])

    def get_filled_template(self):
        for ob in self.ob_list:
            if 'science' in ob:
                return ob['science'][0]

        return "ERROR no OBs with science templates defined"

    def get_example_time_constraints(self, indx):
        ob = self.get_example_ob(indx)
        return ob['time_constraints']





# def get_example_ob():
#     ob = {
#         "metadata":
#             {"name": "standard stars #9",
#             "version": 0.1,
#             "priority": 70.8112646283874,
#             "ob_type": "science",
#             "pi_id": 7766,
#             "sem_id": "2019A_U124",
#             "instrument": "KCWI"},
#         "acquisition": {
#             "metadata": {
#                 "name": "KCWI_ifu_acq_direct",
#                 "ui_name": "KCWI direct",
#                 "instrument": "KCWI",
#                 "type": "acquisition",
#                 "version": 0.1,
#                 "script": "KCWI_ifu_acq_direct"},
#             "parameters": {
#                 "wrap": "auto",
#                 "rotmode": "PA",
#                 "guider_po": "IFU",
#                 "guider_gs_ra": "12:44:55.6",
#                 "guider_gs_dec": "55:22:19.9",
#                 "guider_gs_mode": "auto"},
#                 "template_id": "acq0"
#             },
#         "science": [{
#             "metadata": {
#                 "name": "KCWI_ifu_sci_dither",
#                 "ui_name": "KCWI dither",
#                 "instrument": "KCWI",
#                 "type": "science",
#                 "version": 0.1,
#                 "script": "KCWI_ifu_sci_stare"
#             },
#             "parameters": {
#                 "det1_exptime": 60,
#                 "det1_nexp": 2,
#                 "det2_exptime": 121,
#                 "det2_nexp": 4,
#                 "seq_ndither": 4,
#                 "seq_ditarray": [{"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True},
#                                {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                                {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                                {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}]},
#             "template_id": "sci0"
#             },
#             {"metadata": {
#                 "name": "KCWI_ifu_sci_dither",
#                 "ui_name": "KCWI dither",
#                 "instrument": "KCWI",
#                 "type": "science",
#                 "version": 0.1,
#                 "script": "KCWI_ifu_sci_stare"},
#                 "parameters": {
#                     "det1_exptime": 60,
#                     "det1_nexp": 2,
#                     "det2_exptime": 121,
#                     "det2_nexp": 4,
#                     "seq_ndither": 4,
#                     "seq_ditarray": [
#                       {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True},
#                       {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                       {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                       {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}
#                     ]},
#                 "template_id": "sci1"}
#           ],
#           "associations": ["TBD"],
#           "status": {
#               "state": "Started",
#               "executions": ["2018-04-13 16:38:13", "2020-03-22 07:05:13"],
#               "deleted": False
#           },
#           "time_constraints": ["2021-05-01 08:00:00", "2021-06-01 10:00:00"],
#           "comment": "This is a Test!  Only a Test!"
#           }
#
#     return ob
#
# def get_example_ob_new():
#     ob = {
#         "metadata":
#             {"name": "NEW standard stars #9",
#             "version": 0.2,
#             "priority": 70.1,
#             "ob_type": "science",
#             "pi_id": 7766,
#             "sem_id": "2021A_U777",
#             "instrument": "KCWI"},
#         "acquisition": {
#             "metadata": {
#                 "name": "KCWI_ifu_acq_direct",
#                 "ui_name": "KCWI direct",
#                 "instrument": "KCWI",
#                 "type": "acquisition",
#                 "version": 0.1,
#                 "script": "KCWI_ifu_acq_direct"},
#             "parameters": {
#                 "wrap": "auto",
#                 "rotmode": "PA",
#                 "guider_po": "IFU",
#                 "guider_gs_ra": "12:44:55.6",
#                 "guider_gs_dec": "55:22:19.9",
#                 "guider_gs_mode": "auto"},
#                 "template_id": "acq0"
#             },
#         "science": [
#             {"metadata": {
#                 "name": "KCWI_ifu_sci_dither",
#                 "ui_name": "KCWI dither",
#                 "instrument": "KCWI",
#                 "type": "science",
#                 "version": 0.1,
#                 "script": "KCWI_ifu_sci_stare"
#             },
#             "parameters": {
#                 "det1_exptime": 60,
#                 "det1_nexp": 2,
#                 "det2_exptime": 121,
#                 "det2_nexp": 4,
#                 "seq_ndither": 4,
#                 "seq_ditarray": [{"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True},
#                                {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                                {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                                {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}]},
#                 "template_id": "sci0"
#             },
#             {"metadata": {
#                 "name": "KCWI_ifu_sci_dither",
#                 "ui_name": "KCWI dither",
#                 "instrument": "KCWI",
#                 "type": "science",
#                 "version": 0.1,
#                 "script": "KCWI_ifu_sci_stare"},
#                 "parameters": {
#                     "det1_exptime": 60,
#                     "det1_nexp": 2,
#                     "det2_exptime": 121,
#                     "det2_nexp": 4,
#                     "seq_ndither": 4,
#                     "seq_ditarray": [
#                       {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True},
#                       {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                       {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
#                       {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}
#                     ]},
#                 "template_id": "sci1"}
#           ],
#           "associations": ["TBD"],
#           "status": {
#               "state": "Started",
#               "executions": ["2018-04-13 16:38:13", "2020-03-22 07:05:13"],
#               "deleted": False
#           },
#           "time_constraints": ["2021-05-01 08:00:00", "2021-06-01 10:00:00"],
#           "comment": "This is a new Test!  Only a new Test!"
#           }
#
#     return ob
#
#
# def get_filled_template():
#     filled_template = {
#         "metadata": {
#             "name": "KCWI_ifu_sci_stare",
#             "ui_name": "KCWI stare",
#             "instrument": "KCWI",
#             "template_type": "science",
#             "version": 0.1,
#             "script": "KCWI_ifu_sci_stare"},
#         "parameters": {
#             "det1_exptime": 30.2,
#             "det1_nexp": 4,
#             "det2_exptime": 40.1,
#             "det2_nexp": 5}}
#
#     return filled_template
#
#
# def get_unfilled_template():
#     unfilled_template = {
#         "metadata": {
#             "name": "KCWI_ifu_sci_stare",
#             "ui_name": "KCWI stare",
#             "instrument": "KCWI",
#             "template_type": "science",
#             "version": 0.1,
#             "script": "KCWI_ifu_sci_stare"},
#         "parameters": {
#             "det1_exptime": {
#                 "ui_name": "Blue exposure time",
#                 "option": "range",
#                 "allowed": [0, 3600],
#                 "default": None,
#                 "optionality": "required",
#                 "type": "float"},
#             "det1_nexp": {
#                 "ui_name": "Blue number of exposures",
#                 "option": "range",
#                 "allowed": [0, 3600],
#                 "default": None,
#                 "optionality": "required",
#                 "type": "integer"},
#             "det2_exptime": {
#                 "ui_name": "Red exposure time",
#                 "option": "range",
#                 "allowed": [0, 3600],
#                 "default": None,
#                 "optionality": "optional",
#                 "type": "float"},
#             "det2_nexp": {
#                 "ui_name": "Blue number of exposures",
#                 "option": "range",
#                 "allowed": [0, 3600],
#                 "default": None,
#                 "optionality": "optional",
#                 "type": "integer"}}}
#
#     return unfilled_template
#
#
#
