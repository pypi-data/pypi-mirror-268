from unittest.mock import patch

import pytest
from fedora_messaging.message import Message

import fedbadges.rules

from .utils import example_real_bodhi_message


class MockQuery:
    def __init__(self, returned_count):
        self.returned_count = returned_count

    def count(self):
        return self.returned_count


def test_malformed_criteria():
    """Test that an error is raised when nonsense is provided."""
    with pytest.raises(KeyError):
        fedbadges.rules.Criteria(
            dict(
                watwat="does not exist",
            )
        )


def test_underspecified_criteria():
    """Test that an error is raised when condition is missing."""
    with pytest.raises(ValueError):
        fedbadges.rules.Criteria(
            dict(
                datanommer={
                    "filter": {"topics": ["%(topic)s"], "wat": "baz"},
                    "operation": "count",
                }
            )
        )


def test_malformed_filter():
    """Test that an error is raised for malformed filters"""
    with pytest.raises(KeyError):
        fedbadges.rules.Criteria(
            dict(
                datanommer={
                    "filter": {"topics": ["%(topic)s"], "wat": "baz"},
                    "operation": "count",
                    "condition": {
                        "greater than or equal to": 500,
                    },
                }
            )
        )


@pytest.mark.parametrize(
    ["returned_count", "expectation"],
    [
        (499, False),
        (500, True),
        (501, True),
    ],
)
def test_basic_datanommer(returned_count, expectation):
    criteria = fedbadges.rules.Criteria(
        dict(
            datanommer={
                "filter": {
                    "topics": ["%(topic)s"],
                },
                "operation": "count",
                "condition": {
                    "greater than or equal to": 500,
                },
            }
        )
    )
    message = Message(
        topic="org.fedoraproject.dev.something.sometopic",
    )
    with patch("datanommer.models.Message.grep") as grep:
        grep.return_value = returned_count, 1, MockQuery(returned_count)
        result = criteria.matches(message)
        assert result == expectation
        grep.assert_called_once_with(
            topics=["org.fedoraproject.dev.something.sometopic"],
            defer=True,
        )


@pytest.mark.parametrize(
    ["returned_count", "expectation"],
    [
        (499, False),
        (500, True),
        (501, True),
    ],
)
def test_datanommer_with_lambda_condition(returned_count, expectation):
    criteria = fedbadges.rules.Criteria(
        dict(
            datanommer={
                "filter": {
                    "topics": ["%(topic)s"],
                },
                "operation": "count",
                "condition": {
                    "lambda": "value >= 500",
                },
            }
        )
    )
    message = Message(
        topic="org.fedoraproject.dev.something.sometopic",
    )
    with patch("datanommer.models.Message.grep") as f:
        f.return_value = returned_count, 1, MockQuery(returned_count)
        result = criteria.matches(message)
        assert result == expectation


@pytest.mark.parametrize(
    ["returned_count", "expectation"],
    [
        (4, False),
        (5, True),
        (6, False),
    ],
)
def test_datanommer_formatted_operations(returned_count, expectation):
    criteria = fedbadges.rules.Criteria(
        dict(
            datanommer={
                "filter": {
                    "topics": ["%(topic)s"],
                },
                "operation": {
                    "lambda": "query.count() == %(msg.some_value)s",
                },
                "condition": {
                    "lambda": "value",
                },
            }
        )
    )
    message = Message(
        topic="org.fedoraproject.dev.something.sometopic",
        body=dict(
            some_value=5,
        ),
    )
    with patch("datanommer.models.Message.grep") as grep:
        grep.return_value = returned_count, 1, MockQuery(returned_count)
        result = criteria.matches(message)
        assert result == expectation


@pytest.mark.parametrize(
    ["returned_count", "expectation"],
    [
        (499, False),
        (500, True),
        (501, True),
    ],
)
def test_datanommer_with_lambda_operation(returned_count, expectation):
    criteria = fedbadges.rules.Criteria(
        dict(
            datanommer={
                "filter": {
                    "topics": ["%(topic)s"],
                },
                "operation": {
                    "lambda": "query.count() - 5",
                },
                "condition": {
                    "lambda": "value >= 495",
                },
            }
        )
    )
    message = Message(
        topic="org.fedoraproject.dev.something.sometopic",
    )
    with patch("datanommer.models.Message.grep") as grep:
        grep.return_value = returned_count, 1, MockQuery(returned_count)
        result = criteria.matches(message)
        assert result == expectation


def test_datanommer_with_lambda_filter():
    criteria = fedbadges.rules.Criteria(
        dict(
            datanommer={
                "filter": {
                    "users": {
                        "lambda": "[u for u in msg['message'].usernames "
                        "if not u in ['bodhi', 'hadess']]",
                    }
                },
                "operation": "count",
                "condition": {
                    "greater than or equal to": 0,
                },
            }
        )
    )

    message = example_real_bodhi_message
    returned_count = 0

    with patch("datanommer.models.Message.grep") as grep:
        grep.return_value = returned_count, 1, MockQuery(returned_count)
        result = criteria.matches(message)
        assert result is True
        grep.assert_called_once_with(users=["lmacken"], defer=True)


def test_datanommer_with_dotted_filter():
    criteria = fedbadges.rules.Criteria(
        dict(
            datanommer={
                "filter": {
                    "users": [
                        "%(msg.update.user.name)s",
                    ]
                },
                "operation": "count",
                "condition": {
                    "greater than or equal to": 0,
                },
            }
        )
    )

    message = example_real_bodhi_message
    returned_count = 0

    with patch("datanommer.models.Message.grep") as grep:
        grep.return_value = returned_count, 1, MockQuery(returned_count)
        result = criteria.matches(message)
        assert result is True
        grep.assert_called_once_with(users=["hadess"], defer=True)
