# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Hf text-to-image finetune class."""

from typing import Any, Dict
from azureml.acft.common_components import get_logger_app
from azureml.acft.image.components.finetune.interfaces.azml_interface import AzmlFinetuneInterface
from azureml.acft.image.components.finetune.common.constants.constants import SettingLiterals, SettingParameters
from azureml.acft.image.components.finetune.huggingface.diffusion.models.constant import Literals

logger = get_logger_app(__name__)


class AzmlHfTextToImageFinetune(AzmlFinetuneInterface):
    """Hf image classification finetune class."""

    def __init__(self, params: Dict[str, Any]) -> None:
        """
        :param params: parameters used for training
        :type params: dict
        """
        super().__init__()
        self.params = params

    def get_finetune_args(self) -> Dict[str, Any]:
        """custom args for text to image finetuning

        :return: dictionary of custom args which are not supported by core
                 and needed for text-to-image models
        :rtype: Dict[str, Any]
        """
        custom_args_dict = {}
        lora_config = "unet.*to_q|unet.*to_v|unet.*to_out.0|unet.*add_k_proj|unet.*add_v_proj"
        if Literals.TRAIN_TEXT_ENCODER in self.params and self.params[Literals.TRAIN_TEXT_ENCODER]:
            lora_config += "|text_encoder.*q_proj|text_encoder.*k_proj|text_encoder.*v_proj|text_encoder.*out_proj"

        custom_args_dict.update(
            {"lora_target_modules" : lora_config}
        )
        custom_args_dict[SettingLiterals.REMOVE_UNUSED_COLUMNS] = SettingParameters.REMOVE_UNUSED_COLUMNS
        custom_args_dict["dataloader_pin_memory"] = False

        return custom_args_dict

    def get_custom_trainer_functions(self) -> Dict[str, Any]:
        """Customizable methods for trainer class

        :return: dictionary of custom trainer methods needed for text-to-image models
        :rtype: Dict[str, Any]
        """
        return {}
