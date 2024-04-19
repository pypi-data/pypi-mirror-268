from .scheduler_type import WonderSchedulerType

from diffusers import (
    DDIMScheduler,
    DDPMScheduler,
    DEISMultistepScheduler,
    DPMSolverMultistepScheduler,
    DPMSolverSinglestepScheduler,
    EulerAncestralDiscreteScheduler,
    EulerDiscreteScheduler,
    HeunDiscreteScheduler,
    KDPM2AncestralDiscreteScheduler,
    KDPM2DiscreteScheduler,
    LMSDiscreteScheduler,
    PNDMScheduler,
    UniPCMultistepScheduler)



SCHEDULER_MAP = {
    WonderSchedulerType.DDIM: lambda config, **kwargs: DDIMScheduler.from_config(config, **kwargs),
    WonderSchedulerType.DDPM: lambda config, **kwargs: DDPMScheduler.from_config(config, **kwargs),
    WonderSchedulerType.DEIS_MULTISTEP: lambda config, **kwargs: DEISMultistepScheduler.from_config(config, **kwargs),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP: lambda config, **kwargs: DPMSolverMultistepScheduler.from_config(config, **kwargs),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP_2M_KARRAS: lambda config, **kwargs: DPMSolverMultistepScheduler.from_config(config, use_karras_sigmas=True, **kwargs),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP_2M_SDE: lambda config, **kwargs: DPMSolverMultistepScheduler.from_config(config, algorithm_type='sde-dpmsolver++', **kwargs),
    WonderSchedulerType.DPM_SOLVER_MULTISTEP_2M_SDE_KARRAS: lambda config, **kwargs: DPMSolverMultistepScheduler.from_config(config, use_karras_sigmas=True, algorithm_type='sde-dpmsolver++', **kwargs),
    WonderSchedulerType.DPM_SOLVER_SINGLESTEP: lambda config, **kwargs: DPMSolverSinglestepScheduler.from_config(config, **kwargs),
    WonderSchedulerType.DPM_SOLVER_SINGLESTEP_KARRAS: lambda config, **kwargs: DPMSolverSinglestepScheduler.from_config(config, use_karras_sigmas=True, **kwargs),
    WonderSchedulerType.EULER_ANCESTRAL_DISCRETE: lambda config, **kwargs: EulerAncestralDiscreteScheduler.from_config(config, **kwargs),
    WonderSchedulerType.EULER_DISCRETE: lambda config, **kwargs: EulerDiscreteScheduler.from_config(config, **kwargs),
    WonderSchedulerType.HEUN_DISCRETE: lambda config, **kwargs: HeunDiscreteScheduler.from_config(config, **kwargs),
    WonderSchedulerType.KDPM2_ANCESTRAL_DISCRETE: lambda config, **kwargs: KDPM2AncestralDiscreteScheduler.from_config(config, **kwargs),
    WonderSchedulerType.KDPM2_ANCESTRAL_DISCRETE_KARRAS: lambda config, **kwargs: KDPM2AncestralDiscreteScheduler.from_config(config, use_karras_sigmas=True, **kwargs),
    WonderSchedulerType.KDPM2_DISCRETE: lambda config, **kwargs: KDPM2DiscreteScheduler.from_config(config, **kwargs),
    WonderSchedulerType.KDPM2_DISCRETE_KARRAS: lambda config, **kwargs: KDPM2DiscreteScheduler.from_config(config, use_karras_sigmas=True, **kwargs),
    WonderSchedulerType.LMS_DISCRETE: lambda config, **kwargs: LMSDiscreteScheduler.from_config(config, **kwargs),
    WonderSchedulerType.LMS_DISCRETE_KARRAS: lambda config, **kwargs: LMSDiscreteScheduler.from_config(config, use_karras_sigmas=True, **kwargs),
    WonderSchedulerType.PNDM: lambda config, **kwargs: PNDMScheduler.from_config(config, **kwargs),
    WonderSchedulerType.UNI_PC_MULTISTEP: lambda config, **kwargs: UniPCMultistepScheduler.from_config(config, **kwargs),
}
