import augly.image as imaugs

image_path = "6_test/a1.jpg"
output_path = "6_test\\%s.jpg"

# # Augmentation functions can accept image paths as input and
# # always return the resulting augmented PIL Image
# aug_image = imaugs.overlay_emoji(image_path, opacity=1.0, emoji_size=0.15)
#
# # If an output path is specified, the image will also be saved to a file
# aug_image = imaugs.overlay_onto_screenshot(aug_image, output_path=output_path)
imaugs.skew(image=image_path, output_path=output_path % "skew", axis=1)

imaugs.rotate(image=image_path, output_path=output_path % "rotate", degrees=15)
