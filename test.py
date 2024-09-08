import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from io import StringIO
import datetime
import requests

from stop_and_search import fetch_data , clean_data , daily_update, csv_file

class TestStopAndsearch(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"type": "Person search", "datetime": "2023-01-01T12:00:00Z", "location": {"latitude": "51.5074", "longitude": "-0.1278"}}]
        mock_get.return_value = mock_response

        data = fetch_data('metropolitan', '2024-01')

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['type'], 'Person search')

    @patch('requests.get')
    def test_fetch_data_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = [{"type": "Person search", "datetime": "2023-01-01T12:00:00Z", "location": {"latitude": "51.5074", "longitude": "-0.1278"}}]
        mock_get.return_value = mock_response

        data = fetch_data('metropolitan', '2024-01')

        self.assertEqual(data, [])

    def test_clean_data(self):

        raw_data = {
            "type": ["Person search"],
            "datetime": ["2023-01-01T12:00:00Z"],
            "location": [{"latitude": "51.5074", "longitude": "-0.1278"}]
        }

        df = pd.DataFrame(raw_data)
        df_clean = clean_data(df)
        self.assertEqual(df_clean['datetime'].dtype, 'datetime64[ns, UTC]')
        self.assertFalse(df_clean.isnull().values.any())

    @patch('stop_and_search.fetch_data')
    @patch('pandas.DataFrame.to_csv')
    def test_daily_update(self, mock_to_csv, mock_fetch_data):
        mock_fetch_data.return_value = [
            {"type": "Person search", "datetime": "2023-01-01T12:00:00Z", "location": {"latitude": "51.5074", "longitude": "-0.1278"}}
        ]

        daily_update()

        current_date= datetime.date.today().strftime('%Y-%m')
        mock_fetch_data.assert_called_with('metropolitan', current_date)
        mock_to_csv.assert_called_once()

if __name__ == '__main__':
    unittest.main()