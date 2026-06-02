# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .income import (
    IncomeResource,
    AsyncIncomeResource,
    IncomeResourceWithRawResponse,
    AsyncIncomeResourceWithRawResponse,
    IncomeResourceWithStreamingResponse,
    AsyncIncomeResourceWithStreamingResponse,
)
from .expense import (
    ExpenseResource,
    AsyncExpenseResource,
    ExpenseResourceWithRawResponse,
    AsyncExpenseResourceWithRawResponse,
    ExpenseResourceWithStreamingResponse,
    AsyncExpenseResourceWithStreamingResponse,
)
from .transfer import (
    TransferResource,
    AsyncTransferResource,
    TransferResourceWithRawResponse,
    AsyncTransferResourceWithRawResponse,
    TransferResourceWithStreamingResponse,
    AsyncTransferResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InsightResource", "AsyncInsightResource"]


class InsightResource(SyncAPIResource):
    @cached_property
    def expense(self) -> ExpenseResource:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return ExpenseResource(self._client)

    @cached_property
    def income(self) -> IncomeResource:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return IncomeResource(self._client)

    @cached_property
    def transfer(self) -> TransferResource:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return TransferResource(self._client)

    @cached_property
    def with_raw_response(self) -> InsightResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return InsightResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return InsightResourceWithStreamingResponse(self)


class AsyncInsightResource(AsyncAPIResource):
    @cached_property
    def expense(self) -> AsyncExpenseResource:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncExpenseResource(self._client)

    @cached_property
    def income(self) -> AsyncIncomeResource:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncIncomeResource(self._client)

    @cached_property
    def transfer(self) -> AsyncTransferResource:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncTransferResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInsightResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncInsightResourceWithStreamingResponse(self)


class InsightResourceWithRawResponse:
    def __init__(self, insight: InsightResource) -> None:
        self._insight = insight

    @cached_property
    def expense(self) -> ExpenseResourceWithRawResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return ExpenseResourceWithRawResponse(self._insight.expense)

    @cached_property
    def income(self) -> IncomeResourceWithRawResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return IncomeResourceWithRawResponse(self._insight.income)

    @cached_property
    def transfer(self) -> TransferResourceWithRawResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return TransferResourceWithRawResponse(self._insight.transfer)


class AsyncInsightResourceWithRawResponse:
    def __init__(self, insight: AsyncInsightResource) -> None:
        self._insight = insight

    @cached_property
    def expense(self) -> AsyncExpenseResourceWithRawResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncExpenseResourceWithRawResponse(self._insight.expense)

    @cached_property
    def income(self) -> AsyncIncomeResourceWithRawResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncIncomeResourceWithRawResponse(self._insight.income)

    @cached_property
    def transfer(self) -> AsyncTransferResourceWithRawResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncTransferResourceWithRawResponse(self._insight.transfer)


class InsightResourceWithStreamingResponse:
    def __init__(self, insight: InsightResource) -> None:
        self._insight = insight

    @cached_property
    def expense(self) -> ExpenseResourceWithStreamingResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return ExpenseResourceWithStreamingResponse(self._insight.expense)

    @cached_property
    def income(self) -> IncomeResourceWithStreamingResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return IncomeResourceWithStreamingResponse(self._insight.income)

    @cached_property
    def transfer(self) -> TransferResourceWithStreamingResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return TransferResourceWithStreamingResponse(self._insight.transfer)


class AsyncInsightResourceWithStreamingResponse:
    def __init__(self, insight: AsyncInsightResource) -> None:
        self._insight = insight

    @cached_property
    def expense(self) -> AsyncExpenseResourceWithStreamingResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncExpenseResourceWithStreamingResponse(self._insight.expense)

    @cached_property
    def income(self) -> AsyncIncomeResourceWithStreamingResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncIncomeResourceWithStreamingResponse(self._insight.income)

    @cached_property
    def transfer(self) -> AsyncTransferResourceWithStreamingResponse:
        """
        The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
        """
        return AsyncTransferResourceWithStreamingResponse(self._insight.transfer)
