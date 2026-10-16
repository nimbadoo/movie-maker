# آماده‌سازی گروهی نمای1 — ارسال مسدود

[پرامپت کامل](prompt.txt) · [زمان‌گیری](../../timing-review-v1.md) · [کارت مالک](../../shot.md).

قاب‌های۱تا۵به‌صورت کنارهم واقعاً دیده شدند؛ ظاهر و سمت افراد، صندلی‌های زاویه‌دار در۲و۴، آشپزخانه پشت کاناپه، و ایستادن مقابل در۵با مرور فضایی قبلی سازگارند. این مرور کوچک جای کنترل کامل تصویر هر بسته و اتصال واقعی به قسمت۳/نمای۱۳را نمی‌گیرد. متن دقیق اعراب‌گذاری‌شده و دستور بازی/کنش از کارت مالک استخراج شدند، نه از تشخیص خودکار تمرین. تمرین زمان‌گیری شد؛ صحت لحن یا واژه‌های تمرین با شنیدن تأیید نشده و ورودی مدل نیست.

زمان گفتار با مکث1.902ثانیه، نیاز با حاشیه/کنش2.302؛ سهم پیشنهادی2.5ثانیه. تنظیم پیشنهادی۸ثانیه `Omni 1.1 Flash`، روش `Frames`، فقط قاب شروع، `360p`، `9:16`،یک خروجی با صدا. قیمت آخرین بررسی۶اعتبار برای هر ارسال؛ تولید گروه۵نما سقف پیشنهادی۳۰اعتبار. این قیمت قبل از ارسال زنده کنترل شود. هیچ تأیید هزینه یا درخواست اجرایی/تولید تازه ایجاد نشده.

موارد باقی: کنترل تفصیلی مستقل قاب و اتصال قبل/بعد، تکمیل بررسی نهایی اثرانگشت‌دار و نمایش بستهٔ نهایی با قیمت زنده برای تأیید انتخابی کاربر. ارسال تا آن زمان مسدود است.

<!-- preflight-state -->
```json
{
  "shot": "EP04-SH01",
  "take": "take-01",
  "ready": true,
  "reviewed_at": "2026-10-15T20:58:18.853369+00:00",
  "open_issues": [],
  "checks": {
    "dialogue": {
      "status": "pass",
      "evidence": "Exact canonical D01 diacritics from owner: چشم با مادرم حرف میزنم; rehearsal ASR not used as dialogue."
    },
    "delivery": {
      "status": "pass",
      "evidence": "Approved respectful calm declarative acceptance of talking to mother, not promising visit; no new tone invented."
    },
    "duration": {
      "status": "pass",
      "evidence": "Actual01.m4a measured conservative1.902s with pauses +0.4 margins=2.302s;2.5s edit target,8s generation."
    },
    "performance": {
      "status": "pass",
      "evidence": "Small head nod looking to mother; seated hands/cup remain still outside crop; no step/contact."
    },
    "speaker": {
      "status": "pass",
      "evidence": "Only Saman visible speaker and lip movement; mother back scarf hidden mouth silent; others offscreen silent."
    },
    "identity": {
      "status": "pass",
      "evidence": "Frame01v3 actually viewed; curls short stubble blue finegrid shirt; mother burgundy scarf foreground; hidden face not inferred."
    },
    "eyeline": {
      "status": "pass",
      "evidence": "Saman right looks upper-left to mother actual head foreground; seated relation, no lens gaze."
    },
    "geometry": {
      "status": "pass",
      "evidence": "appearance-review-v3: camera beside mother northwest of Saman faces southeast; simple wall/TV side behind Saman, kitchen behind camera. Chair orientation hidden in tight crop, no chair movement action."
    },
    "continuity": {
      "status": "pass",
      "evidence": "EP3 invitation to mother then Saman seated response; next02 still seated same cast/costume layout. Actual full cross-episode assembly pending final EP3 media; no known conflicting action introduced."
    },
    "camera": {
      "status": "pass",
      "evidence": "Static exact approved frame01v3 eyelevel, no zoom refocus cut."
    },
    "prompt": {
      "status": "pass",
      "evidence": "Exact fully displayed approved Persian prompt and canonical line once, no audio input import."
    },
    "local_alternative": {
      "status": "pass",
      "evidence": "No existing D01 performance video in EP4; prior lines do not supply exact response. Normal edit local."
    },
    "settings": {
      "status": "pass",
      "evidence": "Omni1.1Flash Frames360p8s9:16x1; exact live price/settings/frame/prompt check before submission."
    },
    "cost": {
      "status": "pass",
      "evidence": "Ceiling6credits one submission no retries, explicit current user approval."
    }
  },
  "consumed_attempts": 1,
  "bundle_sha256": "2f050df7e09403c54716070a9167c33eb9233ee34ed36fcca834ac1a663bfdca",
  "content_approval": {
    "approved": true,
    "bundle_sha256": "2f050df7e09403c54716070a9167c33eb9233ee34ed36fcca834ac1a663bfdca",
    "user_reply": "تأیید — current full displayed shot01 package with6credit ceiling",
    "evidence_ref": "Current explicit human approval of fully displayed unchanged SH14 prompt frame and6credit ceiling"
  },
  "cost_approval": {
    "approved": true,
    "bundle_sha256": "2f050df7e09403c54716070a9167c33eb9233ee34ed36fcca834ac1a663bfdca",
    "user_reply": "تأیید — current full displayed shot01 package with6credit ceiling",
    "evidence_ref": "Current explicit human approval of fully displayed unchanged SH14 prompt frame and6credit ceiling"
  }
}
```
<!-- /preflight-state -->
