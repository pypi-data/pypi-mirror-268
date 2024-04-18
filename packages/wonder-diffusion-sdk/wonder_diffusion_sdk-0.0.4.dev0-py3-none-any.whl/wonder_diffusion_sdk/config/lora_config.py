import os


class WonderLora:
    """
    Lora model initialization wrapper.

    NOTES:
        - `unet_only` can be used when there is only one Lora.
        - `base_model_name_or_path` is required when loading multiple Loras with peft.
    """

    def __init__(
        self,
        path: str | os.PathLike = None,
        weight_name: str = None,
        adapter: str = None,
        adapter_weight: float = None,
        base_model_name_or_path: str = None,
    ):
        self.path = path
        self.weight_name = weight_name
        self.adapter = adapter
        self.adapter_weight = adapter_weight
        self.base_model_name_or_path = base_model_name_or_path


class WonderLoraConfig:
    """
    NOTES:
        - When using peft, both Loras must have the same `base_model_name_or_path`.
    """
    def __init__(
        self,
        loras: list[WonderLora] = [],
        use_peft: bool = False,
    ):
        self.loras = loras
        self.use_peft = use_peft
