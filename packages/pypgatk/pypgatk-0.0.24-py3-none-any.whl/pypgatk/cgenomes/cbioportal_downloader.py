import csv
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

from pypgatk.toolbox.exceptions import AppException
from pypgatk.toolbox.general import ParameterConfiguration, check_create_folders, download_file, clear_cache
from pypgatk.toolbox.rest import call_api_raw


class CbioPortalDownloadService(ParameterConfiguration):
    CONFIG_KEY_DATA_DOWNLOADER = 'cbioportal_data_downloader'
    CONFIG_KEY_CBIOPORTAL_DOWNLOAD_URL = 'cbioportal_download_url'
    CONFIG_OUTPUT_DIRECTORY = 'output_directory'
    CONFIG_CBIOPORTAL_API = 'cbioportal_api'
    CONFIG_CBIOPORTAL_API_SERVER = 'base_url'
    CONFIG_CBIOPORTAL_API_CANCER_STUDIES = "cancer_studies"
    CONFIG_LIST_STUDIES = "list_studies"
    CONFIG_MULTITHREADING = "multithreading"
    PROTEINDB = 'proteindb'
    FILTER_INFO = 'filter_info'
    FILTER_COLUMN = 'filter_column'

    def __init__(self, config_data, pipeline_arguments):
        """
      Init the class with the specific parameters.
      :param config_data configuration file
      :param pipeline_arguments pipelines arguments
      """

        super(CbioPortalDownloadService, self).__init__(self.CONFIG_KEY_DATA_DOWNLOADER, config_data,
                                                        pipeline_arguments)

        self._local_path_cbioportal = 'output_directory'
        self._list_studies = []
        self._multithreading = True

        self._cbioportal_base_url = 'https://www.cbioportal.org/api'
        self._cancer_studies_command = 'studies'

        self._cbioportal_download_url = 'https://cbioportal-datahub.s3.amazonaws.com'

        if self.CONFIG_OUTPUT_DIRECTORY in self.get_pipeline_parameters():
            self._local_path_cbioportal = self.get_pipeline_parameters()[self.CONFIG_OUTPUT_DIRECTORY]
        elif self.CONFIG_KEY_DATA_DOWNLOADER in self.get_default_parameters() and \
                self.CONFIG_OUTPUT_DIRECTORY in self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER]:
            self._local_path_cbioportal = self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][
                self.CONFIG_OUTPUT_DIRECTORY]

        if self.CONFIG_LIST_STUDIES in self.get_pipeline_parameters():
            self._list_studies = self.get_pipeline_parameters()[self.CONFIG_LIST_STUDIES]
        elif self.CONFIG_KEY_DATA_DOWNLOADER in self.get_default_parameters() and \
                self.CONFIG_LIST_STUDIES in self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER]:
            self._list_studies = self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][
                self.CONFIG_LIST_STUDIES]

        if self.CONFIG_MULTITHREADING in self.get_pipeline_parameters():
            self._multithreading = self.get_pipeline_parameters()[self.CONFIG_MULTITHREADING]
        elif self.CONFIG_KEY_DATA_DOWNLOADER in self.get_default_parameters() and \
                self.CONFIG_MULTITHREADING in self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER]:
            self._multithreading = self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][
                self.CONFIG_MULTITHREADING]

        if self.CONFIG_CBIOPORTAL_API_SERVER in self.get_pipeline_parameters():
            self._cbioportal_base_url = self.get_pipeline_parameters()[self.CONFIG_CBIOPORTAL_API_SERVER]
        elif (self.CONFIG_KEY_DATA_DOWNLOADER in self.get_default_parameters() and
              self.CONFIG_CBIOPORTAL_API in self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER]
              and self.CONFIG_CBIOPORTAL_API_SERVER in self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][
                  self.CONFIG_CBIOPORTAL_API]):
            self._cbioportal_base_url = \
                self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][self.CONFIG_CBIOPORTAL_API][
                    self.CONFIG_CBIOPORTAL_API_SERVER]

        if self.CONFIG_CBIOPORTAL_API_CANCER_STUDIES in self.get_pipeline_parameters():
            self._cancer_studies_command = self.get_pipeline_parameters()[self.CONFIG_CBIOPORTAL_API_CANCER_STUDIES]
        elif (self.CONFIG_KEY_DATA_DOWNLOADER in self.get_default_parameters() and
              self.CONFIG_CBIOPORTAL_API in self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER]
              and self.CONFIG_CBIOPORTAL_API_CANCER_STUDIES in
              self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][
                  self.CONFIG_CBIOPORTAL_API]):
            self._cancer_studies_command = \
                self.get_default_parameters()[self.CONFIG_KEY_DATA_DOWNLOADER][self.CONFIG_CBIOPORTAL_API][
                    self.CONFIG_CBIOPORTAL_API_CANCER_STUDIES]

        self.prepare_local_cbioportal_repository()
        self.get_cancer_studies()

    def prepare_local_cbioportal_repository(self):
        self.get_logger().debug("Preparing local cbioportal repository, root folder - '{}'".format(
            self.get_local_path_root_cbioportal_repo()))
        check_create_folders([self.get_local_path_root_cbioportal_repo()])
        self.get_logger().debug(
            "Local path for cbioportal Release - '{}'".format(self.get_local_path_root_cbioportal_repo()))

    def get_local_path_root_cbioportal_repo(self):
        return self._local_path_cbioportal

    def get_filter_options(self, variable, default_value):
        return_value = default_value
        if variable in self.get_default_parameters():
            return_value = self.get_default_parameters()[variable]
        elif self.PROTEINDB in self.get_default_parameters() and \
                self.FILTER_INFO in self.get_default_parameters()[self.PROTEINDB] and \
                variable in self.get_default_parameters()[self.PROTEINDB][self.FILTER_INFO]:
            return_value = self.get_default_parameters()[self.PROTEINDB][self.FILTER_INFO][variable]
        return return_value

    def get_cancer_studies(self):
        """
        This method will print the list of all cancer studies for the user.
        :return:
        """
        server = self._cbioportal_base_url
        endpoint = self._cancer_studies_command
        self._cbioportal_studies = call_api_raw(server + "/" + endpoint).text
        return self._cbioportal_studies

    def download_study(self, download_study, url_file_name=None):
        """
        This function will download a study from cBioPortal using the study ID
        :param download_study: Study to be downloaded, if the study is empty or None, all the studies will be
        downloaded.
        :param url_file_name: file tsv containing the urls to be downloaded.
        :return: None
        """

        clear_cache()

        url_file = None
        if url_file_name is not None:
            url_file = open(url_file_name, 'w')

        if self._cbioportal_studies is None or len(self._cbioportal_studies) == 0:
            self.get_cancer_studies()

        if 'all' not in download_study:
            if not self.check_study_identifier(download_study):
                msg = "The following study accession '{}' is not present in cBioPortal Studies".format(download_study)
                self.get_logger().debug(msg)
                raise AppException(msg)
            else:
                self.download_one_study(download_study)
        else:
            csv_reader = csv.reader(self._cbioportal_studies.splitlines(), delimiter="\t")
            line_count = 0
            if self._multithreading:
                processes = []
                with ThreadPoolExecutor(max_workers=10, thread_name_prefix='Thread-Download') as executor:
                    for row in csv_reader:
                        if line_count != 0:
                            processes.append(executor.submit(self.download_one_study, row[0]))
                        line_count = line_count + 1
                for task in as_completed(processes):
                    print(task.result())
            else:
                for row in csv_reader:
                    if line_count != 0:
                        self.download_one_study(row[0], url_file=url_file)
                    line_count = line_count + 1

    def download_one_study(self, download_study, url_file=None):
        file_name = '{}.tar.gz'.format(download_study)
        file_url = '{}/{}'.format(self._cbioportal_download_url, file_name)
        file_name = download_file(file_url=file_url,
                                  file_name=self.get_local_path_root_cbioportal_repo() + '/' + file_name,
                                  log=self.get_logger(), url_file=url_file)
        if file_name is not None:
            msg = "The following study '{}' has been downloaded. ".format(download_study)
        else:
            msg = "The following study '{}' hasn't been downloaded. ".format(download_study)
        self.get_logger().debug(msg)
        return file_name

    def check_study_identifier(self, download_study):
        return download_study in self._cbioportal_studies
