# Validation Framework

1. **Hand-checkable Example**: A micro case with small integers; compute each step manually.
2. **Edge Cases**: division-by-zero protection; bounds clamping for [0,1] variables.
3. **Sensitivity**: One-at-a-time ±20% (tornado) for key parameters.
4. **Scenario Realism**: Parameter ranges consistent with clinical contexts.
5. **Unit Tests**: automated tests for the above in `tests/`.
