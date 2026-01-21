def draw_snowman(height_ft, inches):
    # Convert height to approximate lines (1 line per foot roughly)
    total_inches = height_ft * 12 + inches
    lines = total_inches // 12  # Rough estimate: 1 line per foot
    
    # Base snowman structure
    base = "  (   )  "
    middle = " (     ) "
    top = "  (   )  "
    hat = "   /\\    "
    hat_base = "  /  \\   "
    
    # Print hat
    print("   /\\    ")
    print("  /  \\   ")
    
    # Print head (top) with eyes and nose
    head_lines = lines // 3
    if head_lines > 0:
        print("  ( o o )")  # Eyes
        print("  (   )  ")  # Nose (carrot)
        for _ in range(head_lines - 2):
            print(top)
    
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

# Draw a 6ft 8in snowman
draw_snowman(6, 8)


