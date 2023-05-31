def generate_scripts():
    scripts = {}
    scripts['kcwi_acq'] = [
      ["BEGIN_SLEW", "Starts telescope slew"],
      ["WAITFOR_SLEW", "Execution queue locked while slewing"],
      ["ACQUIRE", "OA acquires to PO"],
      ["WAITFOR_ACQUIRE", "Execution queue locked while acquiring"],
      ["CONFIGURE_FOR_SCIENCE", "Sets up SSC for science"],
      ["WAITFOR_CONFIGURE_SCIENCE", "Execution queue locked while science is being configured"]
    ]

    scripts['kcwi_sci'] = [
      ["EXECUTE_OBSERVATION", "Point and shoot"]
    ]
    return scripts

