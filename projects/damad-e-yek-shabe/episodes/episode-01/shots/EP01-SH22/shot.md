# EP01-SH22

## وضعیت فعلی

- برداشت منتخب: take-01 — در خروجی پذیرفته‌شده.
- اجازهٔ ارسال تازه: **مسدود؛ مجوز بستهٔ تازه کامل نیست**.
- مورد باز: کیفیت اجرای آینده و اجازهٔ هزینه جدا از تأیید متن بررسی شوند.
- قدم بعد: آماده‌سازی بستهٔ دقیق، بررسی پیش از ارسال و دریافت تأیید نسخه و هزینه.
- [ویدیوی منتخب](takes/take-01/video.mp4)
- [قاب فعال](../EP01-SH07/images/EP01-SH07-start-v1.png)

## اطلاعات فعال برای ابزارها

این بلوک تنها مرجع انتخاب برداشت و درخواست ارسال است؛ جدول‌های قسمت از آن ساخته می‌شوند. `send_request: null` یعنی هیچ درخواست ارسال فعالی وجود ندارد. تأییدهای تاریخی مجوز تازه نیستند.

<!-- shot-state -->
```json
{
  "shot": "EP01-SH22",
  "active": true,
  "order": 17,
  "selected_take": "take-01",
  "selected_video": "takes/take-01/video.mp4",
  "selected_sha256": "38db873b83d07d9dd0452ac267d0694ad4c44a0a32fb0c7518d8227cb5943a4c",
  "selection_status": "accepted_episode_cut",
  "selection_evidence": "episodes/episode-01/edit/v3/timeline.json",
  "trim": {
    "in": 0.82,
    "out": 2.74
  },
  "active_frame": "../EP01-SH07/images/EP01-SH07-start-v1.png",
  "send_request": null
}
```
<!-- /shot-state -->

## متن و دستور اجرا

مرجع اصلی این نما؛ دیالوگ، بازی، نوبت گوینده و وضعیت برداشت‌ها در همین پوشه نگه‌داری می‌شوند.

[پیوستگی قسمت](../../continuity.md) · [قواعد پروژه](../../../../project-rules.md)

<a id="ep01-d22"></a>
### `EP01-D22` — مادر
- متن: «فَقَط می‌خوایْم بِبینیمِش.»
- وضعیت متن: تأییدشده توسط کاربر در درخواست شروع ساخت اصلاح قسمت اول؛ برداشت تازه هنوز تولید نشده.
- شناسهٔ گوینده: CH-MNZ
- مخاطب و نما: نازلی؛ EP01-SH22
- جای گوینده و شنونده‌ها: نشسته روی بخش چپ مبل؛ رو به نازلی مقابل مبل. فقط گوینده داخل قاب؛ دو شخصیت دیگر در جای ثابت خارج قاب‌اند.
- نوبت و بازهٔ گفتار: نوبت 17 از ۲۳؛ بازهٔ تخمینی 43.8–45.9 ثانیه؛ بدون هم‌پوشانی.
- مالک صدا و لب‌خوانی: مادر / CH-MNZ؛ فقط همین گوینده، با هویت صوتی برداشت‌های قبلی؛ ثبات صدا باید شنیده و سنجیده شود.
- رفتار شنونده‌ها: ساکت و خارج قاب؛ هیچ لب‌خوانی یا صدای اضافی ندارند.
- حالت و شدت: آرامش مقتدر ۲/۵
- قصد گوینده: کم‌کردن بهانه
- نوع جمله و شیوهٔ بیان: خبری و اطمینان‌بخش
- رفتار قابل‌دیدن: نرم‌شدن ابرو
- وضعیت جهت بازی: تأییدشده توسط کاربر با درخواست شروع ساخت؛ پذیرش برداشت واقعی جداست.
- وضعیت نوبت و چیدمان: تأییدشده؛ چیدمان و قاب‌های مصوب قبلی حفظ شوند.


## مشخصات قاب، اتصال و معیار رد

### EP01-SH22

- نوبت: 17 از ۲۳؛ EP01-D22؛ فقط گویندهٔ تعیین‌شده داخل قاب.
- قاب شروع: [مرجع موجود EP01-SH07](../EP01-SH07/images/EP01-SH07-start-v1.png). هویت، لباس و هندسه حفظ شود؛ دیالوگ قبلی خوانده نشود.
- آغاز و پایان: جای اشخاص ثابت، سینی روی میز، دست‌های نازلی خالی، سه استکان ثابت، در بسته. حرکت فقط طبق جهت بازی همان جمله.

## قالب‌های اختصاصی

#### قالب قاب شروع EP01-SH22
```text
Photorealistic contemporary Iranian romantic comedy, vertical 9:16, soft late-afternoon light from the approved camera-left window. Preserve the actual approved identity, wardrobe and apartment references. A single-speaker close-up or medium close-up of مادر (CH-MNZ), seated in the same fixed sofa position established in the scene map. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door.
Use the scene's physical map, not a mirrored room. Exactly three tea glasses exist: two on the tray and one on the table in front of the seated Mother, never behind Nazli. Objects outside this close-up stay in their physical positions. One coherent still frame, no montage, titles, logos or subtitles.
Concerned family representative, calm and curious rather than threatening. Match Mother voice identity to the existing approved takes; do not invent a new voice.
```
#### قالب ویدئو EP01-SH22
```text
Animate the approved starting frame at natural speed, vertical 9:16. Maintain exact identity, wardrobe, room geometry, eyelines and prop state. A single-speaker close-up or medium close-up of مادر (CH-MNZ), seated in the same fixed sofa position established in the scene map. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door.
One speaking turn only. Only مادر owns the voice and the visible lip movements; never assign these words to another character. Start after the preceding turn, no overlap or extra voice. Use the user-approved per-line emotion, intent and delivery below; directions and IDs are not spoken.
Read Persian vowel marks as pronunciation cues, not pauses. Natural colloquial Persian; رو and تو have short /o/, final و in استکانو and حرفامونو is /o/, نازلی is nāzli with no extra vowel between z and l. Do not rewrite the wording or speed up speech. Quiet apartment ambience, no music, narration or subtitles.
{{DIALOGUE:EP01-D22}}
Target usable shot duration about 2.1s, subject to natural spoken delivery. If the selected tool length cannot fit the line, revise the shot timing before generating.
Concerned family representative, calm and curious rather than threatening. Match Mother voice identity to the existing approved takes; do not invent a new voice.
```

## برداشت‌ها و تاریخچه

- [take-01](takes/take-01/review.md)

؛ اطلاعات تکراری قدیمی فقط سابقه‌اند.
