---
date: 2025-04-08 21:11:19
layout: post
title: "Bang Bang, Snake"
subtitle: Using shebang in Python scripts
description: |
  Make your Python scripts executable without invoking the interpreter 
  explicitly.
image:
  path: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1743633984/dmbuil-github-pages/th2.jpg
  lqip: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1743633984/dmbuil-github-pages/th2.jpg
category: snippets
tags:
 - python
author: dmbuil
paginate: false
---

Anyone that has coded any Python script will agree that the prompt
`python my-cool-script.py` is a bit long: one must remember to invoke Python
interpreter before the script name[^1].
It may even lead to error, such as using the wrong Python version. (Pray that no
_ptyhon_ exists in your system!)

Some time ago I found that Python programs can also include the shebang at the
beginning of the script to make it executable straight away.

Call me old-fashioned, but I always thought that the shebang was a Unix/Bash
thing.
As it turns out, shebang can also be used in Python scripts, both in *Nix
systems and [Windows](https://peps.python.org/pep-0397/)!

Just add the following line at the beginning of your script:

```python
#! python3

print("Bang! Die you snake!")

```

Easy peasy, right?:

![Bang](https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1744148541/dmbuil-github-pages/bang-1.png){: w="500"}
_Example on my machine_

> Don't forget to make the script executable with `chmod +x my-cool-script.py`!
{: .prompt-warning }

If you feel fancy, Python's supported shebang formats are:

- [x] `#! python3`
- [x] `#! /usr/bin/env python`
- [x] `#! /usr/bin/python`
- [x] `#! /usr/local/bin/python`
- [x] `#! /usr/bin/env python3`
- [x] `#! /usr/bin/env python2`

But take into account that the most portable across all platforms is the first
one, as long as the `python3` interpreter is available in the system or can be
interpreted[^2].

On a side note, it is also recommended to add the the
[**encoding**](https://peps.python.org/pep-0263/) line to the script, so that
Python knows how to decode it:

```python
#! python3
# -*- coding: utf-8 -*-

print("Bang! Die you snake!")

```

_Hope it helps!_

---
[^1]: The idea of this post came from these StrackOverflow answers I found when
      searching for methods to make Python scripts easier to run
      [1](https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take),
      [2](https://es.stackoverflow.com/questions/204005/para-qué-sirve-un-shebang-debería-escribir-también-un-comentario-sobre-el).

[^2]: The shebang is not required in Windows, but it is a good practice to
      include it for cross-platform compatibility.
      [More info here](https://docs.python.org/3/using/windows.html#shebang-lines)
      or [here](https://peps.python.org/pep-0397/#id6).
