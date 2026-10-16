# بررسی نهایی نمای۸ — آمادهٔ تأیید، ارسال مسدود

[پرامپت کامل](prompt.txt) · [قاب شروع](../../images/EP04-SH08-start-v1.png) · [زمان‌گیری تمرین](../../timing-review-v1.md) · [شاهد قیمت](flow-cost-check-v1.jpg) · [کارت مالک](../../shot.md).

قاب و خانه و زاویهٔ مقابل۹ دیده شدند؛ یخچال چپ و دیوار کرم راست، سامان راست/مرکز رو به چشم نازلی در چپ/پایین و شانهٔ او در چپ، همان محور۶است. چهره/مو/ته‌ریش و پیراهن آبی سامان با مرجع بررسی‌شده تطبیق دارند؛ نازلی فقط پشت مو/شانه دارد. دوربین ثابت و بدون راه‌رفتن/تماس/کنش در یا وسیله است. بخش پوشیده اندازه‌گیری یا تأیید نشده؛ کنش مرتبطِ قابل‌پیشگیری در این نما وجود ندارد. اتصال واقعی و لب در خروجی بعدی بازبینی می‌شوند.

تمرین زمان‌گیری شد: بازهٔ محافظه‌کارانه۳٫۷۶ثانیه، با حاشیه۴٫۱۶؛ سهم پیشنهادی۴٫۲۵ثانیه و تخمین کل۴۹٫۷۵است. متن تشخیص تمرین اختلاف‌هایی دارد که در گزارش محفوظ‌اند؛ تنها دیالوگ اعراب‌گذاری‌شدهٔ کارت تولید می‌شود. تمرین به مدل فرستاده نمی‌شود و بازبینی شنیداری ادعا نشده است.

پیشنهاد دقیق: `Omni 1.1 Flash`، `Frames` با فقط قاب شروع، عمودی `9:16`، `360p`،۸ثانیه، یک خروجی، صدای اصلی؛ قیمت زنده۶اعتبار و سقف۶برای یک ارسال. تبدیل خودکار صدا نداریم؛ مرجع مشترک سامان عوض نشده و صدای خروجی با آن و اجرای پذیرفتهٔ۶مقایسه خواهد شد. واردکردن نمونهٔ صوت به این مدل ادعا نمی‌شود و کیفیت صدا/لب/فارسی تضمین نیست.

تمام بررسی‌های پیش از تولید برای طراحی و ورودی‌ها انجام شده‌اند؛ ثبات ویدیو، تلفظ و بازی و لب واقعی پس از خروجی بررسی می‌شوند. هیچ فایل/پرامپت نمای۸ بارگذاری نشده و هزینه‌ای مصرف نشده. تأیید محتوا و هزینهٔ این بسته هنوز لازم است؛ تلاش مجدد خودکار یا تولید سایر نماها از این مجوز پوشش نمی‌گیرند.

<!-- preflight-state -->
```json
{
  "shot": "EP04-SH08",
  "take": "take-01",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Canonical EP04-D08 retained with diacritics; first part question, second declarative."
    },
    "duration": {
      "status": "pass",
      "evidence": "../../timing-review-v1.md: actual rehearsal ASR span3.76s; text differences recorded, not canonical rewrite.4.16s conservative with margins, proposed4.25s target; generation8s unchanged."
    },
    "performance": {
      "status": "pass",
      "evidence": "Actual question, dry humor, slight eyebrow raise without laughter; sole speaker Saman; others silent."
    },
    "geometry": {
      "status": "pass",
      "evidence": "House and frames08/09 viewed, refrigerator left and creamwall right behind Saman, reciprocal north stove/cabinets behind Nazli; axis preserved. No contact/walk/door action."
    },
    "identity": {
      "status": "pass",
      "evidence": "Frame08 compared to previously reviewed06 and identity/costume baseline; blue grid shirt, dark curly hair and short stubble. Nazli back hair/teal shoulder only, hidden face not inferred."
    },
    "camera": {
      "status": "pass",
      "evidence": "Same static shoulder view as06; no crop or new image; eyeline left/down."
    },
    "continuity": {
      "status": "pass",
      "evidence": "Accepted07 ends looking right/up;08 looks left/down to Nazli,09 reverse consistent. No change in standing marks. Actual new media connection pending generation."
    },
    "prompt": {
      "status": "pass",
      "evidence": "Exact approved line once; instructions separate. No unsupported claim of importing WAV reference."
    },
    "cost": {
      "status": "pass",
      "evidence": "Live price6credits; one submission/output,ceiling6,no retries. No cost approval yet."
    },
    "delivery": {
      "status": "pass",
      "evidence": "Canonical question then declarative response; no added آخه. Low clear volume and dry humor, no whisper/laughter. Rehearsal listening not claimed and recording is not a production input."
    },
    "speaker": {
      "status": "pass",
      "evidence": "Saman only voice and lips, Nazli hidden mouth silent; others outside frame silent."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Saman left/down at Nazli eyes, accepted07 reverse looks right/up; no lens gaze."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video of D08. Reusing D06 speech changes text and cannot supply this performance; static input not substitute. No auto voice conversion."
    },
    "settings": {
      "status": "pass",
      "evidence": "Live UI: Omni1.1Flash/Frames/360p/9:16/8s/x1. flow-cost-check-v1.jpg; recheck exact files/settings/price immediately before submission."
    }
  },
  "content_approval": {
    "approved": true,
    "bundle_sha256": "010fdf9a8336f8f1cd7d2c389d6742683780e7efc2888440462335a63e653630",
    "user_reply": "تأیید",
    "evidence_ref": "Current user approves displayed EP04-SH08 package Omni1.1Flash,360p,8s,x1,ceiling6credits"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "010fdf9a8336f8f1cd7d2c389d6742683780e7efc2888440462335a63e653630",
    "user_reply": "تأیید",
    "evidence_ref": "Current user approves displayed EP04-SH08 package Omni1.1Flash,360p,8s,x1,ceiling6credits"
  },
  "consumed_attempts": 1,
  "reviewed_at": "2026-10-15T16:57:57Z",
  "bundle_sha256": "010fdf9a8336f8f1cd7d2c389d6742683780e7efc2888440462335a63e653630"
}
```
<!-- /preflight-state -->
