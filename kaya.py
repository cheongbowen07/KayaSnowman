print("      /-----------------\ \n")
print("     /                   \ \n")
print("     |   --         --   | \n")
print("     |         |         | \n")
print("     |         0         | \n")
print("     |    \_________/    | \n")
print("     |                   | \n")
print("     |         |         | \n")
print("      \-----------------/ \n")



def draw_snowman_body(height_ft, inches):
    # Convert height to approximate lines (1 line per foot roughly)
    total_inches = height_ft * 12 + inches
    lines = total_inches // 12  # Rough estimate: 1 line per foot
    
    # Base snowman structure (adjusted to fit head width as a box)
    body_line = "     |                   | "
    base_line = "      \\-----------------/ "
    
    # Print body (middle)
    for _ in range(lines // 3):
        print(body_line_with_arms)
    
    # Add arms and details (adjusted)
    print("     /                   \\ ")
    print("     |                   | ")
    print("     \\                   / ")
    
    # Add legs (sticks)
    print("     |                   | ")
    print("     |                   | ")
    print("      -------------------  ")
    print("     |                   | ")
    print("     |                   | ")
    print("     |                   | ")
    print("     |                   | ")

# Example: Draw body for a 6ft 8in snowman
draw_snowman_body(6, 8)
