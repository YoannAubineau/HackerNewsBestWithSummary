from app.usage import record_usage, today_spend


def test_today_spend_returns_none_without_api_key(httpx_mock, isolated_settings):
    isolated_settings.openrouter_api_key = ""
    assert today_spend() is None
    assert httpx_mock.get_requests() == []


def test_record_usage_noops_without_api_key(httpx_mock, isolated_settings):
    isolated_settings.openrouter_api_key = ""
    record_usage()
    assert httpx_mock.get_requests() == []
