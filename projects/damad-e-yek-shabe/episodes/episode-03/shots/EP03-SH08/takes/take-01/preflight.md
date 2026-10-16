# بررسی پیش از ارسال نمای۸ — در انتظار مرور نهایی

۲۰۲۶/۱۰/۱۵. [پرامپت کامل](prompt.txt) · [قاب نامزد](../../images/EP03-SH08-close-house-v5.png) · [تطبیق واقعی ظاهر و خانه](../../appearance-and-space-v5.md) · [تمرین کاربر](../../audio/user-dialogue-08.m4a).

قاب قبلی کتابخانه را پشت نازلی تکرار می‌کرد؛ قاب نزدیک تازه با ابزار داخلی اصلاح و واقعاً دیده شد. هیچ ویدیوی هزینه‌دار ارسال نشده است. نقش ورودی تولید فقط قاب آغاز v5 است؛ تمرین شماره۸ مرجع محلی تلفظ/ریتم و مرجع مستقل صدای نازلی متعلق به voice-bible است؛ فایل صوتی به مدل بارگذاری نمی‌شود و ثبات صدا تضمین نیست.

تنظیم پیشنهادی و مشاهده‌شده: `Omni 1.1 Flash`، `Frames`، عمودی `9:16`، `360p`،۴ثانیه، یک خروجی، قیمت و سقف۴اعتبار. تمرین انسانی۳٫۰۵ثانیه است؛ سرعت خروجی تغییر نکند، پایان کلمه بریده نشود. گفتار آینده، تلفظ و هماهنگی لب پیشاپیش قبول نشده‌اند و باید در ویدیو بررسی شوند. این نوبت شنیدن مستقل ضبط انجام نشده و ASR جای آن معرفی نمی‌شود؛ زمان کل فایل انسانی مبنای ظرفیت محافظه‌کارانه است.

دامنهٔ پیشنهاد فقط یک آزمون مستقل با صدای اصلی مدل است؛ اتصال نهایی و هویت صوتی خروجی معیار پذیرش بعد از تولیدند، نه تضمین. تا پذیرش این دامنه و قاب/پرامپت و هزینه، ارسال مسدود است. تلاش مجدد خودکار مجاز نیست.

<!-- preflight-state -->
```json
{
  "shot": "EP03-SH08",
  "take": "take-01",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "متن عین کارت D08 و اعراب حفظ؛ دستور از گفتار جدا."
    },
    "delivery": {
      "status": "pass",
      "evidence": "خبری توضیحی، قطعی تأکید اندک؛ بدون تندی و کشش."
    },
    "duration": {
      "status": "pass",
      "evidence": "ضبط واقعی کاربر با afinfo اندازه‌گیری شد۳٫۰۴۹۳۳۳ثانیه؛ کلیپ۴ثانیه حدود۰٫۹۵ثانیه ظرفیت اضافه دارد. ASR۰–۲٫۲۲ تخمین است نه شنیدن؛ متن کارت مرجع است."
    },
    "performance": {
      "status": "pass",
      "evidence": "دفاع آرام/اضطراب۲از۵ و قصد حفظ اختیار، دست ثابت روی ران."
    },
    "identity": {
      "status": "pass",
      "evidence": "appearance-and-space-v5.md؛ تصاویر واقعاً دیده و مقایسه شدند."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "نگاه سمت راست لنز به فرهادِ پیش‌زمینه؛ صورت فرهاد پوشیده است."
    },
    "geometry": {
      "status": "pass",
      "evidence": "قاب نزدیک v5 پس‌زمینه ناسازگار را حذف کرد؛ فقط ناحیه محدود خانه دیده می‌شود، فاصله صندلی‌ها اندازه‌گیری نشده و حرکت صندلی نداریم."
    },
    "continuity": {
      "status": "pass",
      "evidence": "دامنه یک آزمون مستقل: نازلی نشسته، دست خالی، میز خارج برش. اتصال واقعی۷و۹ پس از وجود ویدیوها شرط تدوین نهایی است، نه ادعای کنترل انجام‌شده."
    },
    "camera": {
      "status": "pass",
      "evidence": "ثابت، متوسط نزدیک، محور فرهاد به نازلی حفظ."
    },
    "prompt": {
      "status": "pass",
      "evidence": "prompt.txt شامل متن دقیق و ابتدا/پایان و تنها یک گوینده."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "ویدیویی برای این نما موجود نیست؛ عکس ثابت جای اجرای گفتار نیست."
    },
    "settings": {
      "status": "pass",
      "evidence": "Omni1.1 Flash Frames 4s360p9:16 x1 در رابط داخلی دیده شد؛ قاب v5 بارگذاری و انتخاب شد؛ متن کامل در رابط با prompt.txt تطبیق داده شد؛ تنظیم۴ثانیه/۳۶۰/عمودی/x1 و قیمت۴اعتبار بازخوانی شدند. شاهد ui-ready-for-approval.png؛ درست پیش از تولید دوباره تطبیق شود."
    },
    "speaker": {
      "status": "pass",
      "evidence": "User explicitly approved one independent native-model-voice take after full prompt, corrected v5 frame and lack of voice-identity guarantee disclosed. Only Nazli speaks; generated voice/lips are post-generation acceptance criteria."
    },
    "cost": {
      "status": "pass",
      "evidence": "User این تأیید in direct response to exact four-credit single four-second take package; live UI re-read four credits. No retry."
    }
  },
  "content_approval": {
    "approved": true,
    "bundle_sha256": "7f7e05e449cba75a4e4e200702464d4797d7ca70c65e7e905e7737a6eb29e11c",
    "user_reply": "این تأیید. ولی تاییدهای بعدی رو هم تو باید به من باتن نشون بدی.",
    "evidence_ref": "Current chat: direct response to full SH08 prompt/frame/native-voice experimental scope and explicit four-credit one-attempt quote."
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "7f7e05e449cba75a4e4e200702464d4797d7ca70c65e7e905e7737a6eb29e11c",
    "user_reply": "این تأیید. ولی تاییدهای بعدی رو هم تو باید به من باتن نشون بدی.",
    "evidence_ref": "Current chat: direct response to full SH08 prompt/frame/native-voice experimental scope and explicit four-credit one-attempt quote."
  },
  "consumed_attempts": 1,
  "bundle_sha256": "7f7e05e449cba75a4e4e200702464d4797d7ca70c65e7e905e7737a6eb29e11c"
}
```
<!-- /preflight-state -->

## تأیید و تطبیق زنده

کاربر همین بسته و سقف۴اعتبار را صریحاً تأیید کرد؛ تأییدهای بعدی با گزینه‌های قابل‌کلیک ارائه شوند. متن/قاب/مدت/کیفیت/تعداد/قیمت در تب داخلی قسمت۳ دوباره تطبیق داده شدند؛ یک تلاش مجاز و هنوز مصرف نشده است. محدودیت هویت صدای خروجی محفوظ است.

یک‌بار دکمهٔ تولید با قیمت۴اعتبار فشرده شد؛ مجوز یک تلاش مصرف شده و ارسال مجدد ممنوع است. شاهد ui-submitted-once.png؛ خروجی در انتظار تکمیل.
