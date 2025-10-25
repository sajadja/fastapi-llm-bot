# پروژه ربات پاسخگویی دایرکت

## فایل `.env`:
قبل از اجرا در روت پروژه یک فایل با نام .env و با مقادیر زیر ایجاد کنید (قسمت your_api_key را با کلید api گوگل gemini خود جایگزین کنید):
```
DATABASE_URL=sqlite:///./db/app_data.sqlite
GEMINI_API_KEY={your_api_key}
```

## نحوه اجرا:
پروژه داکرایز شده، دستور زیر را ران کنید و در آدرس `http://localhost:8000/docs` داکیومنت اندپوینت ها در دسترس است.
```
docker compose up --build
```

## نکات:
- این پروژه به صورت بسیار ساده و مینیمال پیاده سازی شده و صرفا برای ارزیابی کیفیت کد زنی قابل استفاده است. (مثلا سرچ محصولات در فایل rag.py بهتر است از embeding ها استفاده کند.)
- برای اینکه فایل دیتابیس روی گیت نیاید هنگام اجرای پروژه در ادرس db/app_data.sqlite ساخته میشود و حدود 100 دیتای تست در آن وارد میشود.
- ساختار پروژه از ریپوزیتوری https://github.com/zhanymkanov/fastapi-best-practices که شامل best practice های fastapi است، الهام گرفته شده.
- تصاویر تست:

<img width="1228" height="416" alt="Pasted image" src="https://github.com/user-attachments/assets/20d5c173-7fbd-4969-a4c3-6713bec976d6" />
<br><br><br><br>
<img width="1231" height="406" alt="Pasted image (2)" src="https://github.com/user-attachments/assets/ed619d0f-3f4e-4536-83f5-421ae17219de" />


