from utils.creds import API_KEY

import io
import warnings

from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image

class MirrorDream():
    def __init__(self):
        pass
    def dream(self, prompt):
        stability_api = client.StabilityInference(
            key=API_KEY,
            verbose=True,
        )
        answers = stability_api.generate(
            prompt=prompt
        )
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    img.save(fp='generated_image.jpg')


