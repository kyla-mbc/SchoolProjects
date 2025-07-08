# from PIL import Image, ImageDraw

# def draw_sunflower(draw, position):
#     # Draw a sunflower
#     draw.ellipse([position[0] - 20, position[1] - 20, position[0] + 20, position[1] + 20], fill="yellow")
#     draw.polygon([(position[0] - 20, position[1]), (position[0] + 20, position[1]),
#                   (position[0], position[1] - 40)], fill="brown")

# def draw_dandelion(draw, position):
#     # Draw a dandelion
#     draw.ellipse([position[0] - 5, position[1] - 30, position[0] + 5, position[1] - 10], fill="white")
#     draw.line([(position[0], position[1] - 30), (position[0], position[1] - 40)], fill="green")

# # Create a blank image
# width, height = 300, 300
# image = Image.new("RGB", (width, height), "lightblue")
# draw = ImageDraw.Draw(image)

# # Draw one sunflower
# sunflower_position = (width // 4, height // 2)
# draw_sunflower(draw, sunflower_position)

# # Draw three dandelions
# dandelion_positions = [(2 * width // 4, height // 2),
#                        (3 * width // 4, height // 2),
#                        (width // 2, height // 4)]
# for position in dandelion_positions:
#     draw_dandelion(draw, position)

# # Save the image
# image.save("flowers_image.png")

# # Display the image (optional, requires an external viewer)
# image.show()


# # Define the square_number function here:
# def square_number(number):
#     return number ** 2

# # Example of usage:
# number = int(input("Give me a number:"))
# result = square_number(number)
# print(f"The square of {number} is {result}")

# def add_numbers(a,b):
#     return a + b

# result = add_numbers(5,7)
# print(f" The result of both your numbers is: {result}")

def arbitrary_loop_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Test the function
print(arbitrary_loop_sum(5))


