# بررسی پیش از ارسال نمای۱۱ — یک‌بار اجرا شد

۲۰۲۶/۱۰/۱۵؛ آماده‌سازی مجاز است؛ این بسته مجوز ارسال ندارد.

[قاب شروع نامزد](../../images/EP03-SH11-house-close-v5.png) · [پرامپت کامل](prompt.txt) · [بررسی فضا](../../house-review-v5.md) · [تطبیق ظاهر](../../appearance-review-v5.md).

متن و بازی مصوب در [کارت مالک](../../shot.md) است؛ پرامپت از همان متن استخراج شد. زمان تمرین مصنوعی محلی۳٫۴۰۴ثانیه است، نه صدای بازیگر یا شاهد روانی اجرا. با این شاهد، بودجهٔ۲٫۵ثانیه قدیمی امن نیست؛ پیشنهاد اجرایی، کلیپ۶ثانیه با سهم تدوین پس از اجرای واقعی حدود۳٫۸تا۴٫۵ثانیه است. این بازه تخمین است؛ سرعت پخش تغییر نکند و اضافات محلی حذف شوند. تمرین مصنوعی ورودی تولید یا صدای نازلی نیست.

[مرجع مستقل صدای نازلی](../../../../../../references/voice/voice-bible.md) باید در روش واقعی قابل‌استفاده باشد؛ توصیف صدا در پرامپت تضمین هویت نیست. این نوبت شنیدن مرجع انجام نشده و نمونهٔ مصنوعی برای تقلید آن استفاده نشده است.

رابط زنده در تب مستقل همین چت بررسی شد: `Omni 1.1 Flash`، مسیر `Frames`، نسبت `9:16`، کیفیت `360p`، یک خروجی؛ مدتهای۴،۶،۸،۱۰ثانیه موجودند. تنظیم حاضر۴ثانیه و قیمت آن۴اعتبار بود؛ قیمت۶ثانیه بررسی نشده. هیچ تنظیمی عوض، تصویری بارگذاری یا تولیدی ارسال نشد؛ تب موقت بسته شد. [شاهد رابط](ui-capabilities.png) و [متن رابط](ui-capabilities.txt).

محدودهٔ این چت با درخواست مستقیم کاربر به چت «`episode 3`» پیام داده شد: شناسهٔ نما `SH11` به بعد، نه ردیف یازدهم ترتیب تدوین که `SH16` است. اسناد مشترک و فایل‌های چت دیگر تغییر نکردند. نمای۱۰ فعلاً کتابخانه را پشت سامان نشان می‌دهد و نیازمند کنترل با خانه است؛ اتصال نهایی۱۰←۱۱←۱۲ هنوز بسته نیست.

## موارد باز

- زمان اجرای انسانی و حاشیهٔ پایان هنوز اندازه‌گیری نشده؛ تمرین مصنوعی جای آن نیست.
- اتصال نهایی با ویدیوی منتخب نمای۱۰ و۱۲ هنوز وجود ندارد.
- روش قابل‌اجرا برای حفظ صدای مرجع نازلی در مدل جاری هنوز تأیید نشده.
- قیمت تنظیم پیشنهادی۶ثانیه و تطبیق ورودی واقعی پیش از ارسال بررسی نشده.
- مرور بسته و تأیید صریح نسخه و سقف هزینه دریافت نشده.

## کنترل محلی

<!-- preflight-state -->
```json
{
  "shot": "EP03-SH11",
  "take": "take-01",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "متن عیناً از کارت مالک استخراج و حرکات حفظ شد؛ فعل خبری، بدون تغییر واژه.",
      "reason": ""
    },
    "delivery": {
      "status": "pass",
      "evidence": "تأکید ملایم فعلاً، نوبت پس از سامان و مکث کوتاه خطاب در پرامپت ثبت شد؛ کیفیت اجرا پس از تولید سنجیده می‌شود.",
      "reason": ""
    },
    "duration": {
      "status": "pass",
      "evidence": "Measured local synthetic rehearsal 3.403673s (not actor recording). Six-second clip leaves 2.596s combined margin; no physical action beyond dialogue. Human timing is unknown, output word boundaries must be checked; no 2.5s target or slowed speech.",
      "reason": ""
    },
    "performance": {
      "status": "pass",
      "evidence": "حالت، قصد و رفتار از کارت مصوب به پرامپت منتقل شد؛ بازی واقعی تولید نشده.",
      "reason": ""
    },
    "speaker": {
      "status": "pass",
      "evidence": "User explicitly approved experimental native-voice take after disclosure that Frames cannot guarantee Nazli voice identity. Only Nazli speaks; mother lips offscreen. Voice likeness and lipsync are output acceptance criteria, not claimed passed.",
      "reason": ""
    },
    "identity": {
      "status": "pass",
      "evidence": "گزارش مستقل appearance-review-v5.md؛ چهره و موی نازلی با پنل چپ و قاب قبلی مقایسه شد؛ فقط شانه مادر دیده می‌شود.",
      "reason": ""
    },
    "eyeline": {
      "status": "pass",
      "evidence": "مشاهده واقعی قاب نسخه۵: چشم نازلی سمت راست لنز و به محل مادر، بدون نگاه مستقیم به لنز؛ چشم مادر خارج قاب است.",
      "reason": ""
    },
    "geometry": {
      "status": "pass",
      "evidence": "house-review-v5.md؛ قاب بسته فقط صورت/بالاتنه و شانه مادر، پس‌زمینه کرم. اثبات فاصله دو صندلی ادعا نشده؛ دست و اشیا خارج قاب‌اند.",
      "reason": ""
    },
    "continuity": {
      "status": "pass",
      "evidence": "Independent test scope approved: close frame contains only Nazli face/blouse and blurred mother shoulder, static cream wall. Card dialogue follows D10 and ends before D12, no reused line or shared visible props. SH10 wrong background remains an assembly hold; final adjacent-video splice is not claimed verified and this take cannot be adopted automatically.",
      "reason": ""
    },
    "camera": {
      "status": "pass",
      "evidence": "متوسط نزدیک ثابت از نزدیکی خط چشم مادر؛ چرخش صندلی و تغییر محور در پرامپت ممنوع.",
      "reason": ""
    },
    "prompt": {
      "status": "pass",
      "evidence": "متن استخراج‌شده در پرامپت وجود دارد؛ دستور اجرا از دیالوگ جدا و منابع دقیق ثبت شدند.",
      "reason": ""
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "در پوشه نما هیچ ویدیوی موجود نیست؛ عکس ثابت جای اجرای گفتار را نمی‌گیرد. ابتدا اصلاح تصویر با ابزار داخلی، بدون ارسال اعتباری `Flow` انجام شد.",
      "reason": ""
    },
    "settings": {
      "status": "pass",
      "evidence": "Live UI-selected Omni 1.1 Flash Frames, 6s, 360p, 9:16, x1; exact v5 first-frame upload selected and screenshot ui-ready.png actually inspected. No last frame required.",
      "reason": ""
    },
    "cost": {
      "status": "pass",
      "evidence": "User تأیید after 5-credit six-second single experimental take quote, no automatic retry; renewed authorization unchanged. Live price 5 credits, ui-ready.png. Upload now succeeded after user changed site permissions.",
      "reason": ""
    }
  },
  "bundle_sha256": "685ed616c89b8a4000a93945eb1fe72048a22b85b1baa554ebe2aac217919c49",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "685ed616c89b8a4000a93945eb1fe72048a22b85b1baa554ebe2aac217919c49",
    "user_reply": "تأیید",
    "evidence_ref": "Current chat: shot summary approved; then explicit 5-credit experimental 6s quote approved; user requested continue after permissions fixed."
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "685ed616c89b8a4000a93945eb1fe72048a22b85b1baa554ebe2aac217919c49",
    "user_reply": "تأیید",
    "evidence_ref": "Current chat: shot summary approved; then explicit 5-credit experimental 6s quote approved; user requested continue after permissions fixed."
  },
  "consumed_attempts": 1
}
```
<!-- /preflight-state -->

## تأیید محتوای نما و قیمت تازه

کاربر در همین چت گفت «تأیید می‌کنم. حالا شروع کن. حالا شروع کن، تأیید می‌کنم.»؛ تأیید متن، قاب پیشنهادی و جهت بازی ثبت شد. این شاهد تأیید هزینه نیست، چون قیمت این اقدام پیش از پاسخ اعلام نشده بود.

قیمت دقیق اکنون **۵اعتبار برای یک خروجی۶ثانیه** با `Omni 1.1 Flash`، کیفیت `360p`، نسبت `9:16` و مسیر `Frames` است؛ [شاهد زنده](ui-price-6s.png). بسته هنوز ارسال نشده و `send_request: null` حفظ شد. ثبات صدای نازلی در این مسیر تضمین نشده؛ پذیرش روش `Seed-VC` برای مادر به معنی پذیرش خودکار صدای نازلی نیست. پیش از تولید، دامنهٔ آزمون صدا و موارد فنی باز باید بسته شوند.

## توقف واقعی پس از تأیید هزینه

کاربر پس از پیشنهاد صریح یک برداشت آزمایشی۶ثانیه با سقف۵اعتبار و بدون تکرار خودکار گفت «تأیید». این مجوز ثبت و هنوز مصرف نشده است. تنظیمات زنده همان۶ثانیه،۳۶۰،عمودی و یک خروجی با قیمت۵اعتبار بود.

بارگذاری [قاب شروع نسخه۵](../../images/EP03-SH11-house-close-v5.png) با پیام کنترل امنیتی مرورگر رد شد: اجازهٔ بارگذاری این درخواست رد شده است. هیچ راه جایگزین برای دورزدن محدودیت امتحان نشد. فایل به‌عنوان قاب شروع انتخاب نشده، پرامپت در رابط وارد نشده و دکمهٔ تولید فشرده نشده است. تلاش ارسال هزینه‌دار صفر؛ کسر اعتبار ناشی از این اقدام نداریم. مجوز هزینه با آمادگی فنی یا درخواست فعال ارسال یکی نیست؛ `send_request: null` و کنترل‌های باز محفوظ‌اند.

### رد دوبارهٔ بارگذاری پس از اجازهٔ تازه

کاربر صریحاً کنترل امنیتی و انجام کار در `Google Flow` را تأیید کرد. در تب باز پروژه مسیر عادی `Start → Upload media` دوباره اجرا شد؛ خودِ بارگذاری با همان پیام رد اجازه توسط کنترل امنیتی مرورگر متوقف شد. فایل انتخاب نشده، دکمه تولید فشرده نشده، مجوز۵اعتبار مصرف نشده و مسیر جایگزین امتحان نشد. نیاز به اقدام واقعی کاربر در رابط بارگذاری باقی است؛ تأیید متنی به‌تنهایی محدودیت رابط را برطرف نکرد.

## گزارش جاریِ آزمون مستقل — جایگزین توقف‌های تاریخی بالا

مجوز بارگذاری اکنون عملاً کار کرد و قاب نسخه۵ در جای آغاز انتخاب و دیده شد؛ پرامپت بدون تغییر وارد شد. محتوای نما و آزمون صدای تولیدی با افشای محدودیت و سقف۵اعتبار صریحاً تأیید شدند. زمان مصنوعی اندازه‌گیری‌شده۳٫۴۰۴ثانیه و حاشیهٔ کلیپ۶ثانیه۲٫۵۹۶ثانیه است؛ این زمان بازیگر نیست. شرط تولیدِ تمرین انسانی جدا در این آزمون وجود ندارد؛ روانی و مرز واژه‌ها در خروجی بررسی می‌شوند.

اتصال تدوین نهایی و خطای پس‌زمینهٔ نمای۱۰ همچنان بازند و به معنای آماده‌بودن کل قسمت نیستند؛ در این قاب مستقل و بسته، هیچ شیء/پس‌زمینهٔ مشترک از نمای۱۰ کپی نشده، جمله و جای نازلی و شانهٔ مادر با کارت و مرجع تطبیق داده شدند. دروازهٔ این ارسال فقط برای یک آزمون مستقل با صدای هنوز انتخاب‌نشده است. نه حرکت آینده، نه هویت صدای خروجی، نه اتصال نهایی پیشاپیش قبول نشده‌اند.

[بستهٔ واقعی پیش از ارسال](ui-ready.png) · [پرامپت دقیق و بدون تغییر](prompt.txt).


یک ارسال۶ثانیه‌ای با قیمت۵اعتبار انجام شد؛ مجوز همان یک تلاش مصرف شد و تکرار مجاز نیست. کسر واقعی دفتر حساب مستقلاً بررسی نشده.


## نتیجه اجرا

بارگذاری پس از تنظیم مجوز توسط کاربر موفق شد. یک ارسال با قیمت۵اعتبار انجام و فایل اصلی ذخیره شد. [گزارش خروجی](review.md) دارای ایراد ورود دست و محدودیت شنیدن است؛ موفقیت تولید به معنی پذیرش برداشت نیست. مجوز یک تلاش مصرف شده و درخواست فعال کارت خالی است.
