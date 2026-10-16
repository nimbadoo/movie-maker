# نمای یازدهم — بستهٔ نهایی آمادهٔ تأیید؛ ارسال مسدود

[پرامپت کامل](prompt.txt) · [قاب شروع](../../images/EP04-SH11-start-v1.png) · [زمان‌گیری](../../timing-review-v1.md) · [شاهد قیمت](flow-cost-check-v1.jpg).

قاب۱۱، پایان واقعی منتخب۱۰، خانه و قاب۱۴واقعاً دیده شدند؛ لباس و مو، نگاه متقابل، جای افراد و پس‌زمینهٔ کابینت/اجاق/یخچال با ایستگاه دوربین تطبیق دارند. میز و صندلی ثابت‌اند؛ کنش تنها تکمیل جمله و آغاز چرخش سر/شانه به خروج پشت دوربین است. عبور کنار میز یا در تازه نداریم. اتصال به۱۴با حذف زمان و دوربین مقابل است؛ اتصال واقعی ویدیو۱۴هنوز قابل‌بررسی نیست.

گفتار تمرینی با مکث حدود۱٫۹۹ثانیه؛ با حاشیه و آغاز چرخش، سهم پیشنهادی۳ثانیه به‌جای۲٫۵است. مجموع تخمینی۴۹٫۵۸ثانیه، مشروط به زمان بقیهٔ نماهاست. شنیدن تمرین یا تأیید لحن از تشخیص خودکار ادعا نشده است.

تنظیم: `Omni 1.1 Flash`، روش `Frames`، فقط قاب شروع، `360p`، عمودی `9:16`،۸ثانیه، یک خروجی همراه صدا. قیمت زنده۶اعتبار؛ سقف۶برای یک ارسال، بدون تلاش مجدد. تمرین به مدل داده نمی‌شود و تبدیل صدا نداریم؛ مرجع اصلی نازلی محفوظ است. ثبات صوتی و اجرای حرکت و لب‌خوانی تضمین نیستند و پس از تولید کنترل می‌شوند.

تنها قاب۱۱ارسال خواهد شد؛ خانه و قاب۱۰/۱۴مرجع بررسی محلی‌اند. هیچ ارسال یا مصرف اعتبار تازه‌ای انجام نشده. تأیید صریح بستهٔ کامل و سقف۶اعتبار لازم است؛ پیش از ارسال قیمت، فایل و پرامپت و تنظیمات دوباره با همین بسته تطبیق داده شوند.

<!-- preflight-state -->
```json
{
  "shot": "EP04-SH11",
  "take": "take-01",
  "ready": true,
  "reviewed_at": "2026-10-15T19:19:01.908009+00:00",
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Exact canonical EP04-D11 باشه. با هَم می‌گیم. preserved with diacritics; rehearsal ASR matches."
    },
    "delivery": {
      "status": "pass",
      "evidence": "Approved reluctant responsible acceptance, low clear volume, short statement, pause and mild emphasis با هم; listening not claimed."
    },
    "duration": {
      "status": "pass",
      "evidence": "timing-review-v1.md actual rehearsal conservative span1.986s +0.4 margins+0.5 estimated turn =2.886s; proposed edit3s, generation8s."
    },
    "performance": {
      "status": "pass",
      "evidence": "Approved small head nod then beginning turn toward existing entrance behind camera after full dialogue; no walking or contact."
    },
    "speaker": {
      "status": "pass",
      "evidence": "Nazli only speaks/lip sync; Saman visible silent mouth closed, parents outside frame silent."
    },
    "identity": {
      "status": "pass",
      "evidence": "Frame11 and accepted10 end actually viewed; Nazli teal shirt brown hair, Saman blue finegrid shirt dark curls stubble consistent in visible areas; hidden face not inferred."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Nazli left looks right/up to Saman eyes, Saman right looks left/down; no lens gaze."
    },
    "geometry": {
      "status": "pass",
      "evidence": "Actual shared roofless house and frame11 viewed: north cabinets/stove, fridge right, floral table/chairs foreground; turn only toward behind camera, no path through furniture/new door."
    },
    "continuity": {
      "status": "pass",
      "evidence": "Accepted10 actual endpoint, frame11 and14 seen; same standing/costume relation;14 opposite camera after time ellipsis reaching chairs. Next actual video pending."
    },
    "camera": {
      "status": "pass",
      "evidence": "Static near kitchen entrance on approved side of axis, existing waist/thigh two-shot retained, no zoom/refocus."
    },
    "prompt": {
      "status": "pass",
      "evidence": "Full Persian prompt matches owner, separates nonspoken directions, exact line once and no unsupported reference audio import."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video performance for D11; earlier lines cannot substitute; editing local, original generated voice retained."
    },
    "settings": {
      "status": "pass",
      "evidence": "Live screenshot flow-cost-check-v1.jpg Omni1.1Flash Frames360p8s9:16x1; only frame11 will be uploaded; recheck before send."
    },
    "cost": {
      "status": "pass",
      "evidence": "Live6credits for one output one attempt; ceiling6, no retry; explicit package and cost approval pending."
    }
  },
  "content_approval": {
    "approved": true,
    "bundle_sha256": "9d7d8dad6817ca2ef76ea29d329c89428a83bc20e68910f9f93d9be4c3f1756d",
    "user_reply": "تأیید",
    "evidence_ref": "Current user explicitly approved exact displayed SH11 package and six-credit ceiling"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "9d7d8dad6817ca2ef76ea29d329c89428a83bc20e68910f9f93d9be4c3f1756d",
    "user_reply": "تأیید",
    "evidence_ref": "Current user explicitly approved exact displayed SH11 package and six-credit ceiling"
  },
  "consumed_attempts": 1,
  "bundle_sha256": "9d7d8dad6817ca2ef76ea29d329c89428a83bc20e68910f9f93d9be4c3f1756d"
}
```
<!-- /preflight-state -->
