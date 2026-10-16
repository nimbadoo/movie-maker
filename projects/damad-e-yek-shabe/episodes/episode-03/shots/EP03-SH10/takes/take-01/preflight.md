# بررسی پیش از ارسال نمای۱۰ — در انتظار مرور

۲۰۲۶/۱۰/۱۵. [پرامپت کامل](prompt.txt) · [قاب نامزد v6](../../images/EP03-SH10-close-house-v6.png) · [مرور واقعی ظاهر/فضا](../../appearance-and-space-v6.md) · [تمرین کاربر](../../audio/user-dialogue-10.m4a).

قاب قبلی کتابخانهٔ پشت دوربین را پشت سامان تکرار می‌کرد؛ قاب نزدیک نامزد اصلاح و واقعاً دیده شد. متن و بازی و پیشروی کوتاه همان کارت محفوظ‌اند. عکس تنها ورودی پیشنهادی تولید، تمرین فقط مرجع محلی ریتم/تلفظ و نه صدای شخصیت یا ورودی بارگذاری است.

ضبط واقعی کاربر۳٫۲۸۴ثانیه است؛ پیشنهاد۴ثانیه بدون شتاب/کشش و قطع کلمه. طرح دوربین کوتاه در طول جمله است و زمان جدا اضافه نمی‌کند. خود صدا در این نوبت شنیده نشده؛ زمان کل فایل انسانی مبنای ظرفیت است و ASR مرز قطعی آوا نیست.

مدل پیشنهادی `Omni 1.1 Flash`، `Frames`، `360p`، عمودی `9:16`، یک خروجی۴ثانیه و سقف۴اعتبار؛ قیمت همین تنظیم در مرورگر داخلی مشاهده شد. صدای اصلی مدل فقط آزمون مستقل با افشای نبود تضمین شباهت است. خروجی/لب/حرکت/هویت صوتی هنوز وجود ندارد و قبولی ادعا نشده. تولید و مجوز هزینه فعلاً نداریم؛ تکرار خودکار ممنوع.

<!-- preflight-state -->
```json
{
  "shot": "EP03-SH10",
  "take": "take-01",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "متن اعراب‌دار D10 عین کارت؛ شرط نازلی هم بخواد حذف یا تغییر نکرده."
    },
    "delivery": {
      "status": "pass",
      "evidence": "بیان خبری شرطی طبیعی؛ تأکید روشن شرط، بدون انتظار جواب اجباری."
    },
    "duration": {
      "status": "pass",
      "evidence": "afinfo روی ضبط واقعی کاربر۳٫۲۸۴ثانیه،۴۸کیلوهرتز مونو؛ کلیپ۴ثانیه۰٫۷۱۶ثانیه ظرفیت اضافه دارد. ASR۰تا۲٫۹۸ فقط شاهد ماشینی است؛ شنیدن مستقل ادعا نشده."
    },
    "performance": {
      "status": "pass",
      "evidence": "صمیمیت جدی/اطمینان۳از۵، قصد بیان خواست شخصی مشروط به نازلی، نگاه کوتاه نازلی سپس مادر؛ ثبت شده."
    },
    "identity": {
      "status": "pass",
      "evidence": "appearance-and-space-v6.md؛ قاب خروجی، هدف و پرتره واقعاً دیده و مقایسه شدند."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "عکس آغاز نگاه سامان به مادر پیش‌زمینه چپ؛ نازلی راست خارج برش با جای ثابت طرح. اجرای تغییر نگاه آینده معیار بازبینی خروجی است."
    },
    "geometry": {
      "status": "pass",
      "evidence": "کتابخانه ناسازگار حذف و قاب بسته شد؛ دیوار کرم، پشت دوربین سمت آشپزخانه. فاصله‌های پوشیده اندازه‌گیری نشده و حرکت صندلی نداریم."
    },
    "continuity": {
      "status": "pass",
      "evidence": "SH09 منتخب: مادر خطاب به سامان پایان می‌دهد؛ این نما پاسخ سامان با لباس ثابت و شانه همان مادر؛ میز/چای خارج برش. اتصال واقعی۱۰به۹و۱۱ بعد از تولید معیار تدوین است."
    },
    "camera": {
      "status": "pass",
      "evidence": "پیشروی مستقیم کوتاه و بسیار آرام۱۰تا۱۵سانتی‌متر مطابق کارت، بدون تغییر محور؛ مسیر بدون مانع در قاب نزدیک."
    },
    "prompt": {
      "status": "pass",
      "evidence": "متن دقیق و مالک گفتار و دستور بازی جدا، آغاز/پایان و سکوت شنونده ثبت شدند."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "هیچ ویدیوی موجود در این نما نیست؛ منبع عکس ثابت جای اجرای گفتار نیست؛ اصلاح پس‌زمینه با ابزار داخلی انجام شد."
    },
    "speaker": {
      "status": "pass",
      "evidence": "User approved exact native-model-voice SH10 single test after full prompt/corrected frame and lack of voice guarantee disclosed. Only Saman speaks, mother mouth hidden; output voice/lip identity remains acceptance criterion."
    },
    "settings": {
      "status": "pass",
      "evidence": "Exact v6 first frame uploaded, selected, seen; exact prompt.txt in UI read back; Omni1.1 Flash Frames 4s360p9:16 x1; price4credits. ui-ready-for-approval.png. Recheck immediately before paid generation."
    },
    "cost": {
      "status": "pass",
      "evidence": "User تأیید after explicit four-credit single4s/360p vertical package; live price reread4credits, no retry."
    }
  },
  "content_approval": {
    "approved": true,
    "bundle_sha256": "95b1e35b8814ebba3bc079671472be1e91ed6cb3105a730fc63a35571dd488d7",
    "user_reply": "تأیید",
    "evidence_ref": "Current chat direct reply to complete SH10 frame/prompt/settings one4s output ceiling4credits and native-voice limitation."
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "95b1e35b8814ebba3bc079671472be1e91ed6cb3105a730fc63a35571dd488d7",
    "user_reply": "تأیید",
    "evidence_ref": "Current chat direct reply to complete SH10 frame/prompt/settings one4s output ceiling4credits and native-voice limitation."
  },
  "consumed_attempts": 1,
  "bundle_sha256": "95b1e35b8814ebba3bc079671472be1e91ed6cb3105a730fc63a35571dd488d7"
}
```
<!-- /preflight-state -->

## تأیید بسته نهایی

کاربر با «تأیید» همین بسته کامل و سقف۴اعتبار را پذیرفت. ورودیv6، متن، مدل/مدت/کیفیت/تعداد و قیمت زنده دوباره تطبیق داده شدند. یک تلاش مجاز است؛ هنوز مصرف نشده.

یک ارسال۴اعتباری انجام شد؛ مجوز یک تلاش مصرف شده و تکرار ممنوع است.
