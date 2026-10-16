# EP01-SH04

## وضعیت فعلی

- برداشت منتخب: take-01 — در خروجی پذیرفته‌شده.
- اجازهٔ ارسال تازه: **مسدود؛ مجوز بستهٔ تازه کامل نیست**.
- مورد باز: کیفیت اجرای آینده و اجازهٔ هزینه جدا از تأیید متن بررسی شوند.
- قدم بعد: آماده‌سازی بستهٔ دقیق، بررسی پیش از ارسال و دریافت تأیید نسخه و هزینه.
- [ویدیوی منتخب](takes/take-01/video.mp4)
- [قاب فعال](images/EP01-SH04-start-v1.png)

## اطلاعات فعال برای ابزارها

این بلوک تنها مرجع انتخاب برداشت و درخواست ارسال است؛ جدول‌های قسمت از آن ساخته می‌شوند. `send_request: null` یعنی هیچ درخواست ارسال فعالی وجود ندارد. تأییدهای تاریخی مجوز تازه نیستند.

<!-- shot-state -->
```json
{
  "shot": "EP01-SH04",
  "active": true,
  "order": 9,
  "selected_take": "take-01",
  "selected_video": "takes/take-01/video.mp4",
  "selected_sha256": "113f6a69bfd528ce64edd2a6096f53fd4ce4a43e5db7baeb4f140d03e514b2e3",
  "selection_status": "accepted_episode_cut",
  "selection_evidence": "episodes/episode-01/edit/v3/timeline.json",
  "trim": {
    "in": 0.364,
    "out": 2.608
  },
  "active_frame": "images/EP01-SH04-start-v1.png",
  "send_request": null
}
```
<!-- /shot-state -->

## متن و دستور اجرا

مرجع اصلی این نما؛ دیالوگ، بازی، نوبت گوینده و وضعیت برداشت‌ها در همین پوشه نگه‌داری می‌شوند.

[پیوستگی قسمت](../../continuity.md) · [قواعد پروژه](../../../../project-rules.md)

<a id="ep01-d09"></a>
### `EP01-D09` — مادر
- متن: «اِسْتِکانُو بِذار زَمین، نازْلی.»
- وضعیت متن: تأییدشده توسط کاربر در گفت‌وگو؛ صدای واقعی تولید نشده.
- شناسهٔ گوینده: CH-MNZ
- مخاطب و نما: نازلی؛ EP01-SH04
- جای گوینده و شنونده‌ها: نشسته روی بخش چپ همان مبل در نقشهٔ ثابت اتاق؛ رو به جای نازلی کنار میز. گوینده داخل قاب و تنها چهرهٔ خوانا است؛ نازلی و فرهاد در جای ثابت خود خارج قاب‌اند.
- نوبت و بازهٔ گفتار: نوبت 9 از ۲۳؛ بازهٔ تخمینی 22.7–26.0 ثانیه؛ بدون هم‌پوشانی.
- مالک صدا و لب‌خوانی: مادر / CH-MNZ؛ فقط همین شخصیت و همین جمله. مرجع صدای فعال هنوز انتخاب و تأیید نشده؛ لب‌های تنها چهرهٔ قابل‌دیدن باید با صدای او هماهنگ شود.
- رفتار شنونده‌ها: نازلی و فرهاد ساکت می‌مانند؛ واکنش کوچک و طبیعی مجاز است ولی کلمات گوینده را لب نمی‌زنند و صدای دیگری نمی‌آید. در قاب این نوبت دهان آن‌ها دیده نمی‌شود.
- وضعیت نوبت و چیدمان: تأییدشده در طرح مطالعهٔ قسمت اول در ۲۰۲۶/۱۰/۱۳؛ قاب‌های اجرایی هنوز جداگانه بازبینی می‌شوند.
- حالت و شدت: توجه جدی و شک مهارشده؛ شدت ۳ از۵.
- قصد گوینده: متوقف‌کردن پذیرایی برای رسیدگی مستقیم به حرف دختر.
- نوع جمله و شیوهٔ بیان: امری، پایین و محکم؛ «نازْلی» خطاب جدی در پایان، بدون دادزدن یا لحن پرسشی.
- رفتار قابل‌دیدن: مادر نگاه ثابت به دختر؛ بعد از جمله صدای گذاشتن سینی/استکان می‌تواند روی برش بیاید، نه حرکت پیچیدهٔ طولانی.
- وضعیت جهت بازی: تأییدشده توسط کاربر در ۲۰۲۶/۱۰/۱۳؛ پذیرش برداشت واقعی هنوز انجام نشده.

## مشخصات قاب، اتصال و معیار رد

### EP01-SH04

<!-- frame-asset:EP01-SH04 -->
[![قاب شروع EP01-SH04؛ فقط گویندهٔ همین نوبت](images/EP01-SH04-start-v1.png)](images/EP01-SH04-start-v1.png)

مرجع اجرایی این نما: [تصویر کامل](images/EP01-SH04-start-v1.png). نقش: قاب شروع با هویت، لباس، نور، جهت نگاه و وضعیت وسایل ثابت. نامزد بازبینی‌شدهٔ تصویر ثابت؛ صدا، حرکت، لب‌خوانی و پذیرش نهایی هنوز وجود ندارند.
<!-- end-frame-asset -->

- نوبت: 9 از ۲۳؛ EP01-D09؛ فقط گویندهٔ تعیین‌شده داخل قاب.
- بازهٔ پیشنهادی در قسمت: 22.7–26.0s؛ زمان واقعی هنوز اندازه‌گیری نشده.
- گویندهٔ داخل قاب: فقط مادر؛ شنونده‌ها خارج قاب و ساکت‌اند.
- آغاز/پایان: مطابق جدول اشیا و دادهٔ همان جمله؛ هیچ انتقال صدایی به دهان شخصیت دیگر مجاز نیست.
- مرجع: خودِ مرجع بصری مصوب v1 برای صورت/لباس/خانه؛ قاب اختصاصی SH03 موجود، قاب‌های دیگر در انتظارند.
- رد: گوینده یا صدای اشتباه، لب‌خوانی شنونده، هم‌پوشانی ناخواسته، اعراب‌خوانی مکانیکی، تغییر صورت/لباس/اشیا، ورود دست بی‌صاحب یا حذف بی‌علت.

## قالب‌های اختصاصی

#### قالب قاب شروع EP01-SH04
```text
Photorealistic contemporary Iranian romantic comedy, vertical 9:16, soft late-afternoon light from the approved camera-left window. Preserve the actual approved identity, wardrobe and apartment references. A single-speaker close-up or medium close-up of مادر (CH-MNZ), seated in the same fixed sofa position established in the scene map. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door. After Mother finishes speaking, Nazli places the tray offscreen, motivated by a brief natural contact sound. Do not show extra hands entering Mother's close-up; the next shot starts with the tray on the table and Nazli's hands empty.
Use the scene's physical map, not a mirrored room. Exactly three tea glasses exist: two on the tray and one on the table in front of the seated Mother, never behind Nazli. Objects outside this close-up stay in their physical positions. One coherent still frame, no montage, titles, logos or subtitles.
```
#### قالب ویدئو EP01-SH04
```text
Animate the approved starting frame at natural speed, vertical 9:16. Maintain exact identity, wardrobe, room geometry, eyelines and prop state. A single-speaker close-up or medium close-up of مادر (CH-MNZ), seated in the same fixed sofa position established in the scene map. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door. After Mother finishes speaking, Nazli places the tray offscreen, motivated by a brief natural contact sound. Do not show extra hands entering Mother's close-up; the next shot starts with the tray on the table and Nazli's hands empty.
One speaking turn only. Only مادر owns the voice and the visible lip movements; never assign these words to another character. Start after the preceding turn, no overlap or extra voice. Use the user-approved per-line emotion, intent and delivery below; directions and IDs are not spoken.
Read Persian vowel marks as pronunciation cues, not pauses. Natural colloquial Persian; رو and تو have short /o/, final و in استکانو and حرفامونو is /o/, نازلی is nāzli with no extra vowel between z and l. Do not rewrite the wording or speed up speech. Quiet apartment ambience, no music, narration or subtitles.
{{DIALOGUE:EP01-D09}}
Target usable shot duration about 3.3s, subject to natural spoken delivery. If the selected tool length cannot fit the line, revise the shot timing before generating.
```

## برداشت‌ها و تاریخچه

- [take-01](takes/take-01/review.md)

؛ اطلاعات تکراری قدیمی فقط سابقه‌اند.
