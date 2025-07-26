"""
LM eval harness on model to compare vs HF baseline computed offline.
Configs are found in configs/$MODEL.yaml

pytest -s -v test_lm_eval_correctness.py \
    --config-list-file=configs/models-small.txt \
    --tp-size=1
"""
from tests.e2e.singlecard.models.test_base import _lm_eval_correctness_test


def test_qwen():
    _lm_eval_correctness_test("Qwen/Qwen3-8B-Base.yaml", 1)
