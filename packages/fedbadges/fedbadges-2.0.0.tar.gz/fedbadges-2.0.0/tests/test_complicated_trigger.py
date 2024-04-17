import logging
from unittest.mock import Mock, patch

import pytest
from fedora_messaging.message import Message

from .utils import get_rule


@pytest.fixture
def rule(rules):
    return get_rule(rules, "Junior Tagger (Tagger I)")


@pytest.fixture
def message():
    return Message(
        topic="org.fedoraproject.prod.fedoratagger.tag.create",
    )


def test_complicated_trigger_against_empty(rule, message):
    assert rule.matches(message, Mock(name="tahrir")) == set()


def test_complicated_trigger_against_partial(rule, message):
    message.body = {"user": {}}
    assert rule.matches(message, Mock(name="tahrir")) == set()


def test_complicated_trigger_against_partial_mismatch(rule, message, tahrir_client, caplog):
    caplog.set_level(logging.ERROR)
    message.body = {"user": None}
    assert rule.matches(message, tahrir_client) == set()
    print(caplog.messages)
    print(caplog.text)
    assert len(caplog.messages) == 1


def test_complicated_trigger_against_full_match(rule, message, tahrir_client):
    message.body = {
        "tag": {
            "dislike": 0,
            "like": 1,
            "package": "mattd",
            "tag": "awesome",
            "total": 1,
            "votes": 1,
        },
        "user": {"anonymous": False, "rank": -1, "username": "ralph", "votes": 4},
        "vote": {
            "like": True,
            "tag": {
                "dislike": 0,
                "like": 1,
                "package": "mattd",
                "tag": "awesome",
                "total": 1,
                "votes": 1,
            },
            "user": {"anonymous": False, "rank": -1, "username": "ralph", "votes": 4},
        },
    }

    # Set up some mock stuff
    class MockQuery:
        def count(self):
            return float("inf")  # Master tagger

    with (
        patch("fedbadges.rules.user_exists_in_fas") as g,
        patch("datanommer.models.Message.grep") as grep,
    ):
        grep.return_value = float("inf"), 1, MockQuery()
        g.return_value = True
        assert rule.matches(message, tahrir_client) == {"ralph"}
