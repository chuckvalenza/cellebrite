from Mits.Families.Qualcomm.DLoadMode import *
# Set this to true if phone is in diag mode upon connection, and we have to
###
configuration_file_name = r"__script_lg_qc_internal.xml" 
config = upy.get_config(configuration_file_name, configuration_params)

upy.ui_async_operation("Connecting", "Please wait")
c = ClientQcDownloadInternal(f)
if config.PHONE_CONNECTED_IN_DIAG_MODE:
c.dump()