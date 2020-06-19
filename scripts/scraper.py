from PIL import Image, ExifTags
##check version before
a=(input("png:"))
img = Image.open(a)
img_exif = img.getexif()
print(type(img_exif))

if img_exif is None:
    print("Sorry, image has no exif data.")
    #scans for exif data

else:
    img_exif_dict = dict(img_exif)
    print(img_exif_dict)
    for key, val in img_exif_dict.items():
        if key in ExifTags.TAGS:
            print(f"{ExifTags.TAGS[key]}:{repr(val)}")

                ##prints all info


if img_exif == "{}":
        print(f"image {a} has no exif data")
        ##some files will intentionally put no exif data but not state 0, making it confusting, this is fixed with this simple statement