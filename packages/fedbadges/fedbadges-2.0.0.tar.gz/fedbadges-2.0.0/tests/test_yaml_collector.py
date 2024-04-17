def test_load_badges_number(consumer):
    """Determine that we can load badges from file."""
    assert len(consumer.badge_rules) == 5


def test_load_badges_contents(consumer):
    """Determine that we can load badges from file."""
    names = set([badge["name"] for badge in consumer.badge_rules])
    assert names == {
        "Like a Rock",
        "The Zen of Foo Bar Baz",
        "Junior Tagger (Tagger I)",
        "Speak Up!",
        "Long Life to Pagure (Pagure I)",
    }
