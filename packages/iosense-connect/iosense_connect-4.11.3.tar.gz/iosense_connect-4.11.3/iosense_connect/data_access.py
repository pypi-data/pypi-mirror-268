import os  # Import the 'os' module for operating system-related functions
import sys  # Import the 'sys' module for system-specific functionality
import time  # Import the 'time' module for time-related functions
import pytz  # Import the 'pytz' module for time zone support
import json  # Import the 'json' module for JSON data handling
import fsspec  # Import the 'fsspec' module for file system-related operations
import urllib3  # Import the 'urllib3' module for HTTP requests
import requests  # Import the 'requests' module for making HTTP requests
import traceback
import numpy as np  # Import the 'numpy' library for numerical operations
import pandas as pd  # Import the 'pandas' library for data manipulation
import paho.mqtt.publish as publish
from datetime import timedelta  # Import the 'timedelta' class for time duration calculations
from cryptography.fernet import Fernet  # Import 'Fernet' from 'cryptography' for encryption
from datetime import datetime, timezone  # Import 'datetime' and 'timezone' for date and time handling
from dateutil.relativedelta import relativedelta  # Import 'relativedelta' for calculating time differences
from concurrent.futures import ThreadPoolExecutor  # Import 'ThreadPoolExecutor' for concurrent execution

# Disable pandas' warning about chained assignment
pd.options.mode.chained_assignment = None

# Disable urllib3's warning about insecure requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DataAccess:
    """Class for accessing data from an API."""
    __version__ = "4.11.3 "

    def __init__(self, userid, url, key):
        """
        Initialize DataAccess instance.

        Args:
            userid (str): User ID for accessing the API.
            url (str): Domain.
            key (str): API key for authentication.
        """
        self.userid = userid
        self.url = url
        self.key = key

    def get_caliberation(self, device_id, metadata, df, onpremise=False):
        """
        Get calibrated dataframe for a device's sensor data.

        :param onpremise: Flag to indicate whether the device is on-premise (default is False).
        :param metadata: Metadata related to the device.
        :param df: Dataframe containing sensor data.
        :param device_id: String identifier for the device.
        :return: Calibrated dataframe

        This method performs calibration on the original data using the formula: y = mx + c,
        where 'y' is the sensor data value, 'm' is the calibration factor, and 'c' is the offset.
        It also handles cases where 'y' is outside the specified min and max values by
        replacing it with the corresponding min or max value.

        """
        # Extract sensor names from the dataframe columns
        sensor_name_list = list(df.columns)
        sensor_name_list.remove('time')

        # Extract sensor IDs from sensor names
        if "(" not in sensor_name_list[0]:
            sensor_id_list = sensor_name_list
        else:
            sensor_id_list = [s[s.rfind("(") + 1:s.rfind(")")] for s in sensor_name_list]

        # If metadata is not provided, fetch it using the get_device_metadata method.
        if len(metadata) == 0:
            metadata = DataAccess.get_device_metadata(self, device_id, onpremise=onpremise)

        # Extract sensor calibration data from the metadata
        data = metadata['params']

        # Iterate through sensor data for calibration
        for (value1, value2) in zip(sensor_id_list, sensor_name_list):
            df_meta = pd.DataFrame(data[str(value1)])

            # Check if calibration data exists for the sensor
            if len(df_meta) != 0:
                df_meta = df_meta.set_index('paramName').transpose()

                # Extract calibration parameters (m and c)
                if 'm' in df_meta.columns and 'c' in df_meta.columns:
                    m = float(df_meta.iloc[0]['m'])
                    c = float(str(df_meta.iloc[0]['c']).replace(',', ''))

                    # Replace specific values in the sensor data
                    df[str(value2)] = df[str(value2)].replace('true', True).replace('false',False).replace('-', '10000000000')

                    # Convert sensor data to float and apply calibration
                    df[str(value2)] = pd.to_numeric(df[value2], errors='coerce')
                    df[str(value2)] = (df[str(value2)] * m) + c

                    # Handle min and max value calibration if available
                    if 'min' in df_meta.columns:
                        min_value = float(df_meta.iloc[0]['min'])
                        df[str(value2)] = np.where(df[str(value2)] <= min_value, min_value, df[str(value2)])
                    if 'max' in df_meta.columns:
                        max_value_str = str(df_meta.iloc[0]['max']).replace('-', '10000000000')
                        max_value = float(max_value_str)
                        df[str(value2)] = np.where(df[str(value2)] >= max_value, max_value, df[str(value2)])
        return df

    def get_device_metadata(self, device_id, onpremise=False):
        """
        Retrieve metadata for a specific device.

        :param onpremise: Flag to indicate whether the device is on-premise (default is False).
        :param device_id: String identifier for the device.
        :return: JSON object containing device metadata.

        This method fetches details related to a particular device, including the device's
        added date, calibration values, sensor details, and more.

        """
        try:
            if str(onpremise).lower() == 'true':
                url = "http://" + self.url + "/api/metaData/device/" + device_id
            else:
                url = "https://" + self.url + "/api/metaData/device/" + device_id
            header = {'userID': self.userid}
            payload = {}
            response = requests.request('GET', url, headers=header, data=payload, verify=False)
            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)['data']
                return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch device Metadata')
            print(e)

    def get_sensor_alias(self, device_id, df, raw_metadata, onpremise=False):
        """
        Map sensor aliases to sensor IDs and update column names in the dataframe.

        :param onpremise: Flag to indicate whether the device is on-premise (default is False).
        :param raw_metadata: JSON object containing device metadata.
        :param device_id: String identifier for the device.
        :param df: Dataframe.
        :return: Dataframe with columns having sensor aliases.

        This method maps sensor aliases or sensor names to their corresponding sensor IDs and updates
        the dataframe's column names to use the format 'sensor_alias_sensor_id'.

        """

        sensors = list(df.columns)
        sensors.remove('time')
        if len(raw_metadata) == 0:
            raw_metadata = DataAccess.get_device_metadata(self, device_id, onpremise=onpremise)
        sensor_spec = 'sensors'
        sensor_param_df = pd.DataFrame(raw_metadata[sensor_spec])
        for sensor in sensors:
            sensor_param_df1 = sensor_param_df[sensor_param_df['sensorId'] == sensor]
            if len(sensor_param_df1) != 0:
                sensor_name = sensor_param_df1.iloc[0]['sensorName']
                sensor_name = sensor_name + " (" + sensor + ")"
                df.rename(columns={sensor: sensor_name}, inplace=True)
        return df, raw_metadata

    def time_grouping(self, df, bands, compute=None):
        """
        Group a time series DataFrame at a specified interval.

        :param compute: Function for aggregation (e.g., mean) over the grouped intervals.
        :param df: DataFrame containing time series data.
        :param bands: String representing the time interval (e.g., '5', '1W', '1D').
        :return: Dataframe with values grouped at the specified interval.

        This method groups a time series DataFrame into specified intervals. For example, if the values in
        the DataFrame are at 30-second intervals, you can group and change the interval to 5 minutes, 10 minutes,
        1 day, or 1 week. The resulting DataFrame contains values at the given interval.

        """

        df['Time'] = pd.to_datetime(df['time'])
        df.sort_values("Time", inplace=True)
        df = df.drop(['time'], axis=1)
        df = df.set_index(['Time'])
        df.index = pd.to_datetime(df.index)
        if compute is None:
            df = df.groupby(pd.Grouper(freq=str(bands) + "Min")).mean()
        else:
            df = df.groupby(pd.Grouper(freq=str(bands) + "Min")).apply(compute)
        df.reset_index(drop=False, inplace=True)
        return df

    def get_cleaned_table(self, df):
        """
        Create a pivoted DataFrame from a raw DataFrame.

        :param df: Raw DataFrame with columns for time, sensor, and values.
        :return: Pivoted DataFrame with time, sensor alias, sensor id, and corresponding values.

        The raw DataFrame has columns like time, sensor, and values. The resulting DataFrame will have
        columns for time and sensor aliases (sensor alias - sensor id) along with their corresponding values.

        """

        df = df.sort_values('time')
        df.reset_index(drop=True, inplace=True)
        results = df.pivot(index='time', columns='sensor', values='value')
        results.reset_index(drop=False, inplace=True)
        return results

    def get_device_details(self, onpremise=False):
        """
        Retrieve details of devices for a particular account.

        :param onpremise: Flag to indicate whether the devices are on-premise (default is False).
        :return: Dataframe with columns for device IDs and device names.

        This method fetches device details, including device IDs and names, for a specific account and returns
        the information in the form of a dataframe.

        """
        try:
            if str(onpremise).lower() == 'true':
                url = "http://" + self.url + "/api/metaData/allDevices"
            else:
                url = "https://" + self.url + "/api/metaData/allDevices"
            header = {'userID': self.userid}
            payload = {}
            response = requests.request('GET', url, headers=header, data=payload, verify=False)
            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)['data']
                df_raw = pd.DataFrame(raw_data)
                return df_raw

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch device Details')
            print(e)

    def get_load_entities(self, onpremise=False, clusters=None):
        """
        Retrieve load entities based on clusters for a particular account.

        :param onpremise: Flag to indicate whether the entities are on-premise (default is False).
        :param clusters: List of cluster names to filter results, or None to fetch all.
        :return: List of cluster data as dictionaries.

        This method retrieves load entities data based on clusters. It allows you to filter the results
        by specifying a list of cluster names or fetch all clusters if clusters parameter is None.

        """
        try:
            if type(clusters) == list:
                len_clusters = len(clusters)
                if len_clusters == 0:
                    raise Exception('Message: No clusters provided')
            elif clusters is None:
                pass
            else:
                raise Exception('Message: Incorrect type of clusters')

            page_count = 1
            cluster_count = 1
            while True:
                if str(onpremise).lower() == 'true':
                    url = "http://" + self.url + "/api/metaData/getAllClusterData/" + self.userid + "/" + str(
                        page_count) + "/" + str(cluster_count)
                else:
                    url = "https://" + self.url + "/api/metaData/getAllClusterData/" + self.userid + "/" + str(
                        page_count) + "/" + str(cluster_count)
                header = {'userID': self.userid}
                payload = {}
                result = []
                response = requests.request('GET', url, headers=header, data=payload, verify=False)
                if response.status_code == 200 and "error" not in json.loads(response.text):
                    raw_data = json.loads(response.text)
                    result = result + raw_data["data"]
                    total_count = json.loads(response.text)['totalCount']
                    cluster_names = [item['name'] for item in raw_data['data']]
                    page_count = page_count + 1
                    cluster_count = total_count
                    if len(cluster_names) == total_count:
                        break
                    if response.status_code != 200:
                        raw = json.loads(response.text)["error"]
                        if raw == "The requested page does not exist as the number of elements requested exceeds the total count.":
                            page_count = page_count - 1
                        else:
                            raise ValueError(raw['error'])
                else:
                    page_count = page_count - 1
            if clusters is None:
                return result
            else:
                cluster_dict = []
                for cluster_name in clusters:
                    desired_dict = next((item for item in result if item['name'] == cluster_name), None)
                    cluster_dict.append(desired_dict)
                return cluster_dict
        except Exception as e:
            traceback.print_exc()
            print('Failed to Fetch Load Entities \t', e)

    def get_cloud_credentials(self, db):
        """
        Retrieve cloud credentials for a specific database.

        :param db: Name or identifier of the database.
        :return: Decrypted credentials for the specified database.

        This method fetches and decrypts the cloud credentials for a given database using Fernet encryption.

        """
        try:
            header = {"userID": self.userid}
            payload = {}
            url = "https://" + self.url + "/api/metaData/getCredentials/" + str(db)
            response = requests.request('GET', url, headers=header, json=payload, verify=False)
            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw)
            else:
                credentials = json.loads(response.text)['data']
                cipher = Fernet(self.key)
                if type(credentials) == list:
                    credentials[0] = cipher.decrypt(credentials[0].encode('utf-8')).decode()

                    credentials[1] = cipher.decrypt(credentials[1].encode('utf-8')).decode()
                else:
                    credentials = cipher.decrypt(credentials.encode('utf-8')).decode()
                return credentials
        except Exception as e:
            traceback.print_exc()
            print(e)

    def get_userinfo(self, onpremise=False):
        """
        Retrieve user information.

        :param onpremise: Flag to indicate whether the user information is on-premise (default is False).
        :return: JSON object with user details including phone, name, gender, email, etc.

        This method fetches user information, including details like phone number, name, gender, email, etc.

        """
        try:
            if str(onpremise).lower() == 'true':
                url = "http://" + self.url + "/api/metaData/user"
            else:
                url = "https://" + self.url + "/api/metaData/user"
            header = {'userID': self.userid}
            payload = {}
            response = requests.request('GET', url, headers=header, data=payload, verify=False)

            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)['data']
                return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch user Information')
            print("Error: \t", e)

    def get_firstdp(self, device_id, sensors=None, cal=True, start_time=None, alias=True, IST=True,
                    onpremise=False):
        """
        Retrieve the first data point (DP) for specified sensors from a given start time.

        :param device_id: String identifier for the device.
        :param sensors: List of sensor IDs or None to fetch all sensors for the device.
        :param cal: Boolean indicating whether to apply calibration (default is True).
        :param start_time: Start time for data retrieval (required).
        :param alias: Boolean indicating whether to use sensor aliases (default is True).
        :param IST: Boolean indicating whether to consider Indian Standard Time (IST) (default is True).
        :param onpremise: Boolean indicating whether the data source is on-premise (default is False).
        :return: DataFrame containing the first data point for specified sensors.

        This method retrieves the first data point for specified sensors from the given start time.
        It also provides options to apply calibration, use sensor aliases, and consider Indian Standard Time (IST).
        """
        metadata = {}
        if start_time is None:
            raise TypeError('Start Time is required.')
        if sensors is None:
            metadata = DataAccess.get_device_metadata(self, device_id, onpremise=onpremise)
            data_sensor = metadata['sensors']
            df_sensor = pd.DataFrame(data_sensor)
            sensor_id_list = list(df_sensor['sensorId'])
            sensors = sensor_id_list
        time_zone = time.tzname[0]
        if time_zone == "IST":
            time_zone = "India Standard Time"
        if start_time is None:
            start_time = datetime.now(pytz.timezone("Asia/Kolkata"))
            start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    start_time = datetime.strptime(str(start_time), "%Y-%m-%d %H:%M:%S.%f%z").strftime(
                        '%Y-%m-%d %H:%M:%S')
                except:
                    start_time = str(start_time) + " 23:59:59" if isinstance(start_time, str) else start_time
        s_time = pd.to_datetime(start_time)
        if time_zone == "India Standard Time":
            s_time = s_time - timedelta(hours=5.5)
        if time_zone == "UTC":
            s_time = s_time - timedelta(hours=5.5)
        st_time = int(round(s_time.timestamp()))
        if type(sensors) == list:
            len_sensors = len(sensors)
            if len_sensors == 0:
                raise Exception('Message: No sensors provided')
            delimiter = ","
            sensor_values = delimiter.join(sensors)
        else:
            raise Exception('Message: Incorrect type of sensors')
        header = {}
        payload = {}
        df = pd.DataFrame()
        if str(onpremise).lower() == "true":
            url = "http://" + self.url + "/api/apiLayer/getMultipleSensorsDPAfter?device=" + device_id + "&sensor=" + sensor_values + "&time=" + str(
                st_time)
        else:
            url = "https://" + self.url + "/api/apiLayer/getMultipleSensorsDPAfter?device=" + device_id + "&sensor=" + sensor_values + "&time=" + str(
                st_time)
        response = requests.request("GET", url, headers=header, data=payload)
        raw = json.loads(response.text)
        if response.status_code != 200:
            raise ValueError(response.status_code, response.text)
        if 'success' in raw:
            raise ValueError(raw)
        else:
            raw_data = json.loads(response.text)[0]
            if len(raw_data) != 0:
                if len(raw_data) > 1:
                    data_list = [
                        {'time': sensor_data[0]['time'], 'sensor': sensor, 'value': sensor_data[0]['value']}
                        for sensor, sensor_data in raw_data.items() if sensor_data]
                    df = pd.DataFrame(data_list)
                else:
                    formatted_data = [{'sensor': key, 'time': value['time'], 'value': value['value']}
                                      for key, value in raw_data.items()]
                    df = pd.DataFrame(formatted_data)
            else:
                print('Incorrect Response received !')
        if len(df) != 0:
            df['time'] = pd.to_datetime(df['time'])
            if IST and time_zone == "India Standard Time":
                df['time'] = df['time'].dt.tz_convert('Asia/Kolkata')
            if IST and time_zone == "UTC":
                df['time'] = df['time'].dt.tz_convert('Asia/Kolkata')
            try:
                df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')
            except:
                df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
            df = DataAccess.get_cleaned_table(self, df)
            if str(alias).lower() == "true":
                df, metadata = DataAccess.get_sensor_alias(self, device_id, df, metadata, onpremise=onpremise)
            if str(cal).lower() == 'true':
                df = DataAccess.get_caliberation(self, device_id, metadata, df, onpremise=onpremise)
        return df

    def get_dp(self, device_id, sensors=None, n=1, cal=True, end_time=None, alias=True, IST=True,
               onpremise=False):
        """
        Retrieve last data points (DP) for specified sensors from a given time range.

        :param device_id: String identifier for the device.
        :param sensors: List of sensor IDs or None to fetch all sensors for the device.
        :param n: Number of data points to retrieve (default is 1).
        :param cal: Boolean indicating whether to apply calibration (default is True).
        :param end_time: End time for data retrieval.
        :param alias: Boolean indicating whether to use sensor aliases (default is True).
        :param IST: Boolean indicating whether to consider Indian Standard Time (IST) (default is True).
        :param onpremise: Boolean indicating whether the data source is on-premise (default is False).
        :return: DataFrame containing data points for specified sensors.

        This method retrieves data points for specified sensors within a given time range.
        It provides options to specify the number of data points to retrieve, apply calibration, use sensor aliases,
        and consider Indian Standard Time (IST).
        """
        metadata = {}
        if sensors is None:
            metadata = DataAccess.get_device_metadata(self, device_id, onpremise=onpremise)
            data_sensor = metadata['sensors']
            df_sensor = pd.DataFrame(data_sensor)
            sensor_id_list = list(df_sensor['sensorId'])
            sensors = sensor_id_list

        rawdata_res = []
        temp = ''
        time_zone = time.tzname[0]
        if time_zone == "IST":
            time_zone = "India Standard Time"
        if end_time is None:
            end_time = datetime.now(pytz.timezone("Asia/Kolkata"))
            end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            # Handle different time formats and convert to 'Y-m-d H:M:S'
            end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    end_time = datetime.strptime(str(end_time), "%Y-%m-%d %H:%M:%S.%f%z").strftime('%Y-%m-%d %H:%M:%S')
                except:
                    end_time = str(end_time) + " 23:59:59" if isinstance(end_time, str) else end_time
        e_time = pd.to_datetime(end_time)
        if time_zone == "India Standard Time":
            e_time = e_time - timedelta(hours=5.5)
        if time_zone == "UTC":
            e_time = e_time - timedelta(hours=5.5)
        en_time = int(round(e_time.timestamp())) * 10000
        if type(sensors) == list:
            len_sensors = len(sensors)
            if len_sensors == 0:
                raise Exception('Message: No sensors provided')
            if n < 1:
                raise ValueError('Incorrect number of data points')
            n = int(n) * len_sensors
            delimiter = ","
            sensor_values = delimiter.join(sensors)
        else:
            raise Exception('Message: Incorrect type of sensors')
        header = {}
        cursor = {'end': en_time, 'limit': n}
        payload = {}
        df = pd.DataFrame()
        counter = 0
        max_retries = 15
        retry = 0
        while cursor['end']:
            try:
                for record in range(counter):
                    sys.stdout.write('\r')
                    sys.stdout.write("Approx Records Fetched %d" % (10000 * record))
                    sys.stdout.flush()
                if str(onpremise).lower() == "true":
                    url = "http://" + self.url + "/api/apiLayer/getLimitedDataMultipleSensors/?device=" + device_id + "&sensor=" + sensor_values + "&eTime=" + str(
                        cursor['end']) + "&lim=" + str(cursor['limit']) + "&cursor=true"
                else:
                    url = "https://" + self.url + "/api/apiLayer/getLimitedDataMultipleSensors/?device=" + device_id + "&sensor=" + sensor_values + "&eTime=" + str(
                        cursor['end']) + "&lim=" + str(cursor['limit']) + "&cursor=true"
                response = requests.request("GET", url, headers=header, data=payload)
                raw = json.loads(response.text)
                if response.status_code != 200:
                    raise ValueError(response.status_code)
                if 'success' in raw:
                    raise ValueError(raw)
                else:
                    raw_data = json.loads(response.text)['data']
                    cursor = json.loads(response.text)['cursor']
                    if len(raw_data) != 0:
                        df = pd.concat([df, pd.DataFrame(raw_data)])
                    counter = counter + 1
            except Exception as e:
                retry += 1
                print(f'Retry Count: {retry}')
                if retry < 5 and retry < max_retries:
                    time.sleep(2)
                elif retry > 5 and retry < max_retries:
                    time.sleep(4)
                elif retry > max_retries:
                    raise Exception('Max retries for data fetching from api-layer exceeded, thus throwing.')

        if len(df) != 0:
            df['time'] = pd.to_datetime(df['time'])
            if IST and time_zone == "India Standard Time":
                df['time'] = df['time'].dt.tz_convert('Asia/Kolkata')
            if IST and time_zone == "UTC":
                df['time'] = df['time'].dt.tz_convert('Asia/Kolkata')
            try:
                df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')
            except:
                df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
            df = DataAccess.get_cleaned_table(self, df)
            if str(alias).lower() == "true":
                df, metadata = DataAccess.get_sensor_alias(self, device_id, df, metadata, onpremise=onpremise)
            if str(cal).lower() == 'true':
                df = DataAccess.get_caliberation(self, device_id, metadata, df, onpremise=onpremise)
        return df

    def influxdb(self, device_id, sensors, start_time, end_time=None, onpremise=False, IST=True,
                 echo=True):
        """
        Retrieve data points from InfluxDB for specified sensors within a given time range.

        :param device_id: String identifier for the device.
        :param sensors: List of sensor IDs.
        :param start_time: Start time for data retrieval.
        :param end_time: End time for data retrieval (optional).
        :param onpremise: Boolean indicating whether the data source is on-premise (default is False).
        :param IST: Boolean indicating whether to consider Indian Standard Time (IST) (default is True).
        :param echo: Boolean indicating whether to display progress information (default is True).
        :return: DataFrame containing data points for specified sensors.

        This method retrieves data points from InfluxDB for specified sensors within a given time range.
        It provides options to specify the end time, consider IST, and display progress information.
        """
        metadata = {}
        if sensors is None:
            # If sensors are not specified, fetch metadata for the device
            metadata = DataAccess.get_device_metadata(self, device_id, onpremise=onpremise)
            data_sensor = metadata['sensors']
            df_sensor = pd.DataFrame(data_sensor)
            sensor_id_list = list(df_sensor['sensorId'])
            sensors = sensor_id_list
        rawdata_res = []
        temp = ''
        time_zone = time.tzname[0]
        if time_zone == "IST":
            time_zone = "India Standard Time"
        flag = 0
        if end_time is None:
            end_time = datetime.now(pytz.timezone("Asia/Kolkata"))
            end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
            flag = 1
        try:
            # Handle different time formats and convert to 'Y-m-d H:M:S'
            end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    end_time = datetime.strptime(str(end_time), "%Y-%m-%d %H:%M:%S.%f%z").strftime('%Y-%m-%d %H:%M:%S')
                except:
                    end_time = str(end_time) + " 23:59:59" if isinstance(end_time, str) else end_time
        try:
            # Handle different time formats and convert to 'Y-m-d H:M:S'
            start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    start_time = datetime.strptime(str(start_time), "%Y-%m-%d %H:%M:%S.%f%z").strftime(
                        '%Y-%m-%d %H:%M:%S')
                except:
                    start_time = str(start_time) + " 00:00:00" if isinstance(start_time, str) else start_time
        s_time = pd.to_datetime(start_time)
        e_time = pd.to_datetime(end_time)
        if time_zone == "India Standard Time":
            s_time = s_time - timedelta(hours=5.5)
            e_time = e_time - timedelta(hours=5.5)
        if time_zone == "UTC":
            s_time = s_time - timedelta(hours=5.5)
            e_time = e_time - timedelta(hours=5.5)
        st_time = int(round(s_time.timestamp())) * 10000
        en_time = int(round(e_time.timestamp())) * 10000
        df = pd.DataFrame()
        header = {}
        payload = {}
        counter = 0
        cursor = {'start': st_time, 'end': en_time}
        max_retries = 15
        retry = 0
        while cursor['start'] and cursor['end']:
            try:
                if echo:
                    for record in range(counter):
                        sys.stdout.write('\r')
                        sys.stdout.write("Approx Records Fetched %d" % (10000 * record))
                        sys.stdout.flush()
                if sensors is not None:
                    if str(onpremise).lower() == 'true':
                        url_api = "http://" + self.url + "/api/apiLayer/getAllData?device="
                    else:
                        url_api = "https://" + self.url + "/api/apiLayer/getAllData?device="
                    if counter == 0:
                        str1 = ","
                        sensor_values = str1.join(sensors)
                        temp = url_api + device_id + "&sensor=" + sensor_values + "&sTime=" + str(
                            st_time) + "&eTime=" + str(
                            en_time) + "&cursor=true&limit=25000"
                    else:
                        str1 = ","
                        sensor_values = str1.join(sensors)
                        temp = url_api + device_id + "&sensor=" + sensor_values + "&sTime=" + str(
                            cursor['start']) + "&eTime=" + str(cursor['end']) + "&cursor=true&limit=25000"
                response = requests.request("GET", temp, headers=header, data=payload)
                raw = json.loads(response.text)
                if response.status_code != 200:
                    raise ValueError(raw['error'])
                if 'success' in raw:
                    raise ValueError(raw['error'])
                else:
                    raw_data = json.loads(response.text)['data']
                    cursor = json.loads(response.text)['cursor']
                    if len(raw_data) != 0:
                        rawdata_res = rawdata_res + raw_data
                    counter = counter + 1
                    df = pd.DataFrame(rawdata_res)
            except Exception as e:
                retry += 1
                print(f'Retry: {retry}')
                if retry < 5 and retry < max_retries:
                    time.sleep(2)
                elif retry > 5 and retry < max_retries:
                    time.sleep(4)
                elif retry > max_retries:
                    raise Exception('Max retries for data fetching from api-layer exceeded, thus throwing.')

        if len(df) != 0:
            df['time'] = pd.to_datetime(df['time'])
            if IST and time_zone == "India Standard Time":
                df['time'] = df['time'].dt.tz_convert('Asia/Kolkata')
            if IST and time_zone == "UTC":
                df['time'] = df['time'].dt.tz_convert('Asia/Kolkata')
            try:
                df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')
            except:
                df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
            if len(df.columns) == 2:
                df['sensor'] = sensors[0]
            df = DataAccess.get_cleaned_table(self, df)
        return df

    def data_query(self, device_id, sensors, start_time, end_time=None, db=None, alias=True, cal=True,
                   bands=None, onpremise=False, compute=None, IST=True):
        """
        Retrieve data from a database (feature store or InfluxDB) based on specified criteria.

        :param device_id: String identifier for the device.
        :param sensors: List of sensor IDs.
        :param start_time: Start time for data retrieval.
        :param end_time: End time for data retrieval (optional).
        :param db: Database type (e.g., 'gcs', 's3', 'az') for feature store (default is None).
        :param alias: Boolean indicating whether to consider sensor alias (default is True).
        :param cal: Boolean indicating whether to apply sensor calibration (default is True).
        :param bands: Time grouping bands for data aggregation (default is None).
        :param onpremise: Boolean indicating whether data is on-premise (default is False).
        :param compute: Aggregation function (e.g., 'mean', 'min', 'max') for time grouping (default is None).
        :param IST: Boolean indicating whether to consider Indian Standard Time (IST) (default is True).
        :return: DataFrame containing the retrieved data.

        This method retrieves data from a database (feature store or InfluxDB) based on the specified criteria.
        It provides options to fetch data from different databases, apply alias, calibration, and time-based aggregation.
        """

        def get_month_year(filename):
            month, year = map(int, filename.split('.')[0].split('-'))
            return datetime(year, month, 1)

        def generate_month_year_dates(start_date, end_date):
            end_date = end_date.strftime("%Y-%m-%d %H:%M:%S") if isinstance(end_date, datetime) else str(end_date)
            start_date = str(start_date) + " 00:00:00" if len(str(start_date).split()) == 1 else str(start_date)
            end_date = str(end_date) + " 00:00:00" if len(str(end_date).split()) == 1 else str(end_date)

            try:
                current_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
                end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
            except:
                current_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f")

            dates = []
            while str(current_date) <= str(end_date):
                month = str(current_date.month)
                month_year = month + "-" + str(current_date.year) + ".parquet"
                dates.append(month_year)
                current_date += relativedelta(months=1)
                current_date = current_date.replace(day=1)

            return dates

        def read_one(filename):
            try:
                with connector.open(container_name + str(device_id) + "/" + str(filename),
                                    "rb") as src_file:
                    df = pd.read_parquet(src_file)
                return df
            except Exception as e:
                print('Exception occured while reading parquet: ',e)
                traceback.print_exc()
                print("Up for retry !")
                with connector.open(container_name + str(device_id) + "/" + str(filename),
                                    "rb") as src_file:
                    df = pd.read_parquet(src_file)
                return df


        def thread_read(filenames_list):
            if len(filenames_list) != 0:
                with ThreadPoolExecutor(max_workers=40) as executor:  # function to thread
                    for record in range(len(filenames_list)):
                        sys.stdout.write('\r')
                        sys.stdout.write("Please Wait .. ")
                        sys.stdout.flush()
                    results = executor.map(read_one, filenames_list)
                fetched_df = pd.concat(results, axis=0)
            else:
                fetched_df = pd.DataFrame()
            return fetched_df

        df = pd.DataFrame()
        metadata = {}
        connector = None
        container_name = None

        if db is not None:
            flag = 0
            time_zone = time.tzname[0]
            if time_zone == "IST":
                time_zone = "India Standard Time"
            if end_time is None:
                end_time = datetime.now(pytz.timezone("Asia/Kolkata"))
                end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
                flag = 1
            try:
                end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
                except ValueError:
                    try:
                        end_time = datetime.strptime(str(end_time), "%Y-%m-%d %H:%M:%S.%f%z").strftime(
                            '%Y-%m-%d %H:%M:%S')
                    except:
                        end_time = str(end_time) + " 23:59:59" if isinstance(end_time, str) else end_time
            try:
                start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S.%f').strftime(
                        '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    try:
                        start_time = datetime.strptime(str(start_time), "%Y-%m-%d %H:%M:%S.%f%z").strftime(
                            '%Y-%m-%d %H:%M:%S')
                    except:
                        start_time = str(start_time) + " 00:00:00" if isinstance(start_time, str) else start_time
            credentials = DataAccess.get_cloud_credentials(self, db)
            if len(credentials) != 0:
                if db == 'gcs':
                    credentials = eval(credentials)
                    connector = fsspec.filesystem("gs", project=credentials["project_id"], token=credentials)
                elif db == 's3':
                    try:
                        credentials = eval(credentials)
                        connector = fsspec.filesystem("s3", key=credentials[0], secret=credentials[1])
                    except:
                        connector = fsspec.filesystem("s3", key=credentials[0], secret=credentials[1])
                elif db == 'az':
                    connector = fsspec.filesystem("az", account_name=credentials[0], account_key=credentials[1])
                else:
                    raise Exception("Wrong Db value entered")
                container_name = "faclon-ds-feature-store/"
                blobs = connector.ls(container_name)
                device_list = [blob.split("/")[1] for blob in blobs]
                if device_id in device_list:
                    blobs = [blob_name.split("/")[2] for blob_name in
                             connector.ls(container_name + str(device_id) + "/")]
                    dates = generate_month_year_dates(start_time, end_time)
                    filenames = list(set(dates).intersection(blobs))
                    filenames = sorted(filenames, key=get_month_year)
                    df = thread_read(filenames)
                    if len(df) != 0:
                        try:
                            start_time = datetime.strptime(str(start_time), '%Y-%m-%d %H:%M:%S')
                            end_time = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S')
                        except ValueError:
                            pass
                        except Exception as e:
                            print('Message:', e)
                        df = df[(df['time'] >= start_time) & (df['time'] <= end_time)]
                        if len(df) != 0:
                            if sensors is None:
                                sensors = list(df.columns)
                                sensors.remove('time')

                            sensors_filtered = list(set(df.columns).intersection(sensors))
                            if sensors and len(sensors_filtered) != 0:
                                sensors_filtered.insert(0, 'time')
                                df = df[sensors_filtered]
                            else:
                                df = pd.DataFrame()
                            if not df.empty:
                                df.sort_values(['time'], inplace=True)
                                df.reset_index(drop=True, inplace=True)
                                last_date = df['time'].iloc[-1]
                                last_date = last_date.to_pydatetime()
                                try:
                                    date1 = datetime.strptime(str(last_date), '%Y-%m-%d %H:%M:%S.%f')
                                except:
                                    date1 = datetime.strptime(str(last_date), '%Y-%m-%d %H:%M:%S')
                                try:
                                    date2 = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S')
                                except:
                                    date2 = datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S.%f')
                                difference = date2 - date1
                                if difference.seconds >= 3600 or difference.seconds >= 60:
                                    if time_zone == "UTC" and flag == 0:
                                        last_date = last_date + timedelta(hours=5.5)
                                        end_time = end_time + timedelta(hours=5.5)
                                    df1 = DataAccess.influxdb(self, device_id, start_time=last_date,
                                                              end_time=end_time, sensors=sensors, echo=True,
                                                              onpremise=False, IST=True)
                                    df = pd.concat([df, df1])
                                    df.reset_index(drop=True, inplace=True)

                                if IST is False:
                                    df['time'] = pd.to_datetime(df['time']) - timedelta(hours=5.5)

                        else:
                            df_devices = DataAccess.get_device_details(self, onpremise=onpremise)
                            device_list = df_devices['devID'].tolist()
                            if device_id in device_list:
                                df = DataAccess.influxdb(self, device_id, sensors, start_time, end_time=end_time,
                                                        onpremise=onpremise,
                                                        IST=IST, echo=True)
                            else:
                                raise Exception('Message: Device not added in account')

                    else:
                        df_devices = DataAccess.get_device_details(self, onpremise=onpremise)
                        device_list = df_devices['devID'].tolist()
                        if device_id in device_list:
                            df = DataAccess.influxdb(self, device_id, sensors, start_time, end_time=end_time,
                                                     onpremise=onpremise,
                                                     IST=IST, echo=True)
                        else:
                            raise Exception('Message: Device not added in account')
                else:
                    df_devices = DataAccess.get_device_details(self, onpremise=onpremise)
                    device_list = df_devices['devID'].tolist()
                    if device_id in device_list:
                        df = DataAccess.influxdb(self, device_id, sensors, start_time, end_time=end_time,
                                                 onpremise=onpremise,
                                                 IST=IST, echo=True)
                    else:
                        raise Exception('Message: Device not added in account')
        else:
            df_devices = DataAccess.get_device_details(self, onpremise=onpremise)
            device_list = df_devices['devID'].tolist()
            if device_id in device_list:
                df = DataAccess.influxdb(self, device_id, sensors, start_time, end_time=end_time, onpremise=onpremise,
                                         IST=IST, echo=True)
            else:
                raise Exception('Message: Device not added in account')

        if len(df) != 0:
            df['time'] = pd.to_datetime(df['time'])
            if str(alias).lower() == "true":
                df, metadata = DataAccess.get_sensor_alias(self, device_id, df, metadata, onpremise=onpremise)
            if str(cal).lower() == 'true':
                df = DataAccess.get_caliberation(self, device_id, metadata, df, onpremise=onpremise)
            if bands is not None:
                df = DataAccess.time_grouping(self, df, bands, compute)
            df = df.set_index(['time'])
            df = df.fillna(value=np.nan)
            df.dropna(axis=0, how='all', inplace=True)
            df.reset_index(drop=False, inplace=True)
            df.drop_duplicates(inplace=True)
            df = df.drop_duplicates(subset=['time'])
        return df

    # Events Notification and Management Functions
    def check_time_format(self, time_str):
        def is_valid_format(time_str, date_format):
            try:
                datetime.strptime(time_str, date_format)
                return True
            except ValueError:
                return False

        formats = [
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%d %H:%M:%S.%f%z",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%S%z"
        ]

        valid_formats = [fmt for fmt in formats if is_valid_format(time_str, fmt)]

        if valid_formats:
            return True, valid_formats[0]
        else:
            return False, None

    def publish_event(self, title, message, meta_data, hover_data, event_tags, created_on, onpremise=False):
        """
        Publish an event/notif to IOSense Platform
        :param title: Optional
        :param message: Message body
        :param meta_data: Metadata
        :param hover_data: Hoverdata
        :param event_tags: _id value returned from fetch all event categories request.
        :param created_on: Optional. Custom notification creation time. Current time if no created on is provided.
        :return: json

        """
        raw_data = []
        try:
            if onpremise:
                url = "http://" + self.url + "/api/eventTag/publishEvent"
            elif not onpremise:
                url = "https://" + self.url + "/api/eventTag/publishEvent"
            else:
                raise Exception("Incorrect onpremise value.")

            header = {'userID': self.userid}
            payload = {
                "title": title,
                "message": message,
                "metaData": meta_data,
                "eventTags": [event_tags],
                "hoverData": hover_data,
                "createdOn": created_on
            }
            response = requests.request('POST', url, headers=header, json=payload, verify=True)

            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)['data']
                return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch event Details')
            print(e)
        return raw_data

    def get_events_in_timeslot(self, start_time, end_time, onpremise=False):
        """

        :param start_time: Start time
        :param end_time: EndTime
        :return: Json

        Fetches events data in given timeslot

        """
        raw_data = []
        try:
            is_valid_start_time, format_used = self.check_time_format(start_time)
            is_valid_end_time, format_used = self.check_time_format(end_time)
            if not is_valid_start_time:
                raise Exception('Incorrect start_time value.')
            if not is_valid_end_time:
                raise Exception('Incorrect end_time value.')
            if str(onpremise).lower() == "true":
                url = "http://" + self.url + "/api/eventTag/fetchEvents/timeslot"
            elif str(onpremise).lower() == "false":
                url = "https://" + self.url + "/api/eventTag/fetchEvents/timeslot"
            else:
                raise Exception('Incorrect onpremise value.')
            header = {'userID': self.userid}
            payload = {
                "startTime": start_time,
                "endTime": end_time
            }
            response = requests.request('PUT', url, headers=header, json=payload, verify=False)
            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)['data']
                return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch event Details')
            print(e)

        return raw_data

    def get_event_data_count(self, end_time=None, count=None, onpremise=False):
        """
        Fetch 'count' number of notifications before end-time provided.
        :param end_time: EndTime
        :param count: Count of notifications. Cannot exceed 10000.
        :return: Json
        """
        raw_data = []
        try:
            if end_time is None:
                end_time = datetime.now()
                end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
            is_valid, format_used = self.check_time_format(end_time)
            if not is_valid:
                raise Exception("Incorrect end_time value.")
            if str(onpremise).lower() == "true":
                url = "http://" + self.url + "/api/eventTag/fetchEvents/count"
            elif str(onpremise).lower() == "false":
                url = "https://" + self.url + "/api/eventTag/fetchEvents/count"
            else:
                raise Exception("Incorrect onpremise value.")
            header = {'userID': self.userid}
            payload = {
                "endTime": end_time,
                "count": count
            }
            response = requests.request('PUT', url, headers=header, json=payload, verify=False)

            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)
                return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch event Count')
            print(e)

        return raw_data

    def get_event_categories(self, onpremise=False):
        """
        Fetch all event tags/categories under a user.
        :return: Event Categories Details
        """
        raw_data = []
        try:
            if str(onpremise).lower() == "true":
                url = "http://" + self.url + "/api/eventTag"
            elif str(onpremise).lower() == "false":
                url = "https://" + self.url + "/api/eventTag"
            else:
                raise Exception('Incorrect onpremise value.')
            header = {'userID': self.userid}
            payload = {}
            response = requests.request('GET', url, headers=header, data=payload, verify=False)

            if response.status_code != 200:
                raw = json.loads(response.text)
                raise ValueError(raw['error'])
            else:
                raw_data = json.loads(response.text)['data']
                return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch event Count')
            print(e)

        return raw_data

    def get_detailed_event(self, event_tags="", start_time=None, end_time=None, onpremise=False):
        """
        Fetches number of times an event was triggered
        :param event_tags: Array of mongoIDs of the concerned event tag. This field is optional
        :param start_time: Start time
        :param end_time: End time
        :param count: Integer
        :return: Json
        """
        raw_data = []
        try:
            # Check for start_time
            if start_time is None:
                raise Exception("Start time is required.")
            is_valid, format_used = self.check_time_format(start_time)
            if not is_valid:
                raise Exception("Incorrect start_time value.")

            # Check for end_time
            if end_time is None:
                end_time = datetime.now()
                end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
            is_valid, format_used = self.check_time_format(end_time)
            if not is_valid:
                raise Exception("Incorrect end_time value.")

            # Check for onpremise
            if str(onpremise).lower() == "true":
                url = "http://" + self.url + f"/api/eventTag/eventLogger"
            elif str(onpremise).lower() == "false":
                url = "https://" + self.url + f"/api/eventTag/eventLogger"
            else:
                raise Exception("Incorrect onpremise value.")

            # Check for event_tag
            if event_tags == "" or event_tags is None:
                tags = []
            else:
                tags = [event_tags]
            header = {'userID': self.userid}
            payload = {
                "startTime": start_time,
                "endTime": end_time,
                "eventTags": tags,
                "count": 1000
            }

            raw_data = []
            page = 1
            while True:
                print(f"Fetching Data from page {page}")
                response = requests.put(url + f"/{page}/1000", headers=header, json=payload, verify=False)
                if response.status_code != 200:
                    raw = json.loads(response.text)
                    raise ValueError(raw['error'])
                else:
                    data = json.loads(response.text)
                    response_data = data['data']['data']
                    raw_data.extend(response_data)
                    total_count = data['data']['totalCount']
                    if len(response_data) >= total_count:
                        break  # Break the loop if no more data is available
                    else:
                        page += 1  # Move to the next page

            return raw_data

        except Exception as e:
            traceback.print_exc()
            print('Failed to fetch event data.')
            print(f"Received: {response.text}")
            print(e)

        return raw_data

    def get_notifications(self,onpremise=False,**kwargs):
        """
            Fetches notifications from the API based on provided parameters.

            Args:
                **kwargs: Keyword arguments for specifying search parameters. Possible arguments include:
                    - search_key: Search keywords.
                    - default_event_tags: Default event tags.
                    - start_time: Start time for filtering notifications.
                    - end_time: End time for filtering notifications.
                    - configurable_event_tags: Configurable event tags.
                    - notif_remark: Notification remarks.
                    - remark_group_name: Remark group name.
                    - sub_users: Sub-users.
                    - master_user: Boolean indicating whether to fetch notifications for the master user.

            Returns:
                list: A list of dictionaries containing notification data.

            Raises:
                Exception: If start_time or end_time is not provided.
        """

        # Function to validate timestamp format
        def validate_time(timestamp_str):
            formats = ["%Y-%m-%d %H:%M:%S"]

            for fmt in formats:
                try:
                    dt = datetime.strptime(timestamp_str, fmt)
                    # Ensure time is not in the future
                    if dt > datetime.now():
                        raise ValueError("Time cannot be in the future.")
                    return int(dt.timestamp()) * 1000
                except ValueError:
                    continue

            raise ValueError(
                "Invalid time format. Please provide time in one of the following formats: 'YYYY-MM-DD HH:MM:SS'.")

        # Function to generate payload
        def generate_payload(search_key=None, default_event_tags=None, start_time=None, end_time=None,
                             configurable_event_tags=None, notif_remark=None, remark_group_name=None, sub_users=None,
                             master_user=None):
            payload = {}
            if default_event_tags is None:
                default_event_tags = []
            if start_time is None or end_time is None:
                raise Exception("Start Time and End Time not specified")
            if start_time:
                try:
                    payload['sTime'] = validate_time(start_time)
                except ValueError as e:
                    print(e)
                    return None

            if end_time:
                try:
                    payload['eTime'] = validate_time(end_time)
                except ValueError as e:
                    print(e)
                    return None

            if search_key is not None or default_event_tags is not None or configurable_event_tags is not None or notif_remark is not None or remark_group_name is not None or sub_users is not None:
                search = {}
                if default_event_tags is not None:
                    search['defaultEventTag'] = default_event_tags
                if configurable_event_tags:
                    search['configurableEventTags'] = configurable_event_tags
                if notif_remark:
                    search['notifRemark'] = notif_remark
                if remark_group_name:
                    search['remarkGroupName'] = remark_group_name
                if sub_users is not None:
                    search['subUser'] = sub_users
                if master_user is not None:
                    search['masterUser'] = master_user

                payload['search'] = search

            return payload


        skip = 1
        total_notifications = []
        headers = {'userID': self.userid}
        payload = generate_payload(**kwargs)
        if payload is None:
            return ["Payload cannot be None"]
        while True:
            print(f"Fetching Data from Page {skip}")
            if onpremise:
                url_with_skip = f"http://{self.url}/api/notif/{skip}/1000"
            elif onpremise is False:
                url_with_skip = f"https://{self.url}/api/notif/{skip}/1000"
            else:
                print("Incorrect onpremise value")
            response = requests.put(url_with_skip, json=payload, headers=headers)
            data = json.loads(response.text)['data']
            total_count = data['totalCount']
            paginated_data = data['paginatedData']

            total_notifications.extend(paginated_data)

            # Break the loop if all notifications have been fetched
            if len(total_notifications) >= total_count:
                break

            skip += 1

        return total_notifications


class DataPublish:
    """Class for publishing data to MQTT broker."""
    __version__ = "4.11.2"

    def __init__(self, username, password, broker, port):
        """Initialize DataPublish instance."""
        self.username = username
        self.password = password
        self.broker = broker
        self.port = port
        self.auth = {'username': self.username, 'password': self.password}

    def publish_multiple_payload(self, messages, chunk_size):
        """
        Publishes multiple messages to MQTT broker.

        Args:
            messages (list): List of dictionaries containing 'topic' and 'payload' keys.
            chunk_size (int): Number of messages to publish in each chunk (maximum is 1000).
            sleep_duration (float): Duration to sleep in seconds between publishing each chunk.

        Raises:
            ValueError: If the message format is invalid or chunk size exceeds 1000.
            Exception: If there's an error during publishing.
        """
        if chunk_size > 1000:
            raise ValueError("Maximum chunk size allowed is 1000")

        def validate_and_publish(messages):
            """Validate messages and publish."""
            valid_messages = []
            for message in messages:
                if 'topic' in message and 'payload' in message:
                    topic = message['topic']
                    payload = message['payload']
                    valid_messages.append((topic, json.dumps(payload)))
                else:
                    raise ValueError("Invalid message format: {}".format(message))
            if valid_messages:
                publish.multiple(valid_messages, hostname=self.broker, port=self.port, auth=self.auth)
            else:
                print("Empty message list received")

        try:
            total_messages = len(messages)
            print("Publishing Messages ....")
            for i in range(0, total_messages, chunk_size):
                chunk = messages[i:i + chunk_size]
                validate_and_publish(chunk)
                time.sleep(1)
            return print("Data Published Successfully!")
        except ValueError as e:
            return print(f"Validation Failed: {e}")
        except Exception as e:
            return print(f"Error during publishing: {e}")

    def publish_single_payload(self, messages, chunk_size):
        """
        Publishes multiple messages to MQTT broker with chunking and delay between chunks.

        Args:
            messages (list): List of dictionaries containing 'topic' and 'payload' keys.
            chunk_size (int): Number of messages to publish in each chunk (maximum is 1000).

        Returns:
            str: Message indicating the success or failure of the publishing process.
        """
        if chunk_size > 1000:
            raise ValueError("Maximum chunk size allowed is 1000")

        failed_messages = []
        total_messages = len(messages)
        try:
            print("Publishing Messages .......")
            for i in range(0, total_messages, chunk_size):
                chunk = messages[i:i + chunk_size]
                for message in chunk:
                    if 'topic' in message and 'payload' in message:
                        topic = message['topic']
                        payload = message['payload']
                        try:
                            publish.single(topic, json.dumps(payload), hostname=self.broker, port=self.port,
                                           auth=self.auth)
                        except Exception as e:
                            failed_messages.append((topic, payload, str(e)))
                            print(f"Error during publishing: {e}")
                    else:
                        failed_messages.append((None, None, f"Invalid message format: {message}"))
                time.sleep(1)
            if failed_messages:
                return print(f"Failed to publish {len(failed_messages)} messages: {failed_messages}")
            else:
                return print("All messages published successfully")
        except Exception as e:
            return print(f"Error during publishing: {e}")

