# Collections

## Strings
Is a collection of charcters

- Use String `.format()` Method
```python
full_name = '{0} {1}'.format('Waldo', 'Weber')
```
for forrmatting output, use:
- `{:d}` integer two digits of width
- `{:.02d}` integer two digits of width, padded with zeroes
- `{:.f}` floating point
- `{:6.2f}` floating point, with 6 digits width AND two decimal places
- `f-string` for your new string format
```
- `f-string` for your new string format
```python
first_name = 'Waldo'
last_name = 'Weber'
full_name = f'{first_name} {last_name}'
```


If you need help with strings, use the REPL
```bash
python
>>> help(str)
```

## Strings as collections

Use ` len()` to count the number of elements (characters) of the string
Use `index()` notation (begins with `0`) to access individual elements of string. Ex: If you want to access the second element of a string use: string.`[1]`