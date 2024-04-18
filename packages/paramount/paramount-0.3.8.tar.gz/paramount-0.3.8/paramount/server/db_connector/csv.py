# CSV implementation
from .db import Database
import os
import pandas as pd


class CSVDatabase(Database):
    def create_or_append(self, df, table_name, primary_key=None):
        # Check if the file exists, and if not, create it with header, else append without header
        filename = table_name+'.csv'
        if not os.path.isfile(filename):
            df.to_csv(filename, mode='a', index=False)
        else:
            df.to_csv(filename, mode='a', index=False, header=False)

    def table_exists(self, table_name):
        return os.path.isfile(table_name+'.csv')

    def update_ground_truth(self, df, table_name):
        df.to_csv(table_name+'.csv', index=False)

    def get_recordings(self, table_name, evaluated_rows_only=False, split_by_id=None, identifier_column_name=None,
                       identifier_value=None, recording_ids=None):
        filename = table_name + '.csv'
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            df = df.map(lambda x: None if pd.isna(x) else x)

            if identifier_column_name and identifier_value and identifier_column_name in df.columns:
                df = df[df[identifier_column_name] == identifier_value]
            if evaluated_rows_only:
                df = df[df['paramount__evaluation'] != '']
            if recording_ids:
                df = df[df['paramount__recording_id'].isin(recording_ids)]

            jsonic_columns = [col for col in df.columns if isinstance(df[col].iloc[0], str) and
                              df[col].iloc[0].startswith(('{', '['))]
            df.update(df[jsonic_columns].applymap(self.try_literal_eval))

            return df
        else:
            # Return an empty DataFrame if the file does not exist
            return pd.DataFrame()

    def get_sessions(self, table_name, split_by_id, identifier_column_name, identifier_value):
        filename = table_name + '.csv'
        if os.path.isfile(filename):
            df = pd.read_csv(filename)
            if identifier_column_name in df.columns:
                df = df[df[identifier_column_name] == identifier_value]
            return df
        else:
            return pd.DataFrame()
