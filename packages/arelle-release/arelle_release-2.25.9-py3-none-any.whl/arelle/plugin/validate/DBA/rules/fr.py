"""
See COPYRIGHT.md for copyright information.
"""
from __future__ import annotations

import datetime
import itertools
from typing import Any, Iterable, cast

from arelle.typing import TypeGetText
from arelle.ValidateXbrl import ValidateXbrl

from arelle.utils.PluginHooks import ValidationHook
from arelle.utils.validate.Decorator import validation
from arelle.utils.validate.Validation import Validation
from . import errorOnDateFactComparison
from ..PluginValidationDataExtension import PluginValidationDataExtension


_: TypeGetText


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr4(
    pluginData: PluginValidationDataExtension,
    val: ValidateXbrl,
    *args: Any,
    **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR4: The end date of the accounting period (gsd:ReportingPeriodEndDate with
    default TypeOfReportingPeriodDimension) must not be before the start date of the
    accounting period (gsd:ReportingPeriodStartDate with default TypeOfReportingPeriodDimension)
    """
    return errorOnDateFactComparison(
        val.modelXbrl,
        fact1Qn=pluginData.reportingPeriodStartDateQn,
        fact2Qn=pluginData.reportingPeriodEndDateQn,
        dimensionQn=pluginData.typeOfReportingPeriodDimensionQn,
        code='DBA.FR4',
        message=_("Error code FR4: Accounting period end date='%(fact2)s' "
                  "must not be before Accounting period start date='%(fact1)s'"),
        assertion=lambda startDate, endDate: startDate <= endDate,
    )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr5(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR5: General meeting date (gsd:DateOfGeneralMeeting) must not be before the
    end date of the accounting period (gsd:ReportingPeriodEndDate with default
    TypeOfReportingPeriodDimension)
    """
    return errorOnDateFactComparison(
        val.modelXbrl,
        fact1Qn=pluginData.reportingPeriodEndDateQn,
        fact2Qn=pluginData.dateOfGeneralMeetingQn,
        dimensionQn=pluginData.typeOfReportingPeriodDimensionQn,
        code='DBA.FR5',
        message=_("Error code FR5: General meeting date='%(fact2)s' "
                  "must be after Accounting period end date='%(fact1)s'"),
        assertion=lambda endDate, meetingDate: endDate < meetingDate,
    )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr7(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR7: Date of approval of the annual report (gsd:DateOfApprovalOfAnnualReport)
    must be after the end date of the Accounting Period (gsd:ReportingPeriodEndDate
    with default TypeOfReportingPeriodDimension).
    """
    return errorOnDateFactComparison(
        val.modelXbrl,
        fact1Qn=pluginData.reportingPeriodEndDateQn,
        fact2Qn=pluginData.dateOfApprovalOfAnnualReportQn,
        dimensionQn=pluginData.typeOfReportingPeriodDimensionQn,
        code='DBA.FR7',
        message=_("Error code FR7: Date of approval of the annual report='%(fact2)s' "
                  "must be after the end date of the accounting period='%(fact1)s'"),
        assertion=lambda endDate, approvalDate: endDate < approvalDate,
    )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr9(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR9: The year's result (fsa:ProfitLoss) must be filled in as part of the income statement.
    The control only looks at instances without dimensions or instances that only have the dimension
    (ConsolidatedSoloDimension with ConsolidatedMember).

    Implementation: Find any occurrence of fsa:ProfitLoss with no dimensions or with dimensions of
    ConsolidatedSoloDimension with ConsolidatedMember.  If nothing is found, trigger an error.
    """
    profLossFacts = val.modelXbrl.factsByQname.get(pluginData.profitLossQn)
    found = False
    if profLossFacts:
        for fact in profLossFacts:
            if fact.context is None:
                continue
            elif (fact.context.dimMemberQname(pluginData.consolidatedSoloDimensionQn) == pluginData.consolidatedMemberQn
                  and fact.context.qnameDims.keys() == {pluginData.consolidatedSoloDimensionQn}):
                found = True
            elif not len(fact.context.qnameDims):
                found = True
    if not found:
        yield Validation.error(
            codes="DBA.FR9",
            msg=_("Error code FR9: The year's result in the income statement must be filled in."),
            modelObject=val.modelXbrl.modelDocument
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr39(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR39: Date of extraordinary dividend (fsb:DateOfExtraordinaryDividendDistributedAfterEndOfReportingPeriod)
    must be after the end of the financial year (gsd:ReportingPeriodEndDate) (with default
    TypeOfReportingPeriodDimension)
    """
    return errorOnDateFactComparison(
        val.modelXbrl,
        fact1Qn=pluginData.reportingPeriodEndDateQn,
        fact2Qn=pluginData.dateOfExtraordinaryDividendDistributedAfterEndOfReportingPeriod,
        dimensionQn=pluginData.typeOfReportingPeriodDimensionQn,
        code='DBA.FR39',
        message=_("Error code FR39: A date for extraordinary dividend '%(fact2)s' "
                  "has been specified. The date must be after the end of the financial year '%(fact1)s'."),
        assertion=lambda endDate, dividendDate: endDate < dividendDate,
    )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr41(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR41: Failure to fill in 'Tax on profit for the year' or 'Tax on ordinary profit'

    If the result for the year is positive(fsa:ProfitLoss) (defined as greater than DKK 1000),
    either Tax on the year's result (fsa:TaxExpense) or Tax on ordinary result
    (fsa:TaxExpenseOnOrdinaryActivities) must be filled in.

    The control does not look at I/S (partnership), K/S (limited partnership) and P/S
    (partner company, like an LLC). (based on what legal form the identification number is
    registered as in the business register).

    Implementation: For each reporting period context that has a fsa:ProfitLoss fact above
    the threshold, check if there is either a non-nil fsa:TaxExpense or fsa:TaxExpenseOnOrdinaryActivities
    fact in the same context. If not, trigger an error.
    """

    # TODO: There appears to be criteria that exempt some filings from this rule.
    # The criteria is based on the legal form of the company, which may or may not be
    # something we can determine from the identification number and/or other instance data.
    # Once we determine if/how that criteria can be implemented, we can add it here.

    modelXbrl = val.modelXbrl
    contextIds = {c.id for c in pluginData.getCurrentAndPreviousReportingPeriodContexts(modelXbrl)}
    contextMap = {k: v for k, v in pluginData.contextFactMap(modelXbrl).items() if k in contextIds}
    for contextId, factMap in contextMap.items():
        profitLossFact = factMap.get(pluginData.profitLossQn)
        if profitLossFact is None:
            continue
        if cast(float, profitLossFact.xValue) <= pluginData.positiveProfitThreshold:
            continue
        taxExpenseFact = factMap.get(pluginData.taxExpenseQn)
        if taxExpenseFact is not None and not taxExpenseFact.isNil:
            continue
        taxExpenseOnOrdinaryActivitiesFact = factMap.get(pluginData.taxExpenseOnOrdinaryActivitiesQn)
        if taxExpenseOnOrdinaryActivitiesFact is not None and not taxExpenseOnOrdinaryActivitiesFact.isNil:
            continue
        yield Validation.warning(
            codes='DBA.FR41',
            msg=_("ADVICE FR41: The annual report does not contain information on tax "
                  "on the year's profit. If the profit for the year in the income "
                  "statement is positive, either 'Tax on profit for the year' or "
                  "'Tax on ordinary profit' must be filled in."),
            modelObject=profitLossFact,
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr48(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR48: Annual reports with a start date of 1/1 2016 or later may not use the fields:
    'Extraordinary result before tax',
    'Extraordinary income',
    'Extraordinary costs',
    as §30 of the Annual Accounts Act is repealed."
    """
    disallowedFactQnames = [pluginData.extraordinaryCostsQn, pluginData.extraordinaryIncomeQn, pluginData.extraordinaryResultBeforeTaxQn]
    foundFacts = []
    for factQname in disallowedFactQnames:
        facts = val.modelXbrl.factsByQname.get(factQname)
        if facts:
            foundFacts.append(facts)
    if len(foundFacts) > 0:
        yield Validation.warning(
            codes="DBA.FR48",
            msg=_("ADVICE FR48: Annual reports with a start date of 1/1 2016 or later must not use the fields:"
                  "'Extraordinary profit before tax', 'Extraordinary income', 'Extraordinary costs'."),
            modelObject=foundFacts
    )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_fr55(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation] | None:
    """
    DBA.FR55: If a period with an end date immediately before the currently selected start
    date (gsd:ReportingPeriodStartDate) has previously been reported, the previous accounting
    period should be marked (gsd:PrecedingReportingPeriodStartDate and gsd:PredingReportingPeriodEndDate).

    Note: "PredingReportingPeriodEndDate" is a typo in the taxonomy.
    """
    reportingPeriods = {}
    for contextId, factMap in pluginData.contextFactMap(val.modelXbrl).items():
        reportTypeFact = factMap.get(pluginData.informationOnTypeOfSubmittedReportQn)
        if reportTypeFact is None or str(reportTypeFact.xValue) not in pluginData.annualReportTypes:
            continue  # Non-annual reports are not considered
        # Structure the above facts into tuples
        reportingPeriods[contextId] = (
            factMap.get(pluginData.reportingPeriodStartDateQn),
            factMap.get(pluginData.reportingPeriodEndDateQn),
            factMap.get(pluginData.precedingReportingPeriodStartDateQn),
            factMap.get(pluginData.precedingReportingPeriodEndDateQn),
        )

    for previousContextId, currentContextId in itertools.permutations(reportingPeriods.keys(), 2):
        previousStartDateFact, previousEndDateFact, __, __ = reportingPeriods[previousContextId]
        currentStartDateFact, currentEndDateFact, precedingStartDateFact, precedingEndDateFact = reportingPeriods[currentContextId]

        # Exit if reporting periods are not sequential
        if previousEndDateFact is None or currentStartDateFact is None:
            continue
        previousEndDate = cast(datetime.datetime, previousEndDateFact.xValue)
        currentStartDate = cast(datetime.datetime, currentStartDateFact.xValue)
        if previousEndDate > currentStartDate:
            continue  # End date not before or equal to start date
        if previousEndDate.date() < currentStartDate.date() - datetime.timedelta(days=1):
            continue  # End date not "immediately" before start date

        # These contexts are sequential
        precedingStartDate = cast(datetime.datetime, precedingStartDateFact.xValue) if precedingStartDateFact is not None else None
        previousStartDate = cast(datetime.datetime, previousStartDateFact.xValue) if previousStartDateFact is not None else None
        precedingEndDate = cast(datetime.datetime, precedingEndDateFact.xValue) if precedingEndDateFact is not None else None
        previousEndDate = cast(datetime.datetime, previousEndDateFact.xValue) if previousEndDateFact is not None else None

        if precedingStartDate != previousStartDate or precedingEndDate != previousEndDate:
            yield Validation.warning(
                codes='DBA.FR55',
                msg=_("ADVICE FR55: The annual report does not contain an indication of the previous accounting period. "
                      "If an annual report with a period with an end date immediately before the currently selected "
                      "start date has previously been reported, the previous accounting period should be indicated. "
                      "Previous period has been found [%(previousStartDate)s - %(previousEndDate)s]"),
                modelObject=(previousStartDateFact, previousEndDateFact, precedingStartDateFact, precedingEndDateFact, currentStartDateFact),
                previousStartDate=previousStartDate,
                previousEndDate=previousEndDate,
            )
