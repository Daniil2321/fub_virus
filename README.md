**Step one**
-

Install the requirements.

```shell
pip install -r requirements.txt
```

**Step two**
-

go to config.json and open this file,
you will see the parameters *text*, *window_count* and *path_to_file*,
the first is responsible for the window text,
the second for the number of windows, third is path to sound file.

**Attention**

If you specify 0 in the *window_count* field,
the windows will open indefinitely!

**Step three**
-

Launch the program.

On windows:
```shell
python main.py
```

On Linux/MacOS
```shell
python3 main.py
```
