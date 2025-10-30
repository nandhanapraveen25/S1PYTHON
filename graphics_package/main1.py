from graphics.rectangle import area as rect_area
from graphics.circle import perimeter as circle_perimeter
from graphics.graphics_3d.cuboid import surface_area as cuboid_area
from graphics.graphics_3d.sphere import surface_area as sphere_area
from graphics_package.graphics.graphics_3d.cuboid import surface_area

print("rectangle area:", rect_area(12,6))
print("circle perimeter:", circle_perimeter(9))
print("cuboid surface area:", cuboid_area(2, 3, 5))
print("sphere surface area:", sphere_area(7))
