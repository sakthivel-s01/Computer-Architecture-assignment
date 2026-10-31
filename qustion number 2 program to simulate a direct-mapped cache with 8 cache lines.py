def simulate_direct_mapped_cache():
    NUM_CACHE_LINES = 8
    access_sequence = [3, 11, 3, 19, 11, 27, 3]

    # Initialize cache with None to represent empty slots
    cache = [None] * NUM_CACHE_LINES

    hits = 0
    misses = 0

    print(
        f"{'Memory Block':<15}{'Cache Line':<15}{'Status':<10}{'Cache Contents (Lines 0 to 7)'}"
    )
    print("-" * 75)

    for block in access_sequence:
        cache_line = block % NUM_CACHE_LINES

        # Check for HIT or MISS
        if cache[cache_line] == block:
            status = "HIT"
            hits += 1
        else:
            status = "MISS"
            misses += 1
            cache[cache_line] = block  # Update cache line with current block

        # Format cache state display
        cache_display = [
            str(b) if b is not None else "-" for b in cache
        ]
        print(
            f"{block:<15}{cache_line:<15}{status:<10}{cache_display}"
        )

    total_accesses = len(access_sequence)
    hit_ratio = hits / total_accesses

    print("-" * 75)
    print(f"Total Accesses : {total_accesses}")
    print(f"Total Hits     : {hits}")
    print(f"Total Misses   : {misses}")
    print(f"Hit Ratio      : {hit_ratio:.2f} ({hit_ratio * 100:.1f}%)")


if __name__ == "__main__":
    simulate_direct_mapped_cache()
