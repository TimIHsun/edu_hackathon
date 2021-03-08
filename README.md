# edu_hackathon
* 檔案夾 Eduathon
  * activities_clawer.rmd: 活動爬蟲
  * activities.csv: 爬蟲結果（還未斷字 -> 沒有category, field）
  * 活動敘述斷字.ipynb: 斷字
  * activities_final.csv: 依照活動敘述斷字後分領域的結果。
    * 欄位說明在issues。

## Activities Classification
- install_ckiptagger.py: need to install 'ckiptagger' first.
- activity_classification.py: input the description of the activities, then it can get the category of the activity.
  - one activity one time.
