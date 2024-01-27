import os

import arcpy


def main():
    while True:
        print()
        print("Hello.")
        print()
        print("This program will: create a geodatabase for geotagged photos, and subsequently add a point feature class with geotagged photos to the gdb.")
        print()
        # set workspace
        while True:
            work_direct = input(
                "Please enter the absolute path to the folder containing the photos: ")
            raw_work_direct = r"{}".format(work_direct)

            print()
            if os.path.exists(raw_work_direct) and os.path.isdir(raw_work_direct):
                os.chdir(raw_work_direct)
                arcpy.env.workspace = raw_work_direct
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
        output_gdb = input(
            "Please input what you would like the newly created gdb to be named. If you have run this program before, please choose a different name than prior: ")
        output_name = output_gdb + ".gdb"

        print()

        print(f"The output file geodatabase will be named {output_name}")
        print()

        # create geodatabase
        gdb_photos = arcpy.CreateFileGDB_management(output_path, output_name)
        raw_gdbpath = r"{}".format(gdb_photos)
        print(raw_gdbpath)

        print()
        print("The file geodatabase has been created within the selected workspace.")
        print()

        # creating the points feature class using photos metadata

        print("Please be advised that the Arcpy functionality may only geotag .jpg or .tif photos")
        print()

        photos_fc = input(
            "Please enter what you would like the photos point feature class to be named. If you have run this program before, please choose a different name for the feature class: ")
        shapefile_name = photos_fc + ".shp"

        arcpy.management.GeoTaggedPhotosToPoints(
            raw_work_direct, shapefile_name, "", "ONLY_GEOTAGGED", "ADD_ATTACHMENTS")

        # want to move these shapefiles from the photos folder (workspace) to the newly created gdb folder:

        destination_shapefile = os.path.join(
            raw_gdbpath, os.path.basename(photos_fc))
        print(f'{shapefile_name} can be found within the working directory, and will be copied into the newly created geodatabase, {output_name}, promptly, for easier access. ')
        arcpy.management.CopyFeatures(shapefile_name, destination_shapefile)
        print()
        print(
            f"A point feature class with the name {photos_fc} has been created with the geotagged photos in the newly created gdb, {output_name}. ")
        print()
        rerun_option = input(
            "If you are finished with this program, please type Y, otherwise if you would like to use the program again, type N: ")
        if rerun_option == "Y" or rerun_option == "y" or rerun_option == "YES" or rerun_option == "yes" or rerun_option == "Yes":
            print()
            print("End of program. Thank you.\nGoodbye.")
            break
        if rerun_option == "N" or rerun_option == "n" or rerun_option == "NO" or rerun_option == "no" or rerun_option == "No":
            continue
        else:
            print("Invalid response. Please rerun the program.\nGoodbye.")
            break


if __name__ == "__main__":
    main()
