#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from novita_client import NovitaClient, Txt2ImgRequest, Samplers, ProgressResponseStatusCode, ModelType, add_lora_to_prompt, save_image, ADEtailer
import logging

logging.basicConfig(level=logging.INFO)


client = NovitaClient(os.getenv('NOVITA_API_KEY'), os.getenv('NOVITA_API_URI', None))

res = client.sync_txt2img(Txt2ImgRequest(
    prompt="a ohwx close up photo of girl as superman",
    batch_size=1,
    cfg_scale=7.0,
    sampler_name=Samplers.DPMPP_M_KARRAS,
    model_name="epicrealism_pureEvolutionV5_97793.safetensors",
    height=512,
    width=512,
    seed=-1,
    adetailer=ADEtailer(
        prompt="a ohwx close up",
    )
),
    enterprise_plan=True,
)

if res.data.status != ProgressResponseStatusCode.SUCCESSFUL:
    raise Exception('Failed to generate image with error: ' +
                    res.data.failed_reason)

save_image(res.data.imgs_bytes[0], "test.png")
