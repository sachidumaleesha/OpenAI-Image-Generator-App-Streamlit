from openai import OpenAI

def generate_images(key, user_prompt, image_size, number_of_images):

    client = OpenAI(
        api_key = key
    )

    response = client.images.generate(
    model="dall-e-2",
    prompt=user_prompt,
    size=image_size,
    quality="standard",
    n=number_of_images,
    )

    image_urls = []
    for i in range(number_of_images):
        image_urls.append(response.data[i].url)

    return image_urls