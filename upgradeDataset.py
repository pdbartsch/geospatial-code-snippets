"""
I found this useful for upgrading annotation feature classes to add additional functionality of ArcGIS Pro.
Read more about that here: 
https://pro.arcgis.com/en/pro-app/tool-reference/data-management/upgrade-dataset.htm
http://pro.arcgis.com/en/pro-app/help/data/annotation/managing-annotation-feature-class-properties.htm
"""

import arcpy
import os

# set variables
database = r"auth\\os_auth.sde" #path to your database connection file (an .sde file). Could also be a path to file gdb
fds = r"CT" # feature dataset
fc = r"Annot_pro" # feature class

# create a path to the above feature class
f = os.path.join(database, fds, fc)

# upgrade the dataset and tell us about it
print('Now upgrading ' + f)
arcpy.UpgradeDataset_management(f)

