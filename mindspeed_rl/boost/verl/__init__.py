from mindspeed_rl.boost.verl.workers.rollout.vllm_rollout.vllm_rollout_spmd import patch_vllm_rollout_spmd
from mindspeed_rl.boost.verl.models.mcore.registry import patch_mcore_registry


def adpat_verl_to_ascend():
    from mindspeed import megatron_adaptor  # noqa: F401

    patch_mcore_registry()
    patch_vllm_rollout_spmd()


adpat_verl_to_ascend()
