import requests

def download_sketch(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Sketch downloaded successfully to {save_path}")
        else:
            print(f"Failed to download the sketch. HTTP status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
sketch_url = "https://drive.google.com/file/d/1wJHTmNHFEV6vHPNGx-ViDLdUk5ThL-0e/view?usp=drive_link"
save_path = "test.ino"

download_sketch(sketch_url, save_path)