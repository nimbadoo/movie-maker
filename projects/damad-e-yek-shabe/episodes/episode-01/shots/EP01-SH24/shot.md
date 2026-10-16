# EP01-SH24

## وضعیت فعلی

- برداشت منتخب: take-01 — در خروجی پذیرفته‌شده.
- اجازهٔ ارسال تازه: **مسدود؛ مجوز بستهٔ تازه کامل نیست**.
- مورد باز: کیفیت اجرای آینده و اجازهٔ هزینه جدا از تأیید متن بررسی شوند.
- قدم بعد: آماده‌سازی بستهٔ دقیق، بررسی پیش از ارسال و دریافت تأیید نسخه و هزینه.
- [ویدیوی منتخب](takes/take-01/video.mp4)
- [قاب فعال](../EP01-SH16/images/EP01-SH16-start-v2.png)

## اطلاعات فعال برای ابزارها

این بلوک تنها مرجع انتخاب برداشت و درخواست ارسال است؛ جدول‌های قسمت از آن ساخته می‌شوند. `send_request: null` یعنی هیچ درخواست ارسال فعالی وجود ندارد. تأییدهای تاریخی مجوز تازه نیستند.

<!-- shot-state -->
```json
{
  "shot": "EP01-SH24",
  "active": true,
  "order": 19,
  "selected_take": "take-01",
  "selected_video": "takes/take-01/video.mp4",
  "selected_sha256": "5858d9c9324cf583b772d35b51e69f98f20ab104e9bd63ad4db3b354362eabd6",
  "selection_status": "accepted_episode_cut",
  "selection_evidence": "episodes/episode-01/edit/v3/timeline.json",
  "trim": {
    "in": 1.236,
    "out": 5.62
  },
  "active_frame": "../EP01-SH16/images/EP01-SH16-start-v2.png",
  "send_request": null
}
```
<!-- /shot-state -->

## متن و دستور اجرا

مرجع اصلی این نما؛ دیالوگ، بازی، نوبت گوینده و وضعیت برداشت‌ها در همین پوشه نگه‌داری می‌شوند.

[پیوستگی قسمت](../../continuity.md) · [قواعد پروژه](../../../../project-rules.md)

<a id="ep01-d24"></a>
### `EP01-D24` — نازلی
- متن: «باید اَزِش بِپُرْسَم، شایَد اِمْشَب وَقْت نَداشتِه باشِه.»
- وضعیت متن: تأییدشده توسط کاربر در درخواست شروع ساخت اصلاح قسمت اول؛ برداشت تازه هنوز تولید نشده.
- شناسهٔ گوینده: CH-NAZ
- مخاطب و نما: مادر؛ EP01-SH24
- جای گوینده و شنونده‌ها: ایستاده در سمت آشپزخانه روبه‌روی مادر؛ دست‌ها خالی، سینی روی میز. فقط گوینده داخل قاب؛ دو شخصیت دیگر در جای ثابت خارج قاب‌اند.
- نوبت و بازهٔ گفتار: نوبت 19 از ۲۳؛ بازهٔ تخمینی 47.9–52.3 ثانیه؛ بدون هم‌پوشانی.
- مالک صدا و لب‌خوانی: نازلی / CH-NAZ؛ فقط همین گوینده، با هویت صوتی برداشت‌های قبلی؛ ثبات صدا باید شنیده و سنجیده شود.
- رفتار شنونده‌ها: ساکت و خارج قاب؛ هیچ لب‌خوانی یا صدای اضافی ندارند.
- حالت و شدت: نگرانی پنهان ۳/۵
- قصد گوینده: خریدن فرصت
- نوع جمله و شیوهٔ بیان: خبری و مردد، بدون مکث طولانی
- رفتار قابل‌دیدن: نگاه کوتاه پایین و بازگشت به مادر
- وضعیت جهت بازی: تأییدشده توسط کاربر با درخواست شروع ساخت؛ پذیرش برداشت واقعی جداست.
- وضعیت نوبت و چیدمان: تأییدشده؛ چیدمان و قاب‌های مصوب قبلی حفظ شوند.


## مشخصات قاب، اتصال و معیار رد

### EP01-SH24

- نوبت: 19 از ۲۳؛ EP01-D24؛ فقط گویندهٔ تعیین‌شده داخل قاب.
- قاب شروع: [مرجع موجود EP01-SH16](../EP01-SH16/images/EP01-SH16-start-v2.png). هویت، لباس و هندسه حفظ شود؛ دیالوگ قبلی خوانده نشود.
- آغاز و پایان: جای اشخاص ثابت، سینی روی میز، دست‌های نازلی خالی، سه استکان ثابت، در بسته. حرکت فقط طبق جهت بازی همان جمله.

## قالب‌های اختصاصی

#### قالب قاب شروع EP01-SH24
```text
Photorealistic contemporary Iranian romantic comedy, vertical 9:16, soft late-afternoon light from the approved camera-left window. Preserve the actual approved identity, wardrobe and apartment references. A single-speaker close-up or medium close-up of نازلی (CH-NAZ), standing with both hands empty near her body; the same tray and its two glasses stay on the near-right side of the coffee table. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door. CAMERA/BLOCKING OVERRIDE: camera is on the seated guests side looking toward Nazli and the kitchen. Behind Nazli show the same sage-green kitchen doorway/fridge and warm wall only. No sofa, coffee table or served glass behind Nazli. The coffee table is between Nazli and seated guests, in FRONT of her on camera side, outside the portrait crop; the third glass is in front of Mother. Preserve this reverse angle in every Nazli shot.
Use the scene's physical map, not a mirrored room. Exactly three tea glasses exist: two on the tray and one on the table in front of the seated Mother, never behind Nazli. Objects outside this close-up stay in their physical positions. One coherent still frame, no montage, titles, logos or subtitles.
Match Nazli voice identity to the existing approved takes; do not invent a new voice.
```
#### قالب ویدئو EP01-SH24
```text
Animate the approved starting frame at natural speed, vertical 9:16. Maintain exact identity, wardrobe, room geometry, eyelines and prop state. A single-speaker close-up or medium close-up of نازلی (CH-NAZ), standing with both hands empty near her body; the same tray and its two glasses stay on the near-right side of the coffee table. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door. CAMERA/BLOCKING OVERRIDE: camera is on the seated guests side looking toward Nazli and the kitchen. Behind Nazli show the same sage-green kitchen doorway/fridge and warm wall only. No sofa, coffee table or served glass behind Nazli. The coffee table is between Nazli and seated guests, in FRONT of her on camera side, outside the portrait crop; the third glass is in front of Mother. Preserve this reverse angle in every Nazli shot.
One speaking turn only. Only نازلی owns the voice and the visible lip movements; never assign these words to another character. Start after the preceding turn, no overlap or extra voice. Use the user-approved per-line emotion, intent and delivery below; directions and IDs are not spoken.
Read Persian vowel marks as pronunciation cues, not pauses. Natural colloquial Persian; رو and تو have short /o/, final و in استکانو and حرفامونو is /o/, نازلی is nāzli with no extra vowel between z and l. Do not rewrite the wording or speed up speech. Quiet apartment ambience, no music, narration or subtitles.
{{DIALOGUE:EP01-D24}}
Target usable shot duration about 4.4s, subject to natural spoken delivery. If the selected tool length cannot fit the line, revise the shot timing before generating.
Match Nazli voice identity to the existing approved takes; do not invent a new voice.
```

## برداشت‌ها و تاریخچه

- [take-01](takes/take-01/review.md)

؛ اطلاعات تکراری قدیمی فقط سابقه‌اند.
