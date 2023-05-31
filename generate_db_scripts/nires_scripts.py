

def generate_scripts():
    scripts = {}

    scripts['nires_acq'] = [
        ['BEGIN_SLEW', 'Starts telescope slew'],
        ['CONFIGURE_FOR_ACQUISITION', 'target parameters, guide camera parameters'],
        ['WAITFOR_CONFIGURE_ACQUISITION', ''],
        ['WAITFOR_SLEW', ''],
        ['ACQUIRE', 'OA acquires to PO'],
        ['WAITFOR_ACQUIRE', ''],
    ]

    scripts['nires_sci'] = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits detector ready'],
        ['EXECUTE_OBSERVATION', ''],
        ['POST_OBSERVATION_CLEANUP', '']
    ]
    return scripts

