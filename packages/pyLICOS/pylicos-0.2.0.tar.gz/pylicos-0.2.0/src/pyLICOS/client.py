import base64
import datetime
import json
import requests
import time

from math import ceil
from http import HTTPStatus

from pyLICOS.src.pyLICOS import communication


class Client:
    MAXIMUM_ATTEMPTS_SUBMISSION = 30
    SERVER_TIMEOUT = 30
    FILE_SIZE = 4

    def queue_processing(self, server_address: str, username: str, user_password: str, zip_path: str,
                         maximization=False, miprelstop: float = None, time_limit: float = None):
        """
        Sends a zip file containing the process data to LICOS processing queue.

        :param server_address: Full URL of LICOS server
        :param username: Username for authentication
        :param user_password: Password for authentication
        :param zip_path: Full path of the zip file. It should contain the .MPS file
        :param maximization: If true, the sense of the optimization will be maximization
        :param miprelstop: Branch and Bound: This determines when the branch and bound tree search will terminate.
            Branch and bound tree search will stop if:
                |MIPOBJVAL - BESTBOUND| ≤ MIPRELSTOP x max(|BESTBOUND|,|MIPOBJVAL|)
            where MIPOBJVAL is the value of the best solution’s objective function and BESTBOUND is the current best
            solution bound.
        :param time_limit: The maximum time in seconds that the Optimizer will run before it terminates,
            including the problem setup time and solution time. For MIP problems, this is the total time taken to solve
            all nodes.
        :return:
        """
        process_id = self._get_process_id(server_address, username, user_password)

        file = open(file=zip_path, mode='rb')
        file_bytes = file.read()
        file.close()

        self._send_compressed_file(server_address, process_id, file_bytes, username, user_password)
        self._send_parameter(server_address, process_id, "MAXIMIZATION", str(maximization), username, user_password)
        if miprelstop is not None:
            self._send_parameter(server_address, process_id, "MIPRELSTOP", str(miprelstop), username, user_password)
        if time_limit is not None:
            self._send_parameter(server_address, process_id, "TIMELIMIT", str(time_limit), username, user_password)

        if self._add_process_on_queue(server_address, process_id, username, user_password):
            return process_id
        else:
            raise Exception("LICOS error")

    def status(self, server_address: str, username: str, password: str, process_id: int):
        """
        Gets the current status of the processing.
        :param server_address: Full URL of LICOS server
        :param username: Username for authentication
        :param password: Password for authentication
        :param process_id: Requested status Processing ID
        :return: Enum of the current status
        """
        current_status = self._get_status(server_address, process_id, username, password)
        if (current_status is None) or (current_status == 'null'):
            return communication.Status.UNKOWN
        else:
            match current_status:
                case 'S':
                    pass
                case 'I':
                    pass
                case 'D':
                    pass
                case 'U':
                    pass
                case 'Q':
                    pass
                case 'A':
                    pass
                case 'E':
                    pass
                case 'T':
                    return communication.Status.QUEUE
                case 'C':
                    return communication.Status.CANCELED
                case '#':
                    return communication.Status.ERROR
                case 'F':
                    return communication.Status.DONE
                case default:
                    return communication.Status.RUNNING

    # TODO testar
    def cancel(self, server_address: str, username: str, password: str, process_id: int) -> bool:
        """
        Cancels the process on LICOS server
        :param server_address:Full URL of LICOS server
        :param username: Username for authentication
        :param password: Password for authentication
        :param process_id: Requested Processing ID that needs to be cancelled
        :return: bool containing final result of the request, true if success false if not
        """
        return self._cancel(server_address, process_id, username, password)

    def download(self, server_address: str, username: str, password: str, process_id: int, file_path: str):
        """
        Gets the output of the processing (a zip file) and saves it on a specified path
        :param server_address: Full URL of LICOS server
        :param username: Username for authentication
        :param password: Password for authentication
        :param process_id: Requested Processing ID
        :param file_path: Full disk path (including file name and extension) where the output file will be saved.
        :return:
        """
        file = self._download_file(server_address, process_id, username, password, "output.zip")

        out_file = open(file_path, mode='wb')
        out_file.write(file)
        out_file.close()

    def run(self, server_adress: str, zip_path: str, output_path: str, maximization: bool = True,
            miprelstop: float = None, time_limit: float = None, username: str = '', password: str = ''):
        """
        Executes the full processing of LICOs, and saves the optmization result on a specified path.
        :param server_adress: Full URL of LICOS server
        :param zip_path: Full path of the zip file. It should contain the .MPS file
        :param output_path: Full disk path (including file name and extension) where the output file will be saved.
        :param maximization: If true (default), the sense of the optimization will be maximization.
        :param miprelstop: Branch and Bound: This determines when the branch and bound tree search will terminate.
            Branch and bound tree search will stop if:
                |MIPOBJVAL - BESTBOUND| ≤ MIPRELSTOP x max(|BESTBOUND|,|MIPOBJVAL|)
            where MIPOBJVAL is the value of the best solution’s objective function and BESTBOUND is the current best
            solution bound.
        :param time_limit: The maximum time in seconds that the Optimizer will run before it terminates,
            including the problem setup time and solution time. For MIP problems, this is the total time taken to solve
            all nodes.
        :param username: Username for authentication
        :param password: Password for authentication
        :return:
        """
        process_id = self.queue_processing(server_adress, username, password, zip_path, maximization, miprelstop,
                                           time_limit)
        status = communication.Status.UNKOWN

        while (status != communication.Status.CANCELED and status != communication.Status.ERROR and
               status != communication.Status.DONE):
            status = self.status(server_adress, username, password, process_id)
            time.sleep(4)

        if status == communication.Status.DONE:
            self.download(server_adress, username, password, process_id, output_path)
        else:
            if status == communication.Status.ERROR:
                raise Exception('Error during processing for ID {0}'.format(process_id))
            else:
                raise Exception('Processing for ID {0} was canceled!'.format(process_id))

        return True

    def _get_process_id(self, queue_service_address: str, username: str, password: str) -> int:
        """
        Get the process ID of the user's current process
        :param queue_service_address: server address
        :param username: Username for authentication
        :param password: Password for authentication
        :return: ID of the running process
        """

        process_id = None

        str_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        link = communication.build_link(queue_service_address,
                                        "QueueService/ObterIDProcessamento?datahora=" + str_time)
        tries = 0
        done = False

        request_header = {}
        communication.add_authentication(header=request_header,
                                         username=username,
                                         password=password)

        while (not done) and (tries < self.MAXIMUM_ATTEMPTS_SUBMISSION):
            try:
                response = requests.post(link, timeout=self.SERVER_TIMEOUT, headers=request_header)

                if response.status_code == HTTPStatus.OK:
                    process_id = int(response.content.decode('ascii'))
                    done = True
                else:
                    time.sleep(3)
                    tries += 1

            except Exception:
                time.sleep(3)
                tries += 1

        if (not done) or (process_id == 0):
            raise Exception("The process ID could not be retrieved.")

        return process_id

    def _send_compressed_file(self, queue_server_address: str, process_id: int, file: [],
                              username: str, password: str):

        parameter_name = 'Entrada'
        filename = 'Entrada.zip'

        file_data = self.split_file(file, self.FILE_SIZE)
        file_data_size = len(file)

        str_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        link = communication.build_link(queue_server_address,
                                        "QueueService/EnviarParametroGenerico?datahora=" + str_time)
        json_dict = {'Nome': parameter_name,
                     'Conteudo': filename,
                     'Caminho': '',
                     'Arquivo': 'True'}

        request_header = {}
        communication.add_authentication(header=request_header, username=username, password=password)
        request_header['Content-type'] = "application/json; charset=utf-8"

        total_sent = 0
        i = 0
        tries = 0
        while i < len(file_data):
            total_sent += len(file_data[i])
            percentage = round(100 * total_sent / file_data_size)

            content = {'IDProcessamento': str(-1 * process_id if i == 0 else process_id),
                       'buffer': base64.b64encode(file_data[i]).decode('utf-8')}
            content.update(json_dict)
            json_content = json.dumps(content)

            try:
                i += 1
                response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT, headers=request_header)

            except Exception:
                if tries < self.MAXIMUM_ATTEMPTS_SUBMISSION:
                    tries += 1
                    i -= 1
                    time.sleep(4)
                    continue
                else:
                    raise Exception("The file could not be sent.")

            if response.status_code != HTTPStatus.OK:
                if tries < self.MAXIMUM_ATTEMPTS_SUBMISSION:
                    tries += 1
                    i -= 1
                    time.sleep(4)
                else:
                    raise Exception("The file could not be sent.")

        return True

    def _send_parameter(self, queue_service_address: str, process_id: int, parameter_name: str,
                        parameter_content: str, username: str, password: str):

        json_dict = {'IDProcessamento': process_id,
                     'Nome': parameter_name,
                     'Conteudo': parameter_content,
                     'Caminho:': '',
                     'Arquivo:': 'False'}
        json_content = json.dumps(json_dict)

        request_header = {}
        communication.add_authentication(header=request_header, username=username, password=password)
        request_header['Content-type'] = "application/json; charset=utf-8"

        str_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        link = communication.build_link(queue_service_address,
                                        "QueueService/EnviarParametroGenerico?datahora=" + str_time)

        tries = 0
        success = False
        while (not success) and (tries < self.MAXIMUM_ATTEMPTS_SUBMISSION):
            try:
                response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT, headers=request_header)
                if response.status_code == HTTPStatus.OK:
                    success = True
                else:
                    time.sleep(3)
                    tries += 1

            except Exception:
                time.sleep(3)
                tries += 1

        return success

    def _add_process_on_queue(self, queue_service_address: str, process_id: int, username: str, password: str):

        str_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        json_dict = {'IDProcessamento': str(process_id),
                     'DataHoraInicioEnvio': str_time,
                     'nomeBanco': '',
                     'IDEmpresa': '',
                     'UsuarioBanco': '',
                     'SenhaBanco': '',
                     'modeloRelatorio': '',
                     'origem': 'LICOS',
                     'IDProcessamentoAnterior': '',
                     'tiposRelatorios': '',
                     'tempoOtimizacao': '',
                     'tipoExecucao': 'completo',
                     'tipo': 'LICOS',
                     'NomeExecutavel': 'LICOS.Solver',
                     'ExecutavelRetorno': '',
                     'ExecutavelStatus': '',
                     'diretorioDataLake': ''}
        json_content = json.dumps(json_dict)

        str_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        link = communication.build_link(queue_service_address,
                                        "QueueService/ProcessarGenerico?datahora=" + str_time)

        request_header = {}
        communication.add_authentication(header=request_header, username=username, password=password)
        request_header['Content-type'] = "application/json; charset=utf-8"

        success = False
        tries = 0

        while (not success) and (tries < self.MAXIMUM_ATTEMPTS_SUBMISSION):
            try:
                response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT, headers=request_header)
                if response.status_code == HTTPStatus.OK:
                    success = True
                else:
                    time.sleep(3)
                    tries += 1
            except Exception:
                time.sleep(3)
                tries += 1

        return success

    def _cancel(self, queue_service_address: str, process_id: int, username: str, password: str):

        request_header = {}
        communication.add_authentication(header=request_header, username=username, password=password)
        request_header['Content-type'] = "application/json; charset=utf-8"

        json_dict = {'IDProcessamento': str(process_id),
                     'RetornoStatus': 'false'}
        json_content = json.dumps(json_dict)

        str_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        link = communication.build_link(queue_service_address,
                                        "QueueService/VerificarProcessamentoNaFila?datahora=" + str_time)

        success = False
        tries = 0
        while (not success) and (tries < self.MAXIMUM_ATTEMPTS_SUBMISSION):
            try:
                response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT, headers=request_header)
                if response.status_code == HTTPStatus.OK:
                    success = True
                else:
                    time.sleep(3)
                    tries += 1
            except Exception:
                tries += 1
                if tries >= self.MAXIMUM_ATTEMPTS_SUBMISSION:
                    raise Exception
                time.sleep(3)

        return success

    def _get_status(self, queue_service_address: str, process_id: int, username: str, password: str):

        str_return = None

        request_header = {}
        communication.add_authentication(header=request_header, username=username, password=password)
        request_header['Content-type'] = "application/json; charset=utf-8"

        json_dict = {'IDProcessamento': str(process_id)}
        json_content = json.dumps(json_dict)

        str_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        link = communication.build_link(queue_service_address,
                                        "QueueService/StatusGenerico?datahora=" + str_time)
        success = False
        tries = 0
        while (not success) and (tries < self.MAXIMUM_ATTEMPTS_SUBMISSION):
            try:
                response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT, headers=request_header)
                if response.status_code == HTTPStatus.OK:
                    response_json = response.content.decode('utf8')
                    str_return = json.loads(response_json)['Status']

                    success = True
                else:
                    time.sleep(3)
                    tries += 1

            except Exception:
                time.sleep(3)
                tries += 1

        if not success:
            raise Exception('It was not possible to get the process status.')
        else:
            return str_return

    def _download_file(self, queue_service_address: str, process_id: int, username: str, password: str,
                       filename_on_server: str) -> bytes:

        file_content = []
        file_size_bytes = int(round(self.FILE_SIZE * 1024 * 1024))

        total_received = 0
        tries = 0

        request_header = {}
        communication.add_authentication(header=request_header, username=username, password=password)
        request_header['Content-type'] = "application/json; charset=utf-8"

        link = communication.build_link(queue_service_address, "QueueService/ReceberTamanhoArquivo")

        json_dict = {'IDProcessamento': str(process_id),
                     'arquivo': filename_on_server}
        json_content = json.dumps(json_dict)

        try:
            response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT, headers=request_header)
        except Exception:
            raise Exception('It was not possible to get the file size of {} of process {}'.format(filename_on_server,
                                                                                                  process_id))

        if response.status_code == HTTPStatus.OK:
            file_size = int(response.content.decode('utf-8'))
        else:
            raise Exception('It was not possible to get the file size of {} of process {}'.format(filename_on_server,
                                                                                                  process_id))

        if file_size > 0:
            link = communication.build_link(queue_service_address, "QueueService/ReceberArquivoParcial")

            while total_received < file_size:

                if total_received + file_size_bytes - 1 >= file_size:
                    end = file_size - 1
                else:
                    end = total_received + file_size_bytes - 1

                json_dict['inicio'] = total_received
                json_dict['fim'] = end

                total_received += (end - total_received + 1)

                json_content = json.dumps(json_dict)

                try:
                    response = requests.post(link, data=json_content, timeout=self.SERVER_TIMEOUT,
                                             headers=request_header)
                except Exception:
                    raise Exception

                if response.status_code == HTTPStatus.OK:
                    file_content.append(base64.b64decode(response.content[1:-1]))
                else:
                    if tries < self.MAXIMUM_ATTEMPTS_SUBMISSION:
                        tries += 1
                        total_received -= file_size_bytes
                    else:
                        raise Exception('It was not possible to download file {} of process {}'.format(
                            filename_on_server,
                            process_id))
        else:
            raise Exception('The file {} of process {} could not be found on server.'.format(filename_on_server,
                                                                                             process_id))

        return bytes().join(file_content)

    @staticmethod
    def split_file(file_bytes: [], size: float):
        split_size = int(round(size * 1024 * 1024, 0))

        split = []
        number_of_splits = int(ceil(len(file_bytes) / split_size))
        for i in range(number_of_splits):
            split.append(file_bytes[i * split_size:(i + 1) * split_size])

        return split
