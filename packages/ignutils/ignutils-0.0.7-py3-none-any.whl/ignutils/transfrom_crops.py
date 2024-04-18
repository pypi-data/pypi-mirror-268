from PIL import Image
import os
import json
import argparse
from shapely.geometry import MultiPolygon,Polygon, Point, LineString
from shapely.affinity import translate

def shift_polygon_points(data, x_shift, y_shift):
    for shape in data['shapes']:
        points = shape['points']
        for i in range(len(points)):
            points[i][0] = int(points[i][0] - x_shift)
            points[i][1] = int(points[i][1] - y_shift)
        shape['points'] = points
    return data

def crop_image(image_path, json_path, output_folder):
    image = Image.open(image_path)

    width, height = image.size

    new_width = width // 2
    new_height = height // 2

    parts = [
        ('left_top', (0, 0)),
        ('right_top', (new_width, 0)),
        ('left_bottom', (0, new_height)),
        ('right_bottom', (new_width, new_height)),
    ]

    for name, (crop_x, crop_y) in parts:
        output_image_path = os.path.join(output_folder, f"{os.path.basename(image_path).split('.')[0]}_{name}.png")
        output_json_path = os.path.join(output_folder, f"{os.path.basename(image_path).split('.')[0]}_{name}.json")
        part = image.crop((crop_x, crop_y, crop_x + new_width, crop_y + new_height))
        part.save(output_image_path)
        
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

        data['imagePath'] = os.path.basename(output_image_path)

        offset_x, offset_y = crop_x, crop_y
        new_shapes = []
        
        for shape in data['shapes']:
            original_polygon = shape['points']
            new_polygon = crop_polygon_to_new_size(original_polygon, offset_x, offset_y, new_width, new_height)
            
            if len(new_polygon) >= 3:
                first_point = new_polygon[0]
                last_point = new_polygon[-1]
                if first_point != last_point:
                    external_point = Point(original_polygon[0])
                    line = LineString([external_point, Point(last_point)])
                    intersection = line.intersection(Polygon(new_polygon))
                    if isinstance(intersection, Point):
                        new_polygon.append([int(intersection.x), int(intersection.y)])

                    top_boundary_line = LineString([[0, 0], [new_width, 0]])
                    intersection_top = top_boundary_line.intersection(Polygon(new_polygon))
                    if isinstance(intersection_top, Point):
                        new_polygon.insert(0, [int(intersection_top.x), int(intersection_top.y)])

                    bottom_boundary_line = LineString([[0, new_height], [new_width, new_height]])
                    intersection_bottom = bottom_boundary_line.intersection(Polygon(new_polygon))
                    if isinstance(intersection_bottom, Point):
                        new_polygon.append([int(intersection_bottom.x), int(intersection_bottom.y)])

            new_shape = shape.copy()
            new_shape['points'] = new_polygon
            new_shapes.append(new_shape)

        data['shapes'] = new_shapes

        if name == 'right_top':
            data = shift_polygon_points(data, new_width, 0)
        elif name == 'right_bottom':
            data = shift_polygon_points(data, new_width, new_height)
        elif name == 'left_bottom':
            data = shift_polygon_points(data, 0, new_height)

        with open(output_json_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)



def crop_polygon_to_new_size(polygon, crop_x, crop_y, new_width, new_height):
    original_polygon = Polygon(polygon)

    # Translate the polygon to the new position
    translated_polygon = translate(original_polygon, xoff=-crop_x, yoff=-crop_y)
    translated_polygon = translated_polygon.buffer(0)  # Apply buffer(0) to fix potential geometry issues
    cropped_polygon = translated_polygon.intersection(Polygon([(0, 0), (new_width, 0), (new_width, new_height), (0, new_height)]))
    translated_back_polygon = translate(cropped_polygon, xoff=crop_x, yoff=crop_y)

    new_polygon = []
    if isinstance(translated_back_polygon, MultiPolygon):
        for poly in translated_back_polygon.geoms:
            if not poly.is_empty:
                new_points = list(poly.exterior.coords)
                new_polygon.extend([[int(x), int(y)] for x, y in new_points])
    else:
        if not translated_back_polygon.is_empty:
            new_points = list(translated_back_polygon.exterior.coords)
            new_polygon = [[int(x), int(y)] for x, y in new_points]

    return new_polygon


def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            json_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}.json")
            crop_image(image_path, json_path, output_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Crop images and corresponding JSONs.')
    parser.add_argument('src', help='Path to the folder containing images and JSONs.')
    parser.add_argument('out', help='Path to the folder where cropped images and JSONs will be saved.')
    args = parser.parse_args()
    
    input_folder = args.src
    output_folder = args.out
    main(input_folder, output_folder)
