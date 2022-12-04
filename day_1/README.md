# APL Solutions
## Part 1
### APL Single-line solution
```
⌈/+/¨{⍵~¯1}¨((¯1,{⍵≡'':-1 ⋄ ⍎⍵}¨(⊃⎕NGET'INPUT_TXT_HERE'1))∊¯1)⊂1,{⍵≡'':-1 ⋄ ⍎⍵}¨(⊃⎕NGET'INPUT_TXT_HERE'1)
```

### Multi-line, slightly more legible version
```
input←⊃⎕NGET'INPUT_TXT_HERE'1
flatten←{⍵≡'':-1 ⋄ ⍎⍵}
getFlatInput←flatten¨input
maskableFlatInput←¯1,getFlatInput
maskedInput←(maskableFlatInput∊¯1)⊂getFlatInput
filteredInput←{⍵~¯1}¨maskedInput
summedInput←+/¨filteredInput
⌈/summedInput
```

## PART 2 - Not yet done :)