def draw_snowman_body(height_ft, inches):
    # Convert height to approximate lines (1 line per foot roughly)
    total_inches = height_ft * 12 + inches
    lines = total_inches // 12  # Rough estimate: 1 line per foot
    
    # Base snowman structure
    base = "  (   )  "
    middle = " (     ) "
    
    # Print body (middle)
    for _ in range(lines // 3):
        print(middle)
    
    # Print base
    for _ in range(lines // 3):
        print(base)
    
    # Add arms and details
    print(" /      \\ ")
    print(" |      | ")
    print(" \\      / ")

# Example: Draw body for a 6ft 8in snowman
draw_snowman_body(6, 8)