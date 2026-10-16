# بررسی نهایی نسخهٔ جمع‌وجور — پیش از ارسال

[پرامپت دقیق](prompt.txt) · [بررسی هویت، نگاه و هندسه](../preflight.md)

قاب و بررسی‌های غیرزمانی همان بستهٔ قبلی‌اند؛ تنها ریتم به نسخهٔ جمع‌وجور تأییدشده تغییر کرد. متن رابط با فایل برابر و قیمت همان۷کریدیت،۱۰ثانیه و یک خروجی بود. هیچ تولیدی پیش از این گزارش انجام نشده است.

خوانش قبلی کاربر۱۱ثانیه بود؛ هدف۸٫۵تا۹٫۵ثانیهٔ نسخهٔ تازه اجرا/زمان‌گیری نشده است. تفسیر دستور اخیر کاربر، پس از افشای این محدودیت، مجوز یک اجرای مولد با همین پرامپت و ریسک زمانی است؛ شرط قبلیِ اثبات جا شدنِ خوانش شخصی برای این اقدام اعمال نمی‌شود. این استثنای موردی، ادعای اندازه‌گیری، تضمین کیفیت یا قاعدهٔ دائمی تازه نیست. همهٔ واژه‌ها باید در خروجی کنترل شوند؛ در صورت نقص، تلاش مجدد خودکار انجام نشود.

مجوز فقط یک ارسال تا۷کریدیت است؛ خروجی فقط برای نمایش جداگانه و بدون جایگزینی در تدوین. احتمال بریدن/حذف واژه، مکث، تغییر صدا یا خطای لب و نگاه هنوز ریسک مولد است و نتیجه تا بررسی واقعی پذیرفته نیست.

<!-- preflight-state -->
```json
{
  "shot": "EP02-SH03",
  "take": "take-03",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "متن عین آخرین درخواست کاربر؛ نامزد می‌شَن و جملهٔ قصهٔ ما برعکس شده محفوظ؛ اعراب و انطباق با کارت مرور شد. صحت تلفظ خروجی هنوز باید پس از تولید شنیده شود.",
      "reason": ""
    },
    "delivery": {
      "status": "pass",
      "evidence": "عین نسخهٔ جمع‌وجور تأییدشده: شروع فوری، گفتار طبیعی و سرزنده، بدون مکث اضافه یا حذف واژه؛ همهٔ سه جمله محفوظ. هدف زمانی با عدم قطعیت به کاربر نشان داده و پذیرفته شد.",
      "reason": ""
    },
    "duration": {
      "status": "not_applicable",
      "evidence": "User approved exactly the paced proposal after explicit disclosure that8.5-9.5s is a target, not a measured result; latest instruction unconditionally authorizes one10s generation. Prior baseline read11s retained as evidence; no faster reading measurement claimed.",
      "reason": "Case-specific user instruction is interpreted to authorize one generative performance with disclosed timing uncertainty, superseding the prior conditional fit gate. This is not a claim of measured fit or final delivery readiness."
    },
    "performance": {
      "status": "pass",
      "evidence": "آخرین پاسخ کاربر همین پرامپت جمع‌وجور را تأیید می‌کند؛ حالت و قصد و رفتار سه جمله همان بستهٔ قبل‌اند.",
      "reason": ""
    },
    "speaker": {
      "status": "pass",
      "evidence": "shot.md: هر سه جمله فقط سامان؛ نازلی ساکت، هر دو داخل قاب؛ فقط لب‌های سامان فعال.",
      "reason": ""
    },
    "identity": {
      "status": "pass",
      "evidence": "preflight-visual-comparison.jpg: قاب ورودی v3 با پرترهٔ مصوب سامان، چیدمان v3 و نماهای مجاورِ خروجی v4 مقایسه شد؛ ناسازگاری آشکار چهره/مو/لباس تشخیص داده نشد. ثبات حرکتِ تولیدنشده تضمین نیست.",
      "reason": ""
    },
    "eyeline": {
      "status": "pass",
      "evidence": "تصویر واقعی ورودی دیده شد: سامان راست رو به چشم نازلی با نگاه کمی پایین، نازلی چپ با نگاه کمی بالا؛ هر دو نیم‌رخ، بدون نگاه به لنز. چشم مخاطب واقعی در قاب قابل تعیین است.",
      "reason": ""
    },
    "geometry": {
      "status": "pass",
      "evidence": "قاب و چیدمان v3 دیده شدند: نازلی بیرون و سامان داخل؛ در نیمه‌باز، لولا سمت ثابت چهارچوب؛ دست راست نازلی روی سطح بیرونی چوب، دست آزاد پایین. لنگه و دست‌ها در پرامپت ثابت‌اند. سلامت حرکت پس از تولید باید کنترل شود.",
      "reason": ""
    },
    "continuity": {
      "status": "pass",
      "evidence": "preflight-visual-comparison.jpg: فریم‌های5.5/5.6ثانیهٔ نمای۲ و9.5/9.6ثانیهٔ اتصال به۴ از تدوین v4 دیده شدند؛ لباس، مکان و دست روی چهارچوب سازگارند. نمای جدید ورود/خروج یا تغییر شیء ندارد؛ اتصال واقعی پس از تولید/تدوین همچنان باید بازبینی شود.",
      "reason": ""
    },
    "camera": {
      "status": "pass",
      "evidence": "قاب فعال دیده شد؛ تصویر جانبی دونفره، دوربین ثابت؛ هیچ حرکت جدید تعریف نشده است.",
      "reason": ""
    },
    "prompt": {
      "status": "pass",
      "evidence": "pace-proposal-v2/prompt.txt در رابط چیده و متن DOM با یکسان‌سازی فاصله‌ها عین فایل بود؛ اعراب و همهٔ واژه‌های متن مرجع محفوظ‌اند.",
      "reason": ""
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "متن تازه حاوی دو جملهٔ تازه و واژگان متفاوت است؛ برداشت قدیمیِ همین نما آن‌ها را ندارد. برش، سکوت یا فریم ثابت این گفتار را تولید نمی‌کند. تولید گفتار تازه لازم است؛ روش هنوز قطعی نشده.",
      "reason": ""
    },
    "settings": {
      "status": "pass",
      "evidence": "رابط همین نوبت: Omni 1.1 Flash؛ Frames؛ 9:16؛ 360p؛10s؛x1؛ تصویر ورودی941×1672 و قاب پایان خالی.",
      "reason": ""
    },
    "cost": {
      "status": "pass",
      "evidence": "قیمت زنده همین نوبت7credits؛ آخرین پیام کاربر سقف۷کریدیت، یک برداشت۱۰ثانیه‌ای و عدم تلاش مجدد را صریحاً تأیید می‌کند.",
      "reason": ""
    }
  },
  "bundle_sha256": "b6a4580c28e3364215bea41f1e9530d29f86aa984ad7424b518db5bf39a5f7a5",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "b6a4580c28e3364215bea41f1e9530d29f86aa984ad7424b518db5bf39a5f7a5",
    "user_reply": "خوبه، همین پرامپت جمع‌وجور رو با سقف ۷ کریدیت برای یک برداشت ۱۰ثانیه‌ای تأیید می‌کنم. فقط یک بار بساز، تلاش مجدد نکن و قبل از جایگزینی توی تدوین، نتیجه رو نشونم بده.",
    "evidence_ref": "Latest direct human instruction in this chat,2026-10-14; accepts paced variant after disclosed timing uncertainty."
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "b6a4580c28e3364215bea41f1e9530d29f86aa984ad7424b518db5bf39a5f7a5",
    "user_reply": "خوبه، همین پرامپت جمع‌وجور رو با سقف ۷ کریدیت برای یک برداشت ۱۰ثانیه‌ای تأیید می‌کنم. فقط یک بار بساز، تلاش مجدد نکن و قبل از جایگزینی توی تدوین، نتیجه رو نشونم بده.",
    "evidence_ref": "Latest direct human instruction in this chat,2026-10-14; accepts paced variant after disclosed timing uncertainty."
  },
  "consumed_attempts": 1,
  "timing": {
    "source": "user reported measured natural read aloud",
    "user_reply": "11",
    "speech_seconds": 11,
    "proposed_start_end_margin_seconds": 0.5,
    "required_seconds": 11.5,
    "approved_seconds": 10,
    "fits": false,
    "raw_audio_reviewed": false
  },
  "submission_note": "Single attempt reserved immediately before one UI click; never retry if dispatch outcome is ambiguous."
}

```
<!-- /preflight-state -->


## پس از تنها ارسال مجاز

یک بار تولید ارسال شد؛ قیمت نمایش‌داده‌شده۷کریدیت. نتیجه در رابط آماده و مدت واقعیِ قابل‌خواندن از پخش‌کننده۱۰٫۰۰۵ثانیه، اندازهٔ `360×640` بود. [صفحهٔ پخش نتیجه](https://flow.google.com/project/b375b947-7a79-4f37-bb43-0231a2960464/edit/6694979f-0e0e-4903-bdb7-fa4ea8f2d933). برداشت فقط در مرورگر برای کاربر پخش شد؛ دانلود به علت رد مجوز توسط سیاست امنیتی مرورگر متوقف و هیچ راه جایگزین یا ارسال مجددی انجام نشد. فایل محلی و اثرانگشت رسانه نداریم؛ صحت تمام گفتار و حرکت هنوز پذیرفته نیست. تدوین تغییر نکرد.


## رفع مانع دانلود با مجوز تازه

کاربر دانلود همین برداشت را صریحاً تأیید کرد؛ دانلود رسمیِ اندازهٔ اصلی موفق و [فایل و گزارش](../review.md) ذخیره شد. فقط ذخیره و بازکردن انجام شد؛ تولید و تدوین تازه انجام نشدند.
