import pymongo

from papahana import util


"""
The test values are retreived from the database defined as 'test' in the 
config file.
"""

class ContainerTestDefaults:
    def __init__(self, mode):
        self.config = util.read_config(mode)
        coll = util.config_collection('containerCollect', conf=self.config)
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
        coll = util.config_collection('obCollect', conf=self.config)
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
        if '_ob_id' in ob.keys():
            del ob['_ob_id']

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
            if 'sequences' in ob:
                return ob['sequences'][0]

        return "ERROR no OBs with sequence templates defined"

    def get_example_time_constraints(self, indx):
        ob = self.get_example_ob(indx)
        return ob['time_constraints']

