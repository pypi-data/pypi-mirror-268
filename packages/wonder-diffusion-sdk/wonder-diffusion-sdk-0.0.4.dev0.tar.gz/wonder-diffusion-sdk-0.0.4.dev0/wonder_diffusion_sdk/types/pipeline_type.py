from enum import Enum


class WonderPipelineType(Enum):
    STABLE_DIFFUSION = 'stable_diffusion'
    STABLE_DIFFUSION_IMG2IMG = 'stable_diffusion_img2img'
    STABLE_DIFFUSION_INPAINT = 'stable_diffusion_inpaint'
    STABLE_DIFFUSION_XL = 'stable_diffusion_xl'
    STABLE_DIFFUSION_XL_IMG2IMG = 'stable_diffusion_xl_img2img'
    STABLE_DIFFUSION_XL_INPAINT = 'stable_diffusion_xl_inpaint'

    def is_sdxl(self):
        return 'stable_diffusion_xl' in self.value
