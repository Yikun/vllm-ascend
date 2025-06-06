from vllm import ModelRegistry


def register_model():
    from .deepseek_mtp import CustomDeepSeekMTP  # noqa: F401
    from .deepseek_v2 import CustomDeepseekV2ForCausalLM  # noqa: F401
    from .deepseek_v2 import CustomDeepseekV3ForCausalLM  # noqa: F401
    from .qwen2_5_vl import \
        AscendQwen2_5_VLForConditionalGeneration  # noqa: F401
    from .qwen2_vl import AscendQwen2VLForConditionalGeneration  # noqa: F401

    ModelRegistry.register_model(
        "DeepSeekMTPModel",
        "vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP")

    ModelRegistry.register_model(
        "Qwen2VLForConditionalGeneration",
        "vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration")

    ModelRegistry.register_model(
        "Qwen2_5_VLForConditionalGeneration",
        "vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration"
    )

    ModelRegistry.register_model(
        "DeepseekV2ForCausalLM",
        "vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM")

    ModelRegistry.register_model(
        "DeepseekV3ForCausalLM",
        "vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM")

    ModelRegistry.register_model(
        "Qwen3MoeForCausalLM",
        "vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM")
