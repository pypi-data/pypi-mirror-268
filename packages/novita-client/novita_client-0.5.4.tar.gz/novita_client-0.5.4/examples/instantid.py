
import os
from novita_client import NovitaClient, InstantIDControlnetUnit
import base64


if __name__ == '__main__':
    client = NovitaClient(os.getenv('NOVITA_API_KEY'), os.getenv('NOVITA_API_URI', None))

    res = client.instant_id(
        model_name="wildcardxXL_v4Rundiffusion_243879.safetensors",
        face_images=[
            # "https://raw.githubusercontent.com/InstantID/InstantID/main/examples/yann-lecun_resize.jpg",
            "https://pbs.twimg.com/media/GGqg2mWbsAAW6H7?format=jpg"
        ],
        prompt="RAW photo, face portrait photo of beautiful 26 y.o woman, cute face, wearing black dress, happy face, hard shadows, cinematic shot, dramatic lighting",
        negative_prompt="(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, amputation",
        id_strength=0.8,
        adapter_strength=0.5,
        steps=20,
        seed=-1,
        width=1024,
        height=1024,
        guidance_scale=7,
        # controlnets=[
        #     InstantIDControlnetUnit(
        #         model_name='controlnet-openpose-sdxl-1.0',
        #         strength=0.4,
        #         preprocessor='openpose',
        #     ),
        #     InstantIDControlnetUnit(
        #         model_name='controlnet-canny-sdxl-1.0',
        #         strength=0.3,
        #         preprocessor='canny',
        #     ),
        # ],
        response_image_type='jpeg',
    )

    print('res:', res)

    if hasattr(res, 'images_encoded'):
        with open(f"instantid.png", "wb") as f:
            f.write(base64.b64decode(res.images_encoded[0]))
