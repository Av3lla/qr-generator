# QR Generator
### QR코드 생성기

---

#### 링크를 입력하고 버튼을 클릭하면 입력된 링크를 QR코드 이미지로 변환해 저장합니다.

---

* #### terminal
    * #### pyinstaller -w -F --icon=./sources/icons/icon.ico ./sources/name.py
    * #### pyinstaller -w -F --icon=./sources/icons/icon.ico ./name.spec


* #### example.spec
    * #### added_files = [('./sources/qr_generator.ui', '.')]
    * #### datas=added_files, 