#
# nosql.py
#

import os
import oci

NOSQL_COMPARTMENT_ID = os.environ.get('NOSQL_COMPARTMENT_ID')
NOSQL_TABLE_ID = os.environ.get('NOSQL_TABLE_ID')
FLASK_ENV = os.environ.get('FLASK_ENV', 'development')

class Nosql():
    def __init__(self):
        if FLASK_ENV == 'development':
            config = oci.config.from_file()
            self.__nosql_client = oci.nosql.NosqlClient(config=config)
        else:        
            signer = oci.auth.signers.get_resource_principals_signer()
            self.__nosql_client = oci.nosql.NosqlClient(config={}, signer=signer)
    
    def add(self, value: dict):
        self.__nosql_client.update_row(
            table_name_or_id=NOSQL_TABLE_ID,
            update_row_details=oci.nosql.models.UpdateRowDetails(
                value=value,
                compartment_id=NOSQL_COMPARTMENT_ID,            
                option='IF_ABSENT'
            )
        )