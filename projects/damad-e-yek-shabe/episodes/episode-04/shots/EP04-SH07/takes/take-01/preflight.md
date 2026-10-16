# بررسی نهایی نمای۷ — آمادهٔ تأیید، ارسال مسدود

[پرامپت کامل](prompt.txt) · [قاب مصوب](../../images/EP04-SH07-start-v1.png) · [کارت مالک](../../shot.md) · [زمان‌گیری](../../timing-review-v1.md) · [شاهد قیمت زنده](flow-cost-check-v1.jpg).

قاب۷، قاب۸ و خانه دیده و تطبیق داده شدند؛ جهت نگاه، لباس، سمت کابینت/اجاق و یخچال، ایستادن و دوربین ثابت سازگارند. اندازهٔ واقعیِ قاب مصوب حفظ شده است. قسمت‌های پوشیده اندازه‌گیری یا حدس زده نشده‌اند. فقط قاب۷ ورودی شروع است؛ خانه و قاب‌های مجاور منابع بررسی‌اند، نه ورودی مخفی یا قاب پایان.

زمان‌گیری تمرین ثبت شد: بازهٔ اصلی۳٫۲۴ثانیه؛ با حاشیه و انتهای محافظه‌کارانه کمتر از۳٫۹ثانیه. سهم۴٫۵ثانیه حفظ شد. تمرین فقط شاهد زمان و خارج از ورودی تولید است؛ کیفیت شنیداری تمرین ادعا نشده. متن و حالت از کارت مصوب منتقل شده‌اند.

قیمت زنده: مدل `Omni 1.1 Flash`، روش `Frames`، کیفیت `360p`، عمودی `9:16`،۸ثانیه، یک خروجی؛۶اعتبار، سقف۶، یک ارسال، بدون تکرار. تولید۸ثانیه‌ای برای زمان گفتار کشیده نمی‌شود؛ پایان اضافی در تدوین محلی کنار گذاشته می‌شود. تبدیل خودکار صدا انجام نخواهد شد؛ مرجع مستقل نازلی حفظ است و خروجی با آن سنجیده می‌شود. نمونهٔ صدای نازلی به این مدل وارد نمی‌شود؛ ثبات صدا تضمین نیست.

بررسی طراحی و ورودی‌ها کامل است؛ پذیرش صدای تولیدنشده، تلفظ، لب‌خوانی و حرکت واقعی پس از خروجی انجام می‌شود. هیچ ویدیوی موجود برای همین جمله نداریم. هیچ تولید/بارگذاری تازه انجام نشده؛ تأیید صریح محتوای همین بسته و هزینه هنوز لازم است. بلافاصله پیش از ارسال، مدل و قیمت و فایل و متن دوباره با بستهٔ تأییدشده تطبیق داده شوند.

<!-- preflight-state -->
```json
{
  "shot": "EP04-SH07",
  "take": "take-01",
  "ready": true,
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Exact approved EP04-D07 and diacritics retained; only Nazli speaks."
    },
    "delivery": {
      "status": "pass",
      "evidence": "Low clear conversational volume, soft specific instruction, mild urgency; emphasis before leaving; no long internal pause."
    },
    "duration": {
      "status": "pass",
      "evidence": "../../timing-review-v1.md: main span3.24s, conservative with margins under3.9s;4.5s edit target fits.8s generation retained. ASR exact sentence without diacritics; listening not claimed."
    },
    "performance": {
      "status": "pass",
      "evidence": "Approved direction copied; small face/head only, no new gesture/contact/turn/walk."
    },
    "speaker": {
      "status": "pass",
      "evidence": "Nazli sole speaker; Saman visible partial profile/shoulder silent, no lip movement; mother/Farhad outside frame silent."
    },
    "identity": {
      "status": "pass",
      "evidence": "Current shot07 frame viewed, compared with kitchen shot05/06 earlier and fixed character bible; Nazli teal buttonshirt, brown shoulder hair; partial Saman blue grid shirt/stubble/hair. Hidden features not inferred."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Nazli looks right/up to Saman; Saman right foreground facing left; same axis as kitchen shot05 and accepted06."
    },
    "geometry": {
      "status": "pass",
      "evidence": "House master and frames07/08 viewed. North cabinet and stove behind Nazli; fridge behind Saman in reverse angle08. No new opening or furniture; floor/distance not measurable in close framing."
    },
    "continuity": {
      "status": "pass",
      "evidence": "06 accepted original voice/pause-cut is predecessor.07 starts after full sentence; same axis, wardrobe, standing marks.08 starts after Nazli finishes. Actual next-video connection pending output."
    },
    "camera": {
      "status": "pass",
      "evidence": "Actual approved frame is wider than old close description; no crop or new image proposed. Fixed camera preserves the accepted image."
    },
    "prompt": {
      "status": "pass",
      "evidence": "No claim of imported audio reference; no read-aloud instructions in dialogue; exact text matched."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing video of D07 available; static frame cannot replace performance. Saman06 conversion rejected; no automatic voice conversion proposed."
    },
    "settings": {
      "status": "pass",
      "evidence": "Live settings rechecked in EP04 project; Omni1.1Flash selected explicitly, Frames360p8s9:16x1. No upload or submission done."
    },
    "cost": {
      "status": "pass",
      "evidence": "Live UI six credits for Omni1.1Flash/360p/8s/9:16/Frames/x1; flow-cost-check-v1.jpg. Ceiling6, one attempt, no retries; approval pending."
    }
  },
  "content_approval": {
    "approved": true,
    "bundle_sha256": "e8624a7b630ae9b17cfcda5aca499cdca6cb92f5b1144dc70e33a5b5f7ea8602",
    "user_reply": "تأیید",
    "evidence_ref": "Current user explicitly approves displayed EP04-SH07 package: Omni 1.1 Flash,360p,8s,one output,ceiling6 credits"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "e8624a7b630ae9b17cfcda5aca499cdca6cb92f5b1144dc70e33a5b5f7ea8602",
    "user_reply": "تأیید",
    "evidence_ref": "Current user explicitly approves displayed EP04-SH07 package: Omni 1.1 Flash,360p,8s,one output,ceiling6 credits"
  },
  "consumed_attempts": 1,
  "reviewed_at": "2026-10-15T16:25:07Z",
  "bundle_sha256": "e8624a7b630ae9b17cfcda5aca499cdca6cb92f5b1144dc70e33a5b5f7ea8602"
}
```
<!-- /preflight-state -->
