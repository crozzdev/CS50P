from twttr import shorten


def test_basic_twitter_example():
    assert shorten("Twitter") == "Twttr"


def test_preserves_consonants_and_spaces():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("Python Programming") == "Pythn Prgrmmng"


def test_empty_string():
    assert shorten("") == ""


def test_only_vowels_lowercase():
    assert shorten("aeiou") == ""


def test_only_vowels_mixed_case():
    assert shorten("aAeEiIoOuU") == ""  # case-insensitive removal


def test_digits_unchanged():
    assert shorten("12345") == "12345"


def test_mixed_digits_and_vowels():
    assert shorten("a1e2i3o4u5") == "12345"


def test_cs50_sample_with_punctuation():
    # From the spec’s examples
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_nonletters_email_underscore_hyphen():
    assert shorten("email@domain.com") == "ml@dmn.cm"
    assert shorten("foo_bar-baz") == "f_br-bz"
    assert shorten("a,b.c!?") == ",b.c!?"


def test_whitespace_variants_preserved():
    # Tabs/newlines remain; only vowels are removed
    assert shorten("a\tb\nE") == "\tb\n"


def test_y_is_not_a_vowel():
    assert shorten("rhythm") == "rhythm"
    assert shorten("slyly") == "slyly"


def test_unicode_and_emoji_preserved():
    # The capital 'I' is removed (vowel), emoji and others pass through
    assert shorten("I ❤️ Python") == " ❤️ Pythn"


def test_accented_vowels_current_behavior():
    # With ASCII-only vowels, accented vowels are kept
    # "crème brûlée" -> remove only plain 'e' characters
    assert shorten("crème brûlée") == "crèm brûlé"


def test_no_nonvowels_removed():
    # Ensure consonants remain untouched
    s = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    assert shorten(s) == s


def test_idempotent():
    # Applying shorten twice should be the same as once
    s = "What's your name?"
    assert shorten(shorten(s)) == shorten(s)


def test_returns_str_type():
    assert isinstance(shorten("abc"), str)
