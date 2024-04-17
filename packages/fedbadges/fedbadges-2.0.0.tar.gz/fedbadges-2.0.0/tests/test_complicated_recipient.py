from unittest.mock import patch

import pytest
from fedora_messaging.message import Message

from .utils import get_rule


class MockQuery:
    def count(self):
        return float("inf")  # Master tagger


def test_complicated_recipient_real(
    rules,
    tahrir_client,
):
    rule = get_rule(rules, "Speak Up!")
    msg = Message(
        topic="org.fedoraproject.prod.meetbot.meeting.complete",
        body={
            "meeting_topic": "testing",
            "attendees": {"zodbot": 2, "threebean": 2},
            "chairs": {},
            "topic": "",
            "url": "fedora-meeting.2013-06-24-19.52",
            "owner": "threebean",
            "channel": "#fedora-meeting",
        },
    )
    with (
        patch("fedbadges.rules.user_exists_in_fas") as g,
        patch("datanommer.models.Message.grep") as grep,
    ):
        grep.return_value = float("inf"), 1, MockQuery()
        g.return_value = True
        assert rule.matches(msg, tahrir_client) == {"zodbot", "threebean"}


def test_complicated_recipient_pagure(
    rules,
    tahrir_client,
):
    rule = get_rule(rules, "Long Life to Pagure (Pagure I)")
    msg = Message(
        topic="io.pagure.prod.pagure.git.receive",
        body={
            "authors": [
                {"fullname": "Pierre-YvesChibon", "name": "pingou"},
                {"fullname": "Lubom\\u00edr Sedl\\u00e1\\u0159", "name": "lsedlar"},
            ],
            "total_commits": 2,
            "start_commit": "da090b8449237e3878d4d1fe56f7f8fcfd13a248",
        },
    )

    with (
        patch("fedbadges.rules.user_exists_in_fas") as g,
        patch("datanommer.models.Message.grep") as grep,
    ):
        grep.return_value = float("inf"), 1, MockQuery()
        g.return_value = True
        assert rule.matches(msg, tahrir_client) == {"pingou", "lsedlar"}


def test_complicated_recipient_pagure_bad(
    rules,
    tahrir_client,
):
    rule = get_rule(rules, "Long Life to Pagure (Pagure I)")
    msg = Message(
        topic="io.pagure.prod.pagure.git.receive",
        body={
            "authors": [
                {
                    "fullname": "Pierre-YvesChibon",
                },
                {
                    "fullname": "Lubom\\u00edr Sedl\\u00e1\\u0159",
                },
            ],
            "total_commits": 2,
            "start_commit": "da090b8449237e3878d4d1fe56f7f8fcfd13a248",
        },
    )

    with (
        patch("fedbadges.rules.user_exists_in_fas") as g,
        patch("datanommer.models.Message.grep") as grep,
    ):
        grep.return_value = float("inf"), 1, MockQuery()
        g.return_value = True
        with pytest.raises(ValueError) as excinfo:
            rule.matches(msg, tahrir_client)
        assert str(excinfo.value) == "Multiple recipients: name not found in the message"
