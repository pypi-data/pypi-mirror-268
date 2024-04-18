import copy
import torch
import logging
from random import randint

from diffusers import (
    DiffusionPipeline,
    AutoencoderKL,
    UNet2DConditionModel
)

from .types import (
    PIPELINE_MAP,
    SCHEDULER_MAP,
    WonderPipelineType,
    WonderSchedulerType)

from .config import (
    DEVICE,
    WonderDiffusionSdkConfig,
    WonderDiffusionModelConfig,
    WonderLora,
    WonderLoraConfig)

from .components import (
    setup_logger,
    enable_lightning
)


class WonderDiffusionSdk:

    def __init__(self, config: WonderDiffusionSdkConfig, logger: logging.Logger = None):
        self.logger = logger if logger else setup_logger()

        self.logger.info(
            'DIFFUSION SDK LOG: Initializing Wonder Diffusion SDK')

        if config.enable_custom_safety_checker:
            self.initialize_safety_checker()

    def initialize_pipeline(self, model_config: WonderDiffusionModelConfig):
        # get precision related args
        args = self.get_precision_args(model_config.precision)
        model_config.kwargs.update(args)

        self.logger.info(
            f'DIFFUSION SDK LOG: Initializing pipeline with kwargs: {model_config.kwargs}')

        # initialize pipeline
        self.pipeline = PIPELINE_MAP[model_config.pipeline_type](
            model_config.pretrained_model_name_or_path, **model_config.kwargs)

        self.pipeline.scheduler = SCHEDULER_MAP[model_config.initial_scheduler](
            self.pipeline.scheduler.config)

        self.pipeline.to(DEVICE)

        # apply optimizations based on model config
        if model_config.use_half_precision_vae:
            self.half_precision_vae(self.pipeline, model_config.precision)

        if model_config.fuse_qkv_projections:
            self.fuse_qkv_projections(self.pipeline)

        if model_config.use_channels_last:
            self.use_channels_last(self.pipeline)

        if model_config.use_deep_cache:
            self.enable_deepcache(self.pipeline)

        if model_config.use_lightning_model:
            self.enable_lightning_model(
                self.pipeline, model_config.lightning_model_step_count)

        return self.pipeline

    def get_precision_args(self, precision):
        args = {}
        if precision == 'bfloat16':
            args['torch_dtype'] = torch.bfloat16
        elif precision == 'float16':
            args['torch_dtype'] = torch.float16
            args['variant'] = 'fp16'
            args['use_safetensors'] = True
        return args

    def half_precision_vae(self, pipeline: DiffusionPipeline, precision: str):
        self.logger.info('DIFFUSION SDK LOG: Using half precision VAE')
        dtype = torch.bfloat16 if precision == 'bfloat16' else torch.float16
        try:
            pipeline.vae = AutoencoderKL.from_pretrained(
                'madebyollin/sdxl-vae-fp16-fix', torch_dtype=dtype).to(DEVICE)
        except Exception as e:
            self.logger.error(
                f'Failed to load half precision VAE model: {e}')

    def fuse_qkv_projections(self, pipeline: DiffusionPipeline):
        self.logger.info('DIFFUSION SDK LOG: Fusing QKV projections')
        try:
            pipeline.unet.fuse_qkv_projections()
            pipeline.vae.fuse_qkv_projections()
        except Exception as e:
            self.logger.error(
                f'Failed to fuse QKV projections: {e}')

    def use_channels_last(self, pipeline: DiffusionPipeline):
        self.logger.info('DIFFUSION SDK LOG: Using channels last')
        try:
            pipeline.unet.to(memory_format=torch.channels_last)
        except Exception as e:
            self.logger.error(
                f'Failed to use channels last: {e}')

    def enable_deepcache(self, pipeline: DiffusionPipeline):
        self.logger.info('DIFFUSION SDK LOG: Enabling deep cache')
        try:
            from .components import enable_deepcache
            self.deepcache_helper = enable_deepcache(pipeline)
        except Exception as e:
            self.logger.error(
                f'Failed to enable deep cache: {e}')

    def disable_deepcache(self):
        if hasattr(self, 'deepcache_helper'):
            self.logger.info('DIFFUSION SDK LOG: Disabling deep cache')
            self.deepcache_helper.disable()

    def enable_lightning_model(self, pipeline=None, step_count=4):
        curr_pipeline = None
        if pipeline != None:
            curr_pipeline = pipeline
        else:
            if hasattr(self, 'pipeline'):
                curr_pipeline = self.pipeline

        if curr_pipeline != None:
            self.logger.info('DIFFUSION SDK LOG: Enabling lightning model')
            enable_lightning(curr_pipeline, step_count)
            self.logger.info(
                f'DIFFUSION SDK LOG: Pipeline scheduler timestep_spacing: {curr_pipeline.scheduler.config.timestep_spacing}')
            self.logger.info(
                f'DIFFUSION SDK LOG: Pipeline scheduler prediction_type: {curr_pipeline.scheduler.config.prediction_type}')

    # Diffusion functions

    def set_scheduler(self, scheduler: WonderSchedulerType, pipeline: DiffusionPipeline = None):
        _pipeline = None
        if pipeline != None:
            _pipeline = pipeline
        elif hasattr(self, 'pipeline'):
            _pipeline = self.pipeline

        if _pipeline != None and scheduler in SCHEDULER_MAP:
            _pipeline.scheduler = SCHEDULER_MAP[scheduler](
                _pipeline.scheduler.config)

    def run(self, args: dict):
        args['generator'], seed = self.generate_seed(args.get('seed', None))
        self.logger.info(f'DIFFUSION SDK LOG: Seed {seed}')

        return self.pipeline(**args).images, seed

    def generate_seed(self, seed=None):
        if seed == None or seed < 0:
            seed = randint(0, 2**32-1)
        return torch.Generator(device=DEVICE).manual_seed(seed), seed

    # Safety checker

    def initialize_safety_checker(self):
        from transformers import AutoFeatureExtractor
        from .components import StableDiffusionSafetyChecker
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(
            'CompVis/stable-diffusion-safety-checker')
        self.safety_checker = StableDiffusionSafetyChecker.from_pretrained(
            'CompVis/stable-diffusion-safety-checker').to(DEVICE)

    def safety_check(self, images):
        if not hasattr(self, 'safety_checker'):
            self.initialize_safety_checker()

        safety_checker_input = self.feature_extractor(
            images, return_tensors='pt').to(DEVICE)
        images, has_nsfw_concept = self.safety_checker(
            images=images, clip_input=safety_checker_input.pixel_values.to(torch.float16))
        return images, has_nsfw_concept

    # Lora

    def initialize_loras(self, config: WonderLoraConfig, pipeline: DiffusionPipeline = None):
        _pipeline = None
        if pipeline != None:
            _pipeline = pipeline
        elif hasattr(self, 'pipeline'):
            _pipeline = self.pipeline

        # Single Lora
        if len(config.loras) == 1:
            _pipeline.load_lora_weights(
                lora.path, weight_name=config.loras[0].weight_name)
        # Multiple Loras
        else:
            if config.use_peft:
                self.load_loras_with_peft(_pipeline, config)
            else:
                adapters = []
                adapter_weights = []
                for lora in config.loras:
                    _pipeline.load_lora_weights(
                        lora.path, weight_name=lora.weight_name, adapter_name=lora.adapter)
                    adapters.append(lora.adapter)
                    adapter_weights.append(lora.adapter_weight)
                _pipeline.set_adapters(
                    adapters, adapter_weights=adapter_weights)

    def load_loras_with_peft(self, pipeline: DiffusionPipeline, config: WonderLoraConfig):
        try:
            from peft import get_peft_model, PeftModel
        except Exception as e:
            self.logger.error(
                f'Failed to import peft: {e}')
            return

        peft_models = []
        adapters = []
        adapter_weights = []
        for lora in config.loras:
            # Load the lora's base unet model
            unet = UNet2DConditionModel.from_pretrained(
                lora.base_model_name_or_path,
                torch_dtype=torch.float16,
                use_safetensors=True,
                variant="fp16",
                subfolder="unet",
            ).to(DEVICE)

            # Load a temporary pipeline to load the lora weights
            temp_pipeline = DiffusionPipeline.from_pretrained(
                lora.base_model_name_or_path,
                torch_dtype=torch.float16,
                variant="fp16",
                unet=unet
            ).to(DEVICE)

            temp_pipeline.load_lora_weights(
                lora.path, weight_name=lora.weight_name, adapter_name=lora.adapter)
            temp_pipeline.set_adapters(adapter_names=lora.adapter)

            adapters.append(lora.adapter)
            adapter_weights.append(lora.adapter_weight)

            unet_copy = copy.deepcopy(unet)
            peft_model = get_peft_model(
                unet_copy,
                temp_pipeline.unet.peft_config[lora.adapter],
                adapter_name=lora.adapter
            )

            original_state_dict = {f"base_model.model.{k}": v for k,
                                   v in temp_pipeline.unet.state_dict().items()}
            peft_model.load_state_dict(original_state_dict, strict=True)
            peft_model.save_pretrained(f'peft_models/{lora.adapter}')

            peft_models.append(peft_model)

            del unet, unet_copy, temp_pipeline, peft_model
            torch.cuda.empty_cache()

        model = PeftModel.from_pretrained(
            pipeline.unet, f'peft_models/{adapters[0]}', adapter_name=adapters[0], subfolder=adapters[0], use_safetensors=True)
        for i in range(1, len(adapters)):
            model.load_adapter(
                f'peft_models/{adapters[i]}', adapter_name=adapters[i], subfolder=adapters[i], use_safetensors=True)

        combined_adapter = adapters[0]
        for i in range(1, len(adapters)):
            combined_adapter += f'_{adapters[i]}'

        model.add_weighted_adapter(
            adapters=adapters,
            weights=adapter_weights,
            combination_type="dare_linear",
            adapter_name=combined_adapter
        )
        model.set_adapters(combined_adapter)

        pipeline.unet = model
