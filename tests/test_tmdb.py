import unittest
from unittest.mock import patch, Mock
from tmdb_client import get_single_movie, get_single_movie_cast

class TestTmdbClient(unittest.TestCase):

    @patch('tmdb_client.requests.get')
    def test_get_single_movie(self, mock_get):
        # Przykładowa odpowiedź z API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 123, "title": "Example Movie"}
        mock_get.return_value = mock_response

        movie_id = 123
        movie_data = get_single_movie(movie_id)

        self.assertEqual(movie_data["id"], 123)
        self.assertEqual(movie_data["title"], "Example Movie")


    @patch('tmdb_client.requests.get')
    def test_get_single_movie_cast(self, mock_get):
        # Przykładowa odpowiedź z API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"cast": [{"name": "Actor 1"}, {"name": "Actor 2"}]}
        mock_get.return_value = mock_response

        movie_id = 123
        cast = get_single_movie_cast(movie_id)

        self.assertEqual(cast, [{"name": "Actor 1"}, {"name": "Actor 2"}])

if __name__ == '__main__':
    unittest.main()
