import requests
from openai import OpenAI
import io
from pypdf import PdfReader

class DivarContest:
    def __init__(self, api_token:str):
        self.api_token = api_token
        self.model = "gpt-4.1-mini"
        self.client = OpenAI(api_key=self.api_token, base_url="https://api.metisai.ir/openai/v1")

    def capture_the_flag(self, question:str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role":"system","content":"desired output format (no extra text, no explanation)"},{"role": "user", "content": question}],
            max_tokens=500,
            temperature=0.1
        )
        return response.choices[0].message.content.strip()

divar_contest = DivarContest('tpsg-OoN2JjOMkmuUqpSQ0knTaPczjXBLPJd')

print('--------- Flag 1 ---------')

request1 = requests.get('https://divar-contest.darkube.app/divar_sample.html').text
print(divar_contest.capture_the_flag(f"Find all the 'لپ‌تاپ' (laptop) in their title in html content in this html: {request1}. Each listing has a time indicating when it was posted (e.g., '۳۰ دقیقه پیش' for 30 minutes ago). Your task is to treat these times as a value to be sorted. Create a list of the laptop names, ordered from the oldest listing (longest time ago) to the newest listing (shortest time ago). The final answer should be a single string with the laptop names separated by a comma. Keep in mind I want a complete answer!"))

print('--------- Flag 2 ---------')

request2 = requests.get("https://divar-contest.darkube.app/divar_sample.html").text
print(divar_contest.capture_the_flag(f"Find all products with 'لپ‌تاپ' (laptop) in their title in html content in this html: {request2} and then calculate the average price of these laptops and return the result as a single number."))

print('--------- Flag 3 ---------')

request3 = requests.get("https://divar.news/").text
print(divar_contest.capture_the_flag("At UOD (University of Divar), you have a final exam tomorrow. The subject of the exam is Divar's History. You have this website https://divar.news/ as the sources of this exam. Go and find needed html tags to solve the question.The question is 'What is the integer value of square root of number of removed spammed ads in divar in 1404?'"))

print('--------- Flag 4 ---------')

request4 = requests.get("https://divar-contest.darkube.app/facts-va32bma-public.pdf")
pdf = io.BytesIO(request4.content)
reader = PdfReader(pdf)
content4 = reader.get_page(0).extract_text().split('\n')
print(divar_contest.capture_the_flag(f"At UOD (University of Divar), your professor has assigned you a task to review other students' articles. Get pdf file from {content4} — find the fake facts in it!(Avoid details and return the answer of question!)"))

print('--------- Flag 5 ---------')

request5 = requests.get("https://divar.ir/Aat1zFlF").content
print(divar_contest.capture_the_flag(f"Some fake ads have been found on Divar. Your professor at UOD (University of Divar) asks you to identify their owner. All of the ads were created by one person, but you are only given one of them. You must find the others yourself and determine the owner's name! starting ad is {request5}"))

print('--------- Flag 6 ---------')

print(divar_contest.capture_the_flag("You will receive the title of a sample ad. Your task is to identify the best root category of the ad using Divar's category hierarchy. title is {طوطی سخنگو}"))

print('--------- Flag 7 ---------')

request6 = requests.request("GET", "https://divar-contest.darkube.app/pending-ads/ad-public-931582.json")
print(divar_contest.capture_the_flag(f"Read this json file: {request6.text} and fetch the pending ads, review the fetched ads and choose the correct tag for each one. It is guaranteed that only one of the issues exists in the ads."))

print('--------- Flag 8 ---------')

request7 = requests.request("GET","https://divar-contest.darkube.app/chat-public-308722.json")
print(divar_contest.capture_the_flag(f"Read this json file: {request7.text} and fetch the reported chats, review the reported chats and choose the correct tag for each one. It is guaranteed that only one of the issues exists in the chats.If its OK say OK and if its not say why"))
