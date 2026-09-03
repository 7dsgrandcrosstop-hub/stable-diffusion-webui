from modules import colab_t4


def test_colab_t4_profile_disabled_by_default():
    assert not colab_t4.enabled({})


def test_colab_t4_profile_accepts_common_true_values():
    for value in ["1", "true", "TRUE", "yes", "on"]:
        assert colab_t4.enabled({"A1111_COLAB_T4": value})


def test_colab_t4_profile_rejects_false_values():
    for value in ["", "0", "false", "off", "anything-else"]:
        assert not colab_t4.enabled({"A1111_COLAB_T4": value})


def test_colab_t4_debug_limit(monkeypatch):
    monkeypatch.delenv("A1111_COLAB_T4", raising=False)
    assert colab_t4.debug_argument_limit(1000) == 1000
    monkeypatch.setenv("A1111_COLAB_T4", "1")
    assert colab_t4.debug_argument_limit(1000) == 4096
