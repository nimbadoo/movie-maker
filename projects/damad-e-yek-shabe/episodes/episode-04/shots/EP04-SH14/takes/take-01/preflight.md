# آماده‌سازی نمای چهاردهم — بستهٔ بازگشت

[قاب شروع](../../images/EP04-SH14-start-v2.png) · [پرامپت کامل](prompt.txt) · [گزارش فضایی](../../spatial-review-v2.md) · [قیمت زنده](flow-cost-check-v1.jpg).

قاب جاری دوباره دیده شد. سامان چپ و نازلی راست، فرهاد نشسته پایین راست؛ خانه و ایستگاه دوربین مقابل در بررسی پیشین تطبیق داده شده‌اند. آشپزخانه پشت دوربین، تلویزیون چپ و پنجره راست است. تناقض متن قدیمی «نازلی چپ سامان» اصلاح شد؛ خود تصویر تغییر نکرد. در منبع۱۱نازلی چرخش به خروج را آغاز می‌کند؛ مسیر کامل تا پذیرایی با حذف زمان کنار گذاشته می‌شود. چون قاب۱۴از حالت ایستاده شروع می‌شود، فقط آرام‌گرفتن بدن داریم؛ نه قدم/نشستن/جابجایی صندلی. اتصال واقعی ویدیو۱۴به۱۲پس از تولید قابل‌کنترل است.

بی‌گفتار؛ زمان‌گیری گفتار نامرتبط است. سهم مصرف۱٫۵ثانیه پیشنهادی برای استقرار، نه کل راه‌رفتن است. منبع ویدیویی موجود با همین استقرار نداریم؛ ثابت‌کردن عکس به‌جای حرکت طبیعی، معادل اجرای مصوب نیست. تدوین عادی محلی خواهد بود.

پیشنهاد همان `Omni 1.1 Flash`، روش `Frames`، فقط این قاب شروع، `360p`، `9:16`،۸ثانیه و یک خروجی است؛ صدای محیط بدون دیالوگ. قیمت زنده۶اعتبار، سقف۶برای یک ارسال و بدون تکرار. هیچ ارسال تازه یا مصرف اعتباری انجام نشده؛ هزینه و بسته نیازمند تأیید صریح‌اند. پیش از ارسال، بستهٔ اثرانگشت‌دار و تطبیق تنظیمات نهایی تکمیل شود؛ این آماده‌سازی مجوز ارسال نیست.

<!-- preflight-state -->
```json
{
  "shot": "EP04-SH14",
  "take": "take-01",
  "ready": true,
  "reviewed_at": "2026-10-15T19:39:37.113743+00:00",
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Silent canonical shot; no old D14 dialogue valid."
    },
    "delivery": {
      "status": "pass",
      "evidence": "No speech sigh laugh or music; faint continuous house ambience only."
    },
    "duration": {
      "status": "pass",
      "evidence": "No dialogue timing applicable;1.5s settling target only, no full walk,8s generation handles."
    },
    "performance": {
      "status": "pass",
      "evidence": "Standing start from approved frame, tiny natural settling/weight only; no step sit or contact."
    },
    "speaker": {
      "status": "pass",
      "evidence": "All silent, no speech lip movement; mother outside frame stays seated."
    },
    "identity": {
      "status": "pass",
      "evidence": "Actual approved frame14 seen; Saman left blue finegrid shirt curls stubble; Nazli right teal/brown hair; Farhad back cream shirt right foreground; hidden face not inferred."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Saman/Nazli look toward seated Farhad down/right; not lens."
    },
    "geometry": {
      "status": "pass",
      "evidence": "Frame14 viewed with shared house prior prep: kitchen/corridor behind camera, TV left window right; fixed angled chairs/table/tray/teacup no rearrangement."
    },
    "continuity": {
      "status": "pass",
      "evidence": "11 turn toward exit then time ellipsis to14 standing by chairs; no walking repeated; downstream12 question from same east side as card, actual video continuity pending."
    },
    "camera": {
      "status": "pass",
      "evidence": "Static approved external Farhad shoulder station, no pan zoom refocus."
    },
    "prompt": {
      "status": "pass",
      "evidence": "Exact displayed approved Persian prompt and frame hash retained, no speech text; first frame only."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video of return settling. Static still does not provide approved natural action. Normal edit local."
    },
    "settings": {
      "status": "pass",
      "evidence": "Live Frames360p9:16,8sx1,Omni1.1Flash verified current UI; no unsupported imported audio."
    },
    "cost": {
      "status": "pass",
      "evidence": "Current live6credits,one submission, ceiling6,no retry; exact explicit user approval."
    }
  },
  "consumed_attempts": 1,
  "bundle_sha256": "70cde29488e59f77e5235c5b8e81df25877d9c5d541735e3e12756675061fbe2",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "70cde29488e59f77e5235c5b8e81df25877d9c5d541735e3e12756675061fbe2",
    "user_reply": "تأیید، نمای چهاردهم رو با همین پرامپت و قاب و سقف ۶ اعتبار تولید کن.",
    "evidence_ref": "Current explicit human approval of fully displayed unchanged SH14 prompt frame and6credit ceiling"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "70cde29488e59f77e5235c5b8e81df25877d9c5d541735e3e12756675061fbe2",
    "user_reply": "تأیید، نمای چهاردهم رو با همین پرامپت و قاب و سقف ۶ اعتبار تولید کن.",
    "evidence_ref": "Current explicit human approval of fully displayed unchanged SH14 prompt frame and6credit ceiling"
  }
}
```
<!-- /preflight-state -->
