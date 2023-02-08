

def kpf_scripts():
    scripts = {}

    scripts['kpf_acq'] = [
        ['BEGIN_SLEW', 'Starts telescope slew'],
        ['CONFIGURE_FOR_ACQUISITION', 'Sets: octagon, (does slew cal), FIU mode, target parameters, guide camera parameters'],
        ['WAITFOR_CONFIGURE_ACQUISITION', 'Waits for FIU mode'],
        ['WAITFOR_SLEW', ''],
        ['ACQUIRE', 'OA acquires to PO'],
        ['WAITFOR_ACQUIRE', ''],
        ['CONFIGURE_SCIENCE', 'Sets CURRENT_BASE, Turns on Tip Tilt, then Sets: octagon (should not move), source select shutters, triggered detectors'],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits for FIU mode, octagon, detector ready']
    ],

    scripts['kpf_sci'] = [
        ['EXECUTE_OBSERVATION', '']
    ]

    return scripts

