import pytest
from fedora_messaging.message import Message

import fedbadges.rules


def test_basic_topic_matching_isolated():
    """Test that the matches method can match a basic topic."""
    trigger = fedbadges.rules.Trigger(
        dict(
            topic="test_topic",
        )
    )
    message = Message(
        topic="test_topic",
    )
    assert trigger.matches(message)


def test_basic_category_matching_isolated():
    """Test that the matches method can match a basic category."""
    trigger = fedbadges.rules.Trigger(
        dict(
            category="test_category",
        )
    )
    message = Message(
        topic="org.fedoraproject.dev.test_category.some_topic",
    )
    assert trigger.matches(message)


def test_basic_conjunction_pass():
    """Test that two anded fields accept the right message"""
    trigger = fedbadges.rules.Trigger(
        {
            "all": [
                dict(topic="org.fedoraproject.dev.test_category.test_topic"),
                dict(category="test_category"),
            ]
        }
    )
    message = Message(
        topic="org.fedoraproject.dev.test_category.test_topic",
    )
    assert trigger.matches(message)


def test_basic_conjunction_fail():
    """Test that two anded fields reject non-matching messages"""
    trigger = fedbadges.rules.Trigger(
        {
            "all": [
                dict(topic="org.fedoraproject.dev.test_category.test_topic"),
                dict(category="test_category"),
            ]
        }
    )
    message = Message(
        topic="org.fedoraproject.dev.test_category.test_topic.doesntmatch",
    )
    assert not trigger.matches(message)


def test_lambdas_pass():
    """Test that lambdas match correctly"""
    trigger = fedbadges.rules.Trigger(
        {
            "lambda": "'s3kr3t' in json.dumps(msg['msg'])",
        }
    )
    message = Message(body=dict(nested=dict(something="s3kr3t")))
    assert trigger.matches(message)


def test_lambdas_fail():
    """Test that lambdas fail correctly"""
    trigger = fedbadges.rules.Trigger(
        {
            "lambda": "'one string' in json.dumps(msg['msg'])",
        }
    )
    message = Message(body=dict(nested=dict(something="another string")))
    assert not trigger.matches(message)


def test_invalid_nesting():
    """Test that invalid nesting is detected and excepted."""
    with pytest.raises(TypeError):
        fedbadges.rules.Trigger(
            {
                "all": dict(
                    topic="org.fedoraproject.dev.test_category.test_topic",
                    category="test_category",
                )
            }
        )


def test_two_fields():
    """Test that passing two statements as a trigger is invalid."""
    with pytest.raises(ValueError):
        fedbadges.rules.Trigger(
            dict(
                topic="test_topic",
                category="test_topic",
            )
        )


def test_malformed_trigger():
    """Test that a single, undefined field is handled as invalid."""
    with pytest.raises(KeyError):
        fedbadges.rules.Trigger(
            dict(
                watwat="does not exist",
            )
        )
