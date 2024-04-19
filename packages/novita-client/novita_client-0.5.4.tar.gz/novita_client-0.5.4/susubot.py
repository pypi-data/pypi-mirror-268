#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from novita_client import NovitaClient, Txt2ImgV3LoRA, Samplers, ProgressResponseStatusCode, ModelType, add_lora_to_prompt, save_image, Txt2ImgRequest, ADEtailer
from novita_client.utils import base64_to_image, input_image_to_pil
from PIL import Image


def make_image_grid(images, rows: int, cols: int, resize: int = None):
    """
    Prepares a single grid of images. Useful for visualization purposes.
    """
    assert len(images) == rows * cols

    if resize is not None:
        images = [img.resize((resize, resize)) for img in images]

    w, h = images[0].size
    grid = Image.new("RGB", size=(cols * w, rows * h))

    for i, img in enumerate(images):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid


client = NovitaClient(os.getenv('NOVITA_API_KEY'), os.getenv('NOVITA_API_URI', None))

res1 = client.sync_txt2img(
    # prompt="a photo of handsome man, close up",
    Txt2ImgRequest(
        prompt="Hana bunny, <lora:HanaBunnyv2_24326:0.6>, <lora:JapaneseDollLikeness_v15_28382:0.3>, photorealistic, extremely wide hips, thick thighs, very faint eyebrows, wearing a sexy outfit, (busty:1.1), fit, gorgeous, asian, plump cheeks, big pupils, big tits, round face, wavy vibrant brown hair, long hair, thick thighs, (heavy lower lips:1.2), 24 year old, in the bedroom, (very light makeup:1.1)",
        negative_prompt="(hands:1.4), (cleft chin:1.4), (smile line:1.2), fingers, face lines, face shadow, extra limbs, defined cheekbones, face detail, (makeup:1.2), (dark eyebrows:1.2), prominent eyebrows, (wrinkles:1.2), (smile line:1.3), (defined cheekbones:1.2), extra limbs, open mouth, teeth, fat, tall, extremely big tits, bad nipples, (teeth:1.2), cross eyed, watermark, bangs, thin",
        model_name='epicrealism_pureEvolutionV5_97793.safetensors',
        batch_size=1,
        steps=30,
        cfg_scale=4.0,
        height=960,
        width=640,
        seed=1234,
        sampler_name=Samplers.DPMPP_M_KARRAS,
        # adetailer=ADEtailer(
        #     prompt="Hana bunny, closeup, <lora:HanaBunnyv2_24326:1.0>",
        #     negative_prompt="cleft chin, smile line, Lines on face, face shadows, bad chin, deformed, defined cheekbones, face detail, dark eyebrows, prominent eyebrows, wrinkles, extra limbs, open mouth, teeth, cross eyed, watermark, bangs",
        #     strength=0.5,
        # )
    )
)

with open('./susubot.png', "wb+") as f:
    f.write(res1.data.imgs_bytes[0])
