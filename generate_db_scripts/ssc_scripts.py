

def ssc_scripts():
    scripts = {}
    metadata = {}

    # metadata['ssc_acq'] ={
    #     "comment": "Script for template: ssc_acq, 0.1.0",
    #     "instrument": "SSC",
    #     "name": "ssc_acq",
    #     "script_type": "acquisition",
    #     "ui_name": "SSC Acq",
    #     "version": "0.1.0"
    # }

    scripts['ssc_acq'] = [
      ["BEGIN_SLEW", "Starts telescope slew"],
      ["WAITFOR_SLEW", "Execution queue locked while slewing"],
      ["ACQUIRE", "OA acquires to PO"],
      ["WAITFOR_ACQUIRE", "Execution queue locked while acquiring"],
      ["CONFIGURE_SCIENCE", "Sets up SSC for science"],
      ["WAITFOR_CONFIGURE_SCIENCE", "Execution queue locked while science is being configured"]
    ]

    scripts['ssc_sci'] = [
      ["EXECUTE_OBSERVATION", "Point and shoot"]
    ]

    # metadata['ssc_sci'] ={
    #     "comment": "Script for template: ssc_acq, 0.1.0",
    #     "instrument": "SSC",
    #     "name": "ssc_sci",
    #     "script_type": "acquisition",
    #     "ui_name": "SSC Acq",
    #     "version": "0.1.0"
    # }

    return scripts

