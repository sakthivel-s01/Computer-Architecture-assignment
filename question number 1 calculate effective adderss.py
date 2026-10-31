# Given values
address_field = 200
r1 = 40

# Memory simulation using a dictionary
memory = {
    200: 500,
    240: 900
}

print("=" * 50)
print("ADDRESSING MODES CALCULATION PROGRAM")
print("=" * 50)
print(f"Given: Address Field = {address_field}, R1 = {r1}")
print("-" * 50)

# a) Immediate Addressing
# Rule: The operand value is explicitly stated in the instruction itself.
immediate_operand = 25
print("a) Immediate Addressing:")
print("   - Rule: The operand is specified directly in the instruction.")
print(f"   - Operand Value: {immediate_operand}")
print()

# b) Direct Addressing
# Rule: Effective Address (EA) = Address field. The operand is fetched from Memory[EA].
ea_direct = address_field
operand_direct = memory.get(ea_direct, "Not Available")
print("b) Direct Addressing:")
print("   - Rule: Effective Address (EA) = Address field. Operand = Memory[EA]")
print(f"   - Effective Address: {ea_direct}")
print(f"   - Operand: {operand_direct}")
print()

# c) Indirect Addressing
# Rule: Effective Address (EA) = Contents of the memory location pointed by the address field.
ea_indirect = memory.get(address_field, "Not Available")
operand_indirect = memory.get(ea_indirect, "Not Available") if isinstance(ea_indirect, int) else "Not Available"
print("c) Indirect Addressing:")
print("   - Rule: Effective Address (EA) = Memory[Address field]. Operand = Memory[EA]")
print(f"   - Effective Address: {ea_indirect}")
print(f"   - Operand: {operand_indirect} (Note: Memory[{ea_indirect}] is not defined in the given values)")
print()

# d) Indexed Addressing (using R1 as index register)
# Rule: Effective Address (EA) = Address field + Contents of Index Register (R1).
ea_indexed = address_field + r1
operand_indexed = memory.get(ea_indexed, "Not Available")
print("d) Indexed Addressing (using R1):")
print("   - Rule: Effective Address (EA) = Address field + Contents of Index Register (R1)")
print(f"   - Effective Address: {ea_indexed}")
print(f"   - Operand: {operand_indexed}")
print("=" * 50)
