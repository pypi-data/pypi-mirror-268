import requests


class HyperGPT:
    def __init__(self, ):
        self.base_url = "http://0.0.0.0:8080"

    def GetToken(self, token):
        url = self.base_url + "/user/get_token"
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{url}?token={token}", headers=headers)
        response = response.json()['token']
        return response

    def Getbalance(self, token):
        url = self.base_url + "/user/getBalance"
        payload = {"token": token}
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + token,
                   }

        response = requests.get(url, params=payload, headers=headers)

        response = response.json()
        return response

    def HyperOpenaiV3(self, token, prompt):

        r"""Let's start talking to openAI just send your question to method
        HYPERGPT.HyperOpenaiV3("your question")
        """
        url = self.base_url + "/ai/gpt3"
        payload = {
            "User": "assistant",
            "Prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?User=assistant&Prompt={prompt}&token={token}", params=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data['content']
                # Process the response data here
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperMidjourney(self, token, prompt):

        url = self.base_url + "/ai/midjourney"
        payload = {
            "prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?prompt={prompt}&token={token}", params=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data['content']
                # Process the response data here
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperChatGpt4(self, token, prompt):
        url = self.base_url + "/ai/gpt4"
        payload = {
            "Prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?Prompt={prompt}&token={token}", params=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"API called successfully {data}")
                return data
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperOpenaiV4(self, token, prompt):
        url = self.base_url + "/ai/gpt4_8k"
        payload = {
            "User": "assistant",
            "Prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?User=assistant&Prompt={prompt}&token={token}", params=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"API called successfully {data}")
                # Process the response data here
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperPortraits(self, token, prompt, number, w, h):
        url = self.base_url + "/ai/davincitext2img"
        payload = {
            "prompt": prompt,
            "token": token,
            "number": number,
            "w": w,
            "h": h
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?prompt={prompt}&token={token}&number={number}&w={w}&h={h}", json=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                return {'result': data['image']}
            else:
                return response
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperCode(self, token, prompt):
        url = self.base_url + "/ai/code"
        payload = {
            "user": "assistant",
            "Prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?user=assistant&Prompt={prompt}&token={token}", params=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                return {'result': data['content']}
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperContracts(self, token, prompt):
        url = self.base_url + "/ai/gpt3"
        payload = {
            "User": "assistant",
            "Prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?User=assistant&Prompt={prompt}&token={token}", json=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                return {'result': data['content']}
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def upload_pdf(self, token, pdf_url):
        url = self.base_url + "/ai/upload_pdf"
        payload = {
            "url": pdf_url,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?url={pdf_url}&token={token}", json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data.get('source_id'):
                    return data
                else:
                    return {'error': data}
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperPdf(self, token, source_id, question):
        url = self.base_url + "/ai/ask_pdf"
        payload = {
            "source_id": source_id,
            "question": question,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?question={question}&source_id={source_id}&token={token}", json=payload,
                                     headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data['response']:
                    return data['response']
                else:
                    return {'error': data}
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperGoogleBard(self, token, prompt):
        url = self.base_url + "/ai/google"
        payload = {
            "Prompt": prompt,
            "token": token
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?Prompt={prompt}&token={token}", json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"API called successfully {data}")
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperArt(self, token, prompt, samples, step, file):
        url = self.base_url + "/ai/imagetoimage"
        payload = {
            "prompt": prompt,
            "token": token,
            "samples": samples,
            "step": step,
            "file": file
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?prompt={prompt}&token={token}&samples={samples}&step={step}&file={file}",
                                     json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperOcr(self, token, file):
        url = self.base_url + "/ai/ocr"
        payload = {
            "token": token,
            "file": file
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?token={token}&file={file}", json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def HyperExtract(self, token, file):
        url = self.base_url + "/ai/imagetotext"
        payload = {
            "token": token,
            "file": file
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{url}?token={token}&file={file}", json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def stability_text_to_image(self, token, choice, prompt, sample, steps, negative, width, height):
        choices = ["512_v2_1", "v1_5", "xl_1024_v1_0", "xl_1024_v0_9", "xl_beta_v2_2_2", "x4_latent_upscaler",
                   "esrgan_v1_x2plus"]
        if choice not in choices:
            raise Exception("The choice must be one of [ 512_v2_1, v1_5, xl_1024_v1_0, xl_1024_v0_9, xl_beta_v2_2_2, "
                            "x4_latent_upscaler, esrgan_v1_x2plus ]")
        url = self.base_url + f"/ai/stability_text_to_image_{choice}"
        payload = {
            "token": token,
            "choice": choice,
            "prompt": prompt,
            "sample": sample,
            "steps": steps,
            "negative": negative,
            "width": width,
            "height": height
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                f"{url}?token={token}&choice={choice}&prompt={prompt}&sample={sample}&steps={steps}&negative={negative}&width={width}&height={height}",
                json=payload, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))

    def stability_image_to_image(self, token, choice, prompt, sample, steps, negative, width, height):
        choices = ["512_v2_1", "v1_5", "xl_1024_v1_0", "xl_1024_v0_9", "xl_beta_v2_2_2", "x4_latent_upscaler",
                   "esrgan_v1_x2plus"]
        if choice not in choices:
            raise Exception("The choice must be one of [ 512_v2_1, v1_5, xl_1024_v1_0, xl_1024_v0_9, xl_beta_v2_2_2, "
                            "x4_latent_upscaler, esrgan_v1_x2plus ]")
        url = self.base_url + f"/ai/stability_image_to_image_{choice}"
        payload = {
            "token": token,
            "choice": choice,
            "prompt": prompt,
            "sample": sample,
            "steps": steps,
            "negative": negative,
            "width": width,
            "height": height
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                f"{url}?token={token}&choice={choice}&prompt={prompt}&sample={sample}&steps={steps}&negative={negative}&width={width}&height={height}",
                json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("API call failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API call failed:", str(e))
