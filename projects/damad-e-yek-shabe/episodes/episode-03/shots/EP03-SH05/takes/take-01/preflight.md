# بررسی پیش از ارسال نمای۵ — پیش‌نویس، تولید نشده

۲۰۲۶/۱۰/۱۵. [پرامپت کامل](prompt.txt) · [کارت مالک](../../shot.md) · [قاب شروع](../../images/EP03-SH05-interest-question-v3.png) · [ضبط تمرینی کاربر](../../audio/user-dialogue-05.m4a) · [تبار ضبط](../../audio/user-dialogue-05-lineage.json).

قاب شروع، خانه از بالا و تصویر هویت خانواده در این نوبت واقعاً دیده شدند. مادر چپ کاناپه، فرهاد راست، سامان پیش‌زمینه راست و نازلی خارج قاب است. آشپزخانه پشت کاناپه، پنجره چپ و نبود چای با این مقطع داستان سازگارند. هندسه اندازه‌گیری نشده و اتصال واقعی به ویدیوی قبلی هنوز کنترل نشده است.

متن و جهت بازی مصوب عین کارت حفظ شدند؛ دو جمله خبری با دعوت آرام به پاسخ، شدت۲از۵، نگاه به سامان و دست‌ها آرام. [مرجع صدا](../../../../../../references/voice/voice-bible.md) مستقل از تمرین کاربر است. فقط مادر گوینده است؛ شنونده‌ها ساکت و لب سامان خارج دید.

ضبط انسانی۵٫۳۱ثانیه است؛ تحلیل ماشینی قبلی پایان گفتار۴٫۶۸ثانیه را ثبت کرده و دو کلمه را متفاوت تشخیص داده است. مدت فایل با `afinfo` نیز۵٫۳۱۰۶۶۷ثانیه و۴۸کیلوهرتز مونو تأیید شد. این نوبت شنیدن انجام نشده؛ متن مصوب با رونویسی ماشینی جایگزین نشده است. پیشنهاد کلیپ۶ثانیه با ریتم طبیعی است؛ مدت تدوین پس از خروجی و بدون بریدن کلمه تعیین شود. محدودیت یک دقیقه برای کل قسمت با مدتهای منتخب فعلی قابل‌حفظ فرض نشود.

در مرورگر داخلی، پروژه صحیح قسمت۳ باز شد؛ تنظیم فعلی `Omni 1.1 Flash`، مسیر `Frames`، عمودی `9:16`، کیفیت `360p`، مدت۶ثانیه، یک خروجی و قیمت۵اعتبار واقعاً مشاهده شد. قاب/صوت بارگذاری و تولید ارسال نشده‌اند. [شاهد تنظیمات و قیمت زنده](ui-price-6s.png). قیمت باید درست پیش از ارسال بازخوانی شود. مسیر حفظ هویت صدای مادر و تأیید نسخه/هزینه هنوز باز است. درخواست عمومی شروع، مجوز اعتبار نیست.

## نتیجه

**آمادهٔ ارسال نیست.** فقط آماده‌سازی محلی انجام شده؛ هزینه خارجی صفر. هر مورد باز پایین باید قبل از تولید بسته شود و بسته نهایی با پرامپت کامل، ورودی‌ها و هزینه به کاربر نشان داده شود.

<!-- preflight-state -->
```json
{
  "shot": "EP03-SH05",
  "take": "take-01",
  "ready": false,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Approved exact shot dialogue and diacritics from shot.md in2shot10credit batch"
    },
    "delivery": {
      "status": "pass",
      "evidence": "Approved performance in shot.md; complete declarative final word"
    },
    "duration": {
      "status": "pass",
      "evidence": "Actual user recording5.311sec SH05 or4.799sec SH06, reference manifest;6sec gives margin; no synthetic rehearsal substituted"
    },
    "performance": {
      "status": "pass",
      "evidence": "Static seated dialogue, approved performance; no new action or tea"
    },
    "speaker": {
      "status": "pass",
      "evidence": "Only mother SH05 or Saman SH06 owns dialogue, all other listeners silent; native voice identity not guaranteed"
    },
    "identity": {
      "status": "pass",
      "evidence": "Actually viewed corrected shot frame with same faces/clothes from prior approved reference; occluded listener face not claimed visible"
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Approved frame gaze to each other; prompt prohibits lens gaze; future movement requires review"
    },
    "geometry": {
      "status": "pass",
      "evidence": "preflight.md: SH05 corrected open kitchen behind sofa; SH06 reverse warm wall TV side with no duplicated rug/window/bookcase, dimensions unmeasured"
    },
    "continuity": {
      "status": "pass",
      "evidence": "After accepted shared sitting, all seated fixed positions; Nazli kitchen offscreen, no tea yet; SH05 thenSH06"
    },
    "camera": {
      "status": "pass",
      "evidence": "Static vertical camera near guest chairs; approved corrected starting frame"
    },
    "prompt": {
      "status": "pass",
      "evidence": "Unchanged SHA from exact approved package; full live editor matched"
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video of this dialogue; corrected only necessary image background"
    },
    "settings": {
      "status": "pass",
      "evidence": "Live IAB Frames9:16 360p6s x1, model Omni1.1Flash shown in prepared screenshot"
    },
    "cost": {
      "status": "pass",
      "evidence": "Live5credits; current user تأیید approves exact one-attempt5credit package"
    }
  },
  "consumed_attempts": 1,
  "bundle_sha256": "1f2b0d90e7189138fab8835723045ee35161e3593ca0fa0fc9fb5a17a9c9a614",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "1f2b0d90e7189138fab8835723045ee35161e3593ca0fa0fc9fb5a17a9c9a614",
    "user_reply": "تأیید",
    "evidence_ref": "Current approval of exact SH15 SH056second360p one attempt5credits within approved10credit batch"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "1f2b0d90e7189138fab8835723045ee35161e3593ca0fa0fc9fb5a17a9c9a614",
    "user_reply": "تأیید",
    "evidence_ref": "Current approval of exact SH15 SH056second360p one attempt5credits within approved10credit batch"
  },
  "submission_state": "completed_one_attempt_no_retry"
}
```
<!-- /preflight-state -->


تأیید همین بسته: کاربر با «تأیید» یک ارسال با سقف۵اعتبار را پذیرفت؛ تکرار مجاز نیست.

<!-- preflight-state -->
```json
{
  "shot": "EP03-SH05",
  "take": "take-01",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Approved exact shot dialogue and diacritics from shot.md in2shot10credit batch"
    },
    "delivery": {
      "status": "pass",
      "evidence": "Approved performance in shot.md; complete declarative final word"
    },
    "duration": {
      "status": "pass",
      "evidence": "Actual user recording5.311sec SH05 or4.799sec SH06, reference manifest;6sec gives margin; no synthetic rehearsal substituted"
    },
    "performance": {
      "status": "pass",
      "evidence": "Static seated dialogue, approved performance; no new action or tea"
    },
    "speaker": {
      "status": "pass",
      "evidence": "Only mother SH05 or Saman SH06 owns dialogue, all other listeners silent; native voice identity not guaranteed"
    },
    "identity": {
      "status": "pass",
      "evidence": "Actually viewed corrected shot frame with same faces/clothes from prior approved reference; occluded listener face not claimed visible"
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Approved frame gaze to each other; prompt prohibits lens gaze; future movement requires review"
    },
    "geometry": {
      "status": "pass",
      "evidence": "preflight.md: SH05 corrected open kitchen behind sofa; SH06 reverse warm wall TV side with no duplicated rug/window/bookcase, dimensions unmeasured"
    },
    "continuity": {
      "status": "pass",
      "evidence": "After accepted shared sitting, all seated fixed positions; Nazli kitchen offscreen, no tea yet; SH05 thenSH06"
    },
    "camera": {
      "status": "pass",
      "evidence": "Static vertical camera near guest chairs; approved corrected starting frame"
    },
    "prompt": {
      "status": "pass",
      "evidence": "Unchanged SHA from exact approved package; full live editor matched"
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video of this dialogue; corrected only necessary image background"
    },
    "settings": {
      "status": "pass",
      "evidence": "Live IAB Frames9:16 360p6s x1, model Omni1.1Flash shown in prepared screenshot"
    },
    "cost": {
      "status": "pass",
      "evidence": "Live5credits; current user تأیید approves exact one-attempt5credit package"
    }
  },
  "consumed_attempts": 0,
  "bundle_sha256": "1f2b0d90e7189138fab8835723045ee35161e3593ca0fa0fc9fb5a17a9c9a614",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "1f2b0d90e7189138fab8835723045ee35161e3593ca0fa0fc9fb5a17a9c9a614",
    "user_reply": "تأیید",
    "evidence_ref": "Current approval of exact SH15 SH056second360p one attempt5credits within approved10credit batch"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "1f2b0d90e7189138fab8835723045ee35161e3593ca0fa0fc9fb5a17a9c9a614",
    "user_reply": "تأیید",
    "evidence_ref": "Current approval of exact SH15 SH056second360p one attempt5credits within approved10credit batch"
  }
}
```
<!-- /preflight-state -->
