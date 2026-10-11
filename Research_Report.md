# Selection Sort Research Report

## Executive Summary

*more to come*
## History

Selection Sort is one of the oldest sorting algorithms in Computer Science.  Because of its simplicity, there is no known original author or documented first-use of the algorithm.   
## Use Cases

While not often used as a general purpose sorting algorithm in modern computing today, Selection Sort does still have its uses in both education and industry.  Due to the inherent simplicity of the algorithm, it is still widely used in Computer Science education.   While not as fast as other more modern sorting algorithms in terms of time-complexity, it still has a real-world use on certain embedded systems that have very expensive memory read/write operations.  Since elements in the list to be sorted can only ever be moved a maximum of **one time** by the sorting operation.
## Comparison to Other Sorting Algorithms

To illustrate the unique value of Selection Sort when compared to other sorting algorithms, we must look at the Worst Case Time Complexity **specifically for Swap Operations**:

| Sorting Algorithm     | Worst Case (Swap Operations) |
| --------------------- | ---------------------------- |
| Selection Sort        | $O(n)$                       |
| Bubble Sort           | $O(n^2)$                     |
| Recursive Bubble Sort | $O(n^2)$                     |
| Quicksort             | $O(nlogn)$                   |
| Insertion Sort        | $O(n^2)$                     |
| Bucket Sort           | N/A - not an inline sort     |
| Radix Sort            | N/A - not an inline sort     |
| Count Sort            | N/A - not an inline sort     |
| Heap Sort             | $O(nlogn)$                   |
| Tree Sort             | N/A - not an inline sort     |
| Shell Sort            | $O(n^2)$                     |
| TimSort               | N/A - not an inline sort     |

## Algorithm
### <ins>Selection Sort</ins>
1.  Get a list of unsorted elements `LIST`
2. Iterate through the list storing the current index as `CURRENT`.
3. Store the value of the `CURRENT` index in `TEMP`
	`TEMP = LIST[CURRENT]`
4. Iterate through the remaining items in the list to find the lowest value and store the index of that item as `LOWEST_IDX` 
5. Move the value of the item at `LOWEST_IDX` to the item at `CURRENT` 
    `LIST[CURRENT] = LIST[LOWEST_IDX]`
6. Move the value `TEMP` to the item at `LOWEST_IDX`
    `LIST[LOWEST_IDX] = TEMP`

### Pseudocode
```
input LIST
for CURRENT from 0 to length(LIST) do
	TEMP <- LIST[CURRENT]
	LOWEST_IDX <- CURRENT
    for SEARCH from CURRENT to length(LIST) do
	    if LIST[SEARCH] < LIST[LOWEST_IDX] then
		    LOWEST_IDX <- SEARCH
	    endif
    endfor
    LIST[CURRENT] <- LIST[LOWEST_IDX]
    LIST[LOWEST_IDX] <- TEMP
endfor
return LIST
```

### Implementation Example (Python)
```python
def selection_sort(l):
    for c in range(len(l)):
        tmp = l[c]
        lowest_idx = c
        for s in range(c, len(l)):
            if l[s] < l[lowest_idx]:
                lowest_idx = s
        l[c] = l[lowest_idx]
        l[lowest_idx] = tmp
    return l
```

<div style="page-break-after: always;"></div>

## Asymptotic Analysis

```mermaid
flowchart TD
A(Asymptotic Analysis - How to analyze the time complexity)
B(Time Function Definition)
C(Three Cases)
D(Asymptotic Notations)
A --> B
A --> C
A --> D
```

### Time Function Definition
```c
void function(int n[]) {                    // T(n)
	int i, j, tmp, lowest_idx;              // 4
	for (i = 0, i < sizeof(n), i++) {       // n + 1
		tmp = n[i]                          // n
		lowest_idx = i                      // n
		for (j = i, j < sizeof(n), j++)     // n * (n + 1)
			if n[j] < n[lowest_idx]         // n * n
				lowest_idx = j              // n * n
		l[i] = l[lowest_idx]                // n
		l[lowest_idx] = tmp                 // n
	}
}
```

$T(n) = 4 + (n + 1) + n + n + (n * (n + 1)) + n^2 + n^2 + n + n$

$T(n) = 3n^2 + 6n + 5$

#### Asymptotic Analysis Rule #1
(keeping only term with highest degree)

$T(n) = 3n^2$

#### Asymptotic Analysis Rule #2
(ignore constants)

$T(n) = n^2$

### Three Cases

#### Worst Case
The worst case for time complexity for this algorithm is when **the list is sorted, but in reverse order**.  This will require moving every element.  However, no matter if all the elements are moved or none of them are moved, the time complexity is $O(n^2)$ because of comparison operations.

See [Big O](#Big%20O)

#### Best Case
The best case for Time Complexity for this algorithm is when **the list is already sorted**.
This will not require moving any elements.  However the time complexity is still $O(n^2)$ because of comparison operations.

See [Big Omega](#Big%20Omega)
#### Average Case
The average case for Time Complexity for this algorithm is when **the list is unsorted**.  The time complexity will always be $O(n^2)$ because of the comparison operations.

See [Big Theta](#Big%20Theta)
<div style="page-break-after: always;"></div>

### Asymptotic Notations
Time Complexity Key:
> [!NOTE]
> $1 <logn < \sqrt{n} < n < \dots < n^2 < n^3 < \dots < 2^n < 3^n < \dots < n^n$
#### Big O
Worst Case: Reverse Sorted List
> [!TIP]
> The function $f(n) = O(g(n)) \iff \exists$ two Constants $C$ and $k$ such that:
>  $\quad f(n) <= C \cdot g(n) \quad \forall n >= k$

$n^2 <= C \cdot g(n) \quad \forall n >= 1$
$n^2 <= n^2$ where $C$ =1 and $g(n) = n^2$

From the definition $n^2 = O(n^2)$
#### Big Omega 
Best Case: Sorted List
> [!TIP]
> The function $f(n) = \Omega(g(n)) \iff \exists$ two Constants $C$ and $k$ such that:
>  $\quad f(n) >= C \cdot g(n) \quad \forall n >= k$

$n^2 >= C \cdot g(n) \quad \forall n >= 1$
$n^2 >= n^2$ where $C$ =1 and $g(n) = n^2$

From the definition $n^2 = \Omega(n^2)$
#### Big Theta
Average Case: Unsorted List
> [!TIP]
> The function $f(n) = \Theta(g(n)) \iff \exists$  three Constants $C_1$, $C_2$, and $k$ such that:
>  $\quad C_1 \cdot g(n) <= f(n) <= C_2 \cdot g(n) \quad \forall n >= k$

$C_1 \cdot g(n) <= n^2 <= C_2 \cdot g(n)$

$n^2 <= n^2 <= n^2 \quad \forall n >= 1$ where $C_1 = 1, C_2 = 1$ and $g(n) = n^2$

Based on the definition $n^2 = \Theta(n)$

### Conclusion

The Selection Sort Algorithm has an *exact bound* since $\Omega(n^2)$, $\Theta(n^2)$, and $O(n^2)$.  Therefore, the time complexity is **quadratic** by definition.

