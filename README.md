# Heap vs Quick vs Merge

Benchmark the three sorts and explain the gaps (cache behaviour).

## Results
- **Quick Sort:** الاسرع في العادة. بيمشي على البيانات ورا بعض، فالكاش بيلاقيها جاهزة.
- **Merge Sort:** سريع وثابت، بس بيحتاج ذاكرة زيادة عشان يقسم ويرجع يجمع.
- **Heap Sort:** مش بيحتاج ذاكرة زيادة، بس بينطط كتير في الذاكرة، فالكاش بيتعب وبيبقى ابطأ.

## How to run
pip install matplotlib
python benchmark.py

هيطلعلك رسمة results.png فيها مقارنة الوقت بينهم.
