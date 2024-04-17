from ..config import DEVICE
from ..types import WonderSchedulerType, SCHEDULER_MAP


checkpoints = {
    1: ["sdxl_lightning_1step_unet_x0.safetensors", 1],
    2: ["sdxl_lightning_2step_unet.safetensors", 2],
    4: ["sdxl_lightning_4step_unet.safetensors", 4],
    8: ["sdxl_lightning_8step_unet.safetensors", 8],
}


def enable_lightning(pipeline, step_count=4):
    try:
        from safetensors.torch import load_file
        from huggingface_hub import hf_hub_download
    except Exception as e:
        print(f'Import failed in enable_lightning: {e}')

    pipeline.scheduler = SCHEDULER_MAP[WonderSchedulerType.EULER_DISCRETE](
        pipeline.scheduler.config, timestep_spacing="trailing", prediction_type="epsilon")

    repo = "ByteDance/SDXL-Lightning"
    checkpoint = checkpoints[step_count][0]
    pipeline.unet.load_state_dict(
        load_file(hf_hub_download(repo, checkpoint), device=DEVICE))
