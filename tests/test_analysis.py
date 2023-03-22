import pytest
from tagoio_sdk import Account
from requests_mock.mocker import Mocker
from analysis import get_profile_id_by_token, my_analysis
from tagoio_sdk.infrastructure.api_request import TagoIORequestError
from tests.mock import *


def test_method_get_profile_id_by_token(requests_mock: Mocker) -> None:
    account = Account(params={"token": MOCK_TOKEN})
    requests_mock.get(f"{URL_TAGOIO}profile", json=PROFILE_LIST)
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/token", json=TOKEN_LIST)

    result = get_profile_id_by_token(account, MOCK_TOKEN)

    assert result == "fake_id"
    assert isinstance(result, str)


def test_method_get_profile_id_by_token_failed(requests_mock: Mocker) -> None:
    account = Account(params={"token": MOCK_TOKEN})
    requests_mock.get(f"{URL_TAGOIO}profile", json=PROFILE_LIST)
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/token", json=TOKEN_LIST_FAIL)

    with pytest.raises(Exception):
        get_profile_id_by_token(account, MOCK_TOKEN)


def test_method_my_analysis_empty_environment() -> None:
    context = Context(environment=[])
    with pytest.raises(ValueError):
        my_analysis(context)


def test_method_my_analysis_without_account_token_in_environment() -> None:
    context = Context(environment=[{"key": "account_token", "value": None}])
    with pytest.raises(ValueError):
        my_analysis(context)


def test_method_my_analysis_no_auto_scape(requests_mock: Mocker) -> None:
    requests_mock.get(f"{URL_TAGOIO}profile", json=PROFILE_LIST)
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/token", json=TOKEN_LIST)
    requests_mock.get(f"{URL_TAGOIO}account/subscription", json=SUBSCRIPTION)
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/summary", json=PROFILE_SUMMARY)
    requests_mock.get(f"{URL_TAGOIO}pricing", json=BILLING)

    result = my_analysis(context=Context(environment=ENVIRONMENT))

    assert result == "Services are okay, no auto-scaling needed."
    assert isinstance(result, str)


def test_method_my_analysis_without_payment_method(requests_mock: Mocker) -> None:
    requests_mock.get(f"{URL_TAGOIO}profile", json=PROFILE_LIST)
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/token", json=TOKEN_LIST)
    requests_mock.get(f"{URL_TAGOIO}account/subscription", json=SUBSCRIPTION)
    PROFILE_SUMMARY["result"]["limit_used"]["sms"] = 100
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/summary", json=PROFILE_SUMMARY)
    requests_mock.get(f"{URL_TAGOIO}pricing", json=BILLING)
    requests_mock.post(
        f"{URL_TAGOIO}account/subscription",
        status_code=400,
        json=EDIT_SUBSCRIPTION_FAIL,
    )

    result = my_analysis(context=Context(environment=ENVIRONMENT))

    assert result.message == "Cannot subscribe without payment method"
    assert isinstance(result, TagoIORequestError)


def test_method_my_analysis_successfully(requests_mock: Mocker) -> None:
    requests_mock.get(f"{URL_TAGOIO}profile", json=PROFILE_LIST)
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/token", json=TOKEN_LIST)
    requests_mock.get(f"{URL_TAGOIO}account/subscription", json=SUBSCRIPTION)
    PROFILE_SUMMARY["result"]["limit_used"]["sms"] = 100
    requests_mock.get(f"{URL_TAGOIO}profile/fake_id/summary", json=PROFILE_SUMMARY)
    requests_mock.get(f"{URL_TAGOIO}pricing", json=BILLING)
    requests_mock.post(f"{URL_TAGOIO}account/subscription",json=EDIT_SUBSCRIPTION)

    result = my_analysis(context=Context(environment=ENVIRONMENT))

    assert result == "Subscription Successfully Updated"
    assert isinstance(result, str)
