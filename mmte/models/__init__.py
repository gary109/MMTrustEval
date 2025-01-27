from mmte.utils.registry import registry
from mmte.models.base import BaseChat, Response
from mmte.models.llava_chat import LLaVAChat
from mmte.models.llava_rlhf_chat import LLaVARLHFChat
from mmte.models.mplug_owl2_chat import mPLUGOwl2Chat
from mmte.models.internvl_chat import InternVLChat
from mmte.models.lrv_instruction_chat import LRVInstructionChat
from mmte.models.openai_chat import OpenAIChat
from mmte.models.google_chat import GoogleChat
from mmte.models.claude3_chat import ClaudeChat
from mmte.models.qwen_plus_chat import QwenPlusChat
from mmte.models.minigpt4_chat import MiniGPT4Chat
from mmte.models.instructblip_chat import InstructBLIPChat
from mmte.models.qwen_chat import QwenChat
from mmte.models.otter_chat import OtterChat
from mmte.models.mplug_owl_chat import mPLUGOwlChat
from mmte.models.internlm_xcomposer_chat import InternLMXComposerChat
from mmte.models.sharegpt4v_chat import ShareGPT4VChat
from mmte.models.cogvlm_chat import CogVLMChat
from mmte.models.phi3_chat import Phi3Chat
from typing import List


def load_chatmodel(model_id:str, device:str="cuda:0") -> 'BaseChat':
    return registry.get_chatmodel_class(model_id)(model_id=model_id, device=device)


def model_zoo() -> List['BaseChat']:
    return registry.list_chatmodels()

