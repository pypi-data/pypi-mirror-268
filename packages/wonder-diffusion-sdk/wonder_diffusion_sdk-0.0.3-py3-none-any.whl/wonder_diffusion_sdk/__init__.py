import torch
import logging
from random import randint

from diffusers import DiffusionPipeline, AutoencoderKL

from .types import (
    PIPELINE_MAP,
    SCHEDULER_MAP,
    WonderPipelineType,
    WonderSchedulerType)

from .config import (
    DEVICE,
    WonderDiffusionSdkConfig,
    WonderDiffusionModelConfig)

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
            self.enable_lightning_model(self.pipeline, model_config.lightning_model_step_count)

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
