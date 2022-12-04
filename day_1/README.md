# APL Solutions

## Part 1

### Single-line solution

```
⌈/+/¨{⍵~¯1}¨((¯1,{⍵≡'':-1 ⋄ ⍎⍵}¨(⊃⎕NGET'INPUT_FILE_PATH_HERE'1))∊¯1)⊂1,{⍵≡'':-1 ⋄ ⍎⍵}¨(⊃⎕NGET'INPUT_FILE_PATH_HERE'1)
```

### Multi-line, more legible version

```
input←⊃⎕NGET'INPUT_FILE_PATH_HERE'1
flatten←{⍵≡'':-1 ⋄ ⍎⍵}
getFlatInput←flatten¨input
maskableFlatInput←¯1,getFlatInput
maskedInput←(maskableFlatInput∊¯1)⊂getFlatInput
filteredInput←{⍵~¯1}¨maskedInput
summedInput←+/¨filteredInput
⌈/summedInput
```

## PART 2 - Not yet done :)

### Single-line solution

```
+/3↑sums[⍒(sums←+/¨{⍵~¯1}¨((¯1,{⍵≡'':-1 ⋄ ⍎⍵}¨(⊃⎕NGET'INPUT_FILE_PATH_HERE'1))∊¯1)⊂1,{⍵≡'':-1 ⋄ ⍎⍵}¨(⊃⎕NGET'INPUT_FILE_PATH_HERE'1))]

```

### Multi-line, more legible version

```
input←⊃⎕NGET'INPUT_FILE_PATH_HERE'1
flatten←{⍵≡'':-1 ⋄ ⍎⍵}
getFlatInput←flatten¨input
maskableFlatInput←¯1,getFlatInput
maskedInput←(maskableFlatInput∊¯1)⊂getFlatInput
filteredInput←{⍵~¯1}¨maskedInput
summedInput←+/¨filteredInput
orderedInput←summedInput[⍒summedInput]
+/3↑orderedInput
```
