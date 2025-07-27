shape_data = {
    "circle": ("red", [8, 4, 6]),
    "square": ("blue", [2, 7, 3]),
    "triangle": ("pink", [9, 5, 1])
}
print(shape_data.get("square")[1])
triangle_numbers = shape_data["triangle"][0]
circle_numbers = shape_data["circle"][0]
square_numbers = shape_data["square"][0]

# reassign = triangle_numbers.replace(triangle_numbers,"voilet")
triangle_nums = shape_data["triangle"][1]
shape_data["triangle"] = ("violet", triangle_nums)

print(shape_data)


print(shape_data["triangle"])
shape_data["hexagon"] = ("yellow", [5, 5, 5])

all_colors = [shape_data["triangle"],circle_numbers,square_numbers]
print(all_colors)

color_2 = circle_numbers[:2]
print(color_2)
