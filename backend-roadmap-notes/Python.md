
# Sending commands to Python

You can send commands to python via:

```python
python3 -c "print('Nossa!')"
```

the `-c`  is the `cmd` flag, which allows a program to be passed in as string (terminates option list).

# Running a module as a script

You can run a module as a script using the command
```python
python3 -m site
```

# REPL

`REPL` is an acronym for Read-Eval-Print Loop. Developers use `REPL` Python to communicate with the Python Interpreter. You can input commands in the `REPL`  and see the results displayed immediately.

To access it you can simply run `python3`


# Shebang

 It is a good practice to start your script file with a shebang as it will tell the operating system which interpreter to use to parse the script. Note that is valuable for any language your might be running your script, therefore it is not something particular to Python. [See more info here.](https://dev.to/meleu/what-the-shebang-really-does-and-why-it-s-so-important-in-your-shell-scripts-2755)


# PEP8

PEP8 is the Style Guide for Python Code.


# Venv

You should make sure that you are with the venv activated before making changes to the python installation.

# IPython

  
IPython provides a rich toolkit to help you make the most out of using Python interactively. Its main components are:

> - A powerful interactive Python shell
>     
> - A [Jupyter](https://jupyter.org/) kernel to work with Python code in Jupyter notebooks and other interactive frontends.


:? -> help


# Scalar types

a.k.a primitive types

## Strings in Python

You can multiply a string in Python:

```python
nome = "Fabricio"
print(nome * 5)
```

the code above will produce the output:

```python
FabricioFabricioFabricioFabricioFabricio
```

## f-strings

```python
nome = "Fabricio"
f"Ola, {nome}"
```

## Classic interpolation %s

```python
msg = "O saldo de %s eh o total %.2f"
nome = "Fabricio"
balance = 325.12

print(msg % (nome, balance))
```

## str.format

```python
nome = "Fabricio"
msg = "Opa salve, {}"
print(msg.format(nome))
```

or

```python
name = "Fabricio"
city = "Centurion"
msg = "Opa, salve {name} bem-vindo a {city}"

msg.format(name=name, city=city)
print(msg)

":"
```


## Emoji

```python
print("\U0001F43C") #prints a panda
print("\N{panda face}") # same
```

