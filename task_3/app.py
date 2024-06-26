from diffusers import StableDiffusionPipeline

pipe= StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]
image.save("astronaut_rides_horse.png")