from Client import Client

client = Client(url= '54.234.209.99:3000' , model_type="SD", endpoint = "txt2img",  prompt="cat sitting aon a table", negative_prompt = "white", image_path = "/home/ubuntu/RILAAS/pexels-pixabay-35967.jpg")

print (client.response.status_code)