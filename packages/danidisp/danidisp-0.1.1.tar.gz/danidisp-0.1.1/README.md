# danidisp
##### My public package (on pip) with useful functions i always use
##### Click [here](https://pypi.org/project/danidisp/#description) for more information
### Installation

```pip3 install danidisp```

### Functions

- ### XOR

  ```py
  xor(a: bytes, b: bytes) -> bytes
  ```
  #### Usage

  ```py
  from danidisp import xor
  
  >>> print(xor(b'Ciao', b'Ciao')) 
  b'\x00\x00\x00\x00'
  ```

- ### Discrete logarithm

  ```py
  dlog(n: int, b: int, mod: int) -> int
  ```

  #### Usage
  ```py
  from danidisp import dlog
  
  >>> pow(2, 123, 2093)
  372
  >>> logdis(372, 2, 2093)
  123
  ```

- ### Base Converter

  ```py
  base_conv(n: str, bs: int = 10, be: int = 10) -> str
  ```

  #### Usage
  ```py
  from danidisp import base_conv
  
  >>> base_conv('44', 5, 8)
  '30'
  >>> base_conv('30', 8, 5)
  '44'
  ```

- ### Clock
  
  ```py
  @clock
  def func(*param) -> Optional[any]:
    # something...
  ```

  #### Usage
  ```py
  from danidisp import clock
  
  @clock
  def f():
    # something to do
  
  f() # f took 0.1235s <- time to execute func
  ```

- #### other functions will appear soon...
