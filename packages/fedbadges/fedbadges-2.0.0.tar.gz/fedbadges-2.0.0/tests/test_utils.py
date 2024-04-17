from fedora_messaging.message import Message

from fedbadges.utils import (
    construct_substitutions,
    format_args,
    single_argument_lambda_factory,
)


def test_lambda_factory():
    expression = "value + 2"
    target = 4
    actual = single_argument_lambda_factory(expression, 2)
    assert actual == target


def test_substitutions_basic():
    msg = Message(body=dict(a=dict(b=dict(c=42))))
    target = {
        "msg": dict(a=dict(b=dict(c=42))),
        "msg.a": dict(b=dict(c=42)),
        "msg.a.b": dict(c=42),
        "msg.a.b.c": 42,
        "topic": "",
    }
    actual = construct_substitutions(msg)
    assert actual == target


def test_substitutions_real():
    msg = Message(
        body={
            "thread": {"tagnames": ["town"], "pk": 2, "title": "alskdjflaksjdf lakjsf a"},
            "created": False,
            "timestamp": 1359947640.0,
            "topmost_post_id": 2,
            "agent": "ralph",
            "newly_mentioned_users": [],
            "diff": "<p>alskdfj... the diff is actually here",
            "post": {
                "vote_up_count": 0,
                "text": "alskdfjalskdjf alkjasdalskdjf ...",
                "summary": "alskdfjalskdjf alkjasdalskdjf ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 2,
                "post_type": "question",
            },
        },
        topic="org.fedoraproject.dev.askbot.post.edit",
    )
    target = {
        "msg.post.text": "alskdfjalskdjf alkjasdalskdjf ...",
        "msg.thread.title": "alskdjflaksjdf lakjsf a",
        "msg.post.vote_down_count": 0,
        "msg.post.post_type": "question",
        "msg.thread.pk": 2,
        "msg.newly_mentioned_users": [],
        "msg.diff": "<p>alskdfj... the diff is actually here",
        "topic": "org.fedoraproject.dev.askbot.post.edit",
        "msg.agent": "ralph",
        "msg.post.comment_count": 0,
        "msg.post": {
            "vote_up_count": 0,
            "text": "alskdfjalskdjf alkjasdalskdjf ...",
            "summary": "alskdfjalskdjf alkjasdalskdjf ...",
            "comment_count": 0,
            "vote_down_count": 0,
            "pk": 2,
            "post_type": "question",
        },
        "msg.timestamp": 1359947640.0,
        "msg.topmost_post_id": 2,
        "msg.post.pk": 2,
        "msg.post.vote_up_count": 0,
        "msg.post.summary": "alskdfjalskdjf alkjasdalskdjf ...",
        "msg.thread.tagnames": ["town"],
        "msg.thread": {"tagnames": ["town"], "pk": 2, "title": "alskdjflaksjdf lakjsf a"},
        "msg": {
            "newly_mentioned_users": [],
            "thread": {"tagnames": ["town"], "pk": 2, "title": "alskdjflaksjdf lakjsf a"},
            "created": False,
            "topmost_post_id": 2,
            "timestamp": 1359947640.0,
            "post": {
                "vote_up_count": 0,
                "text": "alskdfjalskdjf alkjasdalskdjf ...",
                "summary": "alskdfjalskdjf alkjasdalskdjf ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 2,
                "post_type": "question",
            },
            "diff": "<p>alskdfj... the diff is actually here",
            "agent": "ralph",
        },
        "msg.created": False,
    }
    actual = construct_substitutions(msg)
    assert actual == target


def test_format_args_simple():
    subs = {
        "foo.bar.baz": "value",
    }
    obj = {
        "something should be": "%(foo.bar.baz)s",
    }
    target = {
        "something should be": "value",
    }
    actual = format_args(obj, subs)
    assert actual == target


def test_format_args_list():
    subs = {
        "foo.bar.baz": "value",
    }
    obj = {
        "something should be": [
            "%(foo.bar.baz)s",
            "or this",
        ]
    }
    target = {
        "something should be": [
            "value",
            "or this",
        ]
    }
    actual = format_args(obj, subs)
    assert actual == target


def test_format_args_numeric():
    subs = {
        "foo.bar.baz": 42,
    }
    obj = {
        "something should be": "%(foo.bar.baz)i",
    }
    target = {
        "something should be": 42,
    }
    actual = format_args(obj, subs)
    assert actual == target


def test_format_args_nested():
    subs = {
        "wat": "another",
    }
    obj = {
        "one": {
            "thing": {
                "leads": {
                    "to": "%(wat)s",
                    "most": "of the time",
                }
            }
        }
    }
    target = {
        "one": {
            "thing": {
                "leads": {
                    "to": "another",
                    "most": "of the time",
                }
            }
        }
    }
    actual = format_args(obj, subs)
    assert actual == target


def test_format_args_nested_subs():
    subs = {"wat": dict(foo="bar")}
    obj = {
        "envelope": "%(wat)s",
    }
    target = {
        "envelope": dict(foo="bar"),
    }
    actual = format_args(obj, subs)
    assert actual == target
