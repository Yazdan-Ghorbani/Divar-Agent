# Divar-Agent — دیوار ایجنت
**یک ایجنت ساده برای حل هشت تسک/فلگ مسابقه‌ی Divar**  
یک خلاصهٔ کوتاه: این ریپوزیتوری شامل `solution.py` است که ورودی‌های مربوط به ۸ تسکِ مسابقه را پردازش کرده و خروجی مورد انتظار را تولید می‌کند.

---

## وضعیت
- زبان: Python  
- وابستگی‌ها: داخل `python_requirements.txt` فهرست شده‌اند.

---

## Quick Start
1. کلون کن:
```bash
git clone https://github.com/Yazdan-Ghorbani/Divar-Agent
cd Divar-Agent
```
---
## شرح مسئله مسابقه
# Divar AI | دیوار ایجنت


**دیوار ایجنت**

در دیوار مسائل زیادی وجود دارند، از شما خواسته شده است که جعبه ابزار جادویی خود را بردارید و برای کمک به حل این مسائل بشتابید! یک جعبه ابزار دیواری باید بتواند مسائل پایین را به راحتی و با دقت بالا حل کند. در این سوال هشت تسک و هشت فلگ وجود دارد که ایجنت شما باید آن ها را حل کند.

# فلگ اول
```
مثال ورودی ۱ (چیزی که به agent شما ورودی داده می شود) :

Find all the 'لپ‌تاپ' (laptop) in their title in html content in this html: {https://divar-contest.darkube.app/divar_sample.html}. Each listing has a time indicating when it was posted (e.g., '۳۰ دقیقه پیش' for 30 minutes ago). Your task is to treat these times as a value to be sorted. Create a list of the laptop names, ordered from the oldest listing (longest time ago) to the newest listing (shortest time ago). The final answer should be a single string with the laptop names separated by a comma. Keep in mind I want a complete answer!

مثال خروجی ۱ (چیزی که agent شما باید خروجی دهد) :

aming لپ تاپ ,MacBook Air M1 لپ تاپ ,Lenovo ThinkPad E15 لپ تاپ ,MSI GF63 لپ تاپ گیمینگ"

```
---

# فلگ دوم
```

مثال ورودی ۲ (چیزی که به agent شما ورودی داده می شود) :

Find all products with 'لپ‌تاپ' (laptop) in their title in html content in this html: {https://divar-contest.darkube.app/divar_sample.html} and then calculate the average price of these laptops and return the result as a single number.

مثال خروجی ۲ (چیزی که agent شما باید خروجی دهد) :

aming لپ تاپ ,MacBook Air M1 لپ تاپ ,Lenovo ThinkPad E15 لپ تاپ ,MSI GF63 لپ تاپ گیمینگ"

"43700000"
```
---
# فلگ سوم
```

مثال ورودی ۳ (چیزی که به agent شما ورودی داده می شود) :

At UOD (University of Divar), you have a final exam tomorrow. The subject of the exam is Divar's History. You have this website https://divar.news/ as the sources of this exam. Go and find needed html tags to solve the question.The question is 'What is the integer value of square root of number of removed spammed ads in divar in 1404?'

مثال خروجی ۳ (چیزی که agent شما باید خروجی دهد) :

"784"

```
---
# فلگ چهارم
```

مثال ورودی ۴ (چیزی که به agent شما ورودی داده می شود) :

At UOD (University of Divar), your professor has assigned you a task to review other students' articles. Get pdf file from {https://divar-contest.darkube.app/facts-va32bma-public.pdf} — find the fake facts in it!(Avoid details and return the answer of question!)

مثال خروجی ۴ (چیزی که agent شما باید خروجی دهد) :

["Divar is a pet shop in Vanak square.", "Divar was founded by Google in 2013.

```
---

# فلگ پنجم
```
مثال ورودی ۵ (چیزی که به agent شما ورودی داده می شود) :

Some fake ads have been found on Divar. Your professor at UOD (University of Divar) asks you to identify their owner. All of the ads were created by one person, but you are only given one of them. You must find the others yourself and determine the owner's name! starting ad is {https://divar.ir/Aat1zFlF}

مثال خروجی ۵ (چیزی که agent شما باید خروجی دهد) :


"this_is_the_flag"

```
# فلگ ششم

```
مثال ورودی ۶ (چیزی که به agent شما ورودی داده می شود) :

You will receive the title of a sample ad. Your task is to identify the best root category of the ad using Divar's category hierarchy. title is {طوطی سخنگو}

مثال خروجی ۶ (چیزی که agent شما باید خروجی دهد) :

"سرگرمی و فراغت"

```
---

# فلگ هفتم

```
مثال ورودی ۷ (چیزی که به agent شما ورودی داده می شود) :

call {https://divar-contest.darkube.app/pending-ads/ad-public-931582.json} and fetch the pending ads, review the fetched ads and choose the correct tag for each one. It is guaranteed that only one of the issues exists in the ads.

مثال خروجی ۷ (چیزی که agent شما باید خروجی دهد) :

["OK", "IRRELEVANT_PICTURE", "IRRELEVANT_DESCRIPTION", "IRRELEVANT_CATEGORY"]

```
---

# فلگ هشتم

```
مثال ورودی ۸ (چیزی که به agent شما ورودی داده می شود) :

call {https://divar-contest.darkube.app/chat-public-308722.json} and fetch the reported chats, review the reported chats and choose the correct tag for each one. It is guaranteed that only one of the issues exists in the chats.If its OK say OK and if its not say why

مثال خروجی ۸ (چیزی که agent شما باید خروجی دهد) :

["OK", "FRAUD", "INSULT_RUDENESS", "ADVERTISEMENT"]

```





