# بررسی پیش از ارسال — قالب خالی

## تطبیق اجباری ظاهر

[مرجع ثابت شخصیت‌ها](../references/visuals/character-bible.md) و [قالب گزارش تطبیق](appearance-review.md) خوانده شوند؛ هنگام کپی به پوشهٔ برداشت لینک‌ها اصلاح شوند. نسخهٔ مرجع، اثرانگشت تصاویر و نقش هر ورودی و نتیجهٔ مشاهدهٔ هر شخصیت داخل قاب در گزارش نمای مالک ثبت شود. بررسی `identity` فقط با لینک به این گزارش و شاهد واقعی قبول شود؛ تفاوت صورت، مو، ریش، سن، لباس یا روسری و هر مورد لازمِ بررسی‌نشده مانع ارسال‌اند. قابِ قدیمی یا تولیدشدهٔ تازه به‌تنهایی مرجع هویت نیست. برای پذیرش خروجی ویدیو، مرور زمان‌دار و پیوسته لازم است؛ فرم خالی اثبات انجام کار نیست.


در پوشهٔ برداشت برنامه‌ریزی‌شده با نام preflight.md ذخیره شود. هنوز هیچ بررسی یا تأییدی انجام نشده است. مقدارهای اولیه عمداً ارسال را مسدود می‌کنند.

## گزارش قابل‌خواندن

شناسهٔ نما/برداشت و نسخه:
ایراد دقیق و دلیل نیاز به تولید تازه؛ امکان اصلاح محلی:
متن دقیق اعراب‌گذاری‌شده، تلفظ، ریتم، مکث، حالت و پایان سؤال:
قاب و ورودی‌های واقعی؛ شاهد مشاهده و کنترل نگاه/هندسه/پیوستگی:
زمان‌گیری و روش آن؛ تنظیمات؛ قیمت جاری و سقف هزینه:
ایرادهای رفع‌شده و باقی‌مانده؛ محدودیت پیش‌بینی رفتار مدل:
محل و زمان ارائهٔ پرامپت کامل و بسته به کاربر:
پاسخ واقعی کاربر برای تأیید همین نسخه و هزینه؛ مرجع گفت‌وگو:

## اطلاعات کنترل محلی

کلیدها: dialogue متن و تلفظ؛ delivery ریتم و مکث؛ duration زمان؛ performance بازی؛ speaker گوینده؛ identity هویت و لباس؛ eyeline نگاه؛ geometry دست و محیط؛ continuity اتصال؛ camera دوربین؛ prompt تطبیق دستور؛ local_alternative راه محلی؛ settings تنظیمات؛ cost هزینه.

هر بررسی: pass با شاهد واقعی، یا not_applicable با شاهد و دلیل. unchecked و ایراد باز مانع‌اند. اثرانگشت بسته پس از آماده‌شدن فایل‌ها با check_submission.py --fingerprint محاسبه می‌شود؛ محاسبهٔ آن تأیید نیست.

<!-- preflight-state -->
```json
{
  "shot": "EPNN-SHNN",
  "take": "take-NN",
  "ready": false,
  "open_issues": [
    "بررسی هنوز انجام نشده"
  ],
  "checks": {
    "dialogue": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "delivery": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "duration": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "performance": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "speaker": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "identity": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "eyeline": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "geometry": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "continuity": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "camera": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "prompt": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "local_alternative": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "settings": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    },
    "cost": {
      "status": "unchecked",
      "evidence": "",
      "reason": ""
    }
  },
  "bundle_sha256": null,
  "content_approval": {
    "approved": false,
    "bundle_sha256": null,
    "user_reply": "",
    "evidence_ref": ""
  },
  "cost_approval": {
    "approved": false,
    "bundle_sha256": null,
    "user_reply": "",
    "evidence_ref": ""
  },
  "consumed_attempts": 0
}
```
<!-- /preflight-state -->

در بلوک shot-state کارت نما، send_request را فقط برای یک اقدام مشخص تنظیم کنید:

```json
{
  "take": "take-NN",
  "prompt": "prompt.txt",
  "preflight": "preflight.md",
  "input_files": ["images/ACTUAL-FRAME.png"],
  "settings": {
    "model": "ACTUAL MODEL",
    "seconds": 0,
    "quality": "ACTUAL QUALITY",
    "aspect_ratio": "9:16",
    "audio": true,
    "outputs": 1
  },
  "cost": {
    "unit": "ACTUAL UNIT",
    "per_attempt": 0,
    "attempts": 1,
    "ceiling": 0,
    "price_source": "",
    "verified_at": ""
  }
}
```

اعداد و نام‌های مثال قیمت یا تنظیمات واقعی نیستند. مسیر prompt و preflight نسبت به پوشهٔ همان برداشت؛ input_files نسبت به پوشهٔ نماست. کاربر باید خود بستهٔ نهایی و هزینه را صریحاً تأیید کند؛ درج approved=true بدون شواهد معتبر مجوز نیست. هر تغییر فایل، متن، تنظیمات یا هزینه اثرانگشت را تغییر می‌دهد و تأیید دوباره می‌خواهد.

پیش از تولید واقعی، تطبیق رابط زنده با بستهٔ مصوب ثبت شود. پس از هر ارسال، consumed_attempts و هزینهٔ واقعی قابل‌مشاهده ثبت شوند؛ تلاش مجددِ خارج از تعداد مصوب ممنوع است. ابزار فقط کنترل محلی است و هیچ تولیدی انجام نمی‌دهد.
