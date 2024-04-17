# climanu
## climanu the cli menu creater


**description :** climanu used make cli menu like github repo have 

# installation
```
pip install climanu
```

# Example 1

```python
import climanu

mymanu=climanu.SimpleManu()

mymanu.setManu(options=["option 1","option2","option3"],title="my manu",console_text="Select",context="Chose any one")

mymanu.showManu()

print(mymanu.getUserinput())
```

# Example 2

```python
import climanu

mymanu=climanu.TableManu()

mymanu.setManu(columns=["no.","options"],
rows=[["1","apple"],["2","mango"],["3","orange"]],
title="Main Manu",
console_text="Select any one")

mymanu.showManu()
print(mymanu.getUserinput())
print(mymanu.getUserinputRow())
```

**auther**: HuiHola
