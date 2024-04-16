import json
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import MagicMock, patch

import git

from netorca_sdk.consumer import ConsumerSubmission
from netorca_sdk.exceptions import (
    NetorcaAPIError,
    NetorcaAuthenticationError,
    NetorcaException,
    NetorcaGatewayError,
    NetorcaNotFoundError,
    NetorcaServerUnavailableError,
    NetOrcaWrongYAMLFormat,
)


class TestConsumerSubmission(unittest.TestCase):
    def setUp(self):
        self.netorca_api_key = "api_key"
        self.consumer_submission = ConsumerSubmission(self.netorca_api_key)

        # Create a temporary directory and set up test files
        self.test_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.test_dir, ".netorca"))
        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: https://example.com\n")

        with open(os.path.join(self.test_dir, ".netorca", "app.yaml"), "w") as f:
            f.write("app1:\n  service1:\n    key: value\n")

    def tearDown(self):
        # Remove temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_load_from_repository(self):
        with self.assertRaises(NetorcaException):
            self.consumer_submission.load_from_repository("/non_existent_path")

        self.consumer_submission.load_from_repository(self.test_dir)
        self.assertIsNotNone(self.consumer_submission.config)
        self.assertIsNotNone(self.consumer_submission.consumer_submission)

    def test_get_auth(self):
        with self.assertRaises(NetorcaException):
            self.consumer_submission.get_auth()

        self.consumer_submission.load_from_repository(self.test_dir)
        auth = self.consumer_submission.get_auth()
        self.assertIsNotNone(auth)

    def test_get_team(self):
        with patch("netorca_sdk.auth.NetorcaAuth.get_teams_info") as mock_get_teams_info, patch(
            "netorca_sdk.auth.NetorcaAuth.get"
        ) as mock_get:
            mock_get_teams_info.return_value = [{"id": 1, "name": "team1"}]
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"results": [{"id": 1, "name": "team1"}]}

            self.consumer_submission.load_from_repository(self.test_dir)
            team = self.consumer_submission.get_team()
            self.assertEqual(team, {"id": 1, "name": "team1"})

    @patch("netorca_sdk.auth.NetorcaAuth.get_teams_info")
    def test_get_team_from_config(self, mock_get_teams_info):
        self.consumer_submission.use_config = True
        self.consumer_submission.config = {"netorca_global": {"metadata": {"team_name": "TeamA"}}}

        team = self.consumer_submission.get_team()
        self.assertEqual(team, {"name": "TeamA"})

    def test_get_team_no_team_name_in_config(self):
        self.consumer_submission.use_config = True
        self.consumer_submission.config = {
            "netorca_global": {
                "metadata": {
                    # No team_name provided in the config
                }
            }
        }

        with self.assertRaises(NetorcaException) as context:
            self.consumer_submission.get_team()

        self.assertEqual(str(context.exception), "`netorca_global.team_name` is empty.")

    def test_prepare_request(self):
        with patch("netorca_sdk.auth.NetorcaAuth.get_teams_info") as mock_get_teams_info, patch(
            "netorca_sdk.auth.NetorcaAuth.get"
        ) as mock_get:
            mock_get_teams_info.return_value = [{"id": 1, "name": "team1"}]
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"results": [{"id": 1, "name": "team1"}]}

            self.consumer_submission.load_from_repository(self.test_dir)
            full_request = self.consumer_submission.prepare_request()
            self.assertIn("team1", full_request)

    def test_validate(self):
        with patch("netorca_sdk.auth.NetorcaAuth.post") as mock_post, patch(
            "netorca_sdk.auth.NetorcaAuth.get"
        ) as mock_get:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {"is_valid": True}
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"results": [{"id": 1, "name": "team1"}]}

    def test_pretty_print_errors_consumers(self):
        errors = {
            "TeamA": {
                "App1": {
                    "Service1": {
                        "Field1": "Error message 1",
                        "Field2": "Error message 2",
                    },
                    "Service2": {
                        "Field3": ["Error message 3", "Error message 4"],
                    },
                },
            },
            "TeamB": "Team level error",
        }

        expected_output = (
            "----------------------------------------------------------------------------------------------------\n"
            "Application: `App1` validation errors\n"
            "----------------------------------------------------------------------------------------------------\n"
            "+=============+==========+=============+========+========================================+\n"
            "| Application | Service  | ServiceItem | Field  |                 "
            "Reason                 |\n"
            "+=============+==========+=============+========+========================================+\n"
            "|    App1     | Service1 |             | Field1 |            Error message "
            "1             |\n"
            "+-------------+----------+-------------+--------+----------------------------------------+\n"
            "|    App1     | Service1 |             | Field2 |            Error message "
            "2             |\n"
            "+-------------+----------+-------------+--------+----------------------------------------+\n"
            "|    App1     | Service2 |             | Field3 | ['Error message 3', 'Error "
            "message 4'] |\n"
            "+-------------+----------+-------------+--------+----------------------------------------+\n"
            "\n"
        )

        with StringIO() as buf, redirect_stdout(buf):
            ConsumerSubmission.pretty_print_errors(errors)
            output = buf.getvalue()

        self.assertEqual(output, expected_output)

    def test_load_from_repository_invalid_config(self):
        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: \n")

        with self.assertRaises(NetorcaException):
            self.consumer_submission.load_from_repository(self.test_dir)

    def test_load_from_repository_invalid_yaml(self):
        with open(os.path.join(self.test_dir, ".netorca", "app.yaml"), "w") as f:
            f.write("app1:\n  service1:\n    key: value\n  invalid_yaml: :")

        with self.assertRaises(NetorcaException):
            self.consumer_submission.load_from_repository(self.test_dir)

    def test_load_from_repository_duplicate_app(self):
        with open(os.path.join(self.test_dir, ".netorca", "app2.yaml"), "w") as f:
            f.write("app1:\n  service2:\n    key: value\n")

        with self.assertRaises(NetorcaException):
            self.consumer_submission.load_from_repository(self.test_dir)

    def test_validate_no_repository(self):
        validate, error = self.consumer_submission.validate()
        self.assertEqual(validate, False)
        self.assertEqual(len(error), 0)

    def test_submit_no_repository(self):
        submit, error = self.consumer_submission.submit()
        assert submit is False
        self.assertEqual(submit, False)
        self.assertEqual(error, "No application detected. Submission skipped.")

    def test_load_from_repository_missing_metadata(self):
        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: http://localhost:8000\n")

        with open(os.path.join(self.test_dir, ".netorca", "app.yaml"), "w") as f:
            f.write("test_app:\n  some_field: value\n")

        consumer_submission = ConsumerSubmission("fake_api_key")
        consumer_submission.load_from_repository(self.test_dir)
        self.assertIsNone(consumer_submission.config.get("netorca_global", {}).get("metadata"))


class TestConsumerSubmissionNoAppFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_repository"
        os.makedirs(os.path.join(self.test_dir, ".netorca"), exist_ok=True)

        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: http://localhost:8000\n")

    def tearDown(self):
        # Remove test directory and its contents
        import shutil

        shutil.rmtree(self.test_dir)

    def test_load_from_repository_no_app_files(self):
        consumer_submission = ConsumerSubmission("fake_api_key")
        consumer_submission.load_from_repository(self.test_dir)
        validate, error = consumer_submission.validate()
        assert validate is False
        self.assertEqual(len(error), 0)
        self.assertEqual(
            consumer_submission.consumer_submission,
            {},
            "Consumer submission should be empty when there are no application files.",
        )


class TestConsumerSubmissionInvalidYAMLFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_repository"
        os.makedirs(os.path.join(self.test_dir, ".netorca"), exist_ok=True)

        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: http://localhost:8000\n")

        with open(os.path.join(self.test_dir, ".netorca", "invalid.yaml"), "w") as f:
            f.write("app1:\n  - service1\n    key: value\n")  # Invalid YAML format

    def tearDown(self):
        # Remove test directory and its contents
        import shutil

        shutil.rmtree(self.test_dir)

    def test_load_from_repository_invalid_yaml(self):
        consumer_submission = ConsumerSubmission("fake_api_key")
        with self.assertRaises(NetOrcaWrongYAMLFormat):
            consumer_submission.load_from_repository(self.test_dir)


class TestConsumerSubmissionOnlyYamlFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_repository"
        os.makedirs(os.path.join(self.test_dir, ".netorca"), exist_ok=True)

        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: http://localhost:8000\n")

        with open(os.path.join(self.test_dir, ".netorca", "app1.yaml"), "w") as f:
            f.write("app1:\n  services:\n    service1:\n      key: value\n")

        with open(os.path.join(self.test_dir, ".netorca", "app2.txt"), "w") as f:
            f.write("app1:\n  services:\n    service2:\n      key: value\n")

    def tearDown(self):
        # Remove test directory and its contents
        import shutil

        shutil.rmtree(self.test_dir)

    def test_load_from_repository_only_yaml_files(self):
        consumer_submission = ConsumerSubmission("fake_api_key")
        consumer_submission.load_from_repository(self.test_dir)
        self.assertEqual(
            consumer_submission.consumer_submission,
            {"app1": {"services": {"service1": {"key": "value"}}}},
            "Consumer submission should only load .yaml files and ignore other file extensions.",
        )


class TestConsumerSubmissionEmptyService(unittest.TestCase):
    def setUp(self):
        self.netorca_api_key = "api_key"
        self.consumer_submission = ConsumerSubmission(self.netorca_api_key)

        # Create a temporary directory and set up test files
        self.test_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.test_dir, ".netorca"))
        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: https://example.com\n")

        with open(os.path.join(self.test_dir, ".netorca", "app1.yaml"), "w") as f:
            f.write("app1:\n  services:\n")

    def tearDown(self):
        # Remove temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_load_from_repository_empty_service(self):
        # Call the load_from_repository method
        self.consumer_submission.load_from_repository(self.test_dir)

        # Assert that the "service" in the config is an empty dictionary
        self.assertEqual(self.consumer_submission.consumer_submission.get("app1", {}).get("services"), {})


class TestConsumerSubmissionCommitID(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_repository"
        os.makedirs(os.path.join(self.test_dir, ".netorca"), exist_ok=True)

        with open(os.path.join(self.test_dir, ".netorca", "config.yaml"), "w") as f:
            f.write("netorca_global:\n  base_url: http://localhost:8000\n")

    def tearDown(self):
        # Remove test directory and its contents
        import shutil

        shutil.rmtree(self.test_dir)

    @patch("netorca_sdk.consumer.git.Repo")
    def test_load_from_repository_with_commit_id(self, mock_repo):
        # Create a mock git.Repo instance
        mock_commit = MagicMock()
        mock_commit.hexsha = "mock_commit_id"
        mock_repo.return_value.head.commit = mock_commit

        consumer_submission = ConsumerSubmission("fake_api_key")
        consumer_submission.load_from_repository(self.test_dir)

        # Check that the config contains the correct commit_id
        expected_commit_id = "mock_commit_id"
        self.assertEqual(consumer_submission.config["netorca_global"]["commit_id"], expected_commit_id)

    @patch("netorca_sdk.consumer.git.Repo", side_effect=git.exc.InvalidGitRepositoryError)
    def test_get_commit_id_invalid_repo(self, mock_repo):
        consumer_submission = ConsumerSubmission("fake_api_key")
        commit_id = consumer_submission.get_commit_id("/path/to/invalid_repo")

        # Check that an empty string is returned for an invalid repository
        self.assertEqual(commit_id, "")


class TestCheckStatusCode(unittest.TestCase):
    def test_200_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "mock_data"}
        result = ConsumerSubmission.check_status_code(mock_response)
        self.assertEqual(result, {"data": "mock_data"})

    def test_204_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 204
        result = ConsumerSubmission.check_status_code(mock_response)
        self.assertEqual(result, {"status": "deleted"})

    def test_404_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 404
        with self.assertRaises(NetorcaNotFoundError):
            ConsumerSubmission.check_status_code(mock_response)

    def test_400_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad Request"}
        result = ConsumerSubmission.check_status_code(mock_response)
        self.assertEqual(result, {"error": "Bad Request"})

    def test_401_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 401
        with self.assertRaises(NetorcaAuthenticationError):
            ConsumerSubmission.check_status_code(mock_response)

    def test_403_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 403
        with self.assertRaises(NetorcaAuthenticationError):
            ConsumerSubmission.check_status_code(mock_response)

    def test_502_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 502
        with self.assertRaises(NetorcaGatewayError):
            ConsumerSubmission.check_status_code(mock_response)

    def test_503_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 503
        with self.assertRaises(NetorcaServerUnavailableError):
            ConsumerSubmission.check_status_code(mock_response)

    def test_other_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.content = b"Internal Server Error"
        with self.assertRaises(NetorcaAPIError):
            ConsumerSubmission.check_status_code(mock_response)


if __name__ == "__main__":
    unittest.main()
