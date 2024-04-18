from datetime import datetime

from sidradataquality.sdk.api.sidra.dataquality.utils import Utils as DataQualityApiUtils
from sidradataquality.sdk.log.logging import Logger
import SidraDataQualityApiPythonClient

class ValidationService():
    def __init__(self, spark):
        self.logger = Logger(spark, self.__class__.__name__)
        sidra_dataquality_api_client = DataQualityApiUtils(spark).get_SidraDataQualityApiClient()
        self.validation_expectation_api_instance = SidraDataQualityApiPythonClient.SidraDataQualityApiSValidationExpectationsApi(sidra_dataquality_api_client)
        self.validation_result_api_instance = SidraDataQualityApiPythonClient.SidraDataQualityApiSValidationResultsApi(sidra_dataquality_api_client)
        self.validation_entity_delta_api_instance = SidraDataQualityApiPythonClient.SidraDataQualityApiSValidationEntityDeltasApi(sidra_dataquality_api_client)

    def get_validations_by_entity(self, entity_item_id):
        self.logger.debug(f"[Metadata Validation Service][get_validations_by_entity] Get validations by entity {entity_item_id}")
        return self.validation_expectation_api_instance.api_validations_expectations_entity_entity_item_id_get(entity_item_id=str(entity_item_id))
    
    def set_asset_results(self, provider_name, entity_name, entity_item_id, asset_item_id, validation_status = 1, error_count = 0, file_name = ""):
        self.logger.debug(f"[Metadata Validation Service][set_asset_results] Update validation status {validation_status} for asset {asset_item_id}")
        current_date = datetime.now()
        request_body = [
            {
                "idEntity": entity_item_id,
                "idAsset": asset_item_id,
                "validationErrorCount": error_count,
                "date": current_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "idStatus": validation_status,
                "resultPath": f"{provider_name}/{entity_name}/{str(current_date.year)}/{str(current_date.month).zfill(2)}/{str(current_date.day).zfill(2)}/{file_name}"
            }
        ]
        return self.validation_result_api_instance.api_validations_results_put(body=request_body)
    
    def set_entity_delta(self, entity_item_id, current_date = datetime.now()):
        self.logger.debug(f"[Metadata Validation Service][set_entity_delta] Update entity {entity_item_id} delta ({current_date})")
        entity_deltas = { str(entity_item_id): current_date }
        self.validation_entity_delta_api_instance.api_validations_entitydeltas_put(body=entity_deltas)
