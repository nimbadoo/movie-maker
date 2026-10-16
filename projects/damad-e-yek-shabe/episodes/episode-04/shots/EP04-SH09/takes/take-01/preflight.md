# بررسی نهایی نمای۹ — آمادهٔ تأیید، ارسال مسدود

[پرامپت کامل](prompt.txt) · [قاب شروع](../../images/EP04-SH09-start-v1.png) · [زمان‌گیری و حدود آن](../../timing-review-v1.md) · [شاهد قیمت زنده](flow-cost-check-v1.jpg) · [کارت مالک](../../shot.md).

پایان ویدیوی منتخب۸، قاب۹و قاب۱۰واقعاً دیده و لباس، جهت نگاه و محور و صاحب شانه مقایسه شدند. نازلی چپ/مرکز با نگاه راست/بالا و سامان راست پیش‌زمینه است؛ کابینت/اجاق پشت نازلی و یخچال/دیوار پشت سامان در نمای مقابل سازگارند. خانه و هویت/لباس طبق بررسی پیشین حفظ‌اند. نازلی ثابت و فقط دوربین پیشروی بسیار کوتاه مصوب دارد؛ بدون کنش در/دست/وسیله. اجرای واقعی حرکت و ثبات چهره در خروجی بررسی می‌شوند؛ اندازهٔ دقیق۱۰سانتی‌متر تضمین نیست.

تمرین، اجرای دقیق متن کوتاه معرفی نشده؛ متن خودکار بلندتر است. بازهٔ محافظه‌کارانهٔ۰تا۳٫۹۲۳با حاشیه۴٫۳۲۳ثانیه می‌خواهد، پس ظرفیت تدوین۴٫۵در نظر گرفته شد. این ظرفیت به معنی کشیدن جمله نیست. متن کوتاه مصوب بدون واژهٔ اضافه وارد تولید می‌شود و فایل تمرین وارد مدل نمی‌شود؛ بازبینی شنیداری ادعا نشده است.

مدل `Omni 1.1 Flash`، روش `Frames` با فقط قاب شروع، کیفیت `360p`، عمودی،۸ثانیه و یک خروجی با صدا؛ قیمت زنده۶اعتبار، سقف۶، یک ارسال و بدون تکرار. صدای اصلی تولید مبناست؛ تبدیل خودکار صدا انجام نمی‌شود. مرجع مشترک نازلی محفوظ است و خروجی با آن و اجرای پذیرفتهٔ۷مقایسه می‌شود؛ هویت صدا/فارسی/لب تضمین نیست.

قاب مستقل همین نما تنها ورودی ارسالی است؛ خانه و تصاویر قبلی منابع بررسی محلی‌اند، نه قاب پایان. هیچ رسانه/پرامپتی برای نمای۹بارگذاری نشده؛ تأیید دقیق محتوا و هزینه هنوز لازم است. بازبینی متن، طراحی و ورودی‌ها تکمیل شده؛ صدا/لب و حرکت واقعی پس از تولید پذیرش می‌شوند. درست پیش از ارسال، فایل و پرامپت و مدل و تنظیم و قیمت دوباره تطبیق داده شوند.

<!-- preflight-state -->
```json
{
  "shot": "EP04-SH09",
  "take": "take-01",
  "reviewed_at": "2026-10-15T17:39:49Z",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Exact EP04-D09 short approved sentence with diacritics, only once; rehearsal extra words not adopted."
    },
    "delivery": {
      "status": "pass",
      "evidence": "Low clear conversational voice, sincere concern, mild emphasis مادرتو هم; not humorous or breathy whisper. Rehearsal listening not claimed; recording not production input."
    },
    "duration": {
      "status": "pass",
      "evidence": "../../timing-review-v1.md: broader rehearsal upper bound0..3.923s, with margins4.323s; allocate4.5s capacity and generate8s. Not claimed exact canonical reading; final edit follows actual full sentence."
    },
    "performance": {
      "status": "pass",
      "evidence": "Serious concern to protect Saman mother from lie; body stays still, no new contact/gesture/walk. User humor feedback about08 does not rewrite this serious beat."
    },
    "speaker": {
      "status": "pass",
      "evidence": "Nazli sole speaker and lips; Saman right foreground silent. Mother/Farhad outside frame silent."
    },
    "identity": {
      "status": "pass",
      "evidence": "Actual frame09 viewed alongside accepted08 end and frame10. Nazli face/brown shoulder hair/teal buttonshirt consistent with earlier approved07; Saman partial profile hair/stubble/blue grid shirt, hidden features not inferred."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Nazli looks right/up at Saman; accepted08 looks left/down, same axis and standing relation; no lens gaze."
    },
    "geometry": {
      "status": "pass",
      "evidence": "House master reviewed previously; frame09 north cabinets/stove behind Nazli, reverse10 fridge left and creamwall right behind Saman. No new door/prop. Feet/hands outside frame not measured; no related action requested."
    },
    "continuity": {
      "status": "pass",
      "evidence": "Accepted08 last frame actually viewed; matches costume, eyeline and shoulder ownership. Frame09 to10 same axis; camera push only, bodies remain fixed. Real moving-media connection pending output."
    },
    "camera": {
      "status": "pass",
      "evidence": "Approved straight gentle push up to about10cm during speech, ending before last word; no orbit/cross-axis/zoom/refocus. Exact metric movement cannot be guaranteed by generator and will be checked in output."
    },
    "prompt": {
      "status": "pass",
      "evidence": "Full Persian prompt separates instructions from one approved line; no unsupported WAV input claim; no added words; request repeats no dialogue."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing D09 performance video. Static frame and rehearsal cannot replace talking Nazli. Prefer original generated voice, no automatic conversion; normal editing local."
    },
    "settings": {
      "status": "pass",
      "evidence": "Live account UI:Omni1.1Flash Frames360p9:16 8s x1; flow-cost-check-v1.jpg. First frame only, no ending/audio reference upload; exact live binding recheck before submission."
    },
    "cost": {
      "status": "pass",
      "evidence": "Live displayed6credits, one output and one submission,ceiling6,no retry. No content/cost approval yet."
    }
  },
  "content_approval": {
    "approved": true,
    "bundle_sha256": "b931cb131108b73b5ae77c408d5c95ecdc64ab035f20c58c9399db06061be7a9",
    "user_reply": "تأیید",
    "evidence_ref": "Current user approves displayed EP04-SH09 exact prompt/frame Omni1.1Flash360p8sx1 ceiling6credits"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "b931cb131108b73b5ae77c408d5c95ecdc64ab035f20c58c9399db06061be7a9",
    "user_reply": "تأیید",
    "evidence_ref": "Current user approves displayed EP04-SH09 exact prompt/frame Omni1.1Flash360p8sx1 ceiling6credits"
  },
  "consumed_attempts": 1,
  "bundle_sha256": "b931cb131108b73b5ae77c408d5c95ecdc64ab035f20c58c9399db06061be7a9"
}
```
<!-- /preflight-state -->
