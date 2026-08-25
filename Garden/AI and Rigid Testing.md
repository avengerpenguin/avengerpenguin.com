From observation, most AI-written tests I've seen follow the same anti-patterns inexperienced developers do:

- Tests after the fact
- Tests therefore tend to focus on executing the good and asserting the code does what it was written to do, not asset if the behaviour is _correct_ as we get with TDD and BDD
- Thus it couples tightly to implementation details and need redone when we refactor which removes one of the top benefits of behaviour -based tests: that they provide feedback on whether a refactor was indeed safe

This is typical "concrete" around the code test anti-pattern where the tests indeed fail if the code is ever changed, so it feels like it's protecting it, but really it's only holding the code in place and preventing _any_ change which is completely counter to the principle that [[The best measure of Software Quality is ability to change it]].
