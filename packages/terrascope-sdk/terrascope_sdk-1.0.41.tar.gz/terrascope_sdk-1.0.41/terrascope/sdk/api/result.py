import os
import re
import boto3
import shutil
import logging
import tempfile
import pandas as pd
from zipfile import ZipFile
from datetime import datetime
from typing import Dict, List
from collections import defaultdict
from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

from terrascope_api import TerrascopeAsyncClient
from terrascope_api.models.common_models_pb2 import Pagination
from terrascope_api.models.result_pb2 import ResultGetRequest, ResultGetResponse, ResultExportRequest


class APIResult:
    def __init__(self, client: TerrascopeAsyncClient, timeout):
        self.__timeout = timeout
        self.__client = client

    @staticmethod
    async def merge_download_files(
        algorithm_computation_id_to_data_type_to_downloaded_paths: Dict[str, Dict[str, List[str]]],
        download_dir: str = None
    ) -> Dict[str, Dict[str, str]]:
        download_dir = os.getcwd() if not download_dir else download_dir
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        algorithm_computation_id_to_data_type_to_merged_file = defaultdict(lambda: defaultdict(str))
        for (algorithm_computation_id,
                data_type_to_downloaded_paths) in algorithm_computation_id_to_data_type_to_downloaded_paths.items():
            for data_type, downloaded_paths in data_type_to_downloaded_paths.items():
                merged_file_dir = os.path.join(download_dir, algorithm_computation_id)
                os.makedirs(merged_file_dir, exist_ok=True)
                merged_file = os.path.join(merged_file_dir, f'{data_type}.csv')
                logging.info(f"Merging files for algorithm_computation_id {algorithm_computation_id} "
                             f"and data_type {data_type} to {merged_file}")

                header_written = False
                with open(merged_file, 'w') as output_csv:
                    for idx, downloaded_path in enumerate(downloaded_paths):
                        with tempfile.TemporaryDirectory() as working_dir:
                            interim_path = f'{working_dir}/{idx}'
                            os.mkdir(interim_path)
                            with ZipFile(downloaded_path, 'r') as zip_ref:
                                zip_ref.extractall(interim_path)
                            csv_path = f'{interim_path}/{data_type}.csv'
                            with open(csv_path, 'r') as input_csv:
                                if header_written:
                                    next(input_csv)
                                output_csv.write(input_csv.read())
                                header_written = True
                algorithm_computation_id_to_data_type_to_merged_file[algorithm_computation_id][data_type] = merged_file
        return algorithm_computation_id_to_data_type_to_merged_file


    async def export(
        self, algorithm_computation_ids: List[str] = None, analysis_computation_ids: List[str] = None,
        source_aoi_version: int = None, min_observation_start_ts: str = None, max_observation_start_ts: str = None,
        download_dir: str = None
    ) -> Dict[str, Dict[str, List[str]]]:
        """
        algorithm_computation_ids: [Required] List[str] - Algorithm computation IDs

        :return: Dict[str, Dict[str, List[str]]]: mapping of algorithm_computation_id_to_data_type_to_downloaded_paths
        """
        download_dir = os.getcwd() if not download_dir else download_dir
        request = ResultExportRequest(
            algorithm_computation_ids=algorithm_computation_ids,
            analysis_computation_ids=analysis_computation_ids,
            export_type=ResultExportRequest.ExportType.STANDARD,
            file_type=ResultExportRequest.FileType.CSV
        )
        if source_aoi_version:
            request.source_aoi_version = source_aoi_version
        if min_observation_start_ts:
            min_observation_start_dt = datetime.strptime(min_observation_start_ts, '%Y-%m-%d')
            min_observation_start_timestamp = Timestamp()
            min_observation_start_timestamp.FromDatetime(min_observation_start_dt)
            request.min_observation_start_ts.MergeFrom(min_observation_start_timestamp)
        if max_observation_start_ts:
            max_observation_start_dt = datetime.strptime(max_observation_start_ts, '%Y-%m-%d')
            max_observation_start_timestamp = Timestamp()
            max_observation_start_timestamp.FromDatetime(max_observation_start_dt)
            request.max_observation_start_ts.MergeFrom(max_observation_start_timestamp)

        response = await self.__client.api.result.export(request, timeout=self.__timeout)
        s3 = boto3.client(
            's3',
            aws_access_key_id=response.credentials.fields['AccessKeyId'].string_value,
            aws_session_token=response.credentials.fields['SessionToken'].string_value,
            aws_secret_access_key=response.credentials.fields['SecretAccessKey'].string_value
        )
        pattern = r"https://(.*?)\.s3"
        container_name = re.search(pattern, response.base_url_template).group(1)
        downloaded_paths = []
        algorithm_computation_id_to_data_type_to_downloaded_paths = defaultdict(lambda: defaultdict(list))
        for result in response.result_export:
            data_type = result.data_type
            # algorithm_computation_id = result.algorithm_computation_id  TODO add once api updated
            key_path = result.url
            full_download_path = download_dir + os.path.split(key_path)[0]
            filename = 'results.zip'
            os.makedirs(full_download_path)
            downloaded_path = os.path.join(full_download_path, filename)
            s3.download_file(container_name, key_path[1:], downloaded_path)
            downloaded_paths.append(downloaded_path)
            algorithm_computation_id_to_data_type_to_downloaded_paths[
                algorithm_computation_ids[0]][data_type].append(downloaded_path)  # TODO add once api updated

        logging.info(f"Downloaded results for algorithm_computation_ids and data_types: "
                     f"{algorithm_computation_id_to_data_type_to_downloaded_paths}")
        return algorithm_computation_id_to_data_type_to_downloaded_paths

    async def get(self, **kwargs) -> (pd.DataFrame, ResultGetResponse):
        """
         algorithm_computation_id: [Required] str - Algorithm Computation ID
         source_aoi_version: int
         dest_aoi_version: int
         algo_config_class: str
         algo_config_subclass: str
         created_on: TimeStamp
         observation_start_ts: Timestamp
         geom_wkt: str
         result_status: ResultStatus
         include_measurements: bool
         pagination: Pagination
        :return: Tuple(pd.DataFrame of flattened results, ResultGetResponse)
        """
        assert "algorithm_computation_id" in kwargs.keys()
        request = self.__generate_result_get_request(kwargs)
        response = await self.__client.api.result.get(request, timeout=self.__timeout)
        return await self.__process_result_response(request, response), response

    async def __process_result_response(self, request: ResultGetRequest, response: ResultGetResponse) -> pd.DataFrame:
        result_obj_list = await self.__fetch_all_result_responses(request, response)
        # TODO ... too many nested loops this is nasty.
        result_list = []
        for result_response in result_obj_list:
            for result in result_response.results:
                for observation in result.observations:
                    obs_dict = {
                        "result_id": result.id,
                        "created_on": datetime.fromtimestamp(result.created_on.seconds),
                        "source_aoi_version": result.source_aoi_version,
                        "dest_aoi_version": result.dest_aoi_version,
                        "algo_config_class": result.algo_config_class,
                        "algo_config_subclass": result.algo_config_subclass,
                        "observation_id": observation.id,
                        "data_view_id": observation.data_view_id,
                        "observation_created_on": datetime.fromtimestamp(observation.created_on.seconds),
                        "observation_start_ts": datetime.fromtimestamp(observation.start_ts.seconds),
                        "result_status": observation.result_status
                    }
                    # Flatten keys into dict and add to main
                    obs_value = MessageToDict(observation.value)
                    obs_dict.update(obs_value)

                    if len(observation.measurements) == 0:
                        result_list.append(obs_dict.copy())
                    else:
                        for measurement in observation.measurements:
                            obs_dict.update({
                                "measurement_id": measurement.id,
                                "measurement_value": measurement.value,
                                "geom": measurement.geom
                            })
                            result_list.append(obs_dict.copy())
        return pd.DataFrame(result_list)

    async def __fetch_all_result_responses(self, request: ResultGetRequest, response: ResultGetResponse) -> List:
        results_obj_list = []

        # Add first result page if exists
        if response and len(response.results) > 0:
            results_obj_list.append(response)

        # Add subsequent result pages if exist
        pagination: Pagination = response.pagination
        while pagination and pagination.next_page_token:
            pagination = Pagination(
                page_token=pagination.next_page_token, page_size=1000
            )
            request.pagination.MergeFrom(pagination)
            response = await self.__client.api.result.get(request, timeout=self.__timeout)
            if response and len(response.results) > 0:
                results_obj_list.append(response)
        return results_obj_list

    @staticmethod
    def __generate_result_get_request(kwargs: Dict) -> ResultGetRequest:
        request_fragments = []
        for key in kwargs.keys():
            if key == 'algorithm_computation_id':
                request_fragments.append(ResultGetRequest(algorithm_computation_id=kwargs[key]))
            if key == 'source_aoi_version':
                request_fragments.append(ResultGetRequest(source_aoi_version=kwargs[key]))
            if key == 'dest_aoi_version':
                request_fragments.append(ResultGetRequest(dest_aoi_version=kwargs[key]))
            if key == 'algo_config_class':
                request_fragments.append(ResultGetRequest(algo_config_class=kwargs[key]))
            if key == 'algo_config_subclass':
                request_fragments.append(ResultGetRequest(algo_config_subclass=kwargs[key]))
            if key == 'created_on':
                request_fragments.append(ResultGetRequest(created_on=kwargs[key]))
            if key == 'observation_start_ts':
                request_fragments.append(ResultGetRequest(observation_start_ts=kwargs[key]))
            if key == 'geom_wkt':
                request_fragments.append(ResultGetRequest(geom_wkt=kwargs[key]))
            if key == 'result_status':
                request_fragments.append(ResultGetRequest(result_status=kwargs[key]))
            if key == 'include_measurements':
                request_fragments.append(ResultGetRequest(include_measurements=kwargs[key]))
            if key == 'pagination':
                request_fragments.append(ResultGetRequest(pagination=kwargs[key]))

        request = ResultGetRequest()
        for request_fragment in request_fragments:
            request.MergeFrom(request_fragment)

        return request
