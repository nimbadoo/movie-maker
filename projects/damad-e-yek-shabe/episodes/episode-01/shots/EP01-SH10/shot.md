# EP01-SH10

## وضعیت فعلی

- برداشت منتخب: take-02 — در خروجی پذیرفته‌شده.
- اجازهٔ ارسال تازه: **مسدود؛ مجوز بستهٔ تازه کامل نیست**.
- مورد باز: کیفیت اجرای آینده و اجازهٔ هزینه جدا از تأیید متن بررسی شوند.
- قدم بعد: آماده‌سازی بستهٔ دقیق، بررسی پیش از ارسال و دریافت تأیید نسخه و هزینه.
- [ویدیوی منتخب](takes/take-02/video.mp4)
- [قاب فعال](images/EP01-SH10-start-v2.png)

## اطلاعات فعال برای ابزارها

این بلوک تنها مرجع انتخاب برداشت و درخواست ارسال است؛ جدول‌های قسمت از آن ساخته می‌شوند. `send_request: null` یعنی هیچ درخواست ارسال فعالی وجود ندارد. تأییدهای تاریخی مجوز تازه نیستند.

<!-- shot-state -->
```json
{
  "shot": "EP01-SH10",
  "active": true,
  "order": 2,
  "selected_take": "take-02",
  "selected_video": "takes/take-02/video.mp4",
  "selected_sha256": "38ed844a2cb87393893ccc16ff3d3009d1630abc8e6c55d217b99f1f417cdeda",
  "selection_status": "accepted_episode_cut",
  "selection_evidence": "episodes/episode-01/edit/v3/timeline.json",
  "trim": {
    "in": 0.236,
    "out": 2.96
  },
  "active_frame": "images/EP01-SH10-start-v2.png",
  "send_request": null
}
```
<!-- /shot-state -->

## متن و دستور اجرا

مرجع اصلی این نما؛ دیالوگ، بازی، نوبت گوینده و وضعیت برداشت‌ها در همین پوشه نگه‌داری می‌شوند.

[پیوستگی قسمت](../../continuity.md) · [قواعد پروژه](../../../../project-rules.md)

<a id="ep01-d02"></a>
### `EP01-D02` — نازلی
- متن: «مَن تازِه اونجا اِسْتِخْدام شُدَم.»
- وضعیت متن: تأییدشده توسط کاربر در گفت‌وگو؛ صدای واقعی تولید نشده.
- شناسهٔ گوینده: CH-NAZ
- مخاطب و نما: فرهاد؛ EP01-SH10
- جای گوینده و شنونده‌ها: ایستاده کنار ضلع نزدیک و راست میز در نقشهٔ ثابت اتاق؛ برای مخاطبِ هر جمله فقط نگاه را تغییر می‌دهد. گوینده داخل قاب و تنها چهرهٔ خوانا است؛ مادر و فرهاد در جای ثابت خود خارج قاب‌اند.
- نوبت و بازهٔ گفتار: نوبت 2 از ۲۳؛ بازهٔ تخمینی 3.5–6.3 ثانیه؛ بدون هم‌پوشانی.
- مالک صدا و لب‌خوانی: نازلی / CH-NAZ؛ فقط همین شخصیت و همین جمله. مرجع صدای فعال هنوز انتخاب و تأیید نشده؛ لب‌های تنها چهرهٔ قابل‌دیدن باید با صدای او هماهنگ شود.
- رفتار شنونده‌ها: مادر و فرهاد ساکت می‌مانند؛ واکنش کوچک و طبیعی مجاز است ولی کلمات گوینده را لب نمی‌زنند و صدای دیگری نمی‌آید. در قاب این نوبت دهان آن‌ها دیده نمی‌شود.
- وضعیت نوبت و چیدمان: تأییدشده در طرح مطالعهٔ قسمت اول در ۲۰۲۶/۱۰/۱۳؛ قاب‌های اجرایی هنوز جداگانه بازبینی می‌شوند.
- حالت و شدت: تعجب و مخالفت مهارشده؛ شدت ۲ از۵.
- قصد گوینده: یادآوری اهمیت شغل و پس‌زدن تصمیمی که برایش گرفته‌اند.
- نوع جمله و شیوهٔ بیان: خبریِ اعتراضی؛ پاسخ بی‌درنگ و یک‌نفس. «تازِه» یعنی به‌تازگی/اخیراً (recently)، نه «علاوه بر این». تأکید ملایم زمانی روی «تازِه»، بدون مکث، قطع نفس یا شروع دوباره بین «تازِه» و «اونجا اِسْتِخْدام شُدَم»؛ کل جمله یک گروه آهنگین پیوسته است. اعتراض طبیعی به رهاکردن شغلی که همین تازگی شروع شده؛ پایان قطعی، نه خواهش. اصلاح مصوبِ اجرای D02 بر اساس بازخورد کاربر؛ متن جمله تغییر نکند.
- رفتار قابل‌دیدن: نازلی خدمت‌کردن را لحظه‌ای متوقف می‌کند و به فرهاد نگاه می‌کند؛ سینی ثابت می‌ماند.
- وضعیت جهت بازی: تأییدشده توسط کاربر در ۲۰۲۶/۱۰/۱۳؛ پذیرش برداشت واقعی هنوز انجام نشده.

## مشخصات قاب، اتصال و معیار رد

### EP01-SH10

<!-- frame-asset:EP01-SH10 -->
[![قاب اصلاح‌شدهٔ EP01-SH10](images/EP01-SH10-start-v2.png)](images/EP01-SH10-start-v2.png)

نسخهٔ ۲: آشپزخانه پشت نازلی؛ مهمان‌ها و میز چای در جلوی او و بیرون کادرند. مبل خالی و چای پشت نازلی از نسخهٔ فعال حذف شده‌اند. قاب ثابت برای بازبینی؛ حرکت/صدا تولید نشده.
<!-- end-frame-asset -->

- نوبت: 2 از ۲۳؛ EP01-D02؛ فقط گویندهٔ تعیین‌شده داخل قاب.
- بازهٔ پیشنهادی در قسمت: 3.5–6.3s؛ زمان واقعی هنوز اندازه‌گیری نشده.
- گویندهٔ داخل قاب: فقط نازلی؛ شنونده‌ها خارج قاب و ساکت‌اند.
- آغاز/پایان: مطابق جدول اشیا و دادهٔ همان جمله؛ هیچ انتقال صدایی به دهان شخصیت دیگر مجاز نیست.
- مرجع: خودِ مرجع بصری مصوب v1 برای صورت/لباس/خانه؛ قاب اختصاصی SH03 موجود، قاب‌های دیگر در انتظارند.
- رد: گوینده یا صدای اشتباه، لب‌خوانی شنونده، هم‌پوشانی ناخواسته، اعراب‌خوانی مکانیکی، تغییر صورت/لباس/اشیا، ورود دست بی‌صاحب یا حذف بی‌علت.

## قالب‌های اختصاصی

#### قالب قاب شروع EP01-SH10
```text
Photorealistic contemporary Iranian romantic comedy, vertical 9:16, soft late-afternoon light from the approved camera-left window. Preserve the actual approved identity, wardrobe and apartment references. A single-speaker close-up or medium close-up of نازلی (CH-NAZ), standing, holding the same tray with exactly two tea glasses steadily in both hands. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door. CAMERA/BLOCKING OVERRIDE: camera is on the seated guests side looking toward Nazli and the kitchen. Behind Nazli show the same sage-green kitchen doorway/fridge and warm wall only. No sofa, coffee table or served glass behind Nazli. The coffee table is between Nazli and seated guests, in FRONT of her on camera side, outside the portrait crop; the third glass is in front of Mother. Preserve this reverse angle in every Nazli shot.
Use the scene's physical map, not a mirrored room. Exactly three tea glasses exist: two on the tray and one on the table in front of the seated Mother, never behind Nazli. Objects outside this close-up stay in their physical positions. One coherent still frame, no montage, titles, logos or subtitles.
```
#### قالب ویدئو EP01-SH10
```text
Animate the approved starting frame at natural speed, vertical 9:16. Maintain exact identity, wardrobe, room geometry, eyelines and prop state. A single-speaker close-up or medium close-up of نازلی (CH-NAZ), standing, holding the same tray with exactly two tea glasses steadily in both hands. The other two characters remain silent and offscreen in their fixed physical positions; do not show their mouths or add any other dialogue. Only a small eye/head/expression change required by the per-line performance direction. No walking, pouring, gesturing with extra hands or moving the door. CAMERA/BLOCKING OVERRIDE: camera is on the seated guests side looking toward Nazli and the kitchen. Behind Nazli show the same sage-green kitchen doorway/fridge and warm wall only. No sofa, coffee table or served glass behind Nazli. The coffee table is between Nazli and seated guests, in FRONT of her on camera side, outside the portrait crop; the third glass is in front of Mother. Preserve this reverse angle in every Nazli shot.
One speaking turn only. Only نازلی owns the voice and the visible lip movements; never assign these words to another character. Start after the preceding turn, no overlap or extra voice. Use the user-approved per-line emotion, intent and delivery below; directions and IDs are not spoken.
Read Persian vowel marks as pronunciation cues, not pauses. Natural colloquial Persian; رو and تو have short /o/, final و in استکانو and حرفامونو is /o/, نازلی is nāzli with no extra vowel between z and l. Do not rewrite the wording or speed up speech. Quiet apartment ambience, no music, narration or subtitles.
{{DIALOGUE:EP01-D02}}
Target usable shot duration about 2.8s, subject to natural spoken delivery. If the selected tool length cannot fit the line, revise the shot timing before generating.
```

## برداشت‌ها و تاریخچه

- [take-01](takes/take-01/review.md)
- [take-02](takes/take-02/review.md)

؛ اطلاعات تکراری قدیمی فقط سابقه‌اند.
