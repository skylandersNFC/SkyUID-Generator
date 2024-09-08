# SkyUID Generator

**DOWNLOAD: [SkyUID Generator](https://github.com/skylandersNFC/SkyUID-Generator/releases/tag/SkyUID-Generator)**

----------------------------------------

*Disclaimer: **This script won't work for Imaginators dumps, only from SSA to SSC.**

_Imaginator dumps need to be an exact copy of the original dumps, meaning you need to copy all 64 blocks from the original dump to your card.
If you are here, you probably have UID-locked cards, which means you can write 63 out of 64 blocks but not the UID block.
That's why you are using the SkyUID Generator to regenerate those 63 blocks from the original dump to align with your card's UID.
However, with Imaginators, we cannot regenerate anything since those dumps have an extra protection layer in the form of four additional signature blocks.
In order for these to work, you need to write all 64 blocks exactly as they are. You cannot adjust or generate anything.
Since you can only write 63 blocks with your UID-locked cards, you will have a 98% written dump, but never 100%.
And the Imaginators game won't accept 98%._

----------------------------------------
**What is this:**

This is a python GUI app that can create Skylander dumps, adjusted for a specific card UID.

It's helpful if you have NFC UID locked cards (Sector 0, Block 0 Read-Only) and you need to prepare each dump before flashing it, so it's aligned with the UID of your card.

----------------------------------------

**How to run it:**

1. Download the **Windows** version from "**![Releases](https://github.com/skylandersNFC/SkyUID-Generator/releases/tag/SkyUID-Generator)**" (**SkyUID-Generator.zip**)

2. Extract it somewhere and run the "**SkyUID-Generator.exe**"
![SkyUID-Generator-GUI-Windows.exe](https://i.ibb.co/m5z5dXn/image.png)

3. Now you should have the **GUI** running. It will look something like this
![01. SkyUID-Generator-GUI](https://raw.githubusercontent.com/t3hsuppli3r/SkyUID-Generator-GUI/main/img/01.%20SkyUID-Generator-GUI.jpg)

4. On the first "**UID**" field, you only need to provide your card **UID** in order for the script to generate a proper Skylander dump for it.
![03. Dump Selected](https://raw.githubusercontent.com/t3hsuppli3r/SkyUID-Generator-GUI/main/img/03.%20Dump%20Selected.jpg)

5. You can get a **UID** of a card by just placing it on the reader and pressing "**READ TAG**". That's the first thing it will tell you. **Remove any spaces** from the UID so it's "**EF844A3E**" (example)
![00. How to get UID with MWT](https://github.com/skylandersNFC/SkyUID-Generator-GUI/blob/main/img/00.%20How%20to%20get%20UID%20with%20MWT.jpg)

6. On the second field you need to **pick a Skylander from the dropdown menu**. The skylanders listed in the dropdown are from the "[Skylanders Ultimate NFC Pack](https://skylandersnfc.github.io/Skylanders-Ultimate-NFC-Pack/)". Since they are sorted into folders, you **need to go deep enough** until you have **selected a single Skylander** dump and see a result in the "**Output File**" field.
![02. UID and Dumps Dropdown](https://raw.githubusercontent.com/t3hsuppli3r/SkyUID-Generator-GUI/main/img/02.%20UID%20and%20Dumps%20Dropdown.jpg)

7. After **generating a UID** specific dump file, you should see this 
![04. Generating Dump with Specific UID](https://raw.githubusercontent.com/t3hsuppli3r/SkyUID-Generator-GUI/main/img/04.%20Generating%20Dump%20with%20Specific%20UID.jpg)

8. **Check the main directory** of the program, where you started the "**SkyUID-Generator-GUI-WIN.exe**". There you should see your **new dump file**. For example "**UID_24A3C48A_Boomer.dump**"

9. This new dump file will be **adjusted** for the **specific UID** that you have provided.
  
10. Now **flash** this dump into **your card** with MWT or whatever tool you are using. You **will get 63 out of 64** blocks written, and that's **perfectly fine**. The whole idea of SkyUID is that **we don't touch Sector 0, Block 0** on the card (since it's Read-Only), but we **adjust the rest of the data** in the dump file so it can be synchronized with the already existing **Sector 0, Block 0 (UID block)** on the card.
----------------------------------------

**About the "6. Custom Dumps" option:**

1. Navigate to the "**dumps/6. Custom Dumps/My_Custom_NFC_Dump**" folder.

2. Inside this folder, you'll find a file named "**Replace_With_Read_NFC.dump**".

3. Replace this file with **any custom NFC dump** you want to align with a **specific UID**.

4. The name of the custom dump **doesn't matter**, as long as the file format is **.dump**.

5. Be sure to **delete** the "Replace_With_Read_NFC.dump" file, so only your custom dump file **remains** in the folder.

----------------------------------------
**How to compile it yourself as EXE:**
```
pip install pyinstaller

pyinstaller --onefile --icon=.\icon.ico main.py
```
#### Special thanks to:

>[A crushing individual from Discord]() - who refactored the code, added GUI and everything.
>
>[DevZillion](https://github.com/DevZillion) - [TheSkyLib](https://github.com/DevZillion/TheSkyLib)
>
>[Vitorio Miliano]() - [libs/tnp3xxx.py](https://github.com/DevZillion/TheSkyLib/blob/main/libs/tnp3xxx.py)
>
>[Toni Cunyat](https://github.com/elbuit) - [libs/sklykeys.py](https://github.com/DevZillion/TheSkyLib/blob/main/libs/sklykeys.py)
>
>[Nitrus](https://github.com/Nitrus) - [libs/UID.py](https://github.com/DevZillion/TheSkyLib/blob/main/libs/UID.py)

----------------------------------------
