[مرجع مشترک خانه برای همهٔ قسمت‌ها](house/README.md) — تصویر از بالا، پلان، وضعیت مرجع و قواعد تطبیق هر نمای داخل خانه.

# دامادِ یک‌شبه

[مرجع ثابت چهره و لباس شخصیت‌ها](references/visuals/character-bible.md) باید پیش از هر نما خوانده و با خروجی واقعی تطبیق داده شود؛ [قالب گزارش تطبیق](templates/appearance-review.md).


مسیر پروژه از ریشهٔ کارگاه: `projects/damad-e-yek-shabe/`.

[داستان](film.md) · [قواعد](project-rules.md) · [وضعیت و سابقه](status.md) · [مرجع‌های کیمیا](references/README.md)

## مسیر روزمره

قسمت ← فهرست نماها ← کارت نما ← برداشت منتخب یا اصلاح بعدی.

ساختار همهٔ قسمت‌ها:

```text
episode-NN/
  episode.md          معرفی قسمت
  continuity.md       موقعیت، چیدمان و پیوستگی مشترک
  shots.md            فهرست خودکار نماها
  shots/EP…/          کارت و تمام فایل‌های همان نما
  references/         فقط در صورت وجود مرجع مشترک
  edit/               تدوین کامل قسمت
  cover/              کاور تأییدشده و منابع لازم آن
  publishing/         ویدیوی انتشار و کپشن، اگر موجود باشند
```

```text
episodes/episode-02/shots/EP02-SH13/
  shot.md             تنها مرجع فعال متن، بازی، انتخاب و اجازه
  images/             قاب‌ها؛ نسخهٔ فعال در کارت مشخص است
  audio/              مرجع صوت در صورت وجود
  takes/take-07/
    prompt.txt        پرامپت همان برداشت، اگر موجود باشد
    video.mp4         منبع اصلی اگر موجود باشد
    review.md         نتیجه و محدودیت همین برداشت
    preflight.md      برای ارسال آینده؛ موجودبودن فرم مجوز نیست
    edits/            ادیت یا ورودی آماده‌شده، فقط در صورت نیاز
```

هر پوشه با داشتن فایل واقعی ساخته می‌شود. برخی برداشت‌ها فقط ویدیوی ادیت‌شده یا سابقهٔ تولید دارند؛ نبود فایل با فایل ساختگی پوشانده نشده است. قالب‌های اختصاصی دوربین در خود shot.md جمع شده‌اند.

`continuity.md`: پیوستگی مشترک و لینک نماها. مرجع مشترک در references همان قسمت. خروجی کامل در edit قسمت و کاور در `cover/` همان قسمت؛ همهٔ اطلاعات اختصاصی نما در همان نما. پوشهٔ scenes و لایهٔ scene-NN در ساختار فعال وجود ندارند. شناسه‌های روایی قدیمی و تاریخچه حفظ شده‌اند.

جدول قسمت از shot.md ساخته می‌شود؛ بخش انسانی و بلوک فنی در همان کارت‌اند. برای هر تغییر انتخاب، دستور `tools/build_indexes.py` فهرست‌ها را تازه می‌کند. وضعیت تأیید نهایی، انتخاب در تدوین و اجازهٔ ارسال تازه جدا هستند.

## خروجی‌های موجود

- [قسمت۱: نسخهٔ۳ پذیرفته‌شده](episodes/episode-01/edit/v3/EP01-SC01-revision-v3-review.mp4)
- [کاور قسمت۱](episodes/episode-01/cover/EP01-cover-approved.jpg)
- [کاور قسمت۲](episodes/episode-02/cover/README.md)
- [نمای۱۳ قسمت۲: وضعیت و برداشت‌ها](episodes/episode-02/shots/EP02-SH13/shot.md)

همهٔ درخواست‌های ارسال تازه اکنون مسدودند. پرامپت، بررسی مستند و تأیید دقیق هزینه/نسخه لازم‌اند. در این اصلاح ساختار، هیچ تولید یا بازتدوینی انجام نشده است.

## قسمت‌ها

- [episode-01](episodes/episode-01/shots.md)
- [episode-02](episodes/episode-02/shots.md)
- [episode-03](episodes/episode-03/shots.md)
- [episode-04](episodes/episode-04/shots.md)
- [episode-05](episodes/episode-05/shots.md)
- [episode-06](episodes/episode-06/shots.md)
- [episode-07](episodes/episode-07/shots.md)
- [episode-08](episodes/episode-08/shots.md)
- [episode-09](episodes/episode-09/shots.md)
- [episode-10](episodes/episode-10/shots.md)

## ابزارهای محلی

- `build_indexes.py`: فهرست و گالری خودکار.
- `check_submission.py --shot EP02-SH13`: کنترل گزارش و اجازه، بدون ارسال.
- `check_submission.py --shot … --fingerprint`: اثرانگشت بستهٔ آماده، بدون تأیید یا ارسال.
- `build_flow_pack.py --episode 1 --check`: کنترل استخراج قالب‌ها، بدون تولید.
- `assemble_selected.py`: تدوین از برداشت صریح، فقط در نسخهٔ خروجی تازه.
- `validate_structure.py` و `test_workflow.py`: کنترل سلامت و رفتار انتخاب/تأیید.


## نگهداری فایل‌های موردنیاز

فایل‌های آرشیوی تکراری، کاورهای منسوخ و پایان ردشدهٔ قسمت۲ به درخواست کاربر حذف شدند. منابع خام لازم در `sources/` مالک خود هستند؛ پوشهٔ `history` دوباره ساخته نشود. نسخه‌های منتخب و خروجی‌های لازم تدوین، مرجع‌های فعال و بستهٔ منتشرشده حفظ می‌شوند.

[بستهٔ منتشرشدهٔ قسمت۲](episodes/episode-02/publishing/README.md) · [وضعیت جاری](status.md) · [قواعد مشترک انتشار](../../COMMON_RULES.md#episode-publication).


## شروع سریع تسک بعد

[روش‌های تثبیت‌شده و تجربه‌های تولید](production-playbook.md) · [تحویل به قسمت پنج](episodes/episode-05/handoff.md). ابتدا این دو را همراه قواعد بخوانید؛ تأییدهای تاریخی هزینهٔ تازه را مجاز نمی‌کنند.
