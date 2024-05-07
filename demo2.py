from PIL import Image

def encrypt_image(image_path, key):
    # Load the image
    image = Image.open(image_path)
    pixels = image.load()

    # Encrypt the image
    width, height = image.size
    for x in range(width):
        for y in range(height):
            # Apply the encryption method (simple addition)
            r, g, b = pixels[x, y]
            r += key
            g += key
            b += key

            # Keep the RGB values within their bounds
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255

            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = "encrypted_" + image_path
    image.save(encrypted_image_path)
    print(f"Image {image_path} encrypted and saved as {encrypted_image_path}")


def decrypt_image(image_path, key):
    # Load the image
    image = Image.open(image_path)
    pixels = image.load()

    # Decrypt the image
    width, height = image.size
    for x in range(width):
        for y in range(height):
            # Apply the decryption method (simple addition)
            r, g, b = pixels[x, y]
            r -= key
            g -= key
            b -= key

            # Keep the RGB values within their bounds
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0

            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    decrypted_image_path = "decrypted_" + image_path
    image.save(decrypted_image_path)
    print(f"Image {image_path} decrypted and saved as {decrypted_image_path}")


if __name__ == "__main__":
    # Example usage
    image_path = "path/to/your_image.png"
    key = 10

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the image
    decrypted_image_path = "decrypted_" + image_path
    decrypt_image(image_path, key)
