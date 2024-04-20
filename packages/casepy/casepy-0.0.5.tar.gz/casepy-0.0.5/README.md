# casepy

A Python package for generating cases in a list.

## Methods

- CombinationGenerator
    - Generator Core class
- set_parameters(a, b)
    - initialize generator with essential parameters
    - a: number of element to select (ex: 3)
    - b: list of element (ex: [1,2,3,4,5])
- all_case
    - return list of all possible combinations based on the parameters.
- random_case
    - return one random combination in the list of all possible cases.
- i_case
    - return i-th combination in the list of all possible cases.

## Usage

With casepy, you can easily generate a combination of elements in a list.

- Example

Initialize generator

``` Python
import casepy
generator_combination = casepy.CombinationGenerator()
# generating combination cases
generator_permutation = casepy.PermutationGenerator()
# generating permutation cases

generator_combination.set_parameters(4, [1,2,3,4,5])
generator_permutation.set_parameters(4, [1,2,3,4,5])
```

all_case()

``` Python
all_case_list = generator_combination.all_case()
# [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
all_case_list = generator_permutation.all_case()
# [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 3], [1, 2, 4, 5], ...] total 120 cases
```
random_case()
``` Python
random_case = generator_combination.random_case()
# [1, 2, 4, 5] // It can be difference
random_case = generator_permutation.random_case()
# [2, 4, 3, 5] // It can be difference
```
i_case
``` Python
i_case_3 = generator_combination.i_case(3)
# [1,3,4,5]
i_case_3 = generator_permutation.i_case(3)
# [1,2,4,5]
```

------------

This is my first own made Python package.

Please feel free to let me know any feedback or suggestions.

#

Author: DongHoon Kim

Email: donghoon5793@gmail.com