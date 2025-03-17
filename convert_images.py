from PIL import Image
import pillow_heif

def convert_heic_to_jpg(input_path, output_path, quality=95):
    # Load the HEIC image
    heif_image = pillow_heif.open_heif(input_path)
    
    # Convert to PIL Image
    img = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
    
    # Save as JPEG
    img.convert("RGB").save(output_path, "JPEG", quality=quality)

# Example usage
convert_heic_to_jpg("images/IMG_8101.HEIC", "images/output_3.jpg")