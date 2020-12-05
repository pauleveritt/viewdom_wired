# TODO

## Now

## Next

## Soon

## Eventually

- Allow DI to work on generics such as `Optional`, `Tuple`

## Refactor Samples

- Make a base protocol for Component with the __call__ -> VDOM

- In first sample step, make a pluggable app and re-use it in other steps

- Have app/protocols.py in each step for protocols

- Convert `@component(for_=Protocol)` to remove `for_`

  - Or, have a viewdom_wired.protocol_component decorator

- `@adherent` doesn't work with `@dataclass(frozen=True)` unless the class inherits from the protocol

- Do some timing vs. jinja2

## Done

- Get rid of `@component` and `register_component` and instead use `injectable`
from `wired_injector`
