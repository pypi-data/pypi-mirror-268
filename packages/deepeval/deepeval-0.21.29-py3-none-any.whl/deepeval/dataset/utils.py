from typing import List, Optional
from deepeval.dataset.api import Golden, ConversationalGolden
from deepeval.test_case import LLMTestCase, ConversationalTestCase


def convert_test_cases_to_goldens(
    test_cases: List[LLMTestCase],
) -> List[Golden]:
    goldens = []
    for test_case in test_cases:
        golden = {
            "input": test_case.input,
            "actualOutput": test_case.actual_output,
            "expectedOutput": test_case.expected_output,
            "context": test_case.context,
        }
        goldens.append(Golden(**golden))
    return goldens


def convert_goldens_to_test_cases(
    goldens: List[Golden], dataset_alias: Optional[str] = None
) -> List[LLMTestCase]:
    test_cases = []
    for golden in goldens:
        test_case = LLMTestCase(
            input=golden.input,
            actual_output=golden.actual_output,
            expected_output=golden.expected_output,
            context=golden.context,
            retrieval_context=golden.retrieval_context,
            dataset_alias=dataset_alias,
        )
        test_cases.append(test_case)
    return test_cases


def convert_convo_goldens_to_convo_test_cases(
    convo_goldens: List[ConversationalGolden],
    dataset_alias: Optional[str] = None,
) -> List[ConversationalTestCase]:
    conv_test_cases = []
    for convo_golden in convo_goldens:
        conv_test_case = ConversationalTestCase(
            dataset_alias=dataset_alias,
            messages=convert_goldens_to_test_cases(convo_golden.messages),
        )
        conv_test_cases.append(conv_test_case)
    return conv_test_cases
