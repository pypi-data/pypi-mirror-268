import pandas as pd
from functools import lru_cache, cached_property


class DataTable:
    """
    DataTable
    """

    def __init__(self, file):
        self.file = file


    @cached_property
    def headers(self):
        self.file.seek(0)
        first_line = pd.read_csv(self.file, compression='gzip', sep=',', quotechar='"', on_bad_lines='warn', nrows=1, header=None)
        first = first_line.iloc[0].to_list()
        header = {
            'format': first[0],
            'station': first[1],
            'model': first[2],
            'serial': first[3],
            'version': first[4],
            'program': first[5],
            'signature': first[6],
            'table_name': first[7],
        }

        return header


    @cached_property
    def data(self):
        self.file.seek(0)
        df = pd.read_csv(self.file, compression='gzip', header=[0,1,2], sep=',', quotechar='"', on_bad_lines='warn', skiprows=1)
        melted = df.melt(id_vars=[('TIMESTAMP', 'TS', 'Unnamed: 0_level_2'), ('RECORD', 'RN', 'Unnamed: 1_level_2')], var_name=['name', 'unit', 'proc'], value_name='value')

        melted.rename(columns={melted.columns[0]: 'timestamp', melted.columns[1]: 'record'}, inplace=True)

        melted['timestamp']= pd.to_datetime(melted['timestamp'])

        return melted


    @cached_property
    def metrics(self):
        metrics = self.data[["name", "unit", "proc"]].drop_duplicates()
        return metrics.to_dict('records')


    @lru_cache(maxsize=None)
    def metric_data(self, name, unit, proc):
        data = self.data
        filtered = data[(data['name'] == name) & (data['unit'] == unit) & (data['proc'] == proc)].sort_values(by="timestamp", ascending=True)

        metric_data = filtered[['timestamp', 'value']].reset_index(drop=True)

        return metric_data
