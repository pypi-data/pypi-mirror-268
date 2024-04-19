#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2024/04/12 13:32:19
@Author  :   ChenHao
@Description  : 本地模型
@Contact :   jerrychen1990@gmail.com
'''

import json
import requests
from typing import Generator, List

from tqdm import tqdm
from snippets import batchify, jdumps
from agit.common import LLMResp
from loguru import logger


def call_embedding(text: str | List[str], url: str, batch_size=16, norm: bool = True) -> List[float] | List[List[float]]:
    texts = text if isinstance(text, list) else [text]
    batches = batchify(texts, batch_size)
    embeddings = []
    for batch in tqdm(batches):
        params = dict(texts=batch, norm=norm)
        resp = requests.post(url=url, json=params)
        resp.raise_for_status()
        resp_data = resp.json()["data"]
        # logger.debug(f"{resp_data=}")
        embeddings.extend(resp_data["embeddings"])
    return embeddings if isinstance(text, list) else embeddings[0]


def _build_prompt(messages: List[dict], system: str = None):
    prompt = ""
    if system:
        prompt += f"<|system|>\n{system}\n"         
    for message in messages:
        role = message["role"]
        content = message["content"]
        assert role in ["system", "user", "assistant"], f"invalid role : {role} "   
        prompt += f"<|{role}|>\n{content}\n"
    prompt += "<|assistant|>\n"
    return prompt

def tgi_resp2gen(resp)->Generator:
    def gen() :   
        for line in resp.iter_lines():    
            line=line.decode("utf8").strip()
            # logger.debug(f"line: {line}")
            if not line.startswith('data:'):
                continue
            line = line[len('data:'):]
            try:
                chunk = json.loads(line)
                # logger.debug(f"chunk: {chunk}")
                token = chunk['token']["text"]
                # content_decode_res = ''.join(re.findall(r'text":"(.*?)"', line))
                if token not in ["<|endoftext|>", "<|user|>", "<|observation|>", ""]:
                    yield token
                else:
                    continue
            except Exception as e:
                pass
    return gen()

def call_tgi_llm(messages: List[dict], url=None, system:str=None,
                 stream=True, temperature=0.7, top_p=0.95, max_tokens: int = None, do_sample=True, **kwargs) -> LLMResp:
    prompt = _build_prompt(messages, system)
    # data传参
    data = {
        "inputs": prompt,
        "stream": stream,
        "parameters": {
            "do_sample": do_sample,
            "temperature": temperature,
            "top_p": top_p,
            "max_new_tokens": max_tokens,
            "seed": None,
            "stop":  ["<|endoftext|>", "<|user|>", "<|observation|>"]
        }
    }
    details = dict(model_input=data)
    url = f"{url}/generate_stream" if stream else f"{url}/generate"
    logger.debug(f"requesting :{url} with data:{jdumps(data)}")
    resp = requests.post(url, json=data, stream=stream)
    resp.raise_for_status()
    llm_resp = LLMResp(content=None, details=details, usage=None)
    if stream:
        content_gen = tgi_resp2gen(resp)
        llm_resp.content = content_gen
    else:
        model_output =resp.json()
        details.update(model_output=model_output)
        logger.debug(f"model_output: {model_output}")
        content = model_output["generated_text"]
        llm_resp.content=content

    return llm_resp

