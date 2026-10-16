# اصلاح آهنگ سؤال مادر — پیش‌نویس، ارسال نشده

۲۰۲۶/۱۰/۱۵؛ برداشت۲ مستقل از تلاش هزینه‌دار قبلی. بازبینی شنیداری کاربر: پایان برداشت۱ خبری شنیده می‌شود. [پرامپت اصلاحی کامل](prompt.txt)؛ قاب شروع همان [نسخه۴](../../images/EP03-SH12-open-kitchen-v4.png) است؛ تصویر، متن، لباس و دوربین تغییر نکرده‌اند.

## علت و دامنهٔ اصلاح

در پرامپت قبلی «پرسشی ملایم» و علامت سؤال وجود داشت، اما خروجی طبق شنیدن کاربر این جهت را اجرا نکرد. علت داخلی مدل معلوم نیست؛ کافی‌نبودن دستور قبلی یک برداشت از نتیجه است، نه تشخیص قطعی. اصلاح پیشنهادی بر روند شنیدنی زیر و بمی در «خَبَر دارَن؟»، بی‌خبری واقعی مادر و انتظار جواب تمرکز دارد؛ بدون تغییر واژه، فریاد، مکث نمایشی یا کشیدن هجا.

ویرایش دستی زیر و بمیِ چند نمونهٔ انتهایی، تضمین ساختن سؤال طبیعی یا حفظ هویت صدا نیست و اجرا نشده. افزودن سکوت یا کوتاه‌کردن پایان نیز لحن خبری را اصلاح نمی‌کند. منبع قبلی محفوظ است. اجرای دقیق تازه و صدای مرجع همچنان تضمین نشده‌اند؛ اگر شاهد صوتیِ مناسب برای همان جهت در ابزار قابل‌استفاده باشد، پیش از تکرار هزینه‌دار بررسی شود. قیمت تاریخی۵اعتبار مبنای تأیید تازه نیست؛ این نوبت قیمت زنده بررسی نشده و هزینه‌ای ارسال نشده است.

جهت سؤال روشن، درخواست صریح کاربر است؛ اما تأیید بسته و هزینهٔ تلاش تازه هنوز نداریم. تولید خودکار انجام نشود. در بازبینی خروجی، گوش‌دادن به روند پایان جمله معیار است؛ متن و علامت سؤالِ تشخیص گفتار جای آن را نمی‌گیرد.

<!-- preflight-state -->
```json
{
  "shot": "EP03-SH12",
  "take": "take-02",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Exact approved D12 extracted from shot.md with diacritics; no rewrite.",
      "reason": ""
    },
    "delivery": {
      "status": "pass",
      "evidence": "Explicit audible final rise on خبر دارن, no declarative falling cadence, no word stretching. Targeted correction derived from user auditory feedback; future model execution remains unguaranteed.",
      "reason": ""
    },
    "duration": {
      "status": "pass",
      "evidence": "Measured synthetic espeak-ng fa165 rehearsal 3.229977s; not actor audio or auditory verification. Six-second recording leaves 2.770s combined margin, not permission to slow delivery.",
      "reason": ""
    },
    "performance": {
      "status": "pass",
      "evidence": "Same approved cautious curiosity2/5; genuinely seeks Saman answer and retains gaze after question. No new dominant action.",
      "reason": ""
    },
    "speaker": {
      "status": "pass",
      "evidence": "Only mother speaking; Saman mouth hidden, Farhad face occluded by Saman. Native experimental output, voice identity must be reviewed; no unapproved voice substitution.",
      "reason": ""
    },
    "identity": {
      "status": "pass",
      "evidence": "appearance-and-space-v4.md: output and approved canonical mother panel actually viewed; gray hair single scarf and burgundy tunic, cream Farhad and blue Saman visible areas checked.",
      "reason": ""
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Mother eyes toward foreground Saman right of lens, not directly camera. Exact moving eyeline must be reviewed after generation.",
      "reason": ""
    },
    "geometry": {
      "status": "pass",
      "evidence": "Open kitchen behind sofa consistent with viewed cutaway-v2; old narrow doorway removed; foreground Saman and partly occluded Farhad on correct sides. Chairs/tea outside crop, no handling action.",
      "reason": ""
    },
    "continuity": {
      "status": "pass",
      "evidence": "After accepted Nazli D11 before Saman D13; room and clothes unchanged, no new props in crop. No final adjacent-video assembly claim.",
      "reason": ""
    },
    "camera": {
      "status": "pass",
      "evidence": "Static OTS Saman to mother from guest-chair side, seated eye-level. No chair or camera rotation.",
      "reason": ""
    },
    "prompt": {
      "status": "pass",
      "evidence": "Owner dialogue and diacritics unchanged and checked in full revised prompt; only question prosody instructions strengthened; actual textbox matches file.",
      "reason": ""
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video in SH12 folder; corrected still via built-in image_gen, original preserved. Static-frame extension cannot create spoken question.",
      "reason": ""
    },
    "settings": {
      "status": "pass",
      "evidence": "Live UI and screenshot actually viewed: same v4 first frame, Omni1.1 Flash Frames, 6s360p9:16 x1; no submission.",
      "reason": ""
    },
    "cost": {
      "status": "pass",
      "evidence": "Live UI explicitly shows5credits for this single six-second attempt; proposed ceiling5, attempts1; fresh user cost approval still pending.",
      "reason": ""
    }
  },
  "bundle_sha256": "474f07c20dcff4b3d26d4afa492f1c5420415572289642ad89d93c9935f61285",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "474f07c20dcff4b3d26d4afa492f1c5420415572289642ad89d93c9935f61285",
    "user_reply": "تأیید",
    "evidence_ref": "User تأیید after SH12 take02 explicit revised question-prosody package and live five-credit single-output quote."
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "474f07c20dcff4b3d26d4afa492f1c5420415572289642ad89d93c9935f61285",
    "user_reply": "تأیید",
    "evidence_ref": "User تأیید after SH12 take02 explicit revised question-prosody package and live five-credit single-output quote."
  },
  "consumed_attempts": 1
}
```
<!-- /preflight-state -->

## آمادهٔ مرور نهایی

تمام کنترل‌های محتواییِ مرتبط با تغییر بررسی شدند؛ دستور قبلی به‌تنهایی نتیجه نداده بود و اکنون روند شنیدنی پایان و قصد گرفتن جواب صریح شده‌اند. مدل همچنان ممکن است اجرا را رعایت نکند؛ تشخیص گفتار معیار قبولی لحن نیست. همان قاب و متن و تنظیم۶ثانیه/۳۶۰/یک خروجی در رابط واقعی آماده‌اند؛ [شاهد](ui-ready-for-approval.png). قیمت زنده **۵اعتبار برای یک تلاش اصلاحی**؛ تکرار خودکار ندارد. کاربر گفت «تایید می‌کنم، سریع باش، برو جلو، سریع»؛ اجازهٔ ادامهٔ آماده‌سازی محفوظ است، اما چون قیمت همین تلاش هنوز قبل از آن پاسخ به‌طور مشخص اعلام نشده بود، تأیید هزینهٔ جدید ثبت نشده. هیچ دکمه تولیدی فشرده نشد.

## تأیید همین بسته

کاربر پس از نمایش پرامپت کامل، قاب نسخه۴ و قیمت زنده۵اعتبار گفت «تأیید»؛ یک ارسال۶ثانیه‌ای با سقف۵اعتبار مجاز شد. کنترل زنده پیش از ارسال با همین بسته برابر بود.

## نتیجهٔ اجرا

همان بسته یک‌بار با قیمت۵اعتبار ارسال و موفق شد؛ [بازبینی و محدودیت‌ها](review.md) جداست. فایل اصلی ذخیره شد؛ نمونهٔ۴٫۵ثانیه‌ای صدای اصلی را دارد. مجوز یک ارسال مصرف و درخواست کارت خالی شد؛ تکرار مجاز نیست.
