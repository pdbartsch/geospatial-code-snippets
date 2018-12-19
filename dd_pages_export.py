# Name: dd_pages_export.py  - Data Driven Page(s) to PDF 
# Description: exports either a single data Driven Page or all pages from a .mxd document to pdf(s). Replaces multiple previous scripts in favor of user input.
# Author: Paul Bartsch  - updated December 2018
# Intent: for use at UCSB to keep hosted PDF atlas sheets up to date with GIS data and ArcGIS Online Services (see other documents for help keeping online services in sync.)
# Python 2 because this one is intended for use with ArcGIS Desktop maps that have not yet been imported to ArcGIS Pro

## IMPORTS
import arcpy

## CONSTANTS
# out_path 
out_path = r"I:\\My Drive\\ATLAS\\Atlas Export\\" # My Google File Stream Location
# quality of the output pdf
quality = "BEST" #Options include: BEST BETTER NORMAL FASTER FASTEST 
res = 150
# two possible mxd documents. Each setup for data driven pages.
main = r"G:\GIS_Projects\Util_Atlas_Updates\Util_Atlas_Print_DO_NOT_EDIT.mxd"
west = r"G:\GIS_Projects\Util_Atlas_Updates\Util_Atlas_West_Print_DO_NOT_EDIT.mxd"

## DEFAULTS
in_mxd = main
out_prefix = "ucsbatlas"
# selects mxd of either default choice or west campus choice based on user input

## USER INPUTS
# py2 uses raw_input() and py3 uses input()
# because of above this works for ArcGIS Desktop but would need adapting for ArcGIS Pro
mode = raw_input("Please select Mode: 1)Export All Mode or 2)Single Page Mode [1/2]? : ")

## DEFINE FUNCTIONS
# export all data driven pages in chosen mxd document to PDF
def export_multi():
    mxd = arcpy.mapping.MapDocument(in_mxd)
    # pc = mxd.dataDrivenPages.pageCount
    for pageNum in range(first, last):
        mxd.dataDrivenPages.currentPageID = pageNum
        print("Exporting " +descrip+ " page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(last - first)))
        arcpy.mapping.ExportToPDF(mxd, out_path + out_prefix + str("%03d" % (pageNum)) + ".pdf", resolution = res, image_quality = quality)
    # cleanup
    del mxd

# export a single page to PDF based on user input values
def export_single():
    mxd = arcpy.mapping.MapDocument(in_mxd)
    # correct the number for use in file naming and messaging based on UCSB grid naming convention 
    # (e.g. we have a grid 001 and a grid W001)
    pg = int(grid)
    # export to pdf
    # my workflow exports to a Google Drive File Stream location for automatic upload and 
    # update of an online atlas lookup that our employees use to access underground utility grids in PDF form. 
    mxd.dataDrivenPages.currentPageID = page
    print("Exporting " + out_prefix + str("%03d" % pg) + ".pdf to: " + out_path)
    arcpy.mapping.ExportToPDF(mxd, out_path + out_prefix + str("%03d" % pg) + ".pdf", resolution = res, image_quality = quality)
    # cleanup
    del mxd
    
# logic based on user input choices
if mode == '1':
    print('All')
    area = raw_input("Please select either: 1)Main Campus or 2)West Campus. [1/2]? : ")
    single = False
elif mode == '2':
    print('single page mode')
    area = raw_input("Please select either: 1)Main Campus or 2)West Campus. [1/2]? : ")
    grid = raw_input("Please enter a single grid # to export : ")
    single = True
else:
    print("That's not an option.  Exiting script now.  Simply run script again to try again.")
    exit()

# set variables and run appropriate function based on user choices
if single and area == '2': # west campus single mode
    in_mxd = west
    out_prefix = "ucsbatlasW"
    page = int(grid) + 118 #correct the number based on UCSB grid naming convention
    export_single()
elif single: # main campus single mode
    # because Python 2 raw_input is a string
    # go with defaults other than that
    page = int(grid)
    export_single()
elif not single and area =='2': # west campus print all
    in_mxd = west
    out_prefix = "ucsbatlasW"
    first = 119
    last = 328
    descrip = 'West Campus Atlas '
    export_multi()
else: # main campus print all
    first = 1
    last = 119
    descrip = 'Main Campus Atlas '
    export_multi()
