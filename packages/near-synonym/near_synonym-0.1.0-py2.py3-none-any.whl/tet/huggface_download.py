# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2023/4/8 21:50
# @author  : Mo
# @function: 本地下载huggface_hub模型不加密


import os


from huggingface_hub import snapshot_download


os.environ["HF_ENDPOINT"] = os.environ.get("HF_ENDPOINT", "https://hf-mirror.com")
os.environ["PATH_NEAR_SYNONYM_DIR"] = os.environ.get("PATH_NEAR_SYNONYM_DIR", "https://hf-mirror.com")
print(os.environ["PATH_NEAR_SYNONYM_DIR"])
print(os.environ["HF_ENDPOINT"])

repo_id = "fnlp/bart-large-chinese"

path_dir = "E:/DATA/bert-model/00_pytorch/LLM/"
local_dir = path_dir + repo_id.replace("/", "_")
cache_dir = local_dir + "/cache"
snapshot_download(cache_dir=cache_dir,
                  local_dir=local_dir,
                  repo_id=repo_id,
                  local_dir_use_symlinks=False,  # 不转为缓存乱码的形式, auto, Small files (<5MB) are duplicated in `local_dir` while a symlink is created for bigger files.
                  resume_download=True,
                  allow_patterns=[
                                   "*.json",
                                   "*.py",
                                   "*.md",
                                   "*.tar",
                                   "*.bin",
                                   "*.model",
                                  ],
                  ignore_patterns=[
                      "*.safetensors",
                      "*.msgpack",
                      "*.h5",
                      "*.ot",
                      "*.pt",
                  ],
                  )



