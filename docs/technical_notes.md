# Technical Notes - PIE Compiler

## LLVM Domination Fix for String Literals

### Problem Description

When compiling PIE programs with string literals used in output statements within conditional blocks, the compiler would fail with the following error:

```
RuntimeError: Instruction does not dominate all uses!
  %.410 = bitcast ptr @.str81 to ptr
  call void @output_string(ptr %.410)
```

### Root Cause Analysis

#### LLVM Domination Rules

In LLVM IR, an instruction must "dominate" all of its uses. This means that in the control flow graph (CFG), the instruction must be executed before any instruction that uses its result. This is a fundamental requirement for SSA (Static Single Assignment) form.

#### The Bug

The original code in `visit_primary()` method (lines 967-982) was caching bitcast instructions:

```python
if val.startswith('"') and val.endswith('"'):
    str_val = val[1:-1].replace('\\n', '\n') + '\0'
    if str_val in self.global_strings:
        ptr = self.global_strings[str_val]  # Cached bitcast instruction
    else:
        # Create global variable
        global_var = ir.GlobalVariable(...)
        # Create bitcast in current basic block
        if self.builder:
            ptr = self.builder.bitcast(global_var, ir.IntType(8).as_pointer())
        else:
            ptr = global_var.gep([...])
        self.global_strings[str_val] = ptr  # Cache the bitcast
    return ptr
```

**Problem**: When the same string literal was used in different basic blocks (e.g., in different branches of an if/else statement), the cached bitcast instruction from one block would be used in another block, violating the domination rule.

#### Example Scenario

```pie
if (condition) {
    output("Same message", string);  // Creates bitcast in if-block
} else {
    output("Same message", string);  // Tries to use cached bitcast from if-block
}
```

The bitcast created in the if-block doesn't dominate the else-block, causing the error.

### Solution

Store the global variable itself (not the bitcast) in the cache, and create a fresh bitcast instruction for each use:

```python
if val.startswith('"') and val.endswith('"'):
    str_val = val[1:-1].replace('\\n', '\n') + '\0'
    if str_val in self.global_strings:
        global_var = self.global_strings[str_val]  # Cached global variable
    else:
        # Create global variable
        global_var = ir.GlobalVariable(...)
        self.global_strings[str_val] = global_var  # Cache the global variable
    
    # Create a fresh bitcast/GEP for each use
    if self.builder:
        ptr = self.builder.bitcast(global_var, ir.IntType(8).as_pointer())
    else:
        ptr = global_var.gep([...])
    return ptr
```

**Benefits**:
1. Each use of a string literal gets its own bitcast instruction in the current basic block
2. The bitcast always dominates its uses (it's created right before use)
3. Global variables can be safely referenced from any basic block
4. No performance impact - LLVM optimizer will eliminate redundant bitcasts

### Technical Details

#### Why Global Variables Work

Global variables in LLVM are not instructions - they're module-level entities that exist outside the control flow graph. They can be referenced from any basic block without domination issues.

#### Why Bitcast Instructions Don't Work

Bitcast is an instruction that must be placed in a specific basic block. Once placed, it can only be used by instructions that are dominated by that block.

#### Control Flow Example

```
Entry Block
    |
    v
Condition Check
   / \
  /   \
 v     v
If     Else
Block  Block
  \   /
   \ /
    v
Merge Block
```

- A bitcast in the If Block doesn't dominate the Else Block
- A bitcast in the Else Block doesn't dominate the If Block
- A global variable can be referenced from both blocks

### Testing

The fix was verified with multiple test cases:

1. **Simple conditionals**: Output statements in if/else blocks
2. **Nested conditionals**: Multiple levels of if statements
3. **Repeated strings**: Same string literal used in different blocks
4. **Logical operators**: AND (&&) and OR (||) with output statements
5. **Null checking**: Conditionals with null comparisons and output

All tests pass successfully with the fix applied.

### Performance Impact

**None**. The LLVM optimizer will:
- Recognize that multiple bitcasts of the same global variable are redundant
- Eliminate duplicate bitcasts during optimization passes
- Generate the same machine code as before

### Related LLVM Concepts

- **SSA Form**: Static Single Assignment - each variable is assigned exactly once
- **Domination**: In a CFG, block A dominates block B if every path from entry to B goes through A
- **Basic Block**: A sequence of instructions with no branches except at the end
- **Global Variables**: Module-level entities that exist outside the CFG

### References

- LLVM Language Reference: https://llvm.org/docs/LangRef.html
- LLVM Programmer's Manual: https://llvm.org/docs/ProgrammersManual.html
- SSA Form: https://en.wikipedia.org/wiki/Static_single_assignment_form

### Lessons Learned

1. **Don't cache instructions across basic blocks** - Only cache module-level entities (globals, functions)
2. **Create instructions in the current basic block** - Instructions must be created where they're used
3. **Test with control flow** - Always test code generation with if/else, loops, and nested structures
4. **Understand LLVM's SSA requirements** - Domination is fundamental to LLVM IR correctness

---

## Future Considerations

### Potential Optimizations

1. **String Interning**: The current approach already implements string interning by reusing global variables for identical string literals
2. **Constant Folding**: LLVM's optimizer handles this automatically
3. **Dead Code Elimination**: Unused string literals are removed by the optimizer

### Known Limitations

None currently identified. The fix is complete and handles all edge cases.

### Maintenance Notes

When modifying the `visit_primary()` method or adding new literal types:
- Always store module-level entities (globals) in caches, not instructions
- Create fresh instructions (bitcast, GEP, load, etc.) for each use
- Test with complex control flow structures
- Verify LLVM module with `llvm_module.verify()`
