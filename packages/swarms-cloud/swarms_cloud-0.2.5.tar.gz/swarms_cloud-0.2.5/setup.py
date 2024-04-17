# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swarms_cloud',
 'swarms_cloud.loggers',
 'swarms_cloud.schema',
 'swarms_cloud.utils']

package_data = \
{'': ['*']}

install_requires = \
['einops',
 'fastapi==0.110.0',
 'pydantic>2,<3',
 'shortuuid',
 'skypilot',
 'sse-starlette==2.0.0',
 'stripe',
 'swarms',
 'torch',
 'transformers',
 'uvicorn',
 'xformers']

setup_kwargs = {
    'name': 'swarms-cloud',
    'version': '0.2.5',
    'description': 'Swarms Cloud - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Swarms Cloud\nInfrastructure for scalable, reliable, and economical Multi-Modal Model API serving and deployment. We\'re using terraform to orchestrate infrastructure, FastAPI to host the models. If you\'re into deploying models for millions of people, join our discord and help contribute.\n\n\n# Install\n`pip install swarms-cloud`\n\n# Examples\n\n### Example Python\n```python\nimport requests\nimport base64\nfrom PIL import Image\nfrom io import BytesIO\n\n\n# Convert image to Base64\ndef image_to_base64(image_path):\n    with Image.open(image_path) as image:\n        buffered = BytesIO()\n        image.save(buffered, format="JPEG")\n        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")\n    return img_str\n\n\n# Replace \'image.jpg\' with the path to your image\nbase64_image = image_to_base64("images/3897e80dcb0601c0.jpg")\ntext_data = {"type": "text", "text": "Describe what is in the image"}\nimage_data = {\n    "type": "image_url",\n    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},\n}\n\n# Construct the request data\nrequest_data = {\n    "model": "cogvlm-chat-17b",\n    "messages": [{"role": "user", "content": [text_data, image_data]}],\n    "temperature": 0.8,\n    "top_p": 0.9,\n    "max_tokens": 1024,\n}\n\n# Specify the URL of your FastAPI application\nurl = "https://api.swarms.world/v1/chat/completions"\n\n# Send the request\nresponse = requests.post(url, json=request_data)\n# Print the response from the server\nprint(response.text)\n```\n\n### Example API Request in Node\n```js\nconst fs = require(\'fs\');\nconst https = require(\'https\');\nconst sharp = require(\'sharp\');\n\n// Convert image to Base64\nasync function imageToBase64(imagePath) {\n    try {\n        const imageBuffer = await sharp(imagePath).jpeg().toBuffer();\n        return imageBuffer.toString(\'base64\');\n    } catch (error) {\n        console.error(\'Error converting image to Base64:\', error);\n    }\n}\n\n// Main function to execute the workflow\nasync function main() {\n    const base64Image = await imageToBase64("images/3897e80dcb0601c0.jpg");\n    const textData = { type: "text", text: "Describe what is in the image" };\n    const imageData = {\n        type: "image_url",\n        image_url: { url: `data:image/jpeg;base64,${base64Image}` },\n    };\n\n    // Construct the request data\n    const requestData = JSON.stringify({\n        model: "cogvlm-chat-17b",\n        messages: [{ role: "user", content: [textData, imageData] }],\n        temperature: 0.8,\n        top_p: 0.9,\n        max_tokens: 1024,\n    });\n\n    const options = {\n        hostname: \'api.swarms.world\',\n        path: \'/v1/chat/completions\',\n        method: \'POST\',\n        headers: {\n            \'Content-Type\': \'application/json\',\n            \'Content-Length\': requestData.length,\n        },\n    };\n\n    const req = https.request(options, (res) => {\n        let responseBody = \'\';\n\n        res.on(\'data\', (chunk) => {\n            responseBody += chunk;\n        });\n\n        res.on(\'end\', () => {\n            console.log(\'Response:\', responseBody);\n        });\n    });\n\n    req.on(\'error\', (error) => {\n        console.error(error);\n    });\n\n    req.write(requestData);\n    req.end();\n}\n\nmain();\n```\n\n### Example API Request in Go\n\n```go\npackage main\n\nimport (\n    "bytes"\n    "encoding/base64"\n    "encoding/json"\n    "fmt"\n    "image"\n    "image/jpeg"\n    _ "image/png" // Register PNG format\n    "io"\n    "net/http"\n    "os"\n)\n\n// imageToBase64 converts an image to a Base64-encoded string.\nfunc imageToBase64(imagePath string) (string, error) {\n    file, err := os.Open(imagePath)\n    if err != nil {\n        return "", err\n    }\n    defer file.Close()\n\n    img, _, err := image.Decode(file)\n    if err != nil {\n        return "", err\n    }\n\n    buf := new(bytes.Buffer)\n    err = jpeg.Encode(buf, img, nil)\n    if err != nil {\n        return "", err\n    }\n\n    return base64.StdEncoding.EncodeToString(buf.Bytes()), nil\n}\n\n// main is the entry point of the program.\nfunc main() {\n    base64Image, err := imageToBase64("images/3897e80dcb0601c0.jpg")\n    if err != nil {\n        fmt.Println("Error converting image to Base64:", err)\n        return\n    }\n\n    requestData := map[string]interface{}{\n        "model": "cogvlm-chat-17b",\n        "messages": []map[string]interface{}{\n            {\n                "role":    "user",\n                "content": []map[string]string{{"type": "text", "text": "Describe what is in the image"}, {"type": "image_url", "image_url": {"url": fmt.Sprintf("data:image/jpeg;base64,%s", base64Image)}}},\n            },\n        },\n        "temperature": 0.8,\n        "top_p":       0.9,\n        "max_tokens":  1024,\n    }\n\n    requestBody, err := json.Marshal(requestData)\n    if err != nil {\n        fmt.Println("Error marshaling request data:", err)\n        return\n    }\n\n    url := "https://api.swarms.world/v1/chat/completions"\n    request, err := http.NewRequest("POST", url, bytes.NewBuffer(requestBody))\n    if err != nil {\n        fmt.Println("Error creating request:", err)\n        return\n    }\n\n    request.Header.Set("Content-Type", "application/json")\n\n    client := &http.Client{}\n    response, err := client.Do(request)\n    if err != nil {\n        fmt.Println("Error sending request:", err)\n        return\n    }\n    defer response.Body.Close()\n\n    responseBody, err := io.ReadAll(response.Body)\n    if err != nil {\n        fmt.Println("Error reading response body:", err)\n        return\n    }\n\n    fmt.Println("Response:", string(responseBody))\n}\n```\n\n\n\n\n\n## Calculate Pricing\n```python\nfrom transformers import AutoTokenizer\nfrom swarms_cloud import calculate_pricing\n\n# Initialize the tokenizer\ntokenizer = AutoTokenizer.from_pretrained("gpt2")\n\n# Define the example texts\ntexts = ["This is the first example text.", "This is the second example text."]\n\n# Calculate pricing and retrieve the results\ntotal_tokens, total_sentences, total_words, total_characters, total_paragraphs, cost = calculate_pricing(texts, tokenizer)\n\n# Print the total tokens processed\nprint(f"Total tokens processed: {total_tokens}")\n\n# Print the total cost\nprint(f"Total cost: ${cost:.5f}")\n```\n\n\n## Generate an API key\n```python\nfrom swarms_cloud.api_key_generator import generate_api_key\n\nout = generate_api_key(prefix="sk", length=30)\n\nprint(out)\n\n```\n\n# Stack\n- Backend: FastAPI\n- Skypilot for container management\n- Stripe for payment tracking\n- Postresql for database\n- TensorRT for inference\n- Docker for cluster management\n- Kubernetes for managing and autoscaling docker containers\n- Terraform\n\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/swarms-cloud',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
