# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        cron,
        data,
        tags,
        about,
        batch,
        bills,
        chart,
        rules,
        users,
        search,
        budgets,
        insight,
        summary,
        accounts,
        webhooks,
        categories,
        currencies,
        link_types,
        attachments,
        piggy_banks,
        preferences,
        recurrences,
        rule_groups,
        user_groups,
        autocomplete,
        transactions,
        configuration,
        object_groups,
        exchange_rates,
        available_budgets,
        transaction_links,
        transaction_journals,
    )
    from .resources.cron import CronResource, AsyncCronResource
    from .resources.tags import TagsResource, AsyncTagsResource
    from .resources.about import AboutResource, AsyncAboutResource
    from .resources.batch import BatchResource, AsyncBatchResource
    from .resources.bills import BillsResource, AsyncBillsResource
    from .resources.rules import RulesResource, AsyncRulesResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.summary import SummaryResource, AsyncSummaryResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.data.data import DataResource, AsyncDataResource
    from .resources.categories import CategoriesResource, AsyncCategoriesResource
    from .resources.link_types import LinkTypesResource, AsyncLinkTypesResource
    from .resources.attachments import AttachmentsResource, AsyncAttachmentsResource
    from .resources.chart.chart import ChartResource, AsyncChartResource
    from .resources.piggy_banks import PiggyBanksResource, AsyncPiggyBanksResource
    from .resources.preferences import PreferencesResource, AsyncPreferencesResource
    from .resources.recurrences import RecurrencesResource, AsyncRecurrencesResource
    from .resources.rule_groups import RuleGroupsResource, AsyncRuleGroupsResource
    from .resources.user_groups import UserGroupsResource, AsyncUserGroupsResource
    from .resources.autocomplete import AutocompleteResource, AsyncAutocompleteResource
    from .resources.transactions import TransactionsResource, AsyncTransactionsResource
    from .resources.configuration import ConfigurationResource, AsyncConfigurationResource
    from .resources.object_groups import ObjectGroupsResource, AsyncObjectGroupsResource
    from .resources.exchange_rates import ExchangeRatesResource, AsyncExchangeRatesResource
    from .resources.budgets.budgets import BudgetsResource, AsyncBudgetsResource
    from .resources.insight.insight import InsightResource, AsyncInsightResource
    from .resources.available_budgets import AvailableBudgetsResource, AsyncAvailableBudgetsResource
    from .resources.transaction_links import TransactionLinksResource, AsyncTransactionLinksResource
    from .resources.webhooks.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.transaction_journals import TransactionJournalsResource, AsyncTransactionJournalsResource
    from .resources.currencies.currencies import CurrenciesResource, AsyncCurrenciesResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Firefly",
    "AsyncFirefly",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://demo.firefly-iii.org/api",
    "environment_1": "http://firefly.sd.internal/api",
}


class Firefly(SyncAPIClient):
    # client options
    bearer_token: str | None

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Firefly client instance.

        This automatically infers the `bearer_token` argument from the `FIREFLY_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("FIREFLY_BEARER_TOKEN")
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("FIREFLY_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `FIREFLY_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("FIREFLY_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def autocomplete(self) -> AutocompleteResource:
        """
        Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
        """
        from .resources.autocomplete import AutocompleteResource

        return AutocompleteResource(self)

    @cached_property
    def chart(self) -> ChartResource:
        from .resources.chart import ChartResource

        return ChartResource(self)

    @cached_property
    def data(self) -> DataResource:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        from .resources.data import DataResource

        return DataResource(self)

    @cached_property
    def insight(self) -> InsightResource:
        from .resources.insight import InsightResource

        return InsightResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        """
        Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
        """
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def attachments(self) -> AttachmentsResource:
        """
        Endpoints to manage the attachments of the authenticated user, including up- and downloading of the files.
        """
        from .resources.attachments import AttachmentsResource

        return AttachmentsResource(self)

    @cached_property
    def available_budgets(self) -> AvailableBudgetsResource:
        """
        Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
        """
        from .resources.available_budgets import AvailableBudgetsResource

        return AvailableBudgetsResource(self)

    @cached_property
    def bills(self) -> BillsResource:
        """Endpoints to manage a user&#039;s bills and all related objects."""
        from .resources.bills import BillsResource

        return BillsResource(self)

    @cached_property
    def budgets(self) -> BudgetsResource:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        from .resources.budgets import BudgetsResource

        return BudgetsResource(self)

    @cached_property
    def categories(self) -> CategoriesResource:
        """
        Endpoints to manage a user&#039;s categories and get information on transactions and other related objects.
        """
        from .resources.categories import CategoriesResource

        return CategoriesResource(self)

    @cached_property
    def exchange_rates(self) -> ExchangeRatesResource:
        """All currency exchange rates."""
        from .resources.exchange_rates import ExchangeRatesResource

        return ExchangeRatesResource(self)

    @cached_property
    def link_types(self) -> LinkTypesResource:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.link_types import LinkTypesResource

        return LinkTypesResource(self)

    @cached_property
    def transaction_links(self) -> TransactionLinksResource:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.transaction_links import TransactionLinksResource

        return TransactionLinksResource(self)

    @cached_property
    def object_groups(self) -> ObjectGroupsResource:
        """Endpoints to control and manage all of the user&#039;s object groups.

        Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
        """
        from .resources.object_groups import ObjectGroupsResource

        return ObjectGroupsResource(self)

    @cached_property
    def piggy_banks(self) -> PiggyBanksResource:
        """
        Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
        """
        from .resources.piggy_banks import PiggyBanksResource

        return PiggyBanksResource(self)

    @cached_property
    def recurrences(self) -> RecurrencesResource:
        """
        Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
        """
        from .resources.recurrences import RecurrencesResource

        return RecurrencesResource(self)

    @cached_property
    def rule_groups(self) -> RuleGroupsResource:
        """
        Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
        """
        from .resources.rule_groups import RuleGroupsResource

        return RuleGroupsResource(self)

    @cached_property
    def rules(self) -> RulesResource:
        """These endpoints can be used to manage all of the user&#039;s rules.

        Also includes triggers to execute or test rules and individual triggers.
        """
        from .resources.rules import RulesResource

        return RulesResource(self)

    @cached_property
    def tags(self) -> TagsResource:
        """This endpoint manages all of the user&#039;s tags."""
        from .resources.tags import TagsResource

        return TagsResource(self)

    @cached_property
    def currencies(self) -> CurrenciesResource:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        from .resources.currencies import CurrenciesResource

        return CurrenciesResource(self)

    @cached_property
    def transaction_journals(self) -> TransactionJournalsResource:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transaction_journals import TransactionJournalsResource

        return TransactionJournalsResource(self)

    @cached_property
    def transactions(self) -> TransactionsResource:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transactions import TransactionsResource

        return TransactionsResource(self)

    @cached_property
    def user_groups(self) -> UserGroupsResource:
        """
        User groups are the objects around which &quot;financial administrations&quot; are built.
        """
        from .resources.user_groups import UserGroupsResource

        return UserGroupsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        """Endpoints that allow you to search through the user&#039;s financial data.

        Different from the autocomplete endpoints, the search accepts more advanced arguments.
        """
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def summary(self) -> SummaryResource:
        """
        These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
        """
        from .resources.summary import SummaryResource

        return SummaryResource(self)

    @cached_property
    def about(self) -> AboutResource:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.about import AboutResource

        return AboutResource(self)

    @cached_property
    def batch(self) -> BatchResource:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.batch import BatchResource

        return BatchResource(self)

    @cached_property
    def configuration(self) -> ConfigurationResource:
        """These endpoints allow you to manage and update the Firefly III configuration.

        You need to have the &quot;owner&quot; role to update configuration.
        """
        from .resources.configuration import ConfigurationResource

        return ConfigurationResource(self)

    @cached_property
    def cron(self) -> CronResource:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.cron import CronResource

        return CronResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """Use these endpoints to manage the users registered within Firefly III.

        You need to have the &quot;owner&quot; role to access these endpoints.
        """
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def preferences(self) -> PreferencesResource:
        """
        These endpoints can be used to manage the user&#039;s preferences, including some hidden ones.
        """
        from .resources.preferences import PreferencesResource

        return PreferencesResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> FireflyWithRawResponse:
        return FireflyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FireflyWithStreamedResponse:
        return FireflyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._local_bearer_auth if security.get("local_bearer_auth", False) else {}),
        }

    @property
    def _local_bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncFirefly(AsyncAPIClient):
    # client options
    bearer_token: str | None

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncFirefly client instance.

        This automatically infers the `bearer_token` argument from the `FIREFLY_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("FIREFLY_BEARER_TOKEN")
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("FIREFLY_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `FIREFLY_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("FIREFLY_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def autocomplete(self) -> AsyncAutocompleteResource:
        """
        Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
        """
        from .resources.autocomplete import AsyncAutocompleteResource

        return AsyncAutocompleteResource(self)

    @cached_property
    def chart(self) -> AsyncChartResource:
        from .resources.chart import AsyncChartResource

        return AsyncChartResource(self)

    @cached_property
    def data(self) -> AsyncDataResource:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        from .resources.data import AsyncDataResource

        return AsyncDataResource(self)

    @cached_property
    def insight(self) -> AsyncInsightResource:
        from .resources.insight import AsyncInsightResource

        return AsyncInsightResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """
        Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
        """
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def attachments(self) -> AsyncAttachmentsResource:
        """
        Endpoints to manage the attachments of the authenticated user, including up- and downloading of the files.
        """
        from .resources.attachments import AsyncAttachmentsResource

        return AsyncAttachmentsResource(self)

    @cached_property
    def available_budgets(self) -> AsyncAvailableBudgetsResource:
        """
        Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
        """
        from .resources.available_budgets import AsyncAvailableBudgetsResource

        return AsyncAvailableBudgetsResource(self)

    @cached_property
    def bills(self) -> AsyncBillsResource:
        """Endpoints to manage a user&#039;s bills and all related objects."""
        from .resources.bills import AsyncBillsResource

        return AsyncBillsResource(self)

    @cached_property
    def budgets(self) -> AsyncBudgetsResource:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        from .resources.budgets import AsyncBudgetsResource

        return AsyncBudgetsResource(self)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        """
        Endpoints to manage a user&#039;s categories and get information on transactions and other related objects.
        """
        from .resources.categories import AsyncCategoriesResource

        return AsyncCategoriesResource(self)

    @cached_property
    def exchange_rates(self) -> AsyncExchangeRatesResource:
        """All currency exchange rates."""
        from .resources.exchange_rates import AsyncExchangeRatesResource

        return AsyncExchangeRatesResource(self)

    @cached_property
    def link_types(self) -> AsyncLinkTypesResource:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.link_types import AsyncLinkTypesResource

        return AsyncLinkTypesResource(self)

    @cached_property
    def transaction_links(self) -> AsyncTransactionLinksResource:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.transaction_links import AsyncTransactionLinksResource

        return AsyncTransactionLinksResource(self)

    @cached_property
    def object_groups(self) -> AsyncObjectGroupsResource:
        """Endpoints to control and manage all of the user&#039;s object groups.

        Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
        """
        from .resources.object_groups import AsyncObjectGroupsResource

        return AsyncObjectGroupsResource(self)

    @cached_property
    def piggy_banks(self) -> AsyncPiggyBanksResource:
        """
        Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
        """
        from .resources.piggy_banks import AsyncPiggyBanksResource

        return AsyncPiggyBanksResource(self)

    @cached_property
    def recurrences(self) -> AsyncRecurrencesResource:
        """
        Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
        """
        from .resources.recurrences import AsyncRecurrencesResource

        return AsyncRecurrencesResource(self)

    @cached_property
    def rule_groups(self) -> AsyncRuleGroupsResource:
        """
        Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
        """
        from .resources.rule_groups import AsyncRuleGroupsResource

        return AsyncRuleGroupsResource(self)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        """These endpoints can be used to manage all of the user&#039;s rules.

        Also includes triggers to execute or test rules and individual triggers.
        """
        from .resources.rules import AsyncRulesResource

        return AsyncRulesResource(self)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        """This endpoint manages all of the user&#039;s tags."""
        from .resources.tags import AsyncTagsResource

        return AsyncTagsResource(self)

    @cached_property
    def currencies(self) -> AsyncCurrenciesResource:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        from .resources.currencies import AsyncCurrenciesResource

        return AsyncCurrenciesResource(self)

    @cached_property
    def transaction_journals(self) -> AsyncTransactionJournalsResource:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transaction_journals import AsyncTransactionJournalsResource

        return AsyncTransactionJournalsResource(self)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transactions import AsyncTransactionsResource

        return AsyncTransactionsResource(self)

    @cached_property
    def user_groups(self) -> AsyncUserGroupsResource:
        """
        User groups are the objects around which &quot;financial administrations&quot; are built.
        """
        from .resources.user_groups import AsyncUserGroupsResource

        return AsyncUserGroupsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """Endpoints that allow you to search through the user&#039;s financial data.

        Different from the autocomplete endpoints, the search accepts more advanced arguments.
        """
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        """
        These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
        """
        from .resources.summary import AsyncSummaryResource

        return AsyncSummaryResource(self)

    @cached_property
    def about(self) -> AsyncAboutResource:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.about import AsyncAboutResource

        return AsyncAboutResource(self)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.batch import AsyncBatchResource

        return AsyncBatchResource(self)

    @cached_property
    def configuration(self) -> AsyncConfigurationResource:
        """These endpoints allow you to manage and update the Firefly III configuration.

        You need to have the &quot;owner&quot; role to update configuration.
        """
        from .resources.configuration import AsyncConfigurationResource

        return AsyncConfigurationResource(self)

    @cached_property
    def cron(self) -> AsyncCronResource:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.cron import AsyncCronResource

        return AsyncCronResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Use these endpoints to manage the users registered within Firefly III.

        You need to have the &quot;owner&quot; role to access these endpoints.
        """
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        """
        These endpoints can be used to manage the user&#039;s preferences, including some hidden ones.
        """
        from .resources.preferences import AsyncPreferencesResource

        return AsyncPreferencesResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncFireflyWithRawResponse:
        return AsyncFireflyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFireflyWithStreamedResponse:
        return AsyncFireflyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._local_bearer_auth if security.get("local_bearer_auth", False) else {}),
        }

    @property
    def _local_bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class FireflyWithRawResponse:
    _client: Firefly

    def __init__(self, client: Firefly) -> None:
        self._client = client

    @cached_property
    def autocomplete(self) -> autocomplete.AutocompleteResourceWithRawResponse:
        """
        Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
        """
        from .resources.autocomplete import AutocompleteResourceWithRawResponse

        return AutocompleteResourceWithRawResponse(self._client.autocomplete)

    @cached_property
    def chart(self) -> chart.ChartResourceWithRawResponse:
        from .resources.chart import ChartResourceWithRawResponse

        return ChartResourceWithRawResponse(self._client.chart)

    @cached_property
    def data(self) -> data.DataResourceWithRawResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        from .resources.data import DataResourceWithRawResponse

        return DataResourceWithRawResponse(self._client.data)

    @cached_property
    def insight(self) -> insight.InsightResourceWithRawResponse:
        from .resources.insight import InsightResourceWithRawResponse

        return InsightResourceWithRawResponse(self._client.insight)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """
        Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
        """
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithRawResponse:
        """
        Endpoints to manage the attachments of the authenticated user, including up- and downloading of the files.
        """
        from .resources.attachments import AttachmentsResourceWithRawResponse

        return AttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def available_budgets(self) -> available_budgets.AvailableBudgetsResourceWithRawResponse:
        """
        Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
        """
        from .resources.available_budgets import AvailableBudgetsResourceWithRawResponse

        return AvailableBudgetsResourceWithRawResponse(self._client.available_budgets)

    @cached_property
    def bills(self) -> bills.BillsResourceWithRawResponse:
        """Endpoints to manage a user&#039;s bills and all related objects."""
        from .resources.bills import BillsResourceWithRawResponse

        return BillsResourceWithRawResponse(self._client.bills)

    @cached_property
    def budgets(self) -> budgets.BudgetsResourceWithRawResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        from .resources.budgets import BudgetsResourceWithRawResponse

        return BudgetsResourceWithRawResponse(self._client.budgets)

    @cached_property
    def categories(self) -> categories.CategoriesResourceWithRawResponse:
        """
        Endpoints to manage a user&#039;s categories and get information on transactions and other related objects.
        """
        from .resources.categories import CategoriesResourceWithRawResponse

        return CategoriesResourceWithRawResponse(self._client.categories)

    @cached_property
    def exchange_rates(self) -> exchange_rates.ExchangeRatesResourceWithRawResponse:
        """All currency exchange rates."""
        from .resources.exchange_rates import ExchangeRatesResourceWithRawResponse

        return ExchangeRatesResourceWithRawResponse(self._client.exchange_rates)

    @cached_property
    def link_types(self) -> link_types.LinkTypesResourceWithRawResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.link_types import LinkTypesResourceWithRawResponse

        return LinkTypesResourceWithRawResponse(self._client.link_types)

    @cached_property
    def transaction_links(self) -> transaction_links.TransactionLinksResourceWithRawResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.transaction_links import TransactionLinksResourceWithRawResponse

        return TransactionLinksResourceWithRawResponse(self._client.transaction_links)

    @cached_property
    def object_groups(self) -> object_groups.ObjectGroupsResourceWithRawResponse:
        """Endpoints to control and manage all of the user&#039;s object groups.

        Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
        """
        from .resources.object_groups import ObjectGroupsResourceWithRawResponse

        return ObjectGroupsResourceWithRawResponse(self._client.object_groups)

    @cached_property
    def piggy_banks(self) -> piggy_banks.PiggyBanksResourceWithRawResponse:
        """
        Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
        """
        from .resources.piggy_banks import PiggyBanksResourceWithRawResponse

        return PiggyBanksResourceWithRawResponse(self._client.piggy_banks)

    @cached_property
    def recurrences(self) -> recurrences.RecurrencesResourceWithRawResponse:
        """
        Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
        """
        from .resources.recurrences import RecurrencesResourceWithRawResponse

        return RecurrencesResourceWithRawResponse(self._client.recurrences)

    @cached_property
    def rule_groups(self) -> rule_groups.RuleGroupsResourceWithRawResponse:
        """
        Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
        """
        from .resources.rule_groups import RuleGroupsResourceWithRawResponse

        return RuleGroupsResourceWithRawResponse(self._client.rule_groups)

    @cached_property
    def rules(self) -> rules.RulesResourceWithRawResponse:
        """These endpoints can be used to manage all of the user&#039;s rules.

        Also includes triggers to execute or test rules and individual triggers.
        """
        from .resources.rules import RulesResourceWithRawResponse

        return RulesResourceWithRawResponse(self._client.rules)

    @cached_property
    def tags(self) -> tags.TagsResourceWithRawResponse:
        """This endpoint manages all of the user&#039;s tags."""
        from .resources.tags import TagsResourceWithRawResponse

        return TagsResourceWithRawResponse(self._client.tags)

    @cached_property
    def currencies(self) -> currencies.CurrenciesResourceWithRawResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        from .resources.currencies import CurrenciesResourceWithRawResponse

        return CurrenciesResourceWithRawResponse(self._client.currencies)

    @cached_property
    def transaction_journals(self) -> transaction_journals.TransactionJournalsResourceWithRawResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transaction_journals import TransactionJournalsResourceWithRawResponse

        return TransactionJournalsResourceWithRawResponse(self._client.transaction_journals)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithRawResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transactions import TransactionsResourceWithRawResponse

        return TransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def user_groups(self) -> user_groups.UserGroupsResourceWithRawResponse:
        """
        User groups are the objects around which &quot;financial administrations&quot; are built.
        """
        from .resources.user_groups import UserGroupsResourceWithRawResponse

        return UserGroupsResourceWithRawResponse(self._client.user_groups)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        """Endpoints that allow you to search through the user&#039;s financial data.

        Different from the autocomplete endpoints, the search accepts more advanced arguments.
        """
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def summary(self) -> summary.SummaryResourceWithRawResponse:
        """
        These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
        """
        from .resources.summary import SummaryResourceWithRawResponse

        return SummaryResourceWithRawResponse(self._client.summary)

    @cached_property
    def about(self) -> about.AboutResourceWithRawResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.about import AboutResourceWithRawResponse

        return AboutResourceWithRawResponse(self._client.about)

    @cached_property
    def batch(self) -> batch.BatchResourceWithRawResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.batch import BatchResourceWithRawResponse

        return BatchResourceWithRawResponse(self._client.batch)

    @cached_property
    def configuration(self) -> configuration.ConfigurationResourceWithRawResponse:
        """These endpoints allow you to manage and update the Firefly III configuration.

        You need to have the &quot;owner&quot; role to update configuration.
        """
        from .resources.configuration import ConfigurationResourceWithRawResponse

        return ConfigurationResourceWithRawResponse(self._client.configuration)

    @cached_property
    def cron(self) -> cron.CronResourceWithRawResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.cron import CronResourceWithRawResponse

        return CronResourceWithRawResponse(self._client.cron)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """Use these endpoints to manage the users registered within Firefly III.

        You need to have the &quot;owner&quot; role to access these endpoints.
        """
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def preferences(self) -> preferences.PreferencesResourceWithRawResponse:
        """
        These endpoints can be used to manage the user&#039;s preferences, including some hidden ones.
        """
        from .resources.preferences import PreferencesResourceWithRawResponse

        return PreferencesResourceWithRawResponse(self._client.preferences)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncFireflyWithRawResponse:
    _client: AsyncFirefly

    def __init__(self, client: AsyncFirefly) -> None:
        self._client = client

    @cached_property
    def autocomplete(self) -> autocomplete.AsyncAutocompleteResourceWithRawResponse:
        """
        Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
        """
        from .resources.autocomplete import AsyncAutocompleteResourceWithRawResponse

        return AsyncAutocompleteResourceWithRawResponse(self._client.autocomplete)

    @cached_property
    def chart(self) -> chart.AsyncChartResourceWithRawResponse:
        from .resources.chart import AsyncChartResourceWithRawResponse

        return AsyncChartResourceWithRawResponse(self._client.chart)

    @cached_property
    def data(self) -> data.AsyncDataResourceWithRawResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        from .resources.data import AsyncDataResourceWithRawResponse

        return AsyncDataResourceWithRawResponse(self._client.data)

    @cached_property
    def insight(self) -> insight.AsyncInsightResourceWithRawResponse:
        from .resources.insight import AsyncInsightResourceWithRawResponse

        return AsyncInsightResourceWithRawResponse(self._client.insight)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """
        Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
        """
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithRawResponse:
        """
        Endpoints to manage the attachments of the authenticated user, including up- and downloading of the files.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithRawResponse

        return AsyncAttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def available_budgets(self) -> available_budgets.AsyncAvailableBudgetsResourceWithRawResponse:
        """
        Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
        """
        from .resources.available_budgets import AsyncAvailableBudgetsResourceWithRawResponse

        return AsyncAvailableBudgetsResourceWithRawResponse(self._client.available_budgets)

    @cached_property
    def bills(self) -> bills.AsyncBillsResourceWithRawResponse:
        """Endpoints to manage a user&#039;s bills and all related objects."""
        from .resources.bills import AsyncBillsResourceWithRawResponse

        return AsyncBillsResourceWithRawResponse(self._client.bills)

    @cached_property
    def budgets(self) -> budgets.AsyncBudgetsResourceWithRawResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        from .resources.budgets import AsyncBudgetsResourceWithRawResponse

        return AsyncBudgetsResourceWithRawResponse(self._client.budgets)

    @cached_property
    def categories(self) -> categories.AsyncCategoriesResourceWithRawResponse:
        """
        Endpoints to manage a user&#039;s categories and get information on transactions and other related objects.
        """
        from .resources.categories import AsyncCategoriesResourceWithRawResponse

        return AsyncCategoriesResourceWithRawResponse(self._client.categories)

    @cached_property
    def exchange_rates(self) -> exchange_rates.AsyncExchangeRatesResourceWithRawResponse:
        """All currency exchange rates."""
        from .resources.exchange_rates import AsyncExchangeRatesResourceWithRawResponse

        return AsyncExchangeRatesResourceWithRawResponse(self._client.exchange_rates)

    @cached_property
    def link_types(self) -> link_types.AsyncLinkTypesResourceWithRawResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.link_types import AsyncLinkTypesResourceWithRawResponse

        return AsyncLinkTypesResourceWithRawResponse(self._client.link_types)

    @cached_property
    def transaction_links(self) -> transaction_links.AsyncTransactionLinksResourceWithRawResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.transaction_links import AsyncTransactionLinksResourceWithRawResponse

        return AsyncTransactionLinksResourceWithRawResponse(self._client.transaction_links)

    @cached_property
    def object_groups(self) -> object_groups.AsyncObjectGroupsResourceWithRawResponse:
        """Endpoints to control and manage all of the user&#039;s object groups.

        Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
        """
        from .resources.object_groups import AsyncObjectGroupsResourceWithRawResponse

        return AsyncObjectGroupsResourceWithRawResponse(self._client.object_groups)

    @cached_property
    def piggy_banks(self) -> piggy_banks.AsyncPiggyBanksResourceWithRawResponse:
        """
        Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
        """
        from .resources.piggy_banks import AsyncPiggyBanksResourceWithRawResponse

        return AsyncPiggyBanksResourceWithRawResponse(self._client.piggy_banks)

    @cached_property
    def recurrences(self) -> recurrences.AsyncRecurrencesResourceWithRawResponse:
        """
        Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
        """
        from .resources.recurrences import AsyncRecurrencesResourceWithRawResponse

        return AsyncRecurrencesResourceWithRawResponse(self._client.recurrences)

    @cached_property
    def rule_groups(self) -> rule_groups.AsyncRuleGroupsResourceWithRawResponse:
        """
        Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
        """
        from .resources.rule_groups import AsyncRuleGroupsResourceWithRawResponse

        return AsyncRuleGroupsResourceWithRawResponse(self._client.rule_groups)

    @cached_property
    def rules(self) -> rules.AsyncRulesResourceWithRawResponse:
        """These endpoints can be used to manage all of the user&#039;s rules.

        Also includes triggers to execute or test rules and individual triggers.
        """
        from .resources.rules import AsyncRulesResourceWithRawResponse

        return AsyncRulesResourceWithRawResponse(self._client.rules)

    @cached_property
    def tags(self) -> tags.AsyncTagsResourceWithRawResponse:
        """This endpoint manages all of the user&#039;s tags."""
        from .resources.tags import AsyncTagsResourceWithRawResponse

        return AsyncTagsResourceWithRawResponse(self._client.tags)

    @cached_property
    def currencies(self) -> currencies.AsyncCurrenciesResourceWithRawResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        from .resources.currencies import AsyncCurrenciesResourceWithRawResponse

        return AsyncCurrenciesResourceWithRawResponse(self._client.currencies)

    @cached_property
    def transaction_journals(self) -> transaction_journals.AsyncTransactionJournalsResourceWithRawResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transaction_journals import AsyncTransactionJournalsResourceWithRawResponse

        return AsyncTransactionJournalsResourceWithRawResponse(self._client.transaction_journals)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithRawResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transactions import AsyncTransactionsResourceWithRawResponse

        return AsyncTransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def user_groups(self) -> user_groups.AsyncUserGroupsResourceWithRawResponse:
        """
        User groups are the objects around which &quot;financial administrations&quot; are built.
        """
        from .resources.user_groups import AsyncUserGroupsResourceWithRawResponse

        return AsyncUserGroupsResourceWithRawResponse(self._client.user_groups)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        """Endpoints that allow you to search through the user&#039;s financial data.

        Different from the autocomplete endpoints, the search accepts more advanced arguments.
        """
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def summary(self) -> summary.AsyncSummaryResourceWithRawResponse:
        """
        These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
        """
        from .resources.summary import AsyncSummaryResourceWithRawResponse

        return AsyncSummaryResourceWithRawResponse(self._client.summary)

    @cached_property
    def about(self) -> about.AsyncAboutResourceWithRawResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.about import AsyncAboutResourceWithRawResponse

        return AsyncAboutResourceWithRawResponse(self._client.about)

    @cached_property
    def batch(self) -> batch.AsyncBatchResourceWithRawResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.batch import AsyncBatchResourceWithRawResponse

        return AsyncBatchResourceWithRawResponse(self._client.batch)

    @cached_property
    def configuration(self) -> configuration.AsyncConfigurationResourceWithRawResponse:
        """These endpoints allow you to manage and update the Firefly III configuration.

        You need to have the &quot;owner&quot; role to update configuration.
        """
        from .resources.configuration import AsyncConfigurationResourceWithRawResponse

        return AsyncConfigurationResourceWithRawResponse(self._client.configuration)

    @cached_property
    def cron(self) -> cron.AsyncCronResourceWithRawResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.cron import AsyncCronResourceWithRawResponse

        return AsyncCronResourceWithRawResponse(self._client.cron)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """Use these endpoints to manage the users registered within Firefly III.

        You need to have the &quot;owner&quot; role to access these endpoints.
        """
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def preferences(self) -> preferences.AsyncPreferencesResourceWithRawResponse:
        """
        These endpoints can be used to manage the user&#039;s preferences, including some hidden ones.
        """
        from .resources.preferences import AsyncPreferencesResourceWithRawResponse

        return AsyncPreferencesResourceWithRawResponse(self._client.preferences)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class FireflyWithStreamedResponse:
    _client: Firefly

    def __init__(self, client: Firefly) -> None:
        self._client = client

    @cached_property
    def autocomplete(self) -> autocomplete.AutocompleteResourceWithStreamingResponse:
        """
        Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
        """
        from .resources.autocomplete import AutocompleteResourceWithStreamingResponse

        return AutocompleteResourceWithStreamingResponse(self._client.autocomplete)

    @cached_property
    def chart(self) -> chart.ChartResourceWithStreamingResponse:
        from .resources.chart import ChartResourceWithStreamingResponse

        return ChartResourceWithStreamingResponse(self._client.chart)

    @cached_property
    def data(self) -> data.DataResourceWithStreamingResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        from .resources.data import DataResourceWithStreamingResponse

        return DataResourceWithStreamingResponse(self._client.data)

    @cached_property
    def insight(self) -> insight.InsightResourceWithStreamingResponse:
        from .resources.insight import InsightResourceWithStreamingResponse

        return InsightResourceWithStreamingResponse(self._client.insight)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """
        Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
        """
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithStreamingResponse:
        """
        Endpoints to manage the attachments of the authenticated user, including up- and downloading of the files.
        """
        from .resources.attachments import AttachmentsResourceWithStreamingResponse

        return AttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def available_budgets(self) -> available_budgets.AvailableBudgetsResourceWithStreamingResponse:
        """
        Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
        """
        from .resources.available_budgets import AvailableBudgetsResourceWithStreamingResponse

        return AvailableBudgetsResourceWithStreamingResponse(self._client.available_budgets)

    @cached_property
    def bills(self) -> bills.BillsResourceWithStreamingResponse:
        """Endpoints to manage a user&#039;s bills and all related objects."""
        from .resources.bills import BillsResourceWithStreamingResponse

        return BillsResourceWithStreamingResponse(self._client.bills)

    @cached_property
    def budgets(self) -> budgets.BudgetsResourceWithStreamingResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        from .resources.budgets import BudgetsResourceWithStreamingResponse

        return BudgetsResourceWithStreamingResponse(self._client.budgets)

    @cached_property
    def categories(self) -> categories.CategoriesResourceWithStreamingResponse:
        """
        Endpoints to manage a user&#039;s categories and get information on transactions and other related objects.
        """
        from .resources.categories import CategoriesResourceWithStreamingResponse

        return CategoriesResourceWithStreamingResponse(self._client.categories)

    @cached_property
    def exchange_rates(self) -> exchange_rates.ExchangeRatesResourceWithStreamingResponse:
        """All currency exchange rates."""
        from .resources.exchange_rates import ExchangeRatesResourceWithStreamingResponse

        return ExchangeRatesResourceWithStreamingResponse(self._client.exchange_rates)

    @cached_property
    def link_types(self) -> link_types.LinkTypesResourceWithStreamingResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.link_types import LinkTypesResourceWithStreamingResponse

        return LinkTypesResourceWithStreamingResponse(self._client.link_types)

    @cached_property
    def transaction_links(self) -> transaction_links.TransactionLinksResourceWithStreamingResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.transaction_links import TransactionLinksResourceWithStreamingResponse

        return TransactionLinksResourceWithStreamingResponse(self._client.transaction_links)

    @cached_property
    def object_groups(self) -> object_groups.ObjectGroupsResourceWithStreamingResponse:
        """Endpoints to control and manage all of the user&#039;s object groups.

        Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
        """
        from .resources.object_groups import ObjectGroupsResourceWithStreamingResponse

        return ObjectGroupsResourceWithStreamingResponse(self._client.object_groups)

    @cached_property
    def piggy_banks(self) -> piggy_banks.PiggyBanksResourceWithStreamingResponse:
        """
        Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
        """
        from .resources.piggy_banks import PiggyBanksResourceWithStreamingResponse

        return PiggyBanksResourceWithStreamingResponse(self._client.piggy_banks)

    @cached_property
    def recurrences(self) -> recurrences.RecurrencesResourceWithStreamingResponse:
        """
        Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
        """
        from .resources.recurrences import RecurrencesResourceWithStreamingResponse

        return RecurrencesResourceWithStreamingResponse(self._client.recurrences)

    @cached_property
    def rule_groups(self) -> rule_groups.RuleGroupsResourceWithStreamingResponse:
        """
        Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
        """
        from .resources.rule_groups import RuleGroupsResourceWithStreamingResponse

        return RuleGroupsResourceWithStreamingResponse(self._client.rule_groups)

    @cached_property
    def rules(self) -> rules.RulesResourceWithStreamingResponse:
        """These endpoints can be used to manage all of the user&#039;s rules.

        Also includes triggers to execute or test rules and individual triggers.
        """
        from .resources.rules import RulesResourceWithStreamingResponse

        return RulesResourceWithStreamingResponse(self._client.rules)

    @cached_property
    def tags(self) -> tags.TagsResourceWithStreamingResponse:
        """This endpoint manages all of the user&#039;s tags."""
        from .resources.tags import TagsResourceWithStreamingResponse

        return TagsResourceWithStreamingResponse(self._client.tags)

    @cached_property
    def currencies(self) -> currencies.CurrenciesResourceWithStreamingResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        from .resources.currencies import CurrenciesResourceWithStreamingResponse

        return CurrenciesResourceWithStreamingResponse(self._client.currencies)

    @cached_property
    def transaction_journals(self) -> transaction_journals.TransactionJournalsResourceWithStreamingResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transaction_journals import TransactionJournalsResourceWithStreamingResponse

        return TransactionJournalsResourceWithStreamingResponse(self._client.transaction_journals)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithStreamingResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transactions import TransactionsResourceWithStreamingResponse

        return TransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def user_groups(self) -> user_groups.UserGroupsResourceWithStreamingResponse:
        """
        User groups are the objects around which &quot;financial administrations&quot; are built.
        """
        from .resources.user_groups import UserGroupsResourceWithStreamingResponse

        return UserGroupsResourceWithStreamingResponse(self._client.user_groups)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        """Endpoints that allow you to search through the user&#039;s financial data.

        Different from the autocomplete endpoints, the search accepts more advanced arguments.
        """
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def summary(self) -> summary.SummaryResourceWithStreamingResponse:
        """
        These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
        """
        from .resources.summary import SummaryResourceWithStreamingResponse

        return SummaryResourceWithStreamingResponse(self._client.summary)

    @cached_property
    def about(self) -> about.AboutResourceWithStreamingResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.about import AboutResourceWithStreamingResponse

        return AboutResourceWithStreamingResponse(self._client.about)

    @cached_property
    def batch(self) -> batch.BatchResourceWithStreamingResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.batch import BatchResourceWithStreamingResponse

        return BatchResourceWithStreamingResponse(self._client.batch)

    @cached_property
    def configuration(self) -> configuration.ConfigurationResourceWithStreamingResponse:
        """These endpoints allow you to manage and update the Firefly III configuration.

        You need to have the &quot;owner&quot; role to update configuration.
        """
        from .resources.configuration import ConfigurationResourceWithStreamingResponse

        return ConfigurationResourceWithStreamingResponse(self._client.configuration)

    @cached_property
    def cron(self) -> cron.CronResourceWithStreamingResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.cron import CronResourceWithStreamingResponse

        return CronResourceWithStreamingResponse(self._client.cron)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """Use these endpoints to manage the users registered within Firefly III.

        You need to have the &quot;owner&quot; role to access these endpoints.
        """
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def preferences(self) -> preferences.PreferencesResourceWithStreamingResponse:
        """
        These endpoints can be used to manage the user&#039;s preferences, including some hidden ones.
        """
        from .resources.preferences import PreferencesResourceWithStreamingResponse

        return PreferencesResourceWithStreamingResponse(self._client.preferences)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncFireflyWithStreamedResponse:
    _client: AsyncFirefly

    def __init__(self, client: AsyncFirefly) -> None:
        self._client = client

    @cached_property
    def autocomplete(self) -> autocomplete.AsyncAutocompleteResourceWithStreamingResponse:
        """
        Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
        """
        from .resources.autocomplete import AsyncAutocompleteResourceWithStreamingResponse

        return AsyncAutocompleteResourceWithStreamingResponse(self._client.autocomplete)

    @cached_property
    def chart(self) -> chart.AsyncChartResourceWithStreamingResponse:
        from .resources.chart import AsyncChartResourceWithStreamingResponse

        return AsyncChartResourceWithStreamingResponse(self._client.chart)

    @cached_property
    def data(self) -> data.AsyncDataResourceWithStreamingResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        from .resources.data import AsyncDataResourceWithStreamingResponse

        return AsyncDataResourceWithStreamingResponse(self._client.data)

    @cached_property
    def insight(self) -> insight.AsyncInsightResourceWithStreamingResponse:
        from .resources.insight import AsyncInsightResourceWithStreamingResponse

        return AsyncInsightResourceWithStreamingResponse(self._client.insight)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """
        Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
        """
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithStreamingResponse:
        """
        Endpoints to manage the attachments of the authenticated user, including up- and downloading of the files.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithStreamingResponse

        return AsyncAttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def available_budgets(self) -> available_budgets.AsyncAvailableBudgetsResourceWithStreamingResponse:
        """
        Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
        """
        from .resources.available_budgets import AsyncAvailableBudgetsResourceWithStreamingResponse

        return AsyncAvailableBudgetsResourceWithStreamingResponse(self._client.available_budgets)

    @cached_property
    def bills(self) -> bills.AsyncBillsResourceWithStreamingResponse:
        """Endpoints to manage a user&#039;s bills and all related objects."""
        from .resources.bills import AsyncBillsResourceWithStreamingResponse

        return AsyncBillsResourceWithStreamingResponse(self._client.bills)

    @cached_property
    def budgets(self) -> budgets.AsyncBudgetsResourceWithStreamingResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        from .resources.budgets import AsyncBudgetsResourceWithStreamingResponse

        return AsyncBudgetsResourceWithStreamingResponse(self._client.budgets)

    @cached_property
    def categories(self) -> categories.AsyncCategoriesResourceWithStreamingResponse:
        """
        Endpoints to manage a user&#039;s categories and get information on transactions and other related objects.
        """
        from .resources.categories import AsyncCategoriesResourceWithStreamingResponse

        return AsyncCategoriesResourceWithStreamingResponse(self._client.categories)

    @cached_property
    def exchange_rates(self) -> exchange_rates.AsyncExchangeRatesResourceWithStreamingResponse:
        """All currency exchange rates."""
        from .resources.exchange_rates import AsyncExchangeRatesResourceWithStreamingResponse

        return AsyncExchangeRatesResourceWithStreamingResponse(self._client.exchange_rates)

    @cached_property
    def link_types(self) -> link_types.AsyncLinkTypesResourceWithStreamingResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.link_types import AsyncLinkTypesResourceWithStreamingResponse

        return AsyncLinkTypesResourceWithStreamingResponse(self._client.link_types)

    @cached_property
    def transaction_links(self) -> transaction_links.AsyncTransactionLinksResourceWithStreamingResponse:
        """
        Endpoints to manage links between transactions, and manage the type of links available.
        """
        from .resources.transaction_links import AsyncTransactionLinksResourceWithStreamingResponse

        return AsyncTransactionLinksResourceWithStreamingResponse(self._client.transaction_links)

    @cached_property
    def object_groups(self) -> object_groups.AsyncObjectGroupsResourceWithStreamingResponse:
        """Endpoints to control and manage all of the user&#039;s object groups.

        Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
        """
        from .resources.object_groups import AsyncObjectGroupsResourceWithStreamingResponse

        return AsyncObjectGroupsResourceWithStreamingResponse(self._client.object_groups)

    @cached_property
    def piggy_banks(self) -> piggy_banks.AsyncPiggyBanksResourceWithStreamingResponse:
        """
        Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
        """
        from .resources.piggy_banks import AsyncPiggyBanksResourceWithStreamingResponse

        return AsyncPiggyBanksResourceWithStreamingResponse(self._client.piggy_banks)

    @cached_property
    def recurrences(self) -> recurrences.AsyncRecurrencesResourceWithStreamingResponse:
        """
        Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
        """
        from .resources.recurrences import AsyncRecurrencesResourceWithStreamingResponse

        return AsyncRecurrencesResourceWithStreamingResponse(self._client.recurrences)

    @cached_property
    def rule_groups(self) -> rule_groups.AsyncRuleGroupsResourceWithStreamingResponse:
        """
        Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
        """
        from .resources.rule_groups import AsyncRuleGroupsResourceWithStreamingResponse

        return AsyncRuleGroupsResourceWithStreamingResponse(self._client.rule_groups)

    @cached_property
    def rules(self) -> rules.AsyncRulesResourceWithStreamingResponse:
        """These endpoints can be used to manage all of the user&#039;s rules.

        Also includes triggers to execute or test rules and individual triggers.
        """
        from .resources.rules import AsyncRulesResourceWithStreamingResponse

        return AsyncRulesResourceWithStreamingResponse(self._client.rules)

    @cached_property
    def tags(self) -> tags.AsyncTagsResourceWithStreamingResponse:
        """This endpoint manages all of the user&#039;s tags."""
        from .resources.tags import AsyncTagsResourceWithStreamingResponse

        return AsyncTagsResourceWithStreamingResponse(self._client.tags)

    @cached_property
    def currencies(self) -> currencies.AsyncCurrenciesResourceWithStreamingResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        from .resources.currencies import AsyncCurrenciesResourceWithStreamingResponse

        return AsyncCurrenciesResourceWithStreamingResponse(self._client.currencies)

    @cached_property
    def transaction_journals(self) -> transaction_journals.AsyncTransactionJournalsResourceWithStreamingResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transaction_journals import AsyncTransactionJournalsResourceWithStreamingResponse

        return AsyncTransactionJournalsResourceWithStreamingResponse(self._client.transaction_journals)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithStreamingResponse:
        """
        The most-used endpoints in Firefly III, these endpoints are used to manage the user&#039;s transactions.
        """
        from .resources.transactions import AsyncTransactionsResourceWithStreamingResponse

        return AsyncTransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def user_groups(self) -> user_groups.AsyncUserGroupsResourceWithStreamingResponse:
        """
        User groups are the objects around which &quot;financial administrations&quot; are built.
        """
        from .resources.user_groups import AsyncUserGroupsResourceWithStreamingResponse

        return AsyncUserGroupsResourceWithStreamingResponse(self._client.user_groups)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        """Endpoints that allow you to search through the user&#039;s financial data.

        Different from the autocomplete endpoints, the search accepts more advanced arguments.
        """
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def summary(self) -> summary.AsyncSummaryResourceWithStreamingResponse:
        """
        These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
        """
        from .resources.summary import AsyncSummaryResourceWithStreamingResponse

        return AsyncSummaryResourceWithStreamingResponse(self._client.summary)

    @cached_property
    def about(self) -> about.AsyncAboutResourceWithStreamingResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.about import AsyncAboutResourceWithStreamingResponse

        return AsyncAboutResourceWithStreamingResponse(self._client.about)

    @cached_property
    def batch(self) -> batch.AsyncBatchResourceWithStreamingResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.batch import AsyncBatchResourceWithStreamingResponse

        return AsyncBatchResourceWithStreamingResponse(self._client.batch)

    @cached_property
    def configuration(self) -> configuration.AsyncConfigurationResourceWithStreamingResponse:
        """These endpoints allow you to manage and update the Firefly III configuration.

        You need to have the &quot;owner&quot; role to update configuration.
        """
        from .resources.configuration import AsyncConfigurationResourceWithStreamingResponse

        return AsyncConfigurationResourceWithStreamingResponse(self._client.configuration)

    @cached_property
    def cron(self) -> cron.AsyncCronResourceWithStreamingResponse:
        """
        These endpoints deliver general system information, version- and meta information.
        """
        from .resources.cron import AsyncCronResourceWithStreamingResponse

        return AsyncCronResourceWithStreamingResponse(self._client.cron)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """Use these endpoints to manage the users registered within Firefly III.

        You need to have the &quot;owner&quot; role to access these endpoints.
        """
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def preferences(self) -> preferences.AsyncPreferencesResourceWithStreamingResponse:
        """
        These endpoints can be used to manage the user&#039;s preferences, including some hidden ones.
        """
        from .resources.preferences import AsyncPreferencesResourceWithStreamingResponse

        return AsyncPreferencesResourceWithStreamingResponse(self._client.preferences)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = Firefly

AsyncClient = AsyncFirefly
