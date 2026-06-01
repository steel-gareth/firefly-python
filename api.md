# Autocomplete

Types:

```python
from emcees_prod_testing_5.types import (
    AutocompleteBill,
    AutocompleteListAccountsResponse,
    AutocompleteListBillsResponse,
    AutocompleteListBudgetsResponse,
    AutocompleteListCategoriesResponse,
    AutocompleteListCurrenciesResponse,
    AutocompleteListCurrenciesWithCodeResponse,
    AutocompleteListObjectGroupsResponse,
    AutocompleteListPiggyBanksResponse,
    AutocompleteListPiggyBanksWithBalanceResponse,
    AutocompleteListRecurringTransactionsResponse,
    AutocompleteListRuleGroupsResponse,
    AutocompleteListRulesResponse,
    AutocompleteListSubscriptionsResponse,
    AutocompleteListTagsResponse,
    AutocompleteListTransactionTypesResponse,
    AutocompleteListTransactionsResponse,
    AutocompleteListTransactionsWithIDResponse,
)
```

Methods:

- <code title="get /v1/autocomplete/accounts">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_accounts</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_accounts_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_accounts_response.py">AutocompleteListAccountsResponse</a></code>
- <code title="get /v1/autocomplete/bills">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_bills</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_bills_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_bills_response.py">AutocompleteListBillsResponse</a></code>
- <code title="get /v1/autocomplete/budgets">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_budgets</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_budgets_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_budgets_response.py">AutocompleteListBudgetsResponse</a></code>
- <code title="get /v1/autocomplete/categories">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_categories</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_categories_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_categories_response.py">AutocompleteListCategoriesResponse</a></code>
- <code title="get /v1/autocomplete/currencies">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_currencies</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_currencies_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_currencies_response.py">AutocompleteListCurrenciesResponse</a></code>
- <code title="get /v1/autocomplete/currencies-with-code">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_currencies_with_code</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_currencies_with_code_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_currencies_with_code_response.py">AutocompleteListCurrenciesWithCodeResponse</a></code>
- <code title="get /v1/autocomplete/object-groups">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_object_groups</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_object_groups_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_object_groups_response.py">AutocompleteListObjectGroupsResponse</a></code>
- <code title="get /v1/autocomplete/piggy-banks">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_piggy_banks</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_piggy_banks_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_piggy_banks_response.py">AutocompleteListPiggyBanksResponse</a></code>
- <code title="get /v1/autocomplete/piggy-banks-with-balance">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_piggy_banks_with_balance</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_piggy_banks_with_balance_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_piggy_banks_with_balance_response.py">AutocompleteListPiggyBanksWithBalanceResponse</a></code>
- <code title="get /v1/autocomplete/recurring">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_recurring_transactions</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_recurring_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_recurring_transactions_response.py">AutocompleteListRecurringTransactionsResponse</a></code>
- <code title="get /v1/autocomplete/rule-groups">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_rule_groups</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_rule_groups_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_rule_groups_response.py">AutocompleteListRuleGroupsResponse</a></code>
- <code title="get /v1/autocomplete/rules">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_rules</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_rules_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_rules_response.py">AutocompleteListRulesResponse</a></code>
- <code title="get /v1/autocomplete/subscriptions">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_subscriptions</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_subscriptions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_subscriptions_response.py">AutocompleteListSubscriptionsResponse</a></code>
- <code title="get /v1/autocomplete/tags">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_tags</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_tags_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_tags_response.py">AutocompleteListTagsResponse</a></code>
- <code title="get /v1/autocomplete/transaction-types">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_transaction_types</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_transaction_types_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_transaction_types_response.py">AutocompleteListTransactionTypesResponse</a></code>
- <code title="get /v1/autocomplete/transactions">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_transactions</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_transactions_response.py">AutocompleteListTransactionsResponse</a></code>
- <code title="get /v1/autocomplete/transactions-with-id">client.autocomplete.<a href="./src/emcees_prod_testing_5/resources/autocomplete.py">list_transactions_with_id</a>(\*\*<a href="src/emcees_prod_testing_5/types/autocomplete_list_transactions_with_id_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/autocomplete_list_transactions_with_id_response.py">AutocompleteListTransactionsWithIDResponse</a></code>

# Chart

## Account

Types:

```python
from emcees_prod_testing_5.types.chart import (
    ChartDataPoint,
    ChartDataSet,
    AccountRetrieveOverviewResponse,
)
```

Methods:

- <code title="get /v1/chart/account/overview">client.chart.account.<a href="./src/emcees_prod_testing_5/resources/chart/account.py">retrieve_overview</a>(\*\*<a href="src/emcees_prod_testing_5/types/chart/account_retrieve_overview_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/chart/account_retrieve_overview_response.py">AccountRetrieveOverviewResponse</a></code>

## Balance

Types:

```python
from emcees_prod_testing_5.types.chart import BalanceRetrieveBalanceResponse
```

Methods:

- <code title="get /v1/chart/balance/balance">client.chart.balance.<a href="./src/emcees_prod_testing_5/resources/chart/balance.py">retrieve_balance</a>(\*\*<a href="src/emcees_prod_testing_5/types/chart/balance_retrieve_balance_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/chart/balance_retrieve_balance_response.py">BalanceRetrieveBalanceResponse</a></code>

## Budget

Types:

```python
from emcees_prod_testing_5.types.chart import BudgetRetrieveOverviewResponse
```

Methods:

- <code title="get /v1/chart/budget/overview">client.chart.budget.<a href="./src/emcees_prod_testing_5/resources/chart/budget.py">retrieve_overview</a>(\*\*<a href="src/emcees_prod_testing_5/types/chart/budget_retrieve_overview_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/chart/budget_retrieve_overview_response.py">BudgetRetrieveOverviewResponse</a></code>

## Category

Types:

```python
from emcees_prod_testing_5.types.chart import CategoryRetrieveOverviewResponse
```

Methods:

- <code title="get /v1/chart/category/overview">client.chart.category.<a href="./src/emcees_prod_testing_5/resources/chart/category.py">retrieve_overview</a>(\*\*<a href="src/emcees_prod_testing_5/types/chart/category_retrieve_overview_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/chart/category_retrieve_overview_response.py">CategoryRetrieveOverviewResponse</a></code>

# Data

Methods:

- <code title="delete /v1/data/destroy">client.data.<a href="./src/emcees_prod_testing_5/resources/data/data.py">destroy</a>(\*\*<a href="src/emcees_prod_testing_5/types/data_destroy_params.py">params</a>) -> None</code>
- <code title="delete /v1/data/purge">client.data.<a href="./src/emcees_prod_testing_5/resources/data/data.py">purge</a>() -> None</code>

## Bulk

Methods:

- <code title="post /v1/data/bulk/transactions">client.data.bulk.<a href="./src/emcees_prod_testing_5/resources/data/bulk.py">update_transactions</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/bulk_update_transactions_params.py">params</a>) -> None</code>

## Export

Types:

```python
from emcees_prod_testing_5.types.data import ExportFileFilter
```

Methods:

- <code title="get /v1/data/export/accounts">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_accounts</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_accounts_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/bills">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_bills</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_bills_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/budgets">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_budgets</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_budgets_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/categories">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_categories</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_categories_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/piggy-banks">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_piggy_banks</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_piggy_banks_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/recurring">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_recurring</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_recurring_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/rules">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_rules</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_rules_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/tags">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_tags</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_tags_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/data/export/transactions">client.data.export.<a href="./src/emcees_prod_testing_5/resources/data/export.py">export_transactions</a>(\*\*<a href="src/emcees_prod_testing_5/types/data/export_export_transactions_params.py">params</a>) -> BinaryAPIResponse</code>

# Insight

## Expense

Types:

```python
from emcees_prod_testing_5.types.insight import (
    InsightGroupEntry,
    InsightTotalEntry,
    ExpenseGetTotalResponse,
    ExpenseListByAssetAccountResponse,
    ExpenseListByBillResponse,
    ExpenseListByBudgetResponse,
    ExpenseListByCategoryResponse,
    ExpenseListByExpenseAccountResponse,
    ExpenseListByTagResponse,
    ExpenseListWithoutBillResponse,
    ExpenseListWithoutBudgetResponse,
    ExpenseListWithoutCategoryResponse,
    ExpenseListWithoutTagResponse,
)
```

Methods:

- <code title="get /v1/insight/expense/total">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">get_total</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_get_total_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_get_total_response.py">ExpenseGetTotalResponse</a></code>
- <code title="get /v1/insight/expense/asset">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_by_asset_account</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_by_asset_account_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_by_asset_account_response.py">ExpenseListByAssetAccountResponse</a></code>
- <code title="get /v1/insight/expense/bill">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_by_bill</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_by_bill_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_by_bill_response.py">ExpenseListByBillResponse</a></code>
- <code title="get /v1/insight/expense/budget">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_by_budget</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_by_budget_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_by_budget_response.py">ExpenseListByBudgetResponse</a></code>
- <code title="get /v1/insight/expense/category">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_by_category</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_by_category_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_by_category_response.py">ExpenseListByCategoryResponse</a></code>
- <code title="get /v1/insight/expense/expense">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_by_expense_account</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_by_expense_account_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_by_expense_account_response.py">ExpenseListByExpenseAccountResponse</a></code>
- <code title="get /v1/insight/expense/tag">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_by_tag</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_by_tag_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_by_tag_response.py">ExpenseListByTagResponse</a></code>
- <code title="get /v1/insight/expense/no-bill">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_without_bill</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_without_bill_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_without_bill_response.py">ExpenseListWithoutBillResponse</a></code>
- <code title="get /v1/insight/expense/no-budget">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_without_budget</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_without_budget_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_without_budget_response.py">ExpenseListWithoutBudgetResponse</a></code>
- <code title="get /v1/insight/expense/no-category">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_without_category</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_without_category_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_without_category_response.py">ExpenseListWithoutCategoryResponse</a></code>
- <code title="get /v1/insight/expense/no-tag">client.insight.expense.<a href="./src/emcees_prod_testing_5/resources/insight/expense.py">list_without_tag</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/expense_list_without_tag_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/expense_list_without_tag_response.py">ExpenseListWithoutTagResponse</a></code>

## Income

Types:

```python
from emcees_prod_testing_5.types.insight import (
    IncomeGetTotalResponse,
    IncomeListByAssetAccountResponse,
    IncomeListByCategoryResponse,
    IncomeListByRevenueAccountResponse,
    IncomeListByTagResponse,
    IncomeListWithoutCategoryResponse,
    IncomeListWithoutTagResponse,
)
```

Methods:

- <code title="get /v1/insight/income/total">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">get_total</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_get_total_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_get_total_response.py">IncomeGetTotalResponse</a></code>
- <code title="get /v1/insight/income/asset">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">list_by_asset_account</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_list_by_asset_account_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_list_by_asset_account_response.py">IncomeListByAssetAccountResponse</a></code>
- <code title="get /v1/insight/income/category">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">list_by_category</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_list_by_category_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_list_by_category_response.py">IncomeListByCategoryResponse</a></code>
- <code title="get /v1/insight/income/revenue">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">list_by_revenue_account</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_list_by_revenue_account_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_list_by_revenue_account_response.py">IncomeListByRevenueAccountResponse</a></code>
- <code title="get /v1/insight/income/tag">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">list_by_tag</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_list_by_tag_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_list_by_tag_response.py">IncomeListByTagResponse</a></code>
- <code title="get /v1/insight/income/no-category">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">list_without_category</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_list_without_category_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_list_without_category_response.py">IncomeListWithoutCategoryResponse</a></code>
- <code title="get /v1/insight/income/no-tag">client.insight.income.<a href="./src/emcees_prod_testing_5/resources/insight/income.py">list_without_tag</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/income_list_without_tag_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/income_list_without_tag_response.py">IncomeListWithoutTagResponse</a></code>

## Transfer

Types:

```python
from emcees_prod_testing_5.types.insight import (
    TransferGetTotalResponse,
    TransferListByAssetAccountResponse,
    TransferListByCategoryResponse,
    TransferListByTagResponse,
    TransferListWithoutCategoryResponse,
    TransferListWithoutTagResponse,
)
```

Methods:

- <code title="get /v1/insight/transfer/total">client.insight.transfer.<a href="./src/emcees_prod_testing_5/resources/insight/transfer.py">get_total</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/transfer_get_total_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/transfer_get_total_response.py">TransferGetTotalResponse</a></code>
- <code title="get /v1/insight/transfer/asset">client.insight.transfer.<a href="./src/emcees_prod_testing_5/resources/insight/transfer.py">list_by_asset_account</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/transfer_list_by_asset_account_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/transfer_list_by_asset_account_response.py">TransferListByAssetAccountResponse</a></code>
- <code title="get /v1/insight/transfer/category">client.insight.transfer.<a href="./src/emcees_prod_testing_5/resources/insight/transfer.py">list_by_category</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/transfer_list_by_category_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/transfer_list_by_category_response.py">TransferListByCategoryResponse</a></code>
- <code title="get /v1/insight/transfer/tag">client.insight.transfer.<a href="./src/emcees_prod_testing_5/resources/insight/transfer.py">list_by_tag</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/transfer_list_by_tag_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/transfer_list_by_tag_response.py">TransferListByTagResponse</a></code>
- <code title="get /v1/insight/transfer/no-category">client.insight.transfer.<a href="./src/emcees_prod_testing_5/resources/insight/transfer.py">list_without_category</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/transfer_list_without_category_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/transfer_list_without_category_response.py">TransferListWithoutCategoryResponse</a></code>
- <code title="get /v1/insight/transfer/no-tag">client.insight.transfer.<a href="./src/emcees_prod_testing_5/resources/insight/transfer.py">list_without_tag</a>(\*\*<a href="src/emcees_prod_testing_5/types/insight/transfer_list_without_tag_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/insight/transfer_list_without_tag_response.py">TransferListWithoutTagResponse</a></code>

# Accounts

Types:

```python
from emcees_prod_testing_5.types import (
    AccountArray,
    AccountRead,
    AccountRoleProperty,
    AccountSingle,
    AccountTypeFilter,
    AttachmentArray,
    CreditCardTypeProperty,
    InterestPeriodProperty,
    LiabilityDirectionProperty,
    LiabilityTypeProperty,
    Meta,
    PageLink,
    PiggyBankArray,
    ShortAccountTypeProperty,
    TransactionArray,
    TransactionTypeFilter,
)
```

Methods:

- <code title="post /v1/accounts">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/account_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/account_single.py">AccountSingle</a></code>
- <code title="get /v1/accounts/{id}">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">retrieve</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/account_retrieve_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/account_single.py">AccountSingle</a></code>
- <code title="put /v1/accounts/{id}">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/account_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/account_single.py">AccountSingle</a></code>
- <code title="get /v1/accounts">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/account_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/account_array.py">AccountArray</a></code>
- <code title="delete /v1/accounts/{id}">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">delete</a>(id) -> None</code>
- <code title="get /v1/accounts/{id}/attachments">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">list_attachments</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/account_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/accounts/{id}/piggy-banks">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">list_piggy_banks</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/account_list_piggy_banks_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_array.py">PiggyBankArray</a></code>
- <code title="get /v1/accounts/{id}/transactions">client.accounts.<a href="./src/emcees_prod_testing_5/resources/accounts.py">list_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/account_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# Attachments

Types:

```python
from emcees_prod_testing_5.types import AttachableType, AttachmentRead, AttachmentSingle, ObjectLink
```

Methods:

- <code title="post /v1/attachments">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/attachment_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_single.py">AttachmentSingle</a></code>
- <code title="get /v1/attachments/{id}">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/attachment_single.py">AttachmentSingle</a></code>
- <code title="put /v1/attachments/{id}">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/attachment_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_single.py">AttachmentSingle</a></code>
- <code title="get /v1/attachments">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/attachment_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="delete /v1/attachments/{id}">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">delete</a>(id) -> None</code>
- <code title="get /v1/attachments/{id}/download">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">download</a>(id) -> BinaryAPIResponse</code>
- <code title="post /v1/attachments/{id}/upload">client.attachments.<a href="./src/emcees_prod_testing_5/resources/attachments.py">upload</a>(id, body, \*\*<a href="src/emcees_prod_testing_5/types/attachment_upload_params.py">params</a>) -> None</code>

# AvailableBudgets

Types:

```python
from emcees_prod_testing_5.types import (
    ArrayEntryWithCurrencyAndSum,
    AvailableBudgetArray,
    AvailableBudgetRead,
    AvailableBudgetRetrieveResponse,
)
```

Methods:

- <code title="get /v1/available-budgets/{id}">client.available_budgets.<a href="./src/emcees_prod_testing_5/resources/available_budgets.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/available_budget_retrieve_response.py">AvailableBudgetRetrieveResponse</a></code>
- <code title="get /v1/available-budgets">client.available_budgets.<a href="./src/emcees_prod_testing_5/resources/available_budgets.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/available_budget_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/available_budget_array.py">AvailableBudgetArray</a></code>

# Bills

Types:

```python
from emcees_prod_testing_5.types import (
    BillArray,
    BillRead,
    BillRepeatFrequency,
    BillSingle,
    RuleArray,
)
```

Methods:

- <code title="post /v1/bills">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/bill_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/bill_single.py">BillSingle</a></code>
- <code title="get /v1/bills/{id}">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">retrieve</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/bill_retrieve_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/bill_single.py">BillSingle</a></code>
- <code title="put /v1/bills/{id}">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/bill_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/bill_single.py">BillSingle</a></code>
- <code title="get /v1/bills">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/bill_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/bill_array.py">BillArray</a></code>
- <code title="delete /v1/bills/{id}">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">delete</a>(id) -> None</code>
- <code title="get /v1/bills/{id}/attachments">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">list_attachments</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/bill_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/bills/{id}/rules">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">list_rules</a>(id) -> <a href="./src/emcees_prod_testing_5/types/rule_array.py">RuleArray</a></code>
- <code title="get /v1/bills/{id}/transactions">client.bills.<a href="./src/emcees_prod_testing_5/resources/bills.py">list_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/bill_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# Budgets

Types:

```python
from emcees_prod_testing_5.types import (
    AutoBudgetPeriod,
    AutoBudgetType,
    BudgetRead,
    BudgetSingle,
    BudgetListResponse,
)
```

Methods:

- <code title="post /v1/budgets">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/budget_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budget_single.py">BudgetSingle</a></code>
- <code title="get /v1/budgets/{id}">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">retrieve</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/budget_retrieve_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budget_single.py">BudgetSingle</a></code>
- <code title="put /v1/budgets/{id}">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/budget_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budget_single.py">BudgetSingle</a></code>
- <code title="get /v1/budgets">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/budget_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budget_list_response.py">BudgetListResponse</a></code>
- <code title="delete /v1/budgets/{id}">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">delete</a>(id) -> None</code>
- <code title="get /v1/budgets/{id}/attachments">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">list_attachments</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/budget_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/budgets/{id}/transactions">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">list_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/budget_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>
- <code title="get /v1/budgets/transactions-without-budget">client.budgets.<a href="./src/emcees_prod_testing_5/resources/budgets/budgets.py">list_transactions_without_budget</a>(\*\*<a href="src/emcees_prod_testing_5/types/budget_list_transactions_without_budget_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

## Limits

Types:

```python
from emcees_prod_testing_5.types.budgets import BudgetLimitArray, BudgetLimitRead, BudgetLimitSingle
```

Methods:

- <code title="post /v1/budgets/{id}/limits">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">create</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/budgets/limit_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budgets/budget_limit_single.py">BudgetLimitSingle</a></code>
- <code title="get /v1/budgets/{id}/limits/{limitId}">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">retrieve</a>(limit_id, \*, id) -> <a href="./src/emcees_prod_testing_5/types/budgets/budget_limit_single.py">BudgetLimitSingle</a></code>
- <code title="put /v1/budgets/{id}/limits/{limitId}">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">update</a>(limit_id, \*, id, \*\*<a href="src/emcees_prod_testing_5/types/budgets/limit_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budgets/budget_limit_single.py">BudgetLimitSingle</a></code>
- <code title="delete /v1/budgets/{id}/limits/{limitId}">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">delete</a>(limit_id, \*, id) -> None</code>
- <code title="get /v1/budgets/{id}/limits">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">list_0</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/budgets/limit_list_0_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budgets/budget_limit_array.py">BudgetLimitArray</a></code>
- <code title="get /v1/budget-limits">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">list_1</a>(\*\*<a href="src/emcees_prod_testing_5/types/budgets/limit_list_1_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budgets/budget_limit_array.py">BudgetLimitArray</a></code>
- <code title="get /v1/budgets/{id}/limits/{limitId}/transactions">client.budgets.limits.<a href="./src/emcees_prod_testing_5/resources/budgets/limits.py">list_transactions</a>(limit_id, \*, id, \*\*<a href="src/emcees_prod_testing_5/types/budgets/limit_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# Categories

Types:

```python
from emcees_prod_testing_5.types import CategoryRead, CategorySingle, CategoryListResponse
```

Methods:

- <code title="post /v1/categories">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/category_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/category_single.py">CategorySingle</a></code>
- <code title="get /v1/categories/{id}">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">retrieve</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/category_retrieve_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/category_single.py">CategorySingle</a></code>
- <code title="put /v1/categories/{id}">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/category_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/category_single.py">CategorySingle</a></code>
- <code title="get /v1/categories">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/category_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/category_list_response.py">CategoryListResponse</a></code>
- <code title="delete /v1/categories/{id}">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">delete</a>(id) -> None</code>
- <code title="get /v1/categories/{id}/attachments">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">list_attachments</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/category_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/categories/{id}/transactions">client.categories.<a href="./src/emcees_prod_testing_5/resources/categories.py">list_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/category_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# ExchangeRates

Types:

```python
from emcees_prod_testing_5.types import (
    CurrencyExchangeRateArray,
    CurrencyExchangeRateRead,
    CurrencyExchangeRateSingle,
)
```

Methods:

- <code title="post /v1/exchange-rates">client.exchange_rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_single.py">CurrencyExchangeRateSingle</a></code>
- <code title="get /v1/exchange-rates/{id}">client.exchange_rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">retrieve</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_retrieve_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_single.py">CurrencyExchangeRateSingle</a></code>
- <code title="put /v1/exchange-rates/{id}">client.exchange_rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_single.py">CurrencyExchangeRateSingle</a></code>
- <code title="get /v1/exchange-rates">client.exchange_rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_array.py">CurrencyExchangeRateArray</a></code>
- <code title="delete /v1/exchange-rates/{id}">client.exchange_rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">delete</a>(id) -> None</code>
- <code title="post /v1/exchange-rates/by-currencies/{from}/{to}">client.exchange*rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">create_by_currencies</a>(to, \*, from*, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_create_by_currencies_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_array.py">CurrencyExchangeRateArray</a></code>
- <code title="post /v1/exchange-rates/by-date/{date}">client.exchange_rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">create_by_date</a>(path_date, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_create_by_date_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_array.py">CurrencyExchangeRateArray</a></code>
- <code title="delete /v1/exchange-rates/{from}/{to}">client.exchange*rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">delete_all_by_currencies</a>(to, \*, from*) -> None</code>
- <code title="delete /v1/exchange-rates/{from}/{to}/{date}">client.exchange*rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">delete_by_date</a>(date, \*, from*, to) -> None</code>
- <code title="get /v1/exchange-rates/{from}/{to}">client.exchange*rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">list_by_currencies</a>(to, \*, from*, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_list_by_currencies_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_array.py">CurrencyExchangeRateArray</a></code>
- <code title="get /v1/exchange-rates/{from}/{to}/{date}">client.exchange*rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">retrieve_by_date</a>(date, \*, from*, to, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_retrieve_by_date_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_array.py">CurrencyExchangeRateArray</a></code>
- <code title="put /v1/exchange-rates/{from}/{to}/{date}">client.exchange*rates.<a href="./src/emcees_prod_testing_5/resources/exchange_rates.py">update_by_date</a>(date, \*, from*, to, \*\*<a href="src/emcees_prod_testing_5/types/exchange_rate_update_by_date_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_exchange_rate_single.py">CurrencyExchangeRateSingle</a></code>

# LinkTypes

Types:

```python
from emcees_prod_testing_5.types import LinkType, LinkTypeRead, LinkTypeSingle, LinkTypeListResponse
```

Methods:

- <code title="post /v1/link-types">client.link_types.<a href="./src/emcees_prod_testing_5/resources/link_types.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/link_type_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/link_type_single.py">LinkTypeSingle</a></code>
- <code title="get /v1/link-types/{id}">client.link_types.<a href="./src/emcees_prod_testing_5/resources/link_types.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/link_type_single.py">LinkTypeSingle</a></code>
- <code title="put /v1/link-types/{id}">client.link_types.<a href="./src/emcees_prod_testing_5/resources/link_types.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/link_type_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/link_type_single.py">LinkTypeSingle</a></code>
- <code title="get /v1/link-types">client.link_types.<a href="./src/emcees_prod_testing_5/resources/link_types.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/link_type_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/link_type_list_response.py">LinkTypeListResponse</a></code>
- <code title="delete /v1/link-types/{id}">client.link_types.<a href="./src/emcees_prod_testing_5/resources/link_types.py">delete</a>(id) -> None</code>
- <code title="get /v1/link-types/{id}/transactions">client.link_types.<a href="./src/emcees_prod_testing_5/resources/link_types.py">list_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/link_type_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# TransactionLinks

Types:

```python
from emcees_prod_testing_5.types import (
    TransactionLinkArray,
    TransactionLinkRead,
    TransactionLinkSingle,
)
```

Methods:

- <code title="post /v1/transaction-links">client.transaction_links.<a href="./src/emcees_prod_testing_5/resources/transaction_links.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/transaction_link_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_link_single.py">TransactionLinkSingle</a></code>
- <code title="get /v1/transaction-links/{id}">client.transaction_links.<a href="./src/emcees_prod_testing_5/resources/transaction_links.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/transaction_link_single.py">TransactionLinkSingle</a></code>
- <code title="put /v1/transaction-links/{id}">client.transaction_links.<a href="./src/emcees_prod_testing_5/resources/transaction_links.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/transaction_link_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_link_single.py">TransactionLinkSingle</a></code>
- <code title="get /v1/transaction-links">client.transaction_links.<a href="./src/emcees_prod_testing_5/resources/transaction_links.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/transaction_link_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_link_array.py">TransactionLinkArray</a></code>
- <code title="delete /v1/transaction-links/{id}">client.transaction_links.<a href="./src/emcees_prod_testing_5/resources/transaction_links.py">delete</a>(id) -> None</code>

# ObjectGroups

Types:

```python
from emcees_prod_testing_5.types import ObjectGroupRead, ObjectGroupSingle, ObjectGroupListResponse
```

Methods:

- <code title="get /v1/object-groups/{id}">client.object_groups.<a href="./src/emcees_prod_testing_5/resources/object_groups.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/object_group_single.py">ObjectGroupSingle</a></code>
- <code title="put /v1/object-groups/{id}">client.object_groups.<a href="./src/emcees_prod_testing_5/resources/object_groups.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/object_group_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/object_group_single.py">ObjectGroupSingle</a></code>
- <code title="get /v1/object-groups">client.object_groups.<a href="./src/emcees_prod_testing_5/resources/object_groups.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/object_group_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/object_group_list_response.py">ObjectGroupListResponse</a></code>
- <code title="delete /v1/object-groups/{id}">client.object_groups.<a href="./src/emcees_prod_testing_5/resources/object_groups.py">delete</a>(id) -> None</code>
- <code title="get /v1/object-groups/{id}/bills">client.object_groups.<a href="./src/emcees_prod_testing_5/resources/object_groups.py">list_bills</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/object_group_list_bills_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/bill_array.py">BillArray</a></code>
- <code title="get /v1/object-groups/{id}/piggy-banks">client.object_groups.<a href="./src/emcees_prod_testing_5/resources/object_groups.py">list_piggy_banks</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/object_group_list_piggy_banks_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_array.py">PiggyBankArray</a></code>

# PiggyBanks

Types:

```python
from emcees_prod_testing_5.types import PiggyBankEventArray, PiggyBankRead, PiggyBankSingle
```

Methods:

- <code title="post /v1/piggy-banks">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/piggy_bank_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_single.py">PiggyBankSingle</a></code>
- <code title="get /v1/piggy-banks/{id}">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_single.py">PiggyBankSingle</a></code>
- <code title="put /v1/piggy-banks/{id}">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/piggy_bank_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_single.py">PiggyBankSingle</a></code>
- <code title="get /v1/piggy-banks">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/piggy_bank_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_array.py">PiggyBankArray</a></code>
- <code title="delete /v1/piggy-banks/{id}">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">delete</a>(id) -> None</code>
- <code title="get /v1/piggy-banks/{id}/attachments">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">list_attachments</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/piggy_bank_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/piggy-banks/{id}/events">client.piggy_banks.<a href="./src/emcees_prod_testing_5/resources/piggy_banks.py">list_events</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/piggy_bank_list_events_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_event_array.py">PiggyBankEventArray</a></code>

# Recurrences

Types:

```python
from emcees_prod_testing_5.types import (
    AccountTypeProperty,
    RecurrenceArray,
    RecurrenceRead,
    RecurrenceRepetitionType,
    RecurrenceSingle,
    RecurrenceTransactionType,
)
```

Methods:

- <code title="post /v1/recurrences">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/recurrence_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/recurrence_single.py">RecurrenceSingle</a></code>
- <code title="get /v1/recurrences/{id}">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/recurrence_single.py">RecurrenceSingle</a></code>
- <code title="put /v1/recurrences/{id}">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/recurrence_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/recurrence_single.py">RecurrenceSingle</a></code>
- <code title="get /v1/recurrences">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/recurrence_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/recurrence_array.py">RecurrenceArray</a></code>
- <code title="delete /v1/recurrences/{id}">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">delete</a>(id) -> None</code>
- <code title="get /v1/recurrences/{id}/transactions">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">list_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/recurrence_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>
- <code title="post /v1/recurrences/{id}/trigger">client.recurrences.<a href="./src/emcees_prod_testing_5/resources/recurrences.py">trigger_transaction</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/recurrence_trigger_transaction_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# RuleGroups

Types:

```python
from emcees_prod_testing_5.types import RuleGroupRead, RuleGroupSingle, RuleGroupListAllResponse
```

Methods:

- <code title="post /v1/rule-groups">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/rule_group_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_group_single.py">RuleGroupSingle</a></code>
- <code title="get /v1/rule-groups/{id}">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/rule_group_single.py">RuleGroupSingle</a></code>
- <code title="put /v1/rule-groups/{id}">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_group_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_group_single.py">RuleGroupSingle</a></code>
- <code title="delete /v1/rule-groups/{id}">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">delete</a>(id) -> None</code>
- <code title="get /v1/rule-groups">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">list_all</a>(\*\*<a href="src/emcees_prod_testing_5/types/rule_group_list_all_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_group_list_all_response.py">RuleGroupListAllResponse</a></code>
- <code title="get /v1/rule-groups/{id}/rules">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">list_rules</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_group_list_rules_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_array.py">RuleArray</a></code>
- <code title="get /v1/rule-groups/{id}/test">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">test_transactions</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_group_test_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>
- <code title="post /v1/rule-groups/{id}/trigger">client.rule_groups.<a href="./src/emcees_prod_testing_5/resources/rule_groups.py">trigger_rules</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_group_trigger_rules_params.py">params</a>) -> None</code>

# Rules

Types:

```python
from emcees_prod_testing_5.types import (
    RuleActionKeyword,
    RuleRead,
    RuleSingle,
    RuleTriggerKeyword,
    RuleTriggerType,
)
```

Methods:

- <code title="post /v1/rules">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/rule_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_single.py">RuleSingle</a></code>
- <code title="get /v1/rules/{id}">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/rule_single.py">RuleSingle</a></code>
- <code title="put /v1/rules/{id}">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_single.py">RuleSingle</a></code>
- <code title="get /v1/rules">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/rule_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_array.py">RuleArray</a></code>
- <code title="delete /v1/rules/{id}">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">delete</a>(id) -> None</code>
- <code title="get /v1/rules/{id}/test">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">test</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_test_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>
- <code title="post /v1/rules/{id}/trigger">client.rules.<a href="./src/emcees_prod_testing_5/resources/rules.py">trigger</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/rule_trigger_params.py">params</a>) -> None</code>

# Tags

Types:

```python
from emcees_prod_testing_5.types import TagRead, TagSingle, TagListResponse
```

Methods:

- <code title="post /v1/tags">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/tag_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/tag_single.py">TagSingle</a></code>
- <code title="get /v1/tags/{tag}">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">retrieve</a>(tag, \*\*<a href="src/emcees_prod_testing_5/types/tag_retrieve_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/tag_single.py">TagSingle</a></code>
- <code title="put /v1/tags/{tag}">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">update</a>(path_tag, \*\*<a href="src/emcees_prod_testing_5/types/tag_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/tag_single.py">TagSingle</a></code>
- <code title="get /v1/tags">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/tag_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /v1/tags/{tag}">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">delete</a>(tag) -> None</code>
- <code title="get /v1/tags/{tag}/attachments">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">list_attachments</a>(tag, \*\*<a href="src/emcees_prod_testing_5/types/tag_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/tags/{tag}/transactions">client.tags.<a href="./src/emcees_prod_testing_5/resources/tags.py">list_transactions</a>(tag, \*\*<a href="src/emcees_prod_testing_5/types/tag_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# Currencies

Types:

```python
from emcees_prod_testing_5.types import CurrencyRead, CurrencySingle, CurrencyListResponse
```

Methods:

- <code title="post /v1/currencies">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/currency_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>
- <code title="get /v1/currencies/{code}">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">retrieve</a>(code) -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>
- <code title="put /v1/currencies/{code}">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">update</a>(path_code, \*\*<a href="src/emcees_prod_testing_5/types/currency_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>
- <code title="get /v1/currencies">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/currency_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/currency_list_response.py">CurrencyListResponse</a></code>
- <code title="delete /v1/currencies/{code}">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">delete</a>(code) -> None</code>
- <code title="post /v1/currencies/{code}/disable">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">disable</a>(code) -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>
- <code title="post /v1/currencies/{code}/enable">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">enable</a>(code) -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>
- <code title="get /v1/currencies/{code}/accounts">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_accounts</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_accounts_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/account_array.py">AccountArray</a></code>
- <code title="get /v1/currencies/{code}/available-budgets">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_available_budgets</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_available_budgets_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/available_budget_array.py">AvailableBudgetArray</a></code>
- <code title="get /v1/currencies/{code}/bills">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_bills</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_bills_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/bill_array.py">BillArray</a></code>
- <code title="get /v1/currencies/{code}/budget-limits">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_budget_limits</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_budget_limits_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/budgets/budget_limit_array.py">BudgetLimitArray</a></code>
- <code title="get /v1/currencies/{code}/recurrences">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_recurrences</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_recurrences_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/recurrence_array.py">RecurrenceArray</a></code>
- <code title="get /v1/currencies/{code}/rules">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_rules</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_rules_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/rule_array.py">RuleArray</a></code>
- <code title="get /v1/currencies/{code}/transactions">client.currencies.<a href="./src/emcees_prod_testing_5/resources/currencies/currencies.py">list_transactions</a>(code, \*\*<a href="src/emcees_prod_testing_5/types/currency_list_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

## Primary

Methods:

- <code title="get /v1/currencies/primary">client.currencies.primary.<a href="./src/emcees_prod_testing_5/resources/currencies/primary.py">retrieve</a>() -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>
- <code title="post /v1/currencies/{code}/primary">client.currencies.primary.<a href="./src/emcees_prod_testing_5/resources/currencies/primary.py">make_primary</a>(code) -> <a href="./src/emcees_prod_testing_5/types/currency_single.py">CurrencySingle</a></code>

# TransactionJournals

Types:

```python
from emcees_prod_testing_5.types import TransactionRead, TransactionSingle
```

Methods:

- <code title="get /v1/transaction-journals/{id}">client.transaction_journals.<a href="./src/emcees_prod_testing_5/resources/transaction_journals.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/transaction_single.py">TransactionSingle</a></code>
- <code title="delete /v1/transaction-journals/{id}">client.transaction_journals.<a href="./src/emcees_prod_testing_5/resources/transaction_journals.py">delete</a>(id) -> None</code>
- <code title="get /v1/transaction-journals/{id}/links">client.transaction_journals.<a href="./src/emcees_prod_testing_5/resources/transaction_journals.py">list_links</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/transaction_journal_list_links_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_link_array.py">TransactionLinkArray</a></code>

# Transactions

Types:

```python
from emcees_prod_testing_5.types import TransactionTypeProperty
```

Methods:

- <code title="post /v1/transactions">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/transaction_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_single.py">TransactionSingle</a></code>
- <code title="get /v1/transactions/{id}">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/transaction_single.py">TransactionSingle</a></code>
- <code title="put /v1/transactions/{id}">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/transaction_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_single.py">TransactionSingle</a></code>
- <code title="get /v1/transactions">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/transaction_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>
- <code title="delete /v1/transactions/{id}">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">delete</a>(id) -> None</code>
- <code title="get /v1/transactions/{id}/attachments">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">list_attachments</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/transaction_list_attachments_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/attachment_array.py">AttachmentArray</a></code>
- <code title="get /v1/transactions/{id}/piggy-bank-events">client.transactions.<a href="./src/emcees_prod_testing_5/resources/transactions.py">list_piggy_bank_events</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/transaction_list_piggy_bank_events_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/piggy_bank_event_array.py">PiggyBankEventArray</a></code>

# UserGroups

Types:

```python
from emcees_prod_testing_5.types import UserGroupRead, UserGroupSingle, UserGroupListResponse
```

Methods:

- <code title="get /v1/user-groups/{id}">client.user_groups.<a href="./src/emcees_prod_testing_5/resources/user_groups.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/user_group_single.py">UserGroupSingle</a></code>
- <code title="put /v1/user-groups/{id}">client.user_groups.<a href="./src/emcees_prod_testing_5/resources/user_groups.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/user_group_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/user_group_single.py">UserGroupSingle</a></code>
- <code title="get /v1/user-groups">client.user_groups.<a href="./src/emcees_prod_testing_5/resources/user_groups.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/user_group_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/user_group_list_response.py">UserGroupListResponse</a></code>

# Search

Methods:

- <code title="get /v1/search/accounts">client.search.<a href="./src/emcees_prod_testing_5/resources/search.py">accounts</a>(\*\*<a href="src/emcees_prod_testing_5/types/search_accounts_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/account_array.py">AccountArray</a></code>
- <code title="get /v1/search/transactions">client.search.<a href="./src/emcees_prod_testing_5/resources/search.py">transactions</a>(\*\*<a href="src/emcees_prod_testing_5/types/search_transactions_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/transaction_array.py">TransactionArray</a></code>

# Summary

Types:

```python
from emcees_prod_testing_5.types import SummaryRetrieveBasicResponse
```

Methods:

- <code title="get /v1/summary/basic">client.summary.<a href="./src/emcees_prod_testing_5/resources/summary.py">retrieve_basic</a>(\*\*<a href="src/emcees_prod_testing_5/types/summary_retrieve_basic_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/summary_retrieve_basic_response.py">SummaryRetrieveBasicResponse</a></code>

# About

Types:

```python
from emcees_prod_testing_5.types import UserRead, UserSingle, AboutRetrieveInfoResponse
```

Methods:

- <code title="get /v1/about">client.about.<a href="./src/emcees_prod_testing_5/resources/about.py">retrieve_info</a>() -> <a href="./src/emcees_prod_testing_5/types/about_retrieve_info_response.py">AboutRetrieveInfoResponse</a></code>
- <code title="get /v1/about/user">client.about.<a href="./src/emcees_prod_testing_5/resources/about.py">retrieve_user</a>() -> <a href="./src/emcees_prod_testing_5/types/user_single.py">UserSingle</a></code>

# Batch

Methods:

- <code title="post /v1/batch/finish">client.batch.<a href="./src/emcees_prod_testing_5/resources/batch.py">finish</a>() -> None</code>

# Configuration

Types:

```python
from emcees_prod_testing_5.types import (
    ConfigValueFilter,
    Configuration,
    ConfigurationSingle,
    PolymorphicProperty,
    ConfigurationRetrieveResponse,
)
```

Methods:

- <code title="get /v1/configuration">client.configuration.<a href="./src/emcees_prod_testing_5/resources/configuration.py">retrieve</a>() -> <a href="./src/emcees_prod_testing_5/types/configuration_retrieve_response.py">ConfigurationRetrieveResponse</a></code>
- <code title="get /v1/configuration/{name}">client.configuration.<a href="./src/emcees_prod_testing_5/resources/configuration.py">retrieve_value</a>(name) -> <a href="./src/emcees_prod_testing_5/types/configuration_single.py">ConfigurationSingle</a></code>
- <code title="put /v1/configuration/{name}">client.configuration.<a href="./src/emcees_prod_testing_5/resources/configuration.py">update_value</a>(name, \*\*<a href="src/emcees_prod_testing_5/types/configuration_update_value_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/configuration_single.py">ConfigurationSingle</a></code>

# Cron

Types:

```python
from emcees_prod_testing_5.types import CronResultRow, CronRunResponse
```

Methods:

- <code title="get /v1/cron/{cliToken}">client.cron.<a href="./src/emcees_prod_testing_5/resources/cron.py">run</a>(cli_token, \*\*<a href="src/emcees_prod_testing_5/types/cron_run_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/cron_run_response.py">CronRunResponse</a></code>

# Users

Types:

```python
from emcees_prod_testing_5.types import User, UserListResponse
```

Methods:

- <code title="post /v1/users">client.users.<a href="./src/emcees_prod_testing_5/resources/users.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/user_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/user_single.py">UserSingle</a></code>
- <code title="get /v1/users/{id}">client.users.<a href="./src/emcees_prod_testing_5/resources/users.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/user_single.py">UserSingle</a></code>
- <code title="put /v1/users/{id}">client.users.<a href="./src/emcees_prod_testing_5/resources/users.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/user_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/user_single.py">UserSingle</a></code>
- <code title="get /v1/users">client.users.<a href="./src/emcees_prod_testing_5/resources/users.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/user_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /v1/users/{id}">client.users.<a href="./src/emcees_prod_testing_5/resources/users.py">delete</a>(id) -> None</code>

# Preferences

Types:

```python
from emcees_prod_testing_5.types import (
    Preference,
    PreferenceRead,
    PreferenceSingle,
    PreferenceListResponse,
)
```

Methods:

- <code title="post /v1/preferences">client.preferences.<a href="./src/emcees_prod_testing_5/resources/preferences.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/preference_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/preference_single.py">PreferenceSingle</a></code>
- <code title="get /v1/preferences/{name}">client.preferences.<a href="./src/emcees_prod_testing_5/resources/preferences.py">retrieve</a>(name) -> <a href="./src/emcees_prod_testing_5/types/preference_single.py">PreferenceSingle</a></code>
- <code title="put /v1/preferences/{name}">client.preferences.<a href="./src/emcees_prod_testing_5/resources/preferences.py">update</a>(name, \*\*<a href="src/emcees_prod_testing_5/types/preference_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/preference_single.py">PreferenceSingle</a></code>
- <code title="get /v1/preferences">client.preferences.<a href="./src/emcees_prod_testing_5/resources/preferences.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/preference_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/preference_list_response.py">PreferenceListResponse</a></code>

# Webhooks

Types:

```python
from emcees_prod_testing_5.types import (
    Webhook,
    WebhookDelivery,
    WebhookResponse,
    WebhookSingle,
    WebhookTrigger,
    WebhookListResponse,
)
```

Methods:

- <code title="post /v1/webhooks">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/emcees_prod_testing_5/types/webhook_create_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/webhook_single.py">WebhookSingle</a></code>
- <code title="get /v1/webhooks/{id}">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">retrieve</a>(id) -> <a href="./src/emcees_prod_testing_5/types/webhook_single.py">WebhookSingle</a></code>
- <code title="put /v1/webhooks/{id}">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">update</a>(id, \*\*<a href="src/emcees_prod_testing_5/types/webhook_update_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/webhook_single.py">WebhookSingle</a></code>
- <code title="get /v1/webhooks">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">list</a>(\*\*<a href="src/emcees_prod_testing_5/types/webhook_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v1/webhooks/{id}">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">delete</a>(id) -> None</code>
- <code title="post /v1/webhooks/{id}/submit">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">submit</a>(id) -> None</code>
- <code title="post /v1/webhooks/{id}/trigger-transaction/{transactionId}">client.webhooks.<a href="./src/emcees_prod_testing_5/resources/webhooks/webhooks.py">trigger_transaction</a>(transaction_id, \*, id) -> None</code>

## Messages

Types:

```python
from emcees_prod_testing_5.types.webhooks import (
    WebhookMessage,
    MessageRetrieveResponse,
    MessageListResponse,
)
```

Methods:

- <code title="get /v1/webhooks/{id}/messages/{messageId}">client.webhooks.messages.<a href="./src/emcees_prod_testing_5/resources/webhooks/messages/messages.py">retrieve</a>(message_id, \*, id) -> <a href="./src/emcees_prod_testing_5/types/webhooks/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /v1/webhooks/{id}/messages">client.webhooks.messages.<a href="./src/emcees_prod_testing_5/resources/webhooks/messages/messages.py">list</a>(id) -> <a href="./src/emcees_prod_testing_5/types/webhooks/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /v1/webhooks/{id}/messages/{messageId}">client.webhooks.messages.<a href="./src/emcees_prod_testing_5/resources/webhooks/messages/messages.py">delete</a>(message_id, \*, id) -> None</code>

### Attempts

Types:

```python
from emcees_prod_testing_5.types.webhooks.messages import (
    WebhookAttempt,
    AttemptRetrieveResponse,
    AttemptListResponse,
)
```

Methods:

- <code title="get /v1/webhooks/{id}/messages/{messageId}/attempts/{attemptId}">client.webhooks.messages.attempts.<a href="./src/emcees_prod_testing_5/resources/webhooks/messages/attempts.py">retrieve</a>(attempt_id, \*, id, message_id) -> <a href="./src/emcees_prod_testing_5/types/webhooks/messages/attempt_retrieve_response.py">AttemptRetrieveResponse</a></code>
- <code title="get /v1/webhooks/{id}/messages/{messageId}/attempts">client.webhooks.messages.attempts.<a href="./src/emcees_prod_testing_5/resources/webhooks/messages/attempts.py">list</a>(message_id, \*, id, \*\*<a href="src/emcees_prod_testing_5/types/webhooks/messages/attempt_list_params.py">params</a>) -> <a href="./src/emcees_prod_testing_5/types/webhooks/messages/attempt_list_response.py">AttemptListResponse</a></code>
- <code title="delete /v1/webhooks/{id}/messages/{messageId}/attempts/{attemptId}">client.webhooks.messages.attempts.<a href="./src/emcees_prod_testing_5/resources/webhooks/messages/attempts.py">delete</a>(attempt_id, \*, id, message_id) -> None</code>
