import os

import arcpy


print("test")
# set workspace
while True:
    work_direct = input(
        "Please enter the absolute path to the folder containing the photos")

    print()
    if os.path.exists(work_direct) and os.path.isdir(work_direct):
        os.chdir(work_direct)
        arcpy.env.workspace = work_direct
        print(arcpy.env.workspace)
        print("The working directory is now set to: ", os.getcwd())
        print()
        break
    else:
        print("invalid working directory path. Try again.")
        print()


# set local variables
print()
print("It is assumed that you will want the geodatabase located in the current workspace.")

output_path = arcpy.env.workspace
output_name = 'picturesfgdb.gdb'

print()

print("The output file geodatabase will be named picturesfgdb.gdb")
print()

# create geodatabase
geotag_gdb = arcpy.CreateFileGDB_management(output_path, output_name)
# photos_fc = arcpy.management.CreateFeatureclass(
#     geotag_gdb, "italyphotos", "POINT")
print()
print("The file geodatabase has been created within the selected workspace.")
print()

# creating the points feature class using photos metadata


print("Please be advised that the Arcpy functionality may only geotag .jpg or .tif photos")
print()
photos_fc = "ItalyPhotos"
arcpy.management.GeoTaggedPhotosToPoints(
    work_direct, photos_fc, "", "ONLY_GEOTAGGED", "ADD_ATTACHMENTS")
