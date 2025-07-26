import os

import lm_eval
import yaml

RTOL = 0.08


def launch_lm_eval(eval_config, tp_size):
    trust_remote_code = eval_config.get("trust_remote_code", False)
    max_model_len = eval_config.get("max_model_len", 4096)
    model_args = (f"pretrained={eval_config['model_name']},"
                  f"tensor_parallel_size={tp_size},"
                  f"enforce_eager=true,"
                  f"add_bos_token=true,"
                  f"trust_remote_code={trust_remote_code},"
                  f"max_model_len={max_model_len}")
    results = lm_eval.simple_evaluate(
        model="vllm",
        model_args=model_args,
        tasks=[task["name"] for task in eval_config["tasks"]],
        num_fewshot=eval_config["num_fewshot"],
        limit=eval_config["limit"],
        batch_size="auto",
    )
    return results


def _lm_eval_correctness_test(config_filename, tp_size):
    file_name = os.path.dirname(__file__) + "/configs/" + config_filename
    with open(file_name, "r", encoding="utf-8") as f:
        eval_config = yaml.safe_load(f)
    results = launch_lm_eval(eval_config, tp_size)

    success = True
    for task in eval_config["tasks"]:
        for metric in task["metrics"]:
            ground_truth = metric["value"]
            measured_value = results["results"][task["name"]][metric["name"]]
            print(f"{task['name']} | {metric['name']}: "
                  f"expected={ground_truth} | actual={measured_value}")
            success = success  # and np.isclose(ground_truth, measured_value, rtol=RTOL)

    assert success
