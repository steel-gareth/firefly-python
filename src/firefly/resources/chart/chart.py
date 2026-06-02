# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .budget import (
    BudgetResource,
    AsyncBudgetResource,
    BudgetResourceWithRawResponse,
    AsyncBudgetResourceWithRawResponse,
    BudgetResourceWithStreamingResponse,
    AsyncBudgetResourceWithStreamingResponse,
)
from .account import (
    AccountResource,
    AsyncAccountResource,
    AccountResourceWithRawResponse,
    AsyncAccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResourceWithStreamingResponse,
)
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from .category import (
    CategoryResource,
    AsyncCategoryResource,
    CategoryResourceWithRawResponse,
    AsyncCategoryResourceWithRawResponse,
    CategoryResourceWithStreamingResponse,
    AsyncCategoryResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ChartResource", "AsyncChartResource"]


class ChartResource(SyncAPIResource):
    @cached_property
    def account(self) -> AccountResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AccountResource(self._client)

    @cached_property
    def balance(self) -> BalanceResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return BalanceResource(self._client)

    @cached_property
    def budget(self) -> BudgetResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return BudgetResource(self._client)

    @cached_property
    def category(self) -> CategoryResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return CategoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return ChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return ChartResourceWithStreamingResponse(self)


class AsyncChartResource(AsyncAPIResource):
    @cached_property
    def account(self) -> AsyncAccountResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncAccountResource(self._client)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncBalanceResource(self._client)

    @cached_property
    def budget(self) -> AsyncBudgetResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncBudgetResource(self._client)

    @cached_property
    def category(self) -> AsyncCategoryResource:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncCategoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncChartResourceWithStreamingResponse(self)


class ChartResourceWithRawResponse:
    def __init__(self, chart: ChartResource) -> None:
        self._chart = chart

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AccountResourceWithRawResponse(self._chart.account)

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return BalanceResourceWithRawResponse(self._chart.balance)

    @cached_property
    def budget(self) -> BudgetResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return BudgetResourceWithRawResponse(self._chart.budget)

    @cached_property
    def category(self) -> CategoryResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return CategoryResourceWithRawResponse(self._chart.category)


class AsyncChartResourceWithRawResponse:
    def __init__(self, chart: AsyncChartResource) -> None:
        self._chart = chart

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncAccountResourceWithRawResponse(self._chart.account)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncBalanceResourceWithRawResponse(self._chart.balance)

    @cached_property
    def budget(self) -> AsyncBudgetResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncBudgetResourceWithRawResponse(self._chart.budget)

    @cached_property
    def category(self) -> AsyncCategoryResourceWithRawResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncCategoryResourceWithRawResponse(self._chart.category)


class ChartResourceWithStreamingResponse:
    def __init__(self, chart: ChartResource) -> None:
        self._chart = chart

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AccountResourceWithStreamingResponse(self._chart.account)

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return BalanceResourceWithStreamingResponse(self._chart.balance)

    @cached_property
    def budget(self) -> BudgetResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return BudgetResourceWithStreamingResponse(self._chart.budget)

    @cached_property
    def category(self) -> CategoryResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return CategoryResourceWithStreamingResponse(self._chart.category)


class AsyncChartResourceWithStreamingResponse:
    def __init__(self, chart: AsyncChartResource) -> None:
        self._chart = chart

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncAccountResourceWithStreamingResponse(self._chart.account)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncBalanceResourceWithStreamingResponse(self._chart.balance)

    @cached_property
    def budget(self) -> AsyncBudgetResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncBudgetResourceWithStreamingResponse(self._chart.budget)

    @cached_property
    def category(self) -> AsyncCategoryResourceWithStreamingResponse:
        """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""
        return AsyncCategoryResourceWithStreamingResponse(self._chart.category)
